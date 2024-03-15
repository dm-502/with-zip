<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Project Brief</title>
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #FF5733;
        color: #333;
    }
    .container {
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        text-align: center; /* Centering the button */
    }
    h1, p {
        margin: 0 0 20px;
    }
    nav {
        background-color: #333;
        padding: 10px 0;
        text-align: center; /* Centering the menu */
    }
    nav ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        display: inline-block; /* Make the menu horizontal */
    }
    nav ul li {
        display: inline;
        margin-right: 20px;
    }
    nav ul li a {
        color: #fff;
        text-decoration: none;
        font-size: 16px;
    }
    .big-button {
        padding: 20px 50px;
        font-size: 24px;
        background-color: #333;
        color: #fff;
        border: none;
        cursor: pointer;
    }
</style>
</head>
<body>
    <nav>
        <ul>
            <li><a href="Meeting_the_brief.html">Meeting the brief</a></li>
            <li><a href="Overview.html">Overview</a></li>
            <li><a href="Requirements.html">Requirements</a></li>
            <li><a href="Plan_and_design.html">Plan and design</a></li>
            <li><a href="Implementation.html">Implementation</a></li>
            <li><a href="Testing.html">Testing</a></li>
            <li><a href="Evaluation.html">Evaluation</a></li>
            <li><a href="References.html">References</a></li>
        </ul>
    </nav>
    <div class="container">
        <h1>Project Brief</h1>
        <p>This website aims to showcase a brief overview of my Computer Science Coursework Project Brief.</p>
        <h2>Exam number:</h2>
        <p>111996</p>
        <button class="big-button" onclick="toggleText()">Read More</button>
       <body> <img src="SimpleMBpic.jpg" style="width: 80%;"> </body>
        <div id="longText" style="display: none;">
            <h2>Project Name</h2>
            <p>Reaction Speed Game</p><br><br>
        <p><b><br>Introduction</b>
<br><br>


<b>WHAT am I doing for this project?</b><br><br>
For my Leaving Cert Computer Science project I have decided to create a reaction speed game. Since the overall topic is ‘Wellbeing’, I focused on improving our concentration levels. I believe this is a vital area in terms of our health. Improving concentration levels can prove to be beneficial in many ways... such as exam preparation and studying. That is why my main aim is to create a practical technological solution that will solve problems relating to poor concentration levels.
<br><br><br>
<b>WHAT am I making?</b><br><br>
One way to test the user's current concentration level is to see how fast their reaction speed is. This will show their current focus level. That is why I have developed a reaction speed game. My reaction speed game will test the reaction speed of the user. To combat outliers the game runs a handful of times and regards your average score. This correlates with the user’s simultaneous concentration level. Therefore we can not only test what your concentration level is… but also enhance it by decreasing your reaction time.
<br><br><br>

<b>HOW am I doing it?</b><br><br>
A Microbit code made on MakeCode.org is downloaded to the Microbit and connected to a python program (via serial connection). In this case, Thonny. My code will allow the Microbit inputs to be performed on and will inevitably create a few outputs such as your average speed, predictions and graphs. The inputs are gathered on the physical Microbit of course. The code’s outputs can be found in a CSV file after running the game. A website was created to display my project and outline its features.
<br><br><br>

<b>HOW will it work?</b><br><br>
The user will play the game on the Microbit 5 times and the average reaction speed is calculated. The user will also be able to see my estimated predictions for their reaction speed if only given their current concentration/mood level, and vice versa. 
<br><br><br>

<b>HOW can this benefit someone?</b><br><br>
If a person is struggling with poor concentration and/or can’t find a way of improving it… they can use this project to their advantage. Playing the game will not only tell you what your concentration level looks like but it will also improve your concentration level if you decide to play the game a couple of times. Striving for better results will provide motivation and therefore increase the user’s concentration level.
<br><br><br>

<b>WHY am I doing this?</b><br><br>
I decided to create a solution to poor concentration levels as I myself struggle with this sometimes. As a sixth year student, it is not easy to constantly have motivation to study. I feel that a poor level of concentration is the cause of wasteful studying. This relates to the term ‘work smarter not harder’. To me, hours of study without any concentration intensity is a pure waste of time. So, I set myself a mission to find a simple solution to this complicated problem. That is how I ended up creating a reaction speed game.
<br><br><br><br>

<b><br>Overview</b>
<br><br>
My investigation began with a survey of various reaction-based games and activities. I immediately wanted to create something under the ‘concentration level’ headline. I was exploring options ranging from physical reflex games to digital reaction speed challenges. Using Google, I researched different games and activities known to enhance reaction times. While some games relied heavily on luck, I sought options that provided opportunities for players to improve and develop their reaction speeds. 
<br><br>

After considering games like memory tests, mood surveys and puzzles, I concluded that a reaction-speed game would be most suitable for this project. Unlike more complex games, a reaction speed game offers a straightforward and focused way to measure and improve reaction times, aligning well with the objectives of this project. I examined existing digital versions and rules of reaction speed games to inform my design process. 
<br><br>

To streamline development and focus on functionality, I opted not to incorporate graphics into the game. Instead, the game will be rendered in a simple text-based format, allowing for quick implementation and modification. Python was chosen as the programming language for its versatility and my familiarity with it. The game will be designed using a functional programming approach to ensure ease of coding and modification. Utilising the Microbit was beneficial as I needed a way to collect inputs. A serial connection was established from the Microbit code to the python code. This allowed me to create a python code that would perform on the Microbit input, and create an output. Eventually, the results were displayed in a separate file - using csv.
<br><br><br><br>


<b>Objectives for this project include: </b>
<br><br>

Meeting Basic Requirements 
<br><br>
- Develop a reaction speed game that is easy to understand and play. 
<br><br>
- Store the data in a viewable place.
<br><br>
- Create a prediction component that will inform future decisions relating to wellbeing.
<br><br><br>

Meeting Advanced Requirements
<br><br>
- Create a model that performs on a dataset.
<br><br>
- Let the model solve the prescribed 'what-if' problems.
<br><br>
- Display results on a graph-format.
<br><br><br><br>

<b>Design </b>
<br><br>

To fulfil the project requirements, I carefully planned the structure and functionality of the reaction speed game. The game will prompt players to input their reaction speeds at the start. Instead of manually inputting your scores, the code runs a game where the user tests their reaction speed. This is repeated a multitude of times and recorded. The main game function will be designed to accommodate different player configurations, distinguishing between human and other players’ averages. 
<br><br>

During the game, players will be presented with a quick game requiring a rapid response. The game will monitor reaction times and provide feedback on performance, including average reaction times and comparisons. 

<br><br>
Data from each game session, including player reactions and outcomes, will be recorded in a CSV file for further analysis. A table system will enable players to view specific data sets and choose from various statistical analyses, such as the mean results to gain insights into their reaction speed performance. 

<br><br><br><br>
<b>Psuedocode and Flowchart </b>


<br><br><body>
    <img src="Pseudocode_final.png" style="width: 80%;">
    <img src="Flowchart.jpg" style="width: 80%;">
</body> 


<br><br><br><br>

<b>Implementation </b>

<br><br>
The game development process was conducted using Thonny with Python, providing essential debugging tools and syntax highlighting. Initial focus was on implementing player inputs at the start of the game, with provisions for command-line inputs to facilitate testing. 
<br><br>

Significant portions of the code were developed from scratch, drawing on my experience with Python programming. For unfamiliar concepts or functionalities, I researched for documentation, articles, and online forums for guidance and inspiration. The use of AI was also present. If used as a tool, it can prove helpful. Personally, the elaboration of syntax errors impressed me. Often the assistance provided in Thonny was vague so implementing AI was advantageous.

<br><br>
A notable challenge arose during the implementation phase when designing the CSV data recording and statistical analysis features. To address this, I implemented string manipulation techniques to organise and analyse reaction time data effectively. 

<br><br><br><br>

<b>Testing </b>

<br><br>
Extensive testing was conducted throughout the development process, encompassing unit testing, integration testing, and system testing. Issues encountered during integration testing, such as inaccuracy detection, were resolved through careful code review and adjustments. For example, negative speed values often came in as an input. This was due to the slight gap between the end of the countdown and the light popping up. 

<br><br>
System testing validated the overall functionality and integrity of the game, ensuring a smooth and error-free gaming experience. Testing results indicate that the game functions successfully and does not contain any detectable bugs. 


<br><br><br><br>
<b>Evaluation </b>

<br><br>
Reflecting on the project, I acknowledge areas for improvement in the initial design phase, particularly in comprehensive planning and consideration of all project requirements. Despite initial shortcomings, the project successfully achieved its objectives through iterative development and problem-solving. 
<br><br>

Future iterations of the project could benefit from enhanced planning and design processes to address overlooked requirements and ensure a more robust game experience. I believe a more complex game could be developed, as long as determination and commitment is present. Additionally, incorporating graphical elements and user-friendly interfaces could improve accessibility and engagement for players. 

<br><br>

Overall, the project represents a valuable learning experience, highlighting the importance of thorough planning, adaptability in problem-solving, and continuous improvement in software development practices. Through iterative refinement and incorporation of user feedback, future iterations of the project have the potential to deliver even more engaging and effective reaction speed challenges for players.</p>
        
            </p>
        </div>
    </div>

    <script>
        function toggleText() {
            var longText = document.getElementById("longText");
            if (longText.style.display === "none") {
                longText.style.display = "block";
            } else {
                longText.style.display = "none";
            }
        }
    </script>
</body>
</html>
