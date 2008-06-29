<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:py="http://purl.org/kid/ns#"
      py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8"
      http-equiv="Content-Type" py:replace="''"/>
<title> Editing ${page.pagename} - 20 Minute Wiki</title>
</head>
<body>
    <div id="main_content">
        <div style="float:right; width: 10em">
            Editing <span py:replace="page.pagename">Page Name Goes Here</span>
            <br/>
            You can return to the <a href="/">FrontPage</a>.
        </div>
        <form action="save" method="post">
            <input type="hidden" name="pagename" value="${page.pagename}"/>
            <textarea name="data" py:content="page.data" rows="10" cols="60"/>
            <input type="submit" name="submit" value="Save"/>
        </form>
        <!-- Remove <div py:replace="XML(data)">Page text goes here.</div> -->
    </div>
</body>
</html>