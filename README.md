# Exercise for Aggregating Data from websites


Idea: exercise in python for building an end-to-end data workflow
Purpose: Prepare data for analysis on data received
Application: collect data on trading transactions in real-time, then update a report or dashboard (interactive and updates as data flows). Track continuously updating data, as well as certain events, into the real-time database

Workflow:
- open website with trading transactions (TSX, or something FICC related would be better)
- log in if necessary (having an account may allow for customizations)
- continuously monitor the site

- refresh page (or don't since the site does it automatically)
- if nothing new, report "nothing"
- when there is an update of interest (a trade, etc.) scrape the contents and report "something"
- scraped contents moved into database (real time ideal)

(Alternatively: get data from an API if available, then move into real time database)


usage for end results:
- extract information from database for analysis, reporting, etc.

Things never done before:
- (2020/09/10): set up virual environment with Hydrogen for Atom, with pipenv, for interactive coding experience (to replace Jupyter Notebooks). Also went through the process of setting up virtual environments at the beginning of a project, as best practice.
