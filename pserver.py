import os
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Script Runner</title>
<!--    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">-->
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css">
    <style>
        body {{
            padding-top: 50px;
            padding-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Script Runner</h1>
        <form class="form-horizontal" method="GET">
            <div class="form-group">
                <label for="email" class="col-sm-2 control-label">Email</label>
                <div class="col-sm-10">
                    <input type="email" class="form-control" id="email" name="email" placeholder="Email address">
                </div>
            </div>
            <div class="form-group">
                <label for="script" class="col-sm-2 control-label">Script</label>
                <div class="col-sm-10">
                    <select class="form-control" id="script" name="script">
                        {}
                    </select>
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <button type="submit" class="btn btn-primary">Execute</button>
                </div>
            </div>
        </form>
    </div>
</body>
</html>
"""

def generate_html():
    scripts = [f for f in os.listdir('.') if f.endswith('.sh')]
    options = '\n'.join(['<option>{}</option>'.format(s) for s in scripts])
    return html_template.format(options)

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(generate_html())

if __name__ == '__main__':
    server = HTTPServer(('', 8000), MyRequestHandler)
    print('Server started on http://localhost:8000')
    server.serve_forever()
