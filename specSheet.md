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
* * Generate report on the inputted audio/text file.
