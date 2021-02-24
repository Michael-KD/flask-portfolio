function AlertIt(noteId) {
    //let noteId = $('#my-data').data();
    console.log(noteId);
    var answer = confirm ("Please click on OK to delete your note.")
    if (answer)
    window.location=`/delete/${noteId}`;
}

function consoleTest() {
    console.log("This is a test");
}

let wordJS = $('#my-data').data("word");
let wordDefJS = $('#my-data').data("def");
let hintsNum = 0;
let wordHint ="";
let correctWord = wordJS;

//    console.log(wordJS);
//    console.log(wordDefJS);
$(".hint").hide();


function wordScrambleGame(word, def) {
    wordArray = word.split('');
    wordArrayShuffled = shuffle(wordArray);
    wordShuffled = wordArrayShuffled.join('');
    $(".wordspace").text(wordShuffled);
    $(".defspace").text(def);
    console.log(wordShuffled);
}

function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

$(".test").click(function() {
    let wordGuess = $(".guessInput").val();
    let wordGuessLower = wordGuess.toLowerCase();
    if (wordGuessLower === wordJS) {
        console.log("correct");
        $(".result").text("Correct!");
        $(".wordspace").html(`<b>` + wordJS + `</b>`);
        $(".hint").hide();
    }
    else {
        console.log("incorrect")
        $(".result").text("Incorrect... Do you want a hint?");
        $(".hint").show();
    }
});

function hints(num) {
    wordHint = correctWord.slice(0, num);
    console.log(wordHint);
    return wordHint;
}

$(".hint").click(function() {
    hintsNum = hintsNum+1;
    console.log(hintsNum);
    hintFinal = hints(hintsNum);
    console.log(hintFinal);
    $(".hintLetters").text(hintFinal);
    $(".hint").hide();
});

wordScrambleGame(wordJS, wordDefJS);