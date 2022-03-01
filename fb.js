const emailfb = document.getElementById('emailfb');
const passfb = document.getElementById('passfb');
const err0fb = document.getElementById('error_box0');
const err1fb = document.getElementById('error_box1');
const err2fb = document.getElementById('error_box2');

const usersfb = [
    {
        username: "05357853434",
        password: "fvtı09o"
    },
    {
        username: "alp@gmail.com",
        password: "fds135bo"
    }
];

const isExistfb = (username, upassword) => {
    for (const asd of usersfb) {
        if (asd.username === username) {
            if (asd.password === upassword) {
                return true;
            } else {
                err0fb.style.display = 'block';
                err1fb.style.display = 'none';
                err2fb.style.display = 'none';
                return false;
            }
        }
    }
    err2fb.style.display = 'none';
    err1fb.style.display = 'block';
    err0fb.style.display = 'none';
    passfb.value = "";
    return false;
};

const onClickFb = async () => {
    if (emailfb.value === '' || passfb.value === '') {
        err1fb.style.display = 'block';
        err0fb.style.display = 'none';
        err2fb.style.display = 'none';
    }
    else if (isExistfb(emailfb.value, passfb.value)) {
        if (window.opener != null && !window.opener.closed) {
            var txtName = window.opener.document.getElementById("redirectButton");
            txtName.click();
        }
        window.close();
    }
};