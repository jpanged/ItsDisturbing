import webbrowser
import os
import datetime
import json


def makeFile():

    the_data = []
    big_string = ''

    input_data = """{"num_lines": 11, "line0": {"text": "They ran out of yogurt at the store", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.332842, "disgust": 0.032106, "fear": 0.189564, "joy": 0.042066, "sadness": 0.433558}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}, "social": {"openness_big5": 0.607778, "conscientiousness_big5": 0.532194, "extraversion_big5": 0.36527, "agreeableness_big5": 0.408635, "neuroticism_big5": 0.815845}}}, "line1": {"text": "I can't believe you did this to me", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.070895, "disgust": 0.53588, "fear": 0.085751, "joy": 0.015509, "sadness": 0.398202}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.88939}, "social": {"openness_big5": 0.001908, "conscientiousness_big5": 0.552716, "extraversion_big5": 0.170601, "agreeableness_big5": 0.7794, "neuroticism_big5": 0.041148}}}, "line2": {"text": "Rain makes me feel less alon", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.134344, "disgust": 0.01924, "fear": 0.433093, "joy": 0.019464, "sadness": 0.444153}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.75152}, "social": {"openness_big5": 0.021653, "conscientiousness_big5": 0.23409, "extraversion_big5": 0.460403, "agreeableness_big5": 0.595923, "neuroticism_big5": 0.002504}}}, "line3": {"text": "He could only consider me as the living corpse of a would-be suicide, a person dead to shame, an idiot ghost", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.193647, "disgust": 0.323069, "fear": 0.03294, "joy": 3.4e-05, "sadness": 0.565851}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.471477}, "social": {"openness_big5": 0.681763, "conscientiousness_big5": 0.010776, "extraversion_big5": 0.15682, "agreeableness_big5": 0.512846, "neuroticism_big5": 0.276494}}}, "line4": {"text": "What if I just want to die", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.336639, "disgust": 0.157712, "fear": 0.058749, "joy": 0.002626, "sadness": 0.539582}, "writing": {"analytical": 0.801827, "confident": 0.0, "tentative": 0.91961}, "social": {"openness_big5": 0.235004, "conscientiousness_big5": 0.303431, "extraversion_big5": 0.07113, "agreeableness_big5": 0.60043, "neuroticism_big5": 0.074935}}}, "line5": {"text": "I can't take it anymore", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.099987, "disgust": 0.077772, "fear": 0.231003, "joy": 0.003219, "sadness": 0.65732}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}, "social": {"openness_big5": 0.003774, "conscientiousness_big5": 0.260345, "extraversion_big5": 0.048625, "agreeableness_big5": 0.433571, "neuroticism_big5": 0.008086}}}, "line6": {"text": "I will not allow this", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.356441, "disgust": 0.034403, "fear": 0.418217, "joy": 0.01555, "sadness": 0.257707}, "writing": {"analytical": 0.882284, "confident": 0.0, "tentative": 0.0}, "social": {"openness_big5": 0.270438, "conscientiousness_big5": 0.487677, "extraversion_big5": 0.022418, "agreeableness_big5": 0.649679, "neuroticism_big5": 0.24117}}}, "line7": {"text": "This is out of control", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.350118, "disgust": 0.168979, "fear": 0.170767, "joy": 0.023977, "sadness": 0.374915}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}, "social": {"openness_big5": 0.89945, "conscientiousness_big5": 0.370109, "extraversion_big5": 0.585703, "agreeableness_big5": 0.435971, "neuroticism_big5": 0.21098}}}, "line8": {"text": "I'm so scared", "nlu": {"nlu_entity_items": 0}, "tone": {"emotion": {"anger": 0.9, "disgust": 0.0, "fear": 0.9, "joy": 0.0, "sadness": 0.0}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}, "social": {"openness_big5": 0.083603, "conscientiousness_big5": 0.272945, "extraversion_big5": 0.522652, "agreeableness_big5": 0.595476, "neuroticism_big5": 0.0659}}}, "line9": {"text": "Bob is a fun guy", "nlu": {"nlu_entity_items": 1, "entity0": {"type": "Person", "text": "Bob", "relevance": 0.33, "count": 2}}, "tone": {"emotion": {"anger": 0.016145, "disgust": 0.050057, "fear": 0.02948, "joy": 0.638583, "sadness": 0.122409}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}, "social": {"openness_big5": 0.593309, "conscientiousness_big5": 0.246205, "extraversion_big5": 0.763329, "agreeableness_big5": 0.603691, "neuroticism_big5": 0.582389}}}, "line10": {"text": "I want to go to Niagara Falls", "nlu": {"nlu_entity_items": 1, "entity0": {"type": "GeographicFeature", "text": "Niagara Falls", "relevance": 0.33, "count": 1}}, "tone": {"emotion": {"anger": 0.0602, "disgust": 0.033832, "fear": 0.352245, "joy": 0.011553, "sadness": 0.591556}, "writing": {"analytical": 0.0, "confident": 0.0, "tentative": 0.0}, "social": {"openness_big5": 0.0561, "conscientiousness_big5": 0.278882, "extraversion_big5": 0.600057, "agreeableness_big5": 0.626184, "neuroticism_big5": 0.315676}}}}"""

    parsed_input = json.loads(input_data)

    try:
        os.remove("templates/Index.html")
    except OSError:
        pass
    global fileTime
    fileTime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
    fileName = "templates/report_generated_{}.html".format(fileTime)
    text_file = open(fileName, "a")

    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    numberElements = int(parsed_input["num_lines"])
    for i in range(numberElements):
        nluEntities = parsed_input["line{}".format(
            i)]["nlu"]["nlu_entity_items"]
        if nluEntities != 0:
            for j in range(nluEntities):
                nlu_type = parsed_input["line{}".format(
                    i)]["nlu"]["entity{}".format(j)]["type"]
                nlu_text = parsed_input["line{}".format(
                    i)]["nlu"]["entity{}".format(j)]["text"]
                nlu_relevance = 100 * \
                    float(parsed_input["line{}".format(i)]
                          ["nlu"]["entity{}".format(j)]["relevance"])
                tableData_nlu = '''

                    <div class="panel panel-default">
                      <div class="panel-heading">
                        <h3 class="panel-title">
                              NLU Information
                          </h3>
                      </div>
                      <div class="panel-body">



                        <table class="table table-hover">
                            <thead>
                            <tr>
                            <th>Type</th>
                            <th>Text</th>
                            <Relevance</th>
                            </thead>
                          <tbody>
                            <tr>
                              <td width="30%">
                                {0:s}
                              </td>
                              <td width="30%">
                                {1:s}
                              </td>
                              <td width="40%">

                                <div class="progress">
                                  <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{2:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {2:f}%">

                                  </div>
                                </div>

                              </td>
                            </tr>


                          </tbody>
                        </table>




                      </div>
                      <div class="panel-footer">
                        NLU Information
                      </div>
                    </div>

                '''.format(nlu_type, nlu_text, nlu_relevance)

                # tableData_nlu = '<h3>Natural Language Information</h3><table class="table table-striped"><tr><th>Type</th><th>Text</th><th>Relevance</th></tr><tr><td>{}</td><td>{}</td><td>{}</td></tr></table>'.format(
                # nlu_type, nlu_text, nlu_relevance)
                # text_file.write(tableData_nlu)
                # the_data.append(tableData_nlu)
                big_string = big_string + tableData_nlu
        elif nluEntities == 0:
            pass
        text = parsed_input["line{}".format(i)]["text"]
        tone_emotion_anger = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["emotion"]["anger"])
        tone_emotion_joy = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["emotion"]["joy"])
        tone_emotion_fear = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["emotion"]["fear"])
        tone_emotion_sadness = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["emotion"]["sadness"])
        tone_emotion_disguist = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["emotion"]["disgust"])

        tone_social_extraversion = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["social"]["extraversion_big5"])
        tone_social_openness = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["social"]["openness_big5"])
        tone_social_conscientiousness = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["social"]["conscientiousness_big5"])
        tone_social_neuroticism = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["social"]["neuroticism_big5"])
        tone_social_agreeableness = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["social"]["agreeableness_big5"])

        tone_writing_analytical = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["writing"]["analytical"])
        tone_writing_confident = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["writing"]["confident"])
        tone_writing_tentative = 100 * float(parsed_input["line{}".format(
            i)]["tone"]["writing"]["tentative"])

        totalData = '''


        <div class="well">
          <h3>Recgonized Text: {0:s}</h3>
          <p>{1:s}</p>
          <div class="panel panel-default">
            <div class="panel-heading">
              <h3 class="panel-title">
                    Emotion Information
                </h3>
            </div>
            <div class="panel-body">



              <table class="table table-hover">

                <tbody>
                  <tr>
                    <td width="30%">
                      <strong>Anger</strong>
                    </td>
                    <td width="30%">
                      {2:.2f}%
                    </td>
                    <td width="40%">

                      <div class="progress">
                        <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{2:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {2:f}%">

                        </div>
                      </div>

                    </td>
                  </tr>

                  <tr>
                    <td width="30%">
                      <strong>Joy</strong>
                    </td>
                    <td width="30%">
                      {3:.2f}%
                    </td>
                    <td width="40%">

                      <div class="progress">
                        <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{3:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {3:f}%">

                        </div>
                      </div>

                    </td>
                  </tr>

                  <tr>
                    <td width="30%">
                      <strong>Fear</strong>
                    </td>
                    <td width="30%">
                      {4:.2f}%
                    </td>
                    <td width="40%">

                      <div class="progress">
                        <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{4:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {4:f}%">

                        </div>
                      </div>

                    </td>
                  </tr>

                  <tr>
                    <td width="30%">
                      <strong>Sadness</strong>
                    </td>
                    <td width="30%">
                      {5:.2f}%
                    </td>
                    <td width="40%">

                      <div class="progress">
                        <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{5:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {5:f}%">

                        </div>
                      </div>

                    </td>
                  </tr>
                  <tr>
                    <td width="30%">
                      <strong>Disguist</strong>
                    </td>
                    <td width="30%">
                      {6:.2f}%
                    </td>
                    <td width="40%">

                      <div class="progress">
                        <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{6:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {6:f}%">

                        </div>
                      </div>

                    </td>
                  </tr>

                </tbody>
              </table>




            </div>
            <div class="panel-footer">
              Emotion Information
            </div>
          </div>

        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">
                  Social Information
              </h3>
          </div>
          <div class="panel-body">



            <table class="table table-hover">

              <tbody>
                <tr>
                  <td width="30%">
                    <strong>Extraversion</strong>
                  </td>
                  <td width="30%">
                    {7:.2f}%
                  </td>
                  <td width="40%">

                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{7:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {7:f}%">

                      </div>
                    </div>

                  </td>
                </tr>

                <tr>
                  <td width="30%">
                    <strong>Openness</strong>
                  </td>
                  <td width="30%">
                    {8:.2f}%
                  </td>
                  <td width="40%">

                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{8:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {8:f}%">

                      </div>
                    </div>

                  </td>
                </tr>

                <tr>
                  <td width="30%">
                    <strong>Conscientiousness</strong>
                  </td>
                  <td width="30%">
                    {9:.2f}%
                  </td>
                  <td width="40%">

                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{9:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {9:f}%">

                      </div>
                    </div>

                  </td>
                </tr>

                <tr>
                  <td width="30%">
                    <strong>Neuroticism</strong>
                  </td>
                  <td width="30%">
                    {10:.2f}%
                  </td>
                  <td width="40%">

                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{10:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {10:f}%">

                      </div>
                    </div>

                  </td>
                </tr>
                <tr>
                  <td width="30%">
                    <strong>Agreeableness</strong>
                  </td>
                  <td width="30%">
                    {11:.2f}%
                  </td>
                  <td width="40%">

                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{11:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {11:f}%">

                      </div>
                    </div>

                  </td>
                </tr>

              </tbody>
            </table>




          </div>
          <div class="panel-footer">
        Social Information
          </div>
        </div>

        <div class="panel panel-default">
          <div class="panel-heading">
            <h3 class="panel-title">
                  Writing Information
              </h3>
          </div>
          <div class="panel-body">



            <table class="table table-hover">

              <tbody>
                <tr>
                  <td width="30%">
                    <strong>Analytical</strong>
                  </td>
                  <td width="30%">
                    {12:.2f}%
                  </td>
                  <td width="40%">

                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{12:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {12:f}%">

                      </div>
                    </div>

                  </td>
                </tr>

                <tr>
                  <td width="30%">
                    <strong>Confident</strong>
                  </td>
                  <td width="30%">
                    {13:.2f}%
                  </td>
                  <td width="40%">

                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{13:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {13:f}%">

                      </div>
                    </div>

                  </td>
                </tr>

                <tr>
                  <td width="30%">
                    <strong>Tentative</strong>
                  </td>
                  <td width="30%">
                    {14:.2f}%
                  </td>
                  <td width="40%">

                    <div class="progress">
                      <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="{14:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {14:f}%">

                      </div>
                    </div>

                  </td>
                </tr>

              </tbody>
            </table>




          </div>
          <div class="panel-footer">
            Emotion Information
          </div>
        </div>

        </div>


        '''.format(text, "test filejesfhskjhsdkjfhsdkfslfuheafgalefasgfg", tone_emotion_anger, tone_emotion_joy, tone_emotion_fear, tone_emotion_sadness, tone_emotion_disguist, tone_social_extraversion, tone_social_openness, tone_social_conscientiousness, tone_social_neuroticism, tone_social_agreeableness, tone_writing_analytical, tone_writing_confident, tone_writing_tentative)

        # totalData = tableData_text + tableData_emotion + \
        # tableData_social + tableData_writing
        # text_file.write(totalData)
        # the_data.append(totalData)
        big_string = big_string + totalData
    # text_file.close()

    the_string = write_output(the_data)

    textToWrite = '''
    <!DOCTYPE html>
    <html lang="en">

    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">

      <title>Bootstrap 3, from LayoutIt!</title>

      <meta name="description" content="Source code generated using layoutit.com">
      <meta name="author" content="LayoutIt!">

      <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
      <link href="bootstrap/css/style.css" rel="stylesheet">

    </head>

    <body>

      <div class="container-fluid">
        <div class="row">
          <div class="col-md-12">
            <div class="jumbotron">
              <h2>
    					Generated Report
    				</h2>
              <p>
                This report was generated on {} by [PRG_NAME]
              </p>
              <p>
                <a class="btn btn-primary btn-large" href="#">Save report</a>
              </p>
            </div>
    {}


          </div>
        </div>

        <script src="bootstrap/js/jquery.min.js"></script>
        <script src="bootstrap/js/bootstrap.min.js"></script>
        <script src="bootstrap/js/scripts.js"></script>
    </body>

    </html>

    '''.format(currentTime, big_string)
    text_file.write(textToWrite)


def openFile():
    fileName = "report_generated_{}".format(fileTime)
    fileLocation = "file://{}/templates/{}.html".format(os.getcwd(), fileName)
    webbrowser.open(fileLocation, new=2)


def write_output(the_data):
    the_string = ''
    for thing in the_data:
        string = the_string + thing
    return the_string


if __name__ == "__main__":
    makeFile()
    openFile()
