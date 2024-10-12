

# GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfig

Configuration options for authenticating with an OAuth IDP.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | The client id of an OAuth client. |  [optional] |
|**clientSecret** | **String** | The client secret of the OAuth client, to enable OIDC code flow. |  [optional] |
|**displayName** | **String** | The config&#39;s display name set by developers. |  [optional] |
|**enabled** | **Boolean** | True if allows the user to sign in with the provider. |  [optional] |
|**issuer** | **String** | For OIDC Idps, the issuer identifier. |  [optional] |
|**name** | **String** | The name of the OAuthIdpConfig resource, for example: &#39;projects/my-awesome-project/oauthIdpConfigs/oauth-config-id&#39;. Ignored during create requests. |  [optional] |
|**responseType** | [**GoogleCloudIdentitytoolkitAdminV2OAuthResponseType**](GoogleCloudIdentitytoolkitAdminV2OAuthResponseType.md) |  |  [optional] |



