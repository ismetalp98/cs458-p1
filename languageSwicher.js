const ids = [
    "sign-in-text",
    "inputEmail",
    "inputPassword",
    "remember-me-label",
    'showp',
    "help",
    "loginface",
    "newMem",
    "newMema",
    "robot",
    "more",
    "footer-header",
    "sss",
    "center",
    "tou",
    "privacy",
    "cp",
    "ci",
    "wrongPass",
    "wrongPassa",
    "wrongEmail",
    "wrongEmaila",
    "warningEmailEmp",
    "warningEmailEmail",
    "warningEmailPhone",
    "warningPassword"
]

const labels = Object.freeze(
    {
        'en': [
            "Sign In",
            "Email or phone number",
            "Password",
            "Remember me",
            "Show",
            "Need help?",
            "Login with Facebook",
            "New to Netflix? ",
            "Sign up now.",
            "This page is protected by Google reCAPTCHA to ensure you're not a bot. ",
            "Learn more",
            "Questions? Call ",
            "FAQ",
            "Help Center",
            "Terms of Use",
            "Privacy",
            "Cookie Preferences",
            "Corporate Information",
            "Incorrect password. Please try again or you can ",
            "reset your password.",
            "Sorry, we can't find an account with this email address. Please try again or",
            "create a new account.",
            "Please enter a valid email or phone number.",
            "Please enter a valid email address.",
            "Please enter a valid phone number.",
            "Your password must contain between 4 and 60 characters."
        ],
        'tr': [
            "Oturum Aç",
            "E-posta veya telefon numarası",
            "Şifre",
            "Beni hatırla",
            "Göster",
            "Yardım ister misiniz?",
            "Facebook ile oturum aç",
            "Netflix'e katılmak ister misiniz? ",
            "Şimdi kaydolun.",
            "Bu sayfa robot olmadığınızı kanıtlamak için Google reCAPTCHA tarafından korunuyor.",
            "Daha fazlasını öğrenin.",
            "Sorularınız mı var? Arayın ",
            "SSS",
            "Yardım Merkezi",
            "Kullanım Koşulları",
            "Gizlilik",
            "Çerez Tercihleri",
            "Kurumsal Bilgiler",
            "Parola yanlış. Lütfen yeniden deneyin ya da",
            "parolanızı sıfırlayın.",
            "Bu e‑posta adresi ile bağlantılı bir hesap bulamadık. Lütfen yeniden deneyin ya da",
            "yeni bir hesap oluşturun.",
            "Lütfen geçerli bir telefon numarası veya e‑posta adresi girin.",
            "Lütfen geçerli bir e‑posta adresi girin.",
            "Lütfen geçerli bir telefon numarası girin.",
            "Parolanız 4 ila 60 karakter olmalıdır.",
        ],
    }
);

const loadTexts = function (lang) {
    console.log(lang);
    let text = lang === 'tr' ? labels.tr : labels.en;
    for (let i = 0; i < ids.length; i++) {
        if (ids[i] === 'inputEmail') {
            document.getElementById(ids[i]).placeholder = text[i];
        }
        else if (ids[i] === 'inputPassword') {
            document.getElementById(ids[i]).placeholder = text[i];
        }
        else {
            document.getElementById(ids[i]).innerHTML = text[i];
        }
    }
    document.getElementById('signin-button').innerHTML = text[0];
    document.lang = lang;
}

const getSelectedLanguage = function () {
    let selector = document.getElementById("language-selector");
    let value = selector.options[selector.selectedIndex].value;
    return value;
}

const getBrowserLanguage = function () {
    console.log(document.cookie);
    document.cookie.split(';').forEach(element => {
        if (element.trim() === 'tr') {
            return 'tr';
        } else if (element.trim() === 'en') {
            return 'en';
        }
    });
    let lang = navigator.language || navigator.userLanguage;
    lang = lang.slice(0, 2);
    return lang;
}

const setSelectedLanguage = function (lang) {
    lang = lang === 'tr' ? lang : 'en';
    console.log(lang);
    document.cookie = lang + ";";
    document.getElementById('language-selector').value = lang;
}

const setUpLanguage = () => {
    let lang = getBrowserLanguage();
    lang = lang.slice(0, 2);
    loadTexts(lang);
    setSelectedLanguage(lang);
}