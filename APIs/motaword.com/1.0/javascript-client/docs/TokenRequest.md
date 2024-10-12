# MotaWordApi.TokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grantType** | **String** | OAuth2 grant type. Supports &#39;client_credentials&#39;, &#39;password&#39;, &#39;refresh_token&#39; or &#39;user_id&#39;. | 
**password** | **String** | MW Account password (to be used in password grant type) | [optional] 
**refreshToken** | **String** | Refresh token value for refresh token flow. | [optional] 
**scope** | **String** | Authorization scope. Use &#39;privileged&#39; for private endpoints. | 
**userId** | **Number** | Value for user_id grant type flow. | [optional] 
**username** | **String** | MW Account email (to be used in password grant type) | [optional] 


