# Message_REST_API

Application for saving, returning saved and edited short texts. Authorization is required to create, edit and delete messages. 
To become an authorized user, you must create an account and receive an authorization token via e-mail. 

<h2>Deployed to Heroku:</h2> 

https://message-rest-api-ml.herokuapp.com


<h2>Account creation</h2>
To create an account you need to send with method 'post' data to the address given below.

https://message-rest-api-ml.herokuapp.com/register/


Data format:
```
{
    "username": "your_user_name",
    "email": "your@e.mail",
    "password": "your_password"
}
```
<h2>Authorization token</h2>
To obtain an authorization token you need to send with method 'post' data to the address given below.

https://message-rest-api-ml.herokuapp.com/obtain_token/


Data format:
```
{
    "username": "your_user_name",
    "password": "your_password"
}
```

After that you will get response "Token has been send to your email.", and you should see an email from "imjustsendingemails@gmail.com" with the token.

<h2>Token usage</h2>
For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

<h2>Creating message</h2>
To create a message you need to send with method 'post' (remember about authorization header) data to the address given below.

https://message-rest-api-ml.herokuapp.com/message_create/


Data format:
```
{
    "content": "your_message",
}
```
In response you will get:
```
{   
    "id": message_id
    "content": "your_message",
}
```
<h2>Updating message</h2>
To update a message you need to send with method 'put' (remember about authorization header) data to the address given below.

https://message-rest-api-ml.herokuapp.com/message_update/id/


Where id is the "id" parameter from creation response of the message you want to overwrite.

Data format:
```
{
    "content": "your_message",
}
```
In response you will get:
```
{   
    "id": message_id
    "content": "your_message",
}
```
<h2>Deleting message</h2>
To update a message you need to get with method 'delete' (remember about authorization header) to the address given below. 

https://message-rest-api-ml.herokuapp.com/message_destroy/id/


Where id is the "id" parameter from creation response of the message you want to destroy.

<h2>Viewing message</h2>
To view a message you need to get to the address given below with method "get".

https://message-rest-api-ml.herokuapp.com/message_view/id/


Where id is the "id" parameter from creation response of the message you want to view.

In response you will get:
```
{       
    "content": "your_message",
    "display_count": times_displayed
}
```
