const emailfb = document.getElementById('emailfb');
const passfb = document.getElementById('passfb');
const err0fb = document.getElementById('error_box0');
const err1fb = document.getElementById('error_box1');

const usersfb = [
    {
        username: "05362284637",
        password: "Ali3457y"
    },
    {
        username: "ismet@gmail.com",
        password: "asd123er"
    }
];

const isExistfb = (username, upassword) => {
    for (const asd of usersfb) {
        if (asd.username === username) {
            if (asd.password === upassword) {
                return true;
            } else {
                return false;
            }
        }
    }
    return false;
};

const onClickFb = async () => {
    if (emailfb.value === '' || passfb.value === '') {
        err1fb.style.display = 'block';
        err0fb.style.display = 'none';
    }
    else if (isExistfb(emailfb.value, passfb.value)) {
        if (window.opener != null && !window.opener.closed) {
            var txtName = window.opener.document.getElementById("redirectButton");
            txtName.click();
        }
        window.close();
    } else {
        err0fb.style.display = 'block';
        err1fb.style.display = 'none';
    }
};