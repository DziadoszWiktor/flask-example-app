from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>W3.CSS Template</title>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>
    </head>
    <body>
    <div class='w3-top'>
        <div class='w3-bar w3-white w3-wide w3-padding w3-card'>
            <a href='#home' class='w3-bar-item w3-button'><b>EX</b>Flask-App</a>
            <div class='w3-right w3-hide-small'>
              <a href='#projects' class='w3-bar-item w3-button'>Projects</a>
              <a href='#about' class='w3-bar-item w3-button'>About</a>
              <a href='#contact' class='w3-bar-item w3-button'>Contact</a>
            </div>
        </div>
    </div>
    <header class='w3-display-container w3-content w3-wide' style='max-width:1500px;' id='home'>
      <img class='w3-image' src='/w3images/architect.jpg' alt='Architecture' width='1500' height='800'>
          <div class='w3-display-middle w3-margin-top w3-center'>
            <h1 class='w3-xxlarge w3-text-white'><span class='w3-padding w3-black w3-opacity-min'><b>EX</b></span> <span class='w3-hide-small w3-text-light-grey'>Flask-App</span></h1>
          </div>
    </header>
    <div>
        <h1 style='text-align:center'></h1>
    </div>
    </body>
    </html>"""
