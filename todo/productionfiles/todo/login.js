


const login_btn = document.getElementById("login-button");
const login_form = document.querySelector(".login-form");

login_btn.addEventListener("click", function(){
    if (login_form.checkValidity()){
        console.log("yep valid")
        login_btn.innerHTML = "Login <i class=\"fa-solid fa-spinner fa-spin-pulse\"></i>"
        login_btn.classList.add("disabled")

    }
})

