# NextAuthApi.LoginStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountid** | **Number** | Account id | [optional] 
**canprovoke** | **Boolean** | True if a login can be pushed from the server, false otherwise | [optional] 
**hsid** | **String** | Converted session id, used by the websockets | [optional] 
**loggedin** | **Boolean** | True if the user is loggedin, false otherwise | [optional] 
**loginqrdata** | **String** | Base64 encoded data that is represented in the login qr code | [optional] 
**pk** | **String** | Base64 encoded public key of the nextAuth app. This uniquely identifies the account on the nextAuth app, regardless of the username | [optional] 
**userid** | **String** | User name | [optional] 


