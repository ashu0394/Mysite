function login_save() {
        $.ajax({
            type: "POST",
            url: "/myapp/home/",
            data: $('#login-form').serialize(),
            success: function(response) {
                if (response.success == 'true') {
                    window.location.href = '/myapp/mainpage/?name='+response.members;
                }
                if (response.success == 'loginfield') {
                    alert(response.message);
                }

                 if (response.success == 'invalidusername') {
                    alert(response.message);
                }

                if (response.success == 'userinactive') {
                    alert(response.message);
                }

                if (response.success == 'wrongpass') {
                    alert(response.message);
                }

               else {

                    if (response.success == 'false') {
                        alert("Unexpected error occured");
                    }
                    if (response.success == 'noPost') {
                        alert("Not a Post method");
                    }
                }
            },

        });
        }
