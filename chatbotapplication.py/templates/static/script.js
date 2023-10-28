$(document).ready(function() {
    $("#get-question-btn").click(function() {
        $.get('/get_question', function(data) {
            $("#question").text("Question: " + data.question);
            $("#answer").text("Answer: " + data.answer);
        });
    });
});
