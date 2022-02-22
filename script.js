import users from "../frontend/users";

const email = document.getElementById("inputEmail")
const password = document.getElementById("inputPassword")
const emailWarningEmp = document.getElementById("warningEmailEmp")
const emailWarningEmail = document.getElementById("warningEmailEmail")
const emailWarningPhone = document.getElementById("warningEmailPhone")
const passwordWarning = document.getElementById("warningPassword")
const loginButton = document.getElementById("signin-button").onclick = function login() {
    console.log(usersData.users);
}

const onBlur = (ev) => {
    if (ev.name === "email") {
        if (ev.value === "") {
            emailWarningEmail.style.display = "none";
            emailWarningPhone.style.display = "none";
            emailWarningEmp.style.display = "block";
            email.style.borderBottom = '2px solid #e87c03';
        }
        else if (isNaN(parseInt(ev.value)) && !validateEmail(ev.value)) {
            emailWarningEmail.style.display = "block";
            emailWarningEmp.style.display = "none";
            emailWarningPhone.style.display = "none";
            email.style.borderBottom = '2px solid #e87c03';
        }
        else if (!isNaN(parseInt(ev.value)) && !validatePhone(ev.value)) {
            emailWarningEmail.style.display = "none";
            emailWarningEmp.style.display = "none";
            emailWarningPhone.style.display = "block";
            email.style.borderBottom = '2px solid #e87c03';
        } else {
            emailWarningEmail.style.display = "none";
            emailWarningEmp.style.display = "none";
            emailWarningPhone.style.display = "none";
            email.style.borderBottom = 'none';
        }
    }
    if (ev.name === "password") {
        if (String(ev.value).length < 4 || String(ev.value).length > 60) {
            passwordWarning.style.display = "block";
            password.style.borderBottom = '2px solid #e87c03';
        }
        else {
            passwordWarning.style.display = "none";
            password.style.borderBottom = 'none';
        }
    }
};

const validateEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validatePhone = email => {
    const re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
    return re.test(String(email).toLowerCase());
}
