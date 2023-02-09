import SimpleHTTPServer
import SocketServer
import os
import subprocess

PORT = 8000

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.sh'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            script_name = self.path.split('/')[-1]
            output = subprocess.check_output(['./' + script_name], cwd='.', shell=True)
            response = '''
            <html>
            <head>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            </head>
            <body>
                <h1>Output of {}</h1>
                <pre>{}</pre>
                <a href="/">Go back</a>
            </body>
            </html>
            '''.format(script_name, output)
            self.wfile.write(response)
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            script_list = [f for f in os.listdir('.') if f.endswith('.sh')]
            buttons = '\n'.join(['<button><a href="{0}">{0}</a></button>'.format(s) for s in script_list])
            response = '''
            <html>
            <head>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            </head>
            <body>
                <h1>List of scripts</h1>
                {}
            </body>
            </html>
            '''.format(buttons)
            self.wfile.write(response)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

handler = CustomHandler
httpd = SocketServer.TCPServer(("", PORT), handler)

print("serving at port", PORT)
httpd.serve_forever()
