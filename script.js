const email = document.getElementById("inputEmail")
const password = document.getElementById("inputPassword")
const passwordWrapper = document.getElementById("passwordWrapper");
const emailWarningEmp = document.getElementById("warningEmailEmp")
const emailWarningEmail = document.getElementById("warningEmailEmail")
const emailWarningPhone = document.getElementById("warningEmailPhone")
const passwordWarning = document.getElementById("warningPassword");
const userNot = document.getElementById('userNot');
const passNot = document.getElementById('passNot');
const benihatirla = document.getElementById('benihatirla');
const showp = document.getElementById('showp');

const onLoada = () => {
    console.log("onload");
    const myInput = document.getElementById('inputPassword');
    myInput.onpaste = e => e.preventDefault();
    let isLog = false;
    let userName;
    let passwordt;
    document.cookie.split(';').forEach(element => {
        if (element.trim() === 'loggedin') {
            isLog = true;
        } else if (element.trim().includes('userName')) {
            userName = element.trim().split('=')[1];
        } else if (element.trim().includes('password')) {
            passwordt = element.trim().split('=')[1];
        }
    });
    if(userName){
        email.value = userName;
    } 
    if(passwordt){
        password.value = passwordt;
    }
    if (isLog) {
        const elm = document.createElement('a');
        elm.href = "emptyPage.html?logged-in";
        elm.click();
    }
}

const redirectMain = () => {
    document.cookie = "loggedin;";
    if (benihatirla.checked) {
        document.cookie = "userName=" + email.value + "; ";
        document.cookie = "password=" + password.value + "; ";
    }
    const elm = document.createElement('a');
    elm.href = "emptyPage.html?logged-in";
    elm.click();
}

const users = [
    {
        username: "05362284637",
        password: "Ali3457y"
    },
    {
        username: "ismet@gmail.com",
        password: "asd123er"
    }
];

const isExist = (username, upassword) => {
    for (const asd of users) {
        if (asd.username === username) {
            if (asd.password === upassword) {
                return true;
            } else {
                userNot.style.display = "none";
                email.style.borderBottom = 'none';
                passNot.style.display = "block";
                passwordWrapper.style.borderBottom = '2px solid #e87c03';
                return false;
            }
        }
    }
    userNot.style.display = "block";
    email.style.borderBottom = '2px solid #e87c03';
    password.value = "";
    return false;
};

const onClick = () => {
    let check = true;
    if (String(password.value).length < 4 || String(password.value).length > 60) {
        passwordWarning.style.display = "block";
        password.style.borderBottom = '2px solid #e87c03';
        check = false;
    }
    if (email.value === "") {
        emailWarningEmp.style.display = "block";
        emailWarningEmail.style.display = "none";
        emailWarningPhone.style.display = "none";
        email.style.borderBottom = '2px solid #e87c03';
        check = false;
    }
    else if (check && (validateEmail(email.value) || validatePhone(email.value)) && isExist(email.value, password.value)) {
        redirectMain();
    }

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
            passwordWrapper.style.borderBottom = '2px solid #e87c03';
        }
        else {
            passwordWarning.style.display = "none";
            passwordWrapper.style.borderBottom = 'none';
        }
    }
};

const showPss = () => {
    const type = password.type;
    if (type === "password") {
        password.type = "text";
        password.onpaste = e => e.preventDefault();
        if(document.lang === "tr"){
            showp.innerHTML = "Gizle";
        } else {
            showp.innerHTML = "Hide";
        }
    } else {
        password.type = "password";
        password.onpaste = e => e.clipboardData.setData('text/plain', password.value);
        if(document.lang === "tr"){
            showp.innerHTML = "Göster";
        } else {
            showp.innerHTML = "Show";
        }
    }
}

const validateEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validatePhone = email => {
    const re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
    return re.test(String(email).toLowerCase());
}