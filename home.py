print("Content-type:text/html\r\n\r\n")
print('''
<!doctype html>
<html>
   <head>
      <meta charset="UTF-8">
      <title>Incredinity</title>
      <link rel="stylesheet" type="text/css" href="main.css">
   </head>
   <body>
      <div id="google_logo">
         <img src="logo.png">
      </div>
      <div id=query>
         <input name="keyword" type="text"></input>
      </div>
      <div class="buttons">
	  <form action="torrent.py" method="get">
         <button  type="submit" name="id" id="search">Search</button>
      </form>
	  </div>
   </body>
</html>''')