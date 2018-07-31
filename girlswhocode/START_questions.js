/* Buzzfeed Quiz
Create a Buzzfeed Quiz with 5 questions. Create a method for determining what
the results will be. Combine our knowledge of HTML, JS, and CSS to get hired at
Buzzfeed.
1. Finish the function 'creatQuestions'
  a. Make sure you have a list of dictionary of questions
  b. Create the questions and options (aka the radio buttons) DYNAMICALLY
  in JavaScript. In other words, don't hard code the questions; we want to use
  code to access our list of dictionary of questions.
      (HINT 1: HTML is just a bunch of STRINGS. Create HTML code with JS by
      creating strings with tags i.e. ('<input type="radio" name="group" value ="asdf"'))
      (HINT 2: Group the radio button inputs for each question using the SAME name
       or class)
  c. Make sure our changes are reflected in the HTML
      (HINT: getElementById and change its innerHTML)
  d. Call this function WHEN THE PAGE LOADS!!!!
      (HINT: wrap the function in paranthesis like in Overwatch Hero workshop)
2. Define the function 'submitAnswer'
  a. We want to iterate through each group of questions to see what the user
  selected.
  (HINT: a selected answer is "checked"; look up checked radio button)
  b. Determine how your Buzzfeed personality is predicted
      ideas (easy): Assign points to each of your option. If an option makes the
      user a Broccoli, assign a low point (0,1). If an option makes the user a Carrot,
      assign medium high points (4,5). If an option makes the user a Celery,
      assign high points (10). All numbers selected are arbitrary; you decide.
          0-15 points = Broccoli
          16-30 points = Carrot
          30-45 points = Celerey
      ideas (medium):
          Determine which value was selected the MAXIMUM times
          Need to handle TIES.
3. Make more questions, add CSS, add images, use BootStrap
*/
(function createQuestions(){

  /*TODO: ADD MORE QUESTIONS. Create a field for images*/

  var questions = [
    {
      "question": "What color do you prefer your straws?",
      "name": "straws",
      "answers" : {
        "Red": 0,
        "Striped (one color)": 2,
        "Green": 4,
        "Black": 6,
        "Multi-colored Stripes": 8,
        "White": 10
      }
    },
    {
      "question": "How protected is your phone?",
      "name": "Phone",
      "answers" : {
        "Waterproof": 0,
        "Screen protector":2,
        "Decent to Good Phone Case": 4,
        "Case + Screen Protector": 6,
        "Iron Man/Otter": 8,
        "Pretty but vulnerable": 10,
        "Naked lmao": 12
      }
    },
    {
      "question": "Which villain do you prefer?",
      "name": "villain",
      "answers": {
        "Maleficent": 0,
        "Voldemort": 2,
        "Hela": 4,
        "Sauron/Saruman": 6,
        "Ursula": 8,
        "Cruella De Vil": 10
      }
    }
  ];

  var html = "";
  for (var i = 0; i < questions.length; i++){
    html += questions[i]["question"] + "<br>" ;
    for (var key in questions[i]["answers"]){
      html += '<input type="radio" name="' + questions[i]["name"] + '" value="';
      html += questions[i]["answers"][key] + '">' + key + "<br>";
    }
  }

  /* TODO: set the element "survey" 's innerHTML to html'*/
  document.getElementById("quiz").innerHTML = html;

})();

function submitAnswer(){
  var total = 0;
  var categories = ["straws", "Phone", "villain"];

  for (var j = 0; j < categories.length; j ++){
    var cat = document.getElementsByName(categories[j]);
    for (var i = 0; i < cat.length; i++){
      if (cat[i].checked){
        total += parseInt(cat[i].value);
      }
    }
  }

  /* TODO:  Determine your winning "personality" */
  var dead;
  if (total < 5) {
    dead = "Dobby";
  } else if (total < 10) {
    dead = "Boromir";
  } else if (total < 15) {
    dead = "Magnus Chase";
  } else if (total < 20) {
    dead = "Augustus Waters";
  } else if (total < 25) {
    dead = "Marley";
  } else {
    dead = "Simon";
  }



  /*TODO: Replace the empty quotes with the result of the quiz*/
  document.getElementById("results").innerHTML = "YOU ARE "  + dead;
}
