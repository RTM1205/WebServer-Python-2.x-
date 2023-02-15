import os
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from urlparse import urlparse

# HTML template for the welcome page
welcome_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css">
</head>
<body>
    <!-- Option 1: Bootstrap Bundle with Popper 
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script> -->
    <div class="container">
        <h1>Welcome to my mini web!</h1>
        <p>Please select one of the options below:</p>
        <ul>
            <li class="list-group-item"><a href="/form1.html">Form 1</a></li>
            <li class="list-group-item"><a href="/form2.html">Form 2</a></li>
	    <li class="list-group-item"><a href="/wiki.html">Wiki</a></li>
        </ul>
    </div>
</body>
</html>
"""

# HTML template for form 1
form1_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form 1</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Form 1</h1>
        <form method="GET">
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" id="email" name="email" placeholder="Enter email">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" name="password" placeholder="Password">
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
"""

# HTML template for form 2
form2_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form 2</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Form 2</h1>
        <form method="GET">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" class="form-control" id="name" name="name" placeholder="Enter name">
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea class="form-control" id="message" name="message" rows="3"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
"""

def print_wiki(self):
    doc='markdown/wiki.md'
    query = urlparse(self.path).query
    if not query=='':
        query_components = dict(qc.split("=") for qc in query.split("&"))
        doc = query_components["doc"]
    print(self.path[1:])
    try:
        # Check if the file is present in the web root directory
        file_to_open = open(self.path[1:]).read()
        self.send_response(200)
    except:
        # If file is not present send a 404 error
        file_to_open = "File not found"
        self.send_response(404)
    self.end_headers()
    directory = os.getcwd()
    list_archivos = ""
    for path in os.listdir(directory+'/markdown'):
        if path.__contains__('.md') and not path.__contains__('wiki.md'):
            list_archivos += '''<li><a href="wiki.html?doc={0}" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700"><span>{1}</span></a></li>'''.format('markdown/'+path,path.replace(".md",""))
    response = '''
            <html>
            <head>
                <title>Python Web Server Example</title>
                <link href="https://cdn.jsdelivr.net/npm/daisyui@2.50.0/dist/full.css" rel="stylesheet" type="text/css" />
                <script src="https://cdn.tailwindcss.com"></script>
                <link href="resources/styles.css" rel="stylesheet" type="text/css" />
                <link href="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.3/flowbite.min.css" rel="stylesheet" />
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body>
                
                <nav class="bg-white border-gray-200 px-2 sm:px-4 py-2.5 rounded dark:bg-gray-900">
                    <div class="container flex flex-wrap items-center justify-between mx-auto">
                    <a href="/" class="flex items-center">
                        <span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Web Guardias</span>
                    </a>
                    <button data-collapse-toggle="navbar-default" type="button" class="inline-flex items-center p-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600" aria-controls="navbar-default" aria-expanded="false">
                        <span class="sr-only">Open main menu</span>
                        <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z" clip-rule="evenodd"></path></svg>
                    </button>
                    <div class="hidden w-full md:block md:w-auto" id="navbar-default">
                        <ul class="flex flex-col p-4 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
                        <li>
                            <a href="" class="block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 dark:text-white" aria-current="page">Wiki</a>
                        </li>
                        <li>
                            <a href="#" class="block py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent">Ejecutar Comandos</a>
                        </li>
                        <li>
                            
                        </li>
                        </ul>
                    </div>
                    </div>
                </nav>
                
                <button data-drawer-target="default-sidebar" data-drawer-toggle="default-sidebar" aria-controls="default-sidebar" type="button" class="inline-flex items-center p-2 mt-2 ml-3 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
                    <span class="sr-only">Open sidebar</span>
                    <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
                    </svg>
                </button>

                <aside id="default-sidebar" class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0" aria-label="Sidebar">
                    <div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
                        <ul class="space-y-2">
                            <li>
                                <a href="wiki.html" class="flex items-center p-2 text-base font-normal text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700">
                                    <span>Wiki</span>
                                </a>
                            </li>
                            {0}
                        </ul>
                    </div>
                </aside>

                <div class="p-4 sm:ml-64">
                    <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
                        <!-- Lightweight client-side loader that feature-detects and load polyfills only when necessary -->
                        <script src="https://cdn.jsdelivr.net/npm/@webcomponents/webcomponentsjs@2/webcomponents-loader.min.js"></script>

                        <!-- Load the element definition -->
                        <script type="module" src="https://cdn.jsdelivr.net/gh/zerodevx/zero-md@1/src/zero-md.min.js"></script>

                        <!-- Simply set the `src` attribute to your MD file and win -->
                        <zero-md src="{1}"></zero-md>
                    </div>
                </div>
            </div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/1.6.3/flowbite.min.js"></script>
            </body>
            </html>
                '''.format(list_archivos,doc)
    self.wfile.write(response)

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(welcome_template)
	elif '/wiki.html' in self.path:
	    print_wiki(self)
            exit
        elif self.path == '/form1.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(form1_template)
        elif self.path == '/form2.html':
	    self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
	    self.wfile.write(form2_template)
	elif '.md' in self.path:
	    try:
                # Check if the file is present in the web root directory
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                # If file is not present send a 404 error
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(file_to_open)


if __name__ == '__main__':
    server = HTTPServer(('', 8000), MyRequestHandler)
    print('Server started on http://localhost:8000')
    server.serve_forever()
