# It's Disturbing
### Is it?

## Description
Here in the United States, studies show that 10-35% of the population will exhibit domestic violence on their partners, 
yet less than 1% of domestic violence cases are ever reported to police. This is a result of many different factors,
as victims are often in love with, have an intense fear of, or may be financially dependent
on the abuser. Some victims do not even view their current situation as a physically abusive relationship, keeping them stuck 
in that unhealthy lifestyle for years.

Our project "It's Disturbing", uses Watson's Speech and Text analysis API to detect potential cases of physical and verbal abuse, and generate a report to potentially be sent out to doctors, lawyers, specified trusted friends, health centers, or the police. 

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


## Speech to Text
The IBM Watson™ Speech to Text service enables speech recognition capabilities.
The service transcribes speech from various languages and audio formats to text with low latency.


## Installation

To install, use the command line.

```bash
$ pip install watson_developer_cloud/
$ git clone https://github.com/jpanged/siliconhacks2017/
```

Once you have cloned the repository, navigate to the 'main_analyzer' directory.

```bash
$ cd main_analyzer/
$ cd main_analyzer.py .WAV_FILE
```
or

```bash
$ cd main_analyzer/
$ cd main_analyzer.py .TXT_FILE
```
