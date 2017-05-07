import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        values = "Hello World"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
