

# OauthRequestTokenPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**oauthCallback** | **String** | An absolute URL to which IB will redirect the user. This URL is provided by the consumer during registration. This parameter must be set to &#39;oob&#39;.   |  [optional] |
|**oauthConsumerKey** | **String** | The 25-character hexadecimal string that was obtained from Interactive Brokers during the OAuth consumer registration process. |  [optional] |
|**oauthNonce** | **String** | A random string uniquely generated for each request. |  [optional] |
|**oauthSignature** | **String** | The signature for the request generated using the method specified in the oauth_signature_method parameter. See section 9 of the OAuth v1.0a specification for more details on signing requests. |  [optional] |
|**oauthSignatureMethod** | **String** | The signature method used to sign the request. Currently only &#39;RSA-SHA256&#39; is supported. |  [optional] |
|**oauthTimestamp** | **String** | Timestamp expressed in seconds since 1/1/1970 00:00:00 GMT. Must be a positive integer and greater than or equal to any timestamp used in previous requests. |  [optional] |



