import webbrowser
import os
import datetime
import json


def makeFile():

    input_data = """{"line8": {"text": "I'm so scared", "nlu": {}, "tone": {"emotion": {"anger": 0.9, "joy": 0.0, "fear": 0.9, "sadness": 0.0, "disgust": 0.0}, "social": {"extraversion_big5": 0.522652, "openness_big5": 0.083603, "conscientiousness_big5": 0.272945, "neuroticism_big5": 0.0659, "agreeableness_big5": 0.595476}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}}}, "line7": {"text": "This is out of control", "nlu": {}, "tone": {"emotion": {"anger": 0.350118, "joy": 0.023977, "fear": 0.170767, "sadness": 0.374915, "disgust": 0.168979}, "social": {"extraversion_big5": 0.585703, "openness_big5": 0.89945, "conscientiousness_big5": 0.370109, "neuroticism_big5": 0.21098, "agreeableness_big5": 0.435971}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}}}, "line6": {"text": "I will not allow this", "nlu": {}, "tone": {"emotion": {"anger": 0.356441, "joy": 0.01555, "fear": 0.418217, "sadness": 0.257707, "disgust": 0.034403}, "social": {"extraversion_big5": 0.022418, "openness_big5": 0.270438, "conscientiousness_big5": 0.487677, "neuroticism_big5": 0.24117, "agreeableness_big5": 0.649679}, "writing": {"analytical": 0.882284, "confident": 0.0, "tentative": 0.0}}}, "line5": {"text": "I can't take it anymore", "nlu": {}, "tone": {"emotion": {"anger": 0.099987, "joy": 0.003219, "fear": 0.231003, "sadness": 0.65732, "disgust": 0.077772}, "social": {"extraversion_big5": 0.048625, "openness_big5": 0.003774, "conscientiousness_big5": 0.260345, "neuroticism_big5": 0.008086, "agreeableness_big5": 0.433571}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}}}, "line4": {"text": "What if I just want to die", "nlu": {}, "tone": {"emotion": {"anger": 0.336639, "joy": 0.002626, "fear": 0.058749, "sadness": 0.539582, "disgust": 0.157712}, "social": {"extraversion_big5": 0.07113, "openness_big5": 0.235004, "conscientiousness_big5": 0.303431, "neuroticism_big5": 0.074935, "agreeableness_big5": 0.60043}, "writing": {"analytical": 0.801827, "confident": 0.0, "tentative": 0.91961}}}, "line3": {"text": "He could only consider me as the living corpse of a would-be suicide, a person dead to shame, an idiot ghost", "nlu": {}, "tone": {"emotion": {"anger": 0.193647, "joy": 3.4e-05, "fear": 0.03294, "sadness": 0.565851, "disgust": 0.323069}, "social": {"extraversion_big5": 0.15682, "openness_big5": 0.681763, "conscientiousness_big5": 0.010776, "neuroticism_big5": 0.276494, "agreeableness_big5": 0.512846}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.471477}}}, "line2": {"text": "Rain makes me feel less alon", "nlu": {}, "tone": {"emotion": {"anger": 0.134344, "joy": 0.019464, "fear": 0.433093, "sadness": 0.444153, "disgust": 0.01924}, "social": {"extraversion_big5": 0.460403, "openness_big5": 0.021653, "conscientiousness_big5": 0.23409, "neuroticism_big5": 0.002504, "agreeableness_big5": 0.595923}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.75152}}}, "line1": {"text": "I can't believe you did this to me", "nlu": {}, "tone": {"emotion": {"anger": 0.070895, "joy": 0.015509, "fear": 0.085751, "sadness": 0.398202, "disgust": 0.53588}, "social": {"extraversion_big5": 0.170601, "openness_big5": 0.001908, "conscientiousness_big5": 0.552716, "neuroticism_big5": 0.041148, "agreeableness_big5": 0.7794}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.88939}}}, "line0": {"text": "They ran out of yogurt at the store", "nlu": {}, "tone": {"emotion": {"anger": 0.332842, "joy": 0.042066, "fear": 0.189564, "sadness": 0.433558, "disgust": 0.032106}, "social": {"extraversion_big5": 0.36527, "openness_big5": 0.607778, "conscientiousness_big5": 0.532194, "neuroticism_big5": 0.815845, "agreeableness_big5": 0.408635}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}}}}"""

    parsed_input = json.loads(input_data)

    try:
        os.remove("templates/Index.html")
    except OSError:
        pass
    text_file = open("templates/Index.html", "a")

    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
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
        <h1>Generated Report</h1>
      </div>

      <p class="lead">Generated on {}</p>
      </div>
      <div class="content">
      <table class="table table-striped">




      </table>
    </div>

    <footer class="footer">
      <div class="container">
        <p class="text-muted">Silicon Hacks 2017. Dominic Gaieor | Alex Garcia | Josiah Pang | Celestine Co</p>
      </div>
    </footer>


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="bootstrap/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>'''.format(currentTime)
    text_file.write(textToWrite)
    numberElements = 8
    for i in range(numberElements):
        text = parsed_input["line{}".format(i)]["text"]
        tone_emotion_anger = parsed_input["line{}".format(
            i)]["tone"]["emotion"]["anger"]
        tone_emotion_joy = parsed_input["line{}".format(
            i)]["tone"]["emotion"]["joy"]
        tone_emotion_fear = parsed_input["line{}".format(
            i)]["tone"]["emotion"]["fear"]
        tone_emotion_sadness = parsed_input["line{}".format(
            i)]["tone"]["emotion"]["sadness"]
        tone_emotion_disguist = parsed_input["line{}".format(
            i)]["tone"]["emotion"]["disgust"]

        tone_social_extraversion = parsed_input["line{}".format(
            i)]["tone"]["social"]["extraversion_big5"]
        tone_social_openness = parsed_input["line{}".format(
            i)]["tone"]["social"]["openness_big5"]
        tone_social_conscientiousness = parsed_input["line{}".format(
            i)]["tone"]["social"]["conscientiousness_big5"]
        tone_social_neuroticism = parsed_input["line{}".format(
            i)]["tone"]["social"]["neuroticism_big5"]
        tone_social_agreeableness = parsed_input["line{}".format(
            i)]["tone"]["social"]["agreeableness_big5"]

        tone_writing_analytical = parsed_input["line{}".format(
            i)]["tone"]["writing"]["analytical"]
        tone_writing_confident = parsed_input["line{}".format(
            i)]["tone"]["writing"]["confident"]
        tone_writing_tentative = parsed_input["line{}".format(
            i)]["tone"]["writing"]["tentative"]

        tableData_emotion = '<h3>Emotion Information</h3><table class="table table-striped"><tr><th>Anger</th><th>Joy</th><th>Fear</th><th>Sadness</th><th>Disguist</th></tr><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table>'.format(
            tone_emotion_anger, tone_emotion_joy, tone_emotion_fear, tone_emotion_sadness, tone_emotion_disguist)
        tableData_social = '<h3>Social Information</h3><table class="table table-striped"><tr><th>Extraversion</th><th>Openness</th><th>Conscientiousness</th><th>Neuroticism</th><th>Agreeableness</th></tr><tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr></table>'.format(
            tone_social_extraversion, tone_social_openness, tone_social_conscientiousness, tone_social_neuroticism, tone_social_agreeableness)
        tableData_writing = '<h3>Writing Information</h3><table class="table table-striped"><tr><th>Analytical</th><th>Confident</th><th>Tentative</th></tr><tr><td>{}</td><td>{}</td><td>{}</td></tr></table>'.format(
            tone_writing_analytical, tone_writing_confident, tone_writing_tentative)
        tableData_text = '<h2>Text: {}</h2>'.format(text)

        totalData = tableData_text + tableData_emotion + \
            tableData_social + tableData_writing
        text_file.write(totalData)
    text_file.close()


def openFile():
    fileLocation = "file://{}/templates/Index.html".format(os.getcwd())
    webbrowser.open(fileLocation, new=2)


if __name__ == "__main__":
    makeFile()
    openFile()
