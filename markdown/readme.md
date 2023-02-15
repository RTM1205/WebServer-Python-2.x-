# WikiServer
## Como añadir al WebServer
Añade esa parte al principio del do_get y encapsula tu código dentro del else
```python
if '/wiki.html' in self.path:
            #self.wfile.write(file_to_open)
            print_wiki(self)
            exit
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
        else:
```
También copia el método que escribe la página
```python
def print_wiki(self):
    doc='markdown/wiki.md'
    query = urlparse(self.path).query
    if not query=='':
        query_components = dict(qc.split("=") for qc in query.split("&"))
        doc = query_components["doc"]
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
```
