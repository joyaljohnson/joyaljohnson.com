"""Local preview server that mimics GitHub Pages: /cv serves cv.html, missing pages serve 404.html."""
import http.server, os, sys

class Handler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path) and os.path.exists(path + ".html"):
            self.path = self.path.split("?")[0].split("#")[0] + ".html"
        return super().send_head()

http.server.ThreadingHTTPServer(("", int(sys.argv[1])), Handler).serve_forever()
