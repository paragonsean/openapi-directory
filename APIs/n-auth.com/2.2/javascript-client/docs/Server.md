# NextAuthApi.Server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountCount** | **Number** | Number of accounts registered with this server | [optional] 
**appandroid** | **String** | URL of the app in Google Play | [optional] 
**appios** | **String** | URL of the app in the App Store | [optional] 
**appname** | **String** | name of the app | [optional] 
**appurl** | **String** | URL (prefix) to launch the app | [optional] 
**lastLogin** | **Number** | Last login on this server | [optional] 
**logo** | **String** | Base 64 encoded logo | 
**owner** | **Number** | Owner id | [optional] 
**pinTimeout** | **Number** | Time (minutes) since the last time the user entered his PIN, that the user is not requested a PIN at login. -1 means that the user is never asked for a PIN before logging in, 0 means that the user is asked every time he wants to login | 
**pinTransTimeout** | **Number** | Time (minutes) since the last time the user entered his PIN, that the user is not requested a PIN at transaction approval. -1 means that the user is never asked for a PIN before approving a transaction, 0 means that the user is asked every time he wants to approve a transaction | 
**pingTime** | **Number** | Time (seconds) that the nextAuth app has before it needs to reply to a ping request from the nextAuth server (continuous authentication) | 
**serverFlags** | **[String]** | Server flags | 
**serverName** | **String** | Server name | 
**serverid** | **String** | Base64 encoded id of the nextAuth server | 
**serverpk** | **String** | Base64 encoded public key of the nextAuth server | 
**siteurl** | **String** | URL of the main website | [optional] 
**wsurl** | **String** | Websocket URL | [optional] 


