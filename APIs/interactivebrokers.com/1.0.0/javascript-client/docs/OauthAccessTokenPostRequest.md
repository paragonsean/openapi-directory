# Ibkr3rdPartyWebApi.OauthAccessTokenPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oauthConsumerKey** | **String** | The 25-character hexadecimal string that was obtained from Interactive Brokers during the OAuth consumer registration process. | [optional] 
**oauthNonce** | **String** | A random string uniquely generated for each request. | [optional] 
**oauthSignature** | **String** | The signature for the request generated using the method specified in the oauth_signature_method parameter. See section 9 of the OAuth v1.0a specification for more details on signing requests. | [optional] 
**oauthSignatureMethod** | **String** | The signature method used to sign the request. Currently only &#39;RSA-SHA256&#39; is supported. | [optional] 
**oauthTimestamp** | **String** | Timestamp expressed in seconds since 1/1/1970 00:00:00 GMT. Must be a positive integer and greater than or equal to any timestamp used in previous requests. | [optional] 
**oauthToken** | **String** | The request token obtained from IB via /request_token. | [optional] 
**oauthVerifier** | **String** | The verification code received from IB after the user has granted authorization. | [optional] 


