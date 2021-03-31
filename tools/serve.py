"""
Use livereload to serve, build, and reload the website when files change.
"""
from livereload import Server, shell


server = Server()
files = ["eportfolio/**/*"]
for filename in files:
    server.watch(filename, "make build")
server.serve(root="eportfolio/_build/html", port="8008", host="localhost", open_url_delay=1)
