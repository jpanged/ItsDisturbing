# It's Disturbing
### Is it?

UPDATE: Winner of SiliconHacks 2017 Most Technically Challenging Hack & #HackHarassment Challenge (Solution against online harassment)

HackerEarth Submission: https://siliconhacks.hackerearth.com/sprints/siliconhacks/dashboard/pleasantonAndThePlebs/submission/

![logo](https://github.com/jpanged/siliconhacks2017/blob/master/graphics/bluemix-logo-right.png)


## Description
Here in the United States, studies show that 10-35% of the population will exhibit domestic violence on their partners, 
yet less than 1% of domestic violence cases are ever reported to police. This is a result of many different factors,
as victims are often in love with, have an intense fear of, or may be financially dependent
on the abuser. Some victims do not even view their current situation as a physically abusive relationship, keeping them stuck 
in that unhealthy lifestyle for years.

Our project aims to analyze speech and text input for potential red flags related to actions contained in WIC code 5150, PC 261, PC 273, and other similarly related behaviors. It uses Watson's Speech and Text analysis API to detect potential cases of physical and verbal abuse, and generate a report to potentially be sent out to doctors, lawyers, specified trusted friends, health centers, or the police. Examples include self harm, harm to others, and sexual assault. It accomplishes this by looking into the tone of a sentence through emotions such as anger or fear. Along with that, it checks if entities are contained in the same sentence. Entities include things such as People or Places. If a high level of negative emotions are connected to an entity, we believe a reg flag can be raised.

We use the Watson API to process our speech and text, specifically SpeechToText, ToneAnalyzer, and NaturalLanguageUnderstanding. The flow of data goes from speech -> text -> tone/entity -> output

Initially, we wanted to have the service built into a more interactive webapp where users could upload their own audio or text. In addition, we thought it would be cool if hardware could be integrated into the code, where a microphone could take live input, process it, and return a report. We quickly realized, however, that the scope of our time along with understanding and knowledge created a disparity between what we could do and what we wanted to do. Eventually, we just aimed to have some sort of working speech/text processor that outputs data. In addition, we wanted to have the results on a .tech domain (itsdisturbing.tech), but get.tech never got back to us. When they do, it would not be too difficult to accomplish what we want with the domain.

Currently, our data outputs to a HTML file formatted with Bootstrap. It shows the levels of different tones along with any entities that are identified. For the future, we would want to structure the output in a more useful way to the user. This would include a summary of the entire text/speech's findings as opposed to just sentence by sentence. An educational component would also be a logical next step, where resources would be available if red flags were raised. With regards to red flags, we also need to create a better way to relate tone and entities to quantify the data.

As our entire team consists of first years, we realize we do not have much of the technical competence yet for some implementations. Our goal for SiliconHacks was just to start and finish a project that could work, and get more experience through the learn by doing model. We are happy to have something to show for our weekend, and this is definitely a project that can be worked on past this weekend.


![toneicon](https://github.com/jpanged/siliconhacks2017/blob/master/graphics/nlu.png)
## Natural Language Understanding
The IBM Watson™ Natural Language Understanding service uses natural language processing to analyze semantic features of any text.

### Entities
Identify people, cities, organizations, and many other types of entities in your text.

| Names     | Description                                                                                             |
| --------- |:------------------------------------------------------------------------------------------------------- |
| Relevance | Relevance score ranging from 0 to 1. A 0 means it's not relevant, and a 1 means it's highly relevant.   |
| Text      | Entity                                                                                                  |
| Type      | Entity type                                                                                             |
| Count     | Number of times the entity is mentioned in the text                                                     |


![toneicon](https://github.com/jpanged/siliconhacks2017/blob/master/graphics/toneanalyzer.png)
## Tone Analyzer
The IBM Watson™ Tone Analyzer service uses linguistic analysis to detect communication tones in written text along three major categories: emotion, language, and social.

### Emotion
Emotional tone measures different types of emotions and feelings that people express.

####    Joy
    Joy or happiness has shades of enjoyment, satisfaction and pleasure.
    There is a sense of well-being, inner peace, love, safety and contentment.

####    Fear
    A response to impending danger.
    It is a survival mechanism that is a reaction to some negative stimulus.
    It may be a mild caution or an extreme phobia.
    
####    Sadness
    Indicates a feeling of loss and disadvantage.
    When a person can be observed to be quiet, less energetic and withdrawn.
    It may be inferred that sadness exists.
    
####    Disgust
    An emotional response of revulsion to something considered offensive or unpleasant.
    It is a sensation that refers to something revolting.
    
####    Anger
      Evoked due to injustice, conflict, humiliation, negligence or betrayal.
      If anger is active, the individual attacks the target, verbally or physically.
      If anger is passive, the person silently sulks and feels tension and hostility.
    
    

### Langauge
Describes perceived writing style.

####    Analytical
    A person's reasoning and analytical attitude about things.
 Low Scores                                | High Scores                                                 |
 ----------------------------------------- |:----------------------------------------------------------- |
 Little or no evidence of analytical tone. | Intellectual, rational, systematic, emotionless, impersonal |

####    Confidence
    A person's degree of certainty.
| Low Scores                                   | High Scores                              |
| -------------------------------------------- |:---------------------------------------- |
| Little or no evidence of confidence in tone. | Assured, collected, hopeful, egotistical |

####    Tentative
    A person's degree of inhibition.
| Low Scores                                      | High Scores                          |
| ----------------------------------------------- |:------------------------------------ |
| Little or no evidence of tentativeness in tone. | Questionable, doubtful, or debatable |



### Social
Watson quantifies emotion using the five factor model (FFM) aka the Big Five personality traits:

####    Openness
    The extent a person is willing to experience a variety of activities.
| Low Scores    | High Scores   |
| ------------- |:------------- |
| Down-to-earth | Imaginative   |
| Uncreative    | Creative      |
| Conventional  | Original      |
| Uncurious     | Curious       |
  
####    Conscientiousness
    The tendency to act in an organized or thoughtful way.
| Low Scores    | High Scores    |
| ------------- |:-------------- |
| Negligent     | Conscientious  |
| Lazy          | Hard-working   |
| Disorganized  | Well-organized |
| Late          | Punctual       |

####    Extraversion
    The tendency to seek stimulation in the company of others.
| Low Scores    | High Scores   |
| ------------- |:------------- |
| Loner         | Joiner        |
| Quiet         | Talkative     |
| Passive       | Active        |
| Reserved      | Affectionate  |

####    Agreeableness
    The tendency to be compassionate and cooperative towards others.
| Low Scores    | High Scores   |
| ------------- |:------------- |
| Suspicious    | Trusting      |
| Critical      | Lenient       |
| Ruthless      | Soft-hearted  |
| Irritable     | Good-natured  |

####    Neuroticism
    The extent a person's emotion is sensitive to the environment.
| Low Scores    | High Scores    |
| ------------- |:-------------- |
| Calm          | Worried        |
| Even-tempered | Temperamental  |
| Comfortable   | Self-conscious |
| Unemotional   | Emotional      |


![toneicon](https://github.com/jpanged/siliconhacks2017/blob/master/graphics/speechtotext.png)
## Speech to Text
The IBM Watson™ Speech to Text service enables speech recognition capabilities.
The service transcribes speech from various languages and audio formats to text with low latency.


## Installation

To install, use the command line.

```bash
$ pip install watson_developer_cloud/
$ git clone https://github.com/jpanged/siliconhacks2017.git
```

Once you have cloned the repository, navigate to the 'main_analyzer' directory.

```bash
$ cd main_analyzer/
$ python3 main_analyzer.py .WAV_FILE
```
or

```bash
$ cd main_analyzer/
$ python3 main_analyzer.py .TXT_FILE
```

## API Resources, IBM Watson™

- [Natural Language Understanding](https://www.ibm.com/watson/developercloud/natural-language-understanding/api/v1/)
- [Tone Analyzer](https://www.ibm.com/watson/developercloud/tone-analyzer/api/v3/)
- [Speech to Text](https://www.ibm.com/watson/developercloud/speech-to-text/api/v1/)
