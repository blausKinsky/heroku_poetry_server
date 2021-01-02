$("document").ready(function(){
    $("#send").click(function(){
        var message = $("#message").val();        $.ajax({
            url: "http://localhost:5000/api/",
            type: "GET",
            contentType: "application/json",
          //This is where we get our generated text from the server
            data: JSON.stringify({"message": message})        }).done(function(data) {
            $("#message").text(data);        });    });});

// $("document").ready(function(){
// 	//make an infinite while loop here
//         var message = $("#message").val();        $.ajax({
//             url: "http://localhost:5000/api/",
//             type: "GET",
//             contentType: "application/json"
//             }).done(function(data) {
//             	//data should be an object that contains a duration and the text
//             	//setTimeout for the duration and inside that timeout (#message).text(data)
//             $("#message").text(data);        });    });



