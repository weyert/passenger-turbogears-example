import turbogears as tg
from turbogears import controllers, expose, flash

from wiki20.model import Page
from docutils.core import publish_parts
import re
from sqlobject import SQLObjectNotFound

import logging
log = logging.getLogger("wiki20.controllers")

wikiwords = re.compile(r"\b([A-Z]\w+[A-Z]+\w+)")

class Root(controllers.RootController):
    @expose(template="wiki20.templates.page")

    def index(self, pagename="FrontPage"):
        try:
            page = Page.byPagename(pagename)
        except SQLObjectNotFound:
            raise tg.redirect("notfound", pagename=pagename)
        content = publish_parts(page.data, writer_name="html")['html_body']

        root = str(tg.url('/'))
        content = wikiwords.sub(r'<a href="%s\1">\1</a>' % root, content)
        
        return dict(data=content, page=page)

    @expose("wiki20.templates.edit")
    def notfound(self, pagename):
        page = Page(pagename=pagename, data="")
        return dict(page=page)

    @expose(template="wiki20.templates.edit")
    def edit(self, pagename):
        page = Page.byPagename(pagename)
        return dict(page=page)

    @expose("wiki20.templates.pagelist")
    @expose("json")
    def pagelist(self):
        pages = [page.pagename for page in Page.select(orderBy=Page.q.pagename)]
        return dict(pages=pages)
        
    @expose()
    def save(self, pagename, data, submit):
        page = Page.byPagename(pagename)
        page.data = data
        tg.flash("Changes saved!")
        raise tg.redirect("/%s" % pagename)
    
    @expose()
    def default(self, pagename):
        return self.index(pagename)