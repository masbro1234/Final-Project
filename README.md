# ⚽ SoccerStat: Premier League Stats Web App  
**By Chris Gravagna and Mason Brown**

---

## 🎯 Big Idea & Project Goals

SoccerStat is a simple, clean web application that lets users search for Premier League teams or players and instantly view their statistics for a specific season. 

As lifelong soccer fans, we wanted to create something that felt natural and useful — a site where anyone could look up a favorite player or club and quickly see performance stats in a no-frills, beginner-friendly way. Some people have a hard time finding exactly how a team or player did during a specific season, so we tried to be the answer to that. 

---

## 👨‍💻 User Instructions

1. Visit the homepage (screenshot below).
2. Enter either a **player name** or **team name**.
3. Choose the **search type** from the dropdown (player or team).
4. Enter a **season year** (e.g., `2023`) — recent years work best.
5. Click **Search** to view results!

🟡 *Note:* The app uses the free tier of the API-Football service, which only supports recent seasons (usually 2022–2023). Older years may return no results.

---

## ⚙️ How It Works (Implementation Overview)

- **Framework:** Python with Flask
- **Data Source:** API-Football ([https://api-football.com])
- **Team Stats Shown:** Wins, Draws, Losses, Goals For, Goals Against + Team Logo
- **Player Stats Shown:** Goals, Assists, Team Name + Player Photo

### Technical Flow:
- The Flask backend takes in user form data (`query`, `search_type`, and `season`).
- Based on the search type, it queries different endpoints from API-Football.
- The JSON response is parsed and passed into a Jinja2 HTML template.
- The results page renders stats and logos/photos dynamically based on the response.

---

## 🖼 Visual Results

### 🔎 Homepage
The user enters the player or team name, selects the type and season, then clicks search.

![Home Page](https://github.com/masbro1234/Final-Project/blob/main/Project.JPG?raw=true)

---

### 🏟 Team Results (Manchester City, 2023)
Displays match record and stats, with a clean layout and team logo.

![Team Result](https://github.com/masbro1234/Final-Project/blob/main/Project2.JPG?raw=true)

---

### 👤 Player Results (Erling Haaland, 2023)
Shows goals, assists, and club info, plus an official player photo.

![Player Result](https://github.com/masbro1234/Final-Project/blob/main/Project3.JPG?raw=true)

---

## 📌 Known Limitations

- ❗ **Season Access Limit:** Only recent Premier League seasons (2022, 2023) are available on the free API plan.
- 📉 **No Stats = No Results:** If a player didn’t play that year or isn’t spelled exactly right, the API won’t return data.
- 🌐 **Local Only:** Currently hosted at `http://127.0.0.1:5000/` — for public access, you’d need to use a tool like ngrok or Render.

---

## 💭 Final Reflection & Takeaways

This was more than just a coding assignment — it was the first time we fully built and styled a web app from scratch. We had to debug confusing JSON objects, handle errors from missing data, and design routes that were beginner-friendly but still functional.

Most importantly, we walked away with:

- Confidence using Flask and APIs in real-world settings
- A better understanding of templating logic with Jinja
- A working, shareable project that shows our growth
