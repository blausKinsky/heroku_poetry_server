// $("document").ready(function(){
//     $("#send").click(function(){
//         var message = $("#message").val();        $.ajax({
//             url: "http://localhost:5000/api/",
//             type: "GET",
//             contentType: "application/json",
//             data: JSON.stringify({"message": message})        }).done(function(data) {
//             $("#message").text(data);        });    });});


//setTimeout(function(){ alert("Hello"); }, 3000);

$("document").ready(function(){
	    while (true){setTimeout( function(){
	    	var message = $("#message").val();
	    	$.ajax({
            url: "http://localhost:5000/api/",
            type: "GET",
            contentType: "application/json"
            }).done(function(data) {
            $("#message").text(data);
                    });
	            },2000)
	        } });

