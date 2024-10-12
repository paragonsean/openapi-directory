

# PostToken200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | Authentication token that should be given in every authenticated request to the API |  [optional] |
|**expiresIn** | **Integer** | Validity of the token given in seconds, 3600s &#x3D; 1h by default |  [optional] |
|**refreshToken** | **String** | Use this token when your access token has expired. See &lt;a href&#x3D;\&quot;/documentation/authentication.html#refresh-an-expired-token\&quot;&gt;Refresh an expired token&lt;/a&gt; section for more details. |  [optional] |
|**scope** | **String** | Unused, always equal to \&quot;null\&quot; |  [optional] |
|**tokenType** | **String** | Token type, always equal to \&quot;bearer\&quot; |  [optional] |



