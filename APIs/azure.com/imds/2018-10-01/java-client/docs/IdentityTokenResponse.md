

# IdentityTokenResponse

This is the response from the Identity_GetToken operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | This is the requested access token. The app can use this token to authenticate to the sink resource. |  [optional] |
|**clientId** | **String** | This is the client_id specified in the request, if any. |  [optional] |
|**expiresIn** | **String** | This is how long the access token is valid (in seconds). |  [optional] |
|**expiresOn** | **String** | This is the time when the access token expires. The date is represented as the number of seconds from 1970-01-01T0:0:0Z UTC until the expiration time. This value is used to determine the lifetime of cached tokens. |  [optional] |
|**extExpiresIn** | **String** | This indicates the extended lifetime of the token. |  [optional] |
|**msiResId** | **String** | This is the msi_res_id specified in the request, if any. |  [optional] |
|**notBefore** | **String** | This is the time when the access token becomes effective. The date is represented as the number of seconds from 1970-01-01T0:0:0Z UTC until the expiration time. |  [optional] |
|**objectId** | **String** | This is the object_id specified in the request, if any. |  [optional] |
|**resource** | **String** | This is the app ID URI of the sink resource. |  [optional] |
|**tokenType** | **String** | This indicates the token type value. |  [optional] |



