import os

html = """
<html>
  <head>
   <script>
    function runScript(scriptNumber) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/run-" + scriptNumber, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        document.getElementById("output").innerHTML = xhr.responseText;
      }
     };
     xhr.send();
    }
   </script>
  </head>
  <body>
    <h1>Ejecutar scripts SSH</h1>
    %s
  </body>
</html>
"""

buttons = ""

for filename in os.listdir("."):
    if filename.endswith(".sh"):
        script_number = filename.split(".")[0].split("-")[-1]
        buttons += '<button id="run-script-%s" onclick="runScript(%s)">Ejecutar %s</button><br>' % (script_number, script_number ,filename)


print(html % buttons)
with open("index.html", "w") as file:
    file.write(html % buttons)
