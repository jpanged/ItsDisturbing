import webbrowser
import os
import datetime
import json

the_data = []
# input_data = """{
#   "num_lines": 3,
#   "summary": "according to honor laws aviation there is no way P. should be able to fly its wings are too small to get its fat little body off the ground wanna kill you Alex ",
#   "lines": [
#     {
#       "line": {
#         "text": "according to honor laws aviation there is no way P. should be able to fly ",
#         "hash": "f363fea27a2171ec2ab3823c09990f6e",
#         "nlu": {
#           "nlu_entity_items": 0
#         },
#         "tone": {
#           "emotion": {
#             "anger": 0.039552,
#             "disgust": 0.106574,
#             "fear": 0.161657,
#             "joy": 0.049043,
#             "sadness": 0.124611
#           },
#           "writing": {
#             "analytical": 0.904038,
#             "confident": 0.0,
#             "tentative": 0.0
#           },
#           "social": {
#             "openness_big5": 0.292165,
#             "conscientiousness_big5": 0.763999,
#             "extraversion_big5": 0.660921,
#             "agreeableness_big5": 0.671976,
#             "neuroticism_big5": 0.967221
#           }
#         }
#       }
#     },
#     {
#       "line": {
#         "text": "its wings are too small to get its fat little body off the ground ",
#         "hash": "1ae222a221d64538a878d46649e5f468",
#         "nlu": {
#           "nlu_entity_items": 0
#         },
#         "tone": {
#           "emotion": {
#             "anger": 0.193606,
#             "disgust": 0.437186,
#             "fear": 0.325455,
#             "joy": 0.021466,
#             "sadness": 0.321767
#           },
#           "writing": {
#             "analytical": 0.0,
#             "confident": 0.0,
#             "tentative": 0.0
#           },
#           "social": {
#             "openness_big5": 0.309621,
#             "conscientiousness_big5": 0.342797,
#             "extraversion_big5": 0.37454,
#             "agreeableness_big5": 0.26146,
#             "neuroticism_big5": 0.342685
#           }
#         }
#       }
#     },
#     {
#       "line": {
#         "text": "wanna kill you Alex",
#         "hash": "492465e206ac6aa56a940cf02b109b6c",
#         "nlu": {
#           "nlu_entity_items": 1,
#           "entity0": {
#             "type": "Person",
#             "text": "Alex",
#             "relevance": 0.33,
#             "count": 1
#           }
#         },
#         "tone": {
#           "emotion": {
#             "anger": 0.756906,
#             "disgust": 0.135541,
#             "fear": 0.117287,
#             "joy": 0.012102,
#             "sadness": 0.21201
#           },
#           "writing": {
#             "analytical": 0.0,
#             "confident": 0.0,
#             "tentative": 0.0
#           },
#           "social": {
#             "openness_big5": 0.056399,
#             "conscientiousness_big5": 0.286041,
#             "extraversion_big5": 0.443854,
#             "agreeableness_big5": 0.545598,
#             "neuroticism_big5": 0.120981
#           }
#         }
#       }
#     }
#   ]
# }"""


def makeFile(input_data):

    big_string = ''

    input_data = input_data
    parsed_input = json.loads(input_data)

    try:
        os.remove("templates/Index.html")
    except OSError:
        pass
    global fileTime
    fileTime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")
    fileName = "templates/report_generated_{}.html".format(fileTime)
    text_file = open(fileName, "a+")

    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    tot_anger = []
    tot_joy = []
    tot_fear = []
    tot_sadness = []
    tot_disgust = []
    tot_extraversion = []
    tot_openness = []
    tot_conscientiousness = []
    tot_neuroticism = []
    tot_agreeableness = []
    tot_analytical = []
    tot_confident = []
    tot_tentative = []

    numberElements = int(parsed_input["num_lines"])
    print(type(parsed_input))
    print(parsed_input["lines"][2]["line"]["nlu"])
    for i in range(numberElements):
        nluEntities = parsed_input["lines"][i]["line"]["nlu"]["nlu_entity_items"]
        if nluEntities != 0:
            for j in range(nluEntities):
                nlu_type = parsed_input["lines"][i]["line"]["nlu"]["entity{}".format(j)]["type"]
                nlu_text = parsed_input["lines"][i]["line"]["nlu"]["entity{}".format(j)]["text"]
                nlu_relevance = 100 * \
                    float(parsed_input["lines"][i]["line"]
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
                            <th>Relevance</th>
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
                                  <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{2:.2f}" aria-valuemin="0" aria-valuemax="100" style="min-width: 4em; width: {2:f}%%;">
                                    {2:.0f}%
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
        text = parsed_input["lines"][i]["line"]["text"]
        str_to_ret = ""

        tone_emotion_anger = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["emotion"]["anger"])
        if tone_emotion_anger > 40.0:
            str_to_ret += "<br>Anger: the response to injustice, conflict, humiliation, negligence or betrayal."
        tot_anger.append(tone_emotion_anger)

        tone_emotion_joy = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["emotion"]["joy"])
        if tone_emotion_joy > 40.0:
            str_to_ret += "<br>Joy: the response to enjoyment, satisfaction, and pleasure"
        tot_joy.append(tone_emotion_joy)

        tone_emotion_fear = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["emotion"]["fear"])
        if tone_emotion_fear > 40.0:
            str_to_ret += "<br>Fear: the response to impending danger"
        tot_fear.append(tone_emotion_fear)

        tone_emotion_sadness = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["emotion"]["sadness"])
        if tone_emotion_sadness > 40.0:
            str_to_ret += "<br>Sadness: the response to loss and disadvantage"
        tot_sadness.append(tone_emotion_sadness)

        tone_emotion_disgust = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["emotion"]["disgust"])
        if tone_emotion_disgust > 40.0:
            str_to_ret += "<br>Disgust: the response to something offensive or unpleasant"
        tot_disgust.append(tone_emotion_disgust)

        tone_social_extraversion = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["social"]["extraversion_big5"])
        if tone_social_extraversion > 40.0:
            str_to_ret += "<br>Extraversion: the tendency to seek stimulation in the company of others"
        tot_extraversion.append(tone_social_extraversion)

        tone_social_openness = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["social"]["openness_big5"])
        if tone_social_openness > 40.0:
            str_to_ret += "<br>Openness: the extent a person is willing to experience a variety of activities"
        tot_openness.append(tone_social_openness)

        tone_social_conscientiousness = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["social"]["conscientiousness_big5"])
        if tone_social_conscientiousness > 40.0:
            str_to_ret += "<br>Conscientiousness: the tendency to act in an organized or thoughtful way"
        tot_disgust.append(tone_social_conscientiousness)

        tone_social_neuroticism = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["social"]["neuroticism_big5"])
        if tone_social_neuroticism > 40.0:
            str_to_ret += "<br>Neuroticism: the extent a person's emotion is sensitive to the environment"
        tot_neuroticism.append(tone_social_neuroticism)

        tone_social_agreeableness = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["social"]["agreeableness_big5"])
        if tone_social_agreeableness > 40.0:
            str_to_ret += "<br>Agreeableness: the tendency to be compassionate and cooperative towards others"
        tot_agreeableness.append(tone_social_agreeableness)

        tone_writing_analytical = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["writing"]["analytical"])
        if tone_writing_analytical > 40.0:
            str_to_ret += "<br>Analytical: a person's reasoning and analytical attitude about things"
        tot_analytical.append(tone_writing_analytical)

        tone_writing_confident = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["writing"]["confident"])
        if tone_writing_confident > 40.0:
            str_to_ret += "<br>Confident: a person's degree of certainty"
        tot_confident.append(tone_writing_confident)

        tone_writing_tentative = 100 * float(parsed_input["lines"][i]["line"]
            ["tone"]["writing"]["tentative"])
        if tone_writing_tentative > 40.0:
            str_to_ret += "<br>Tentative: a person's degree of inhibition"
        tot_tentative.append(tone_writing_tentative)


        totals = '''

            <div class="well">
              <div class="panel panel-default">
                <div class="panel-heading">
                  <h3 class="panel-title">
                        Aggregated Totals
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
                            <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{2:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {2:f}%">

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
                            <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{3:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {3:f}%">

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
                            <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{4:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {4:f}%">

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
                            <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{5:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {5:f}%">

                            </div>
                          </div>

                        </td>
                      </tr>
                      <tr>
                        <td width="30%">
                          <strong>Disgust</strong>
                        </td>
                        <td width="30%">
                          {6:.2f}%
                        </td>
                        <td width="40%">

                          <div class="progress">
                            <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{6:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {6:f}%">

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
                          <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{7:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {7:f}%">

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
                          <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{8:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {8:f}%">

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
                          <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{9:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {9:f}%">

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
                          <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{10:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {10:f}%">

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
                          <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{11:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {11:f}%">

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
                          <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{12:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {12:f}%">

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
                          <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{13:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {13:f}%">

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
                          <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{14:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {14:f}%">

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

            '''.format("", "", makeAverages(tot_anger),
                       makeAverages(tot_joy),
                       makeAverages(tot_fear),
                       makeAverages(tot_sadness),
                       makeAverages(tot_disgust),
                       makeAverages(tot_extraversion),
                       makeAverages(tot_openness),
                       makeAverages(tot_conscientiousness),
                       makeAverages(tot_neuroticism),
                       makeAverages(tot_agreeableness),
                       makeAverages(tot_analytical),
                       makeAverages(tot_confident),
                       makeAverages(tot_tentative))

        totalData = '''


        <div class="well">
          <h3>Recognized Text: {0:s}</h3>
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
                        <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{2:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {2:f}%">

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
                        <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{3:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {3:f}%">

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
                        <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{4:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {4:f}%">

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
                        <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{5:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {5:f}%">

                        </div>
                      </div>

                    </td>
                  </tr>
                  <tr>
                    <td width="30%">
                      <strong>Disgust</strong>
                    </td>
                    <td width="30%">
                      {6:.2f}%
                    </td>
                    <td width="40%">

                      <div class="progress">
                        <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{6:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {6:f}%">

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
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{7:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {7:f}%">

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
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{8:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {8:f}%">

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
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{9:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {9:f}%">

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
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{10:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {10:f}%">

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
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{11:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {11:f}%">

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
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{12:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {12:f}%">

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
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{13:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {13:f}%">

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
                      <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="{14:.2f}" aria-valuemin="0" aria-valuemax="100" style="width: {14:f}%">

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


        '''.format(text, str_to_ret, tone_emotion_anger, tone_emotion_joy, tone_emotion_fear, tone_emotion_sadness, tone_emotion_disgust, tone_social_extraversion, tone_social_openness, tone_social_conscientiousness, tone_social_neuroticism, tone_social_agreeableness, tone_writing_analytical, tone_writing_confident, tone_writing_tentative)

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

      <title>Generated Report</title>

      <link href="src/css/bootstrap.min.css" rel="stylesheet">
      <link href="src/css/style.css" rel="stylesheet">

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
                This report was generated on {} by [It's Disturbing],
              </p>
              <h6>
                Alex Garcia, Celestine Co, Dominic Gaiero, & Josiah Pang
            </h6>
            <p>{}</p>
              <!--<p>
                <a class="btn btn-primary btn-large" href="#">Save report</a>
              </p>-->
            </div>
    {}


          </div>
        </div>

        <script src="src/js/jquery.min.js"></script>
        <script src="src/js/bootstrap.min.js"></script>
        <script src="src/js/scripts.js"></script>
    </body>

    </html>

    '''.format(currentTime, totals, big_string)
    text_file.write(textToWrite)
    text_file.close()


def openFile():
    fileName = "report_generated_{}".format(fileTime)
    fileLocation = "file://{}/templates/{}.html".format(os.getcwd(), fileName)
    webbrowser.open(fileLocation, new=2)


def makeAverages(inputList):
    length = 0
    total = 0
    for thing in inputList:
        total += thing
        length += 1
    if length == 0:
        return 0
    else:
        average = total / length
        return average

def write_output(the_data):
    the_string = ''
    for thing in the_data:
        string = the_string + thing
    return the_string


def outPutFile(input_data):
    input_data = input_data
    makeFile(input_data)
    openFile()


if __name__ == "__main__":
    outPutFile(input_data)
