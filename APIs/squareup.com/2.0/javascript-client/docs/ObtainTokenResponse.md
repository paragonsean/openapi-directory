# SquareConnectApi.ObtainTokenResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | A valid OAuth access token. OAuth access tokens are 64 bytes long. Provide the access token in a header with every request to Connect API endpoints. See [OAuth API: Walkthrough](https://developer.squareup.com/docs/oauth-api/walkthrough) for more information. | [optional] 
**expiresAt** | **String** | The date when access_token expires, in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format. | [optional] 
**idToken** | **String** | Then OpenID token belonging to this this person. Only present if the OPENID scope is included in the authorize request. | [optional] 
**merchantId** | **String** | The ID of the authorizing merchant&#39;s business. | [optional] 
**planId** | **String** | __LEGACY FIELD__. The ID of the subscription plan the merchant signed up for. Only present if the merchant signed up for a subscription during authorization. | [optional] 
**refreshToken** | **String** | A refresh token. OAuth refresh tokens are 64 bytes long. For more information, see [OAuth access token management](https://developer.squareup.com/docs/oauth-api/how-it-works#oauth-access-token-management). | [optional] 
**shortLived** | **Boolean** | A boolean indicating the access token is a short-lived access token. The short-lived access token returned in the response will expire in 24 hours. | [optional] 
**subscriptionId** | **String** | __LEGACY FIELD__. The ID of a subscription plan the merchant signed up for. Only present if the merchant signed up for a subscription during authorization. | [optional] 
**tokenType** | **String** | This value is always _bearer_. | [optional] 


