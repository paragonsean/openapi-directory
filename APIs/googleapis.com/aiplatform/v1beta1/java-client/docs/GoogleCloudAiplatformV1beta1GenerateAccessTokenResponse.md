

# GoogleCloudAiplatformV1beta1GenerateAccessTokenResponse

Response message for NotebookInternalService.GenerateToken.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | Short-lived access token string which may be used to access Google APIs. |  [optional] |
|**expiresIn** | **Integer** | The time in seconds when the access token expires. Typically that&#39;s 3600. |  [optional] |
|**scope** | **String** | Space-separated list of scopes contained in the returned token. https://cloud.google.com/docs/authentication/token-types#access-contents |  [optional] |
|**tokenType** | **String** | Type of the returned access token (e.g. \&quot;Bearer\&quot;). It specifies how the token must be used. Bearer tokens may be used by any entity without proof of identity. |  [optional] |



