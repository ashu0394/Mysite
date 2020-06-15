function set_password() {
        $.ajax({
            type: "POST",
            url: "/myapp/setpassworddone/",
            data: $('#setpassword-form').serialize(),
            success: function(response) {

                if (response.success == 'true') {
                    alert(response.message);
                    window.location.href = '/myapp/login/';
                }
                if (response.success == 'setpasswordfield') {
                    alert(response.message);
                }

                if (response.success == 'invalidmob') {
                    alert(response.message);
                }
                if (response.success == 'passnotmatch') {
                    alert(response.message);
                }
                 if (response.success == 'digitrequire') {
                    alert(response.message);
                }

                if (response.success == 'digitlimit') {
                    alert(response.message);
                }

               else {

                    if (response.success == 'false') {
                        alert("Unexpected error occured");
                    }
                }
            },

        });
        }
