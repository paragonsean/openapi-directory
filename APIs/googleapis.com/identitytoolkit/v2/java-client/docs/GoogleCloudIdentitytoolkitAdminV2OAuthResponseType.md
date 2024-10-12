

# GoogleCloudIdentitytoolkitAdminV2OAuthResponseType

The response type to request for in the OAuth authorization flow. You can set either `id_token` or `code` to true, but not both. Setting both types to be simultaneously true (`{code: true, id_token: true}`) is not yet supported. See https://openid.net/specs/openid-connect-core-1_0.html#Authentication for a mapping of response type to OAuth 2.0 flow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Boolean** | If true, authorization code is returned from IdP&#39;s authorization endpoint. |  [optional] |
|**idToken** | **Boolean** | If true, ID token is returned from IdP&#39;s authorization endpoint. |  [optional] |
|**token** | **Boolean** | Do not use. The &#x60;token&#x60; response type is not supported at the moment. |  [optional] |



