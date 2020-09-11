# Exercise for Aggregate Data from Prolific


Idea: exercise in python for building an end-to-end data workflow
Purpose: Prepare data for analysis on the studies received
Application: collect data on the studies sent to me on the studies website, Prolific, so it can be later analyzed

Workflow:
- open https://app.prolific.co/studies and ensure logged in as me
- continuously monitor prolific website
- refresh page (or don't since the site does it automatically)
- if nothing, report "nothing"
- when there is an update of interest (i.e new job) scrape the contents and report "something"
- scraped contents moved into database (real time ideal)

usage for end results:
- extract information from database for analysis, reporting, etc.