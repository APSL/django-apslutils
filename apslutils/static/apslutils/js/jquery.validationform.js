// file: angularform.js
// Author: Apsl

function getCookieValue(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) != -1) return c.substring(name.length,c.length);
    }
    return "";
}

$("form.validationForm").find("input, textarea").blur(function() {
    var field = $(this);
    var value = $(field).val();
    var name = $(field).attr("name");
    var button = $(this).closest("form").find("input[type='submit'], button[type='submit']");    
    
    var params = {
	"_cleanField": true, 
	"field": name, 
	"form": $(this).closest("form").serialize()
    };

    $.ajax({
	method: "post",
	url: window.location.href,
	data: params,
	headers: {
	    "X-CSRFToken": getCookieValue("csrftoken")
	},
	success: function(response) {
	    var content = $(field).closest("div.form-group");
	    $(content).find("span").remove();
	    
	    var labelico = $(content).find("label span");
	    if (!labelico.length)
		$(content).find("label").prepend("<span/>");

	    if (response.field_error) {
		$(content).addClass("has-error").removeClass("has-success");
		$(content).find(".controls").append("<span class='text-danger'>" + 
						    response.field_description + "</span>")
		$(content).find("label span").text("✘");
	    } else {
		$(content).removeClass("has-error").addClass("has-success");
		$(content).find("label span").text("✔");
	    }

	    if (response.form_valid) {
		$(button).prop("disabled", false);
	    } else {
		$(button).prop("disabled", true);
	    }
	}
    });

    // TODO: Habilitar botón sólo si todo el formulario es válido.
    // TODO: Tener en cuenta validaciones globales.
    // TODO: Comportament dels checkboxes.
    
});
