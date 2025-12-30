from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Tech Bots | Developer</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    height: 100vh;
    background: #050505;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
}

/* RGB BORDER */
.rgb-border {
    padding: 3px;
    border-radius: 26px;
    background: linear-gradient(
        270deg,
        red, orange, yellow, lime, cyan, blue, magenta, red
    );
    background-size: 600% 600%;
    animation: rgb 6s linear infinite;
}

@keyframes rgb {
    0% { background-position: 0% 50%; }
    100% { background-position: 600% 50%; }
}

.card {
    width: 390px;
    padding: 28px;
    border-radius: 24px;
    background: rgba(15,15,15,0.92);
    backdrop-filter: blur(18px);
    text-align: center;
}

.avatar {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    border: 3px solid cyan;
    box-shadow: 0 0 20px cyan;
    object-fit: cover;
    margin-bottom: 12px;
}

.name {
    font-size: 22px;
    font-weight: 600;
}

.username {
    color: cyan;
    font-size: 14px;
    margin-bottom: 10px;
}

.section {
    margin-top: 18px;
    padding-top: 12px;
    border-top: 1px solid rgba(255,255,255,0.1);
    text-align: left;
}

.section h3 {
    font-size: 15px;
    margin-bottom: 8px;
    color: #00ffd5;
}

.section p, .section li {
    font-size: 13px;
    opacity: 0.95;
    line-height: 1.6;
}

.commands {
    list-style: none;
    padding: 0;
    margin: 0;
}

.commands li {
    display: flex;
    justify-content: space-between;
    padding: 6px 0;
    border-bottom: 1px dashed rgba(255,255,255,0.08);
}

.commands li span {
    color: #9ff;
}

.btn {
    display: inline-block;
    margin-top: 16px;
    padding: 11px 26px;
    border-radius: 30px;
    background: linear-gradient(135deg, #00ffd5, #00ff88);
    color: #000;
    font-weight: 600;
    text-decoration: none;
    box-shadow: 0 0 20px rgba(0,255,200,0.8);
    transition: 0.3s;
}

.btn:hover {
    transform: scale(1.08);
    box-shadow: 0 0 30px rgba(0,255,200,1);
}

.footer {
    margin-top: 14px;
    font-size: 12px;
    opacity: 0.6;
    text-align: center;
}
</style>
</head>

<body>

<div class="rgb-border">
<div class="card">

    <img class="avatar" src="https://www.catbox.to/pF5HWUHlYWGd3TO/preview">
    <div class="name">Toxic Dev</div>
    <div class="username">@ikbug</div>

    <div class="section">
        <h3>🤖 Bot Info</h3>
        <p>
            Name: <b>Siya Music</b><br>
            Version: <b>v2.3</b><br>
            Language: <b>Python</b><br>
            Library: <b>Pyrogram</b><br>
            Status: <b>Online 24/7</b>
        </p>
    </div>

    <div class="section">
        <h3>📜 Commands</h3>
        <ul class="commands">
            <li><span>/start</span> <small>Start the bot</small></li>
            <li><span>/help</span> <small>Get help menu</small></li>
            <li><span>/ping</span> <small>Check bot status</small></li>
            <li><span>/play</span> <small>song play</small></li>
            <li><span>/settings</span> <small>Bot settings</small></li>
        </ul>
    </div>

    <div class="section">
        <h3>👨‍💻 Developer</h3>
        <p>
            Python • Telegram Bots • Web Dev<br>
            Building bots that hit different ⚡
        </p>
    </div>

    <a class="btn" href="https://t.me/ikbug" target="_blank">
        🚀 Contact on Telegram
    </a>

    <div class="footer">
        Tech Bots • Official Developer Page
    </div>

</div>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run()
