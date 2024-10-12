

# AuthTokenResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | The access token that can be used to call the     DigiLocker APIs. |  |
|**expiresIn** | **Long** | The duration in seconds for which the access token is             valid. |  |
|**refreshToken** | **String** | The refresh token used to refresh the above access   token when it expires. This will value will be   returned only in case of web applications and not be   returned for limited input devices. |  |
|**scope** | **String** | Scope of the token. |  |
|**tokenType** | **String** | The type of token which will always be Bearer. |  |



