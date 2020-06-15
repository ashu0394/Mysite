function save_user() {
        $.ajax({
            type: "POST",
            url: "/myapp/registersuccess/",
            data: $('#register-form').serialize(),
            success: function(response) {
                if (response.success == 'true') {
                    alert(response.message);
                    window.location.href = '/myapp/setpassword/';
                }
                if (response.success == 'registerfield') {
                    alert(response.message);
                }

                 if (response.success == 'digitrequire') {
                    alert(response.message);
                }

                if (response.success == 'digitlimit') {
                    alert(response.message);
                }

               else {

                    if (response.success == 'noPost') {
                        alert("Not a Post method");
                    }
                }
            },

        });
        }
