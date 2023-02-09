index_html = """
<html>
  <head>
    <script>
      function runScript(scriptName) {{
        var xhr = new XMLHttpRequest();
        xhr.open("GET", scriptName, true);
        xhr.onreadystatechange = function() {{
          if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {{
            document.getElementById("output").innerHTML = xhr.responseText;
          }}
        }};
        xhr.send();
      }}
    </script>
  </head>
  <body>
    <div id="buttons">
      {buttons}
    </div>
    <div id="output">
    </div>
  </body>
</html>
"""

index_html = index_html.format(buttons=buttons_html)
