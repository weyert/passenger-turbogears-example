<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml/DTD/xhtml-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:py="http://purl.org/kid/ns#"
      py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"
      py:replace="''"/>
<title> Page Listing - 20 Minute Wiki</title>
</head>
<body>
    <div id="main_content">
        <h1>All Of Your Pages</h1>
        <ul>
            <li py:for="pagename in pages">
            <a href="${tg.url('/' + pagename)}"
                py:content="pagename">Page Name Here.</a>
            </li>
        </ul>
    </div>
</body>
</html>