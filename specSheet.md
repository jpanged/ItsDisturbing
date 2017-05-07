# Spec Sheet

Input: Voice data
Upload voice data to Watson cloud
Watson Cloud analyzes data to determine:
* Tone
* Content

Output report (PDF)
* Voice to text transcription of event
* What data contains
* Red flags
* Possible actions that can be taken (and why they should be taken)

Log output to database


Web Output
* Browse logs
* Listen to input


Objectives:
* SpeechToText: convert audio files into text files
* ToneAnalyzer: analyze negativities from text files into numerical scores
* NaturalLanguageUnderstanding: analyze semantic features of text input
    - Analyze text for "redflag" keywords
    - May involve potential actions the user will take
* Generate report on the inputted audio/text file.
  * Add progress bar for visualizations of each category.


Look for:
* Danger to Self
  * Words or actions showing intent to commit suicide or bodily harm.
  * Words or actions indicating gross disregard for personal safety.
  * Words or actions indicating a specific plan to suicide.
  * Means available to carry out suicide plan (i.e. pills, firearms present or
available).
* Danger to Others
  * Threats against particular individuals.
  * Attempts to harm certain individuals.
  * Means available to carry out threats or to repeat attempts (i.e.firearms, or other weapons).
  * Expressed intention or attempts to engage in dangerous activity
* Grave disiblity
  * Signs of malnourishment or dehydration.
  * Inability to articulate a plan for obtaining food.
  * No food available in the house or at hand if not in a house.
  * Irrational beliefs about food that is available (i.e. it’s poisoned, inedible, etc.)
  * Destruction or giving away of clothing to the point where the person cannot clothe themselves.
  * Inability to formulate a reasonable plan to obtain shelter.
