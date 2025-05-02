# Team Project
 
 Chris Gravagna and Mason Brown

# Project Proposal: SoccerStat — A Chill Soccer Stats Web App

## 1. The Big Idea

So our idea is called **SoccerStat** — it’s a simple website where you can look up soccer players or teams and get some stats, like goals, assists, match history, etc. We’re both big soccer fans and played a lot growing up, so we thought it’d be fun to build something around that. 

- **Minimum Viable Product (MVP):**
  - A working Flask app where you can type in a team or player and get some basic stats from either a dataset or a soccer API.
  - Clean layout using Flask templates and HTML.
  - Display things like goals, win/loss record, and maybe recent matches.

- **Stretch Goal:**
  - Add some visualizations using `matplotlib` or `plotly`.  
        ##ChatGPT helped us come up with this idea — we thought graphs would be a cool way to show the data##
  - Let users compare two players or teams.
  - Maybe add a login feature where people can save their favorite teams (if we’re feeling bold).

## 2. Learning Objectives

- **Shared Goals:**
  - Get better at Python and actually build a full project with Flask.
  - Learn how to pull data from APIs or CSVs and turn it into something useful.
  - Practice using GitHub more.

- **Individual Goals:**
  - *Chris:* Wants to improve at frontend stuff like designing templates and making the site look clean.
  - *Me (Mason):* Focusing on backend stuff like getting the data, doing the logic, and setting up Flask routes.

We’re in a bunch of classes together and see eachother almost every day, so working on this will just be a natural part of our week.

## 3. Implementation Plan

We’re using **Flask** to build the app because that’s what we’ve been using in class and it’s pretty beginner-friendly. For the data, we’re gonna try APIs like [Football-Data.org](https://www.football-data.org/) or [API-Football](https://www.api-football.com/), but can also find some CSV datasets from [Kaggle](https://www.kaggle.com/) just in case.

We’ll use **Pandas** to clean and process the data, and if we do graphs, we’ll try out **matplotlib** or **plotly** as we also stated above.  
    ##We got this suggestion from ChatGPT when we asked how to show soccer stats visually##

## 4. Project Schedule

| Week | What We’re Doing |
|------|-------------------|
| Week 1 | Set up the Flask project, test out datasets or APIs |
| Week 2 | Build the search feature and show basic stats |
| Week 3 | Work on organizing the data and improving the display |
| Week 4 | Try to add comparison feature + charts if we’re ready |
| Week 5 | Final cleanup and bug fixes if needed|

## 5. Collaboration Plan

Since we hang out almost every day, our plan is just to meet up a few times a week and code together in person — whether it’s in class or wherever. We’ll split up the tasks a bit(Chris = frontend, Mason = backend), but we’ll help each other when needed. We’ll use GitHub to share code. 

## 6. Risks and Limitations

- Some of the APIs might limit how much data we can get, so we’re keeping CSV files as a backup plan.
- Charts and comparisons could be time-consuming, so we’re okay dropping them if we run out of time.

## 7. Extra Course Content That’d Be Helpful

- More help on how to work with APIs and format JSON data
- Tips for making Flask templates look nicer without overcomplicating things

---

Overall, we’re just excited to build something around a sport that we care about and we both think it is so cool to be able to code your own website and not use a generater. 