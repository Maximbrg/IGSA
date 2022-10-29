# IGSA

Run Instructions:
1. First download the data and put it in the right folder: <br/>
  1.1 For ClassDiagram download the ecore files from http://mar-search.org/status and put these files into the folder ../classDiagrm/Experiment_1/ecore/<br/>
  1.2 For ME-MAP download the json files from https://drive.google.com/drive/folders/1Hua5tx6yqdkcI0PSq7J4Ggp23m2o4ihb?usp=share_link and put these files into the folder ../meMap/maps/<br/>
  1.1 For wikiHow download the ecore files from https://drive.google.com/drive/folders/12fMRokLqHziYXFS19HH50iFavLULL-30?usp=sharing and put these files into the folder ../wikiHow/maps/
 
 2. Update the following settings if needed in Framework/ThresholdSettings/IGSASettings
- domain:: 0 - classDiagram, 1 - ME-MAP, 2- wikiHow
- createVector:: should be False if you run the a domain expriement for the first time otherwise, True
- algorithm:: 0 - IGSA, 1 - A* Semantic
- path:: the path to the project directory

3. Run the main.py file
