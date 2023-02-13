import SimpleHTTPServer
import SocketServer
import os

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8005

Handler = MyRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)

path = os.getcwd()

# Generate buttons dynamically for each .sh file
html = '<!DOCTYPE html><html><head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous"><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script></head><body><div class="container"><h1>Available Scripts</h1><br>'
for filename in os.listdir(path):
    if filename.endswith(".sh"):
        html += '<button type="button" class="btn btn-info run-script" data-script="' + filename + '">Run ' + filename + '</button>'
html += '<br><br><pre id="script-output"></pre></div><script>$(".run-script").click(function() {var script = $(this).data("script");$.ajax({type: "POST",url: script,success: function(data) {$("#script-output").text(data);}});});</script></body></html>'

with open('index.html', 'w') as index:
    index.write(html)

httpd.serve_forever()
