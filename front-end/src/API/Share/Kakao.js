const {Kakao} = window;
const APP_KEY = process.env.REACT_APP_KAKAO_JAVASCRIPT_KEY;

export default function initialize() {
    console.log(APP_KEY);
    Kakao.init("Ada2ce74b8235f51ccb9769d07b1a6d57");
}