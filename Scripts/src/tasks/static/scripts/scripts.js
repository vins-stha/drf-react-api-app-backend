function filterOnChange() {
    let status = document.getElementsByName('task-state')[0].value;
    $.ajax({
        method: "get",
        url: "/api/v1/tasks?status=" + status

    })
        .done(function (message) {
            $("body").html(message);

        })
        .fail(function (error) {
            $('.error-message').css('visibility','visible');
            $('.error-message').html(error);
            console.log("Something went wrong", error);
        });

}


