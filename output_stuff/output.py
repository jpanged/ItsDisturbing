import webbrowser
import os

def makeFile():

    NLP_data = {
        'tone': 'Person',
        'text': 'John',
        'relevance': '0.45'
    }

    speech_to_text = {
        'text': 'This is sample text',
    }

    tone_analysis_emotion = {
        'anger': '0.23',
        'disgust': '0.22',
        'fear': '0.43',
        'joy': '0.12',
        'sadness': '0.11'
    }

    tone_analysis_writing = {
        'analytical': '0.123',
        'confident': '0.43',
        'tentative': '0.5'
    }

    tone_analysis_social = {
        'openness': '0.33',
        'Conscientiousness': '0.23',
        'extroversion': '0.2223',
        'agreeableness': '0.44',
        'emotional range': '0.43'
    }

    tone = {
        'emotion': tone_analysis_emotion,
        'writing': tone_analysis_writing,
        'social': tone_analysis_social
    }

    data = {
        'NLP': NLP_data,
        'tone': tone

    }

    try:
        os.remove("templates/Index.html")
    except OSError:
        pass
    text_file = open("templates/Index.html", "a")


    textToWrite = '''
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Sticky Footer Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="bootstrap/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="sticky-footer.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="bootstrap/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="bootstrap/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <!-- Begin page content -->
    <div class="container">
      <div class="page-header">
        <h1>Sticky footer</h1>
      </div>
      <p class="lead">Pin a fixed-height footer to the bottom of the viewport in desktop browsers with this custom HTML and CSS.</p>
      <p>Use <a href="../sticky-footer-navbar">the sticky footer with a fixed navbar</a> if need be, too.</p>
    </div>

    <footer class="footer">
      <div class="container">
        <p class="text-muted">Place sticky footer content here.</p>
      </div>
    </footer>


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="bootstrap/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>'''
    text_file.write(textToWrite)
    for x in data:
            text_file.write("<td>{}</td>".format(x))
            for y in data[x]:
                values = "<tr>{}</tr><tr>{}</tr>".format(y,data[x][y])
                print(values)
                text_file.write(values)

    text_file.close()


def openFile():
    fileLocation = "file://{}/templates/Index.html".format(os.getcwd())
    webbrowser.open(fileLocation, new=2)


if __name__ == "__main__":
    makeFile()
    openFile()
