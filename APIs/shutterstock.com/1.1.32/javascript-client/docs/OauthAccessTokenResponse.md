# ShutterstockApiExplorer.OauthAccessTokenResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | Access token that can be used for future requests | 
**expiresIn** | **Number** | Number of seconds before token expires, only present for expiring tokens | [optional] 
**refreshToken** | **String** | A refresh token that can be used to renew the access_token when it expires, only present for expiring tokens | [optional] 
**tokenType** | **String** | Type of token | [default to &#39;Bearer&#39;]
**userToken** | **String** | Metadata about the access_token, only present for expiring tokens | [optional] 


