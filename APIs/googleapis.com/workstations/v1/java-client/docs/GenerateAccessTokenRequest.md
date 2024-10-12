

# GenerateAccessTokenRequest

Request message for GenerateAccessToken.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expireTime** | **String** | Desired expiration time of the access token. This value must be at most 24 hours in the future. If a value is not specified, the token&#39;s expiration time will be set to a default value of 1 hour in the future. |  [optional] |
|**ttl** | **String** | Desired lifetime duration of the access token. This value must be at most 24 hours. If a value is not specified, the token&#39;s lifetime will be set to a default value of 1 hour. |  [optional] |



