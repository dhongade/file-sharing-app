$("form[name=SignUp]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url:"/user/signup",
        type:"POST",
        data: data,
        datatype:"json",
        success: function(resp){
            console.log(resp);
            // console.log(access_token);
            window.location.href = "/table";
        },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeclass("error--hidden");
        }
    });

    e.preventDefault();
})

$("form[name=LogIn]").submit(function(e){

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url:"/user/login",
        type:"POST",
        data: data,
        datatype:"json",
        success: function(resp){
            console.log(resp);
            // console.log(access_token);
            window.location.href = "/table";
        },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeclass("error--hidden");
        }
    });

    e.preventDefault();
})


