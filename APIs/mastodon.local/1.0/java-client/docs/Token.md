

# Token

Represents an OAuth token used for authenticating with the API and performing actions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | An OAuth token to be used for authorization. |  [optional] |
|**createdAt** | **Integer** | When the token was generated. UNIX Timestamp. |  [optional] |
|**scope** | **String** | The OAuth scopes granted by this token, space-separated. |  [optional] |
|**tokenType** | **String** | The OAuth token type. Mastodon uses &#x60;Bearer&#x60; tokens. |  [optional] |



