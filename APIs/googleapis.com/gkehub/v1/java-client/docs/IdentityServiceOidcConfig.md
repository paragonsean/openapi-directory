

# IdentityServiceOidcConfig

Configuration for OIDC Auth flow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateAuthorityData** | **String** | PEM-encoded CA for OIDC provider. |  [optional] |
|**clientId** | **String** | ID for OIDC client application. |  [optional] |
|**clientSecret** | **String** | Input only. Unencrypted OIDC client secret will be passed to the GKE Hub CLH. |  [optional] |
|**deployCloudConsoleProxy** | **Boolean** | Flag to denote if reverse proxy is used to connect to auth provider. This flag should be set to true when provider is not reachable by Google Cloud Console. |  [optional] |
|**enableAccessToken** | **Boolean** | Enable access token. |  [optional] |
|**encryptedClientSecret** | **byte[]** | Output only. Encrypted OIDC Client secret |  [optional] [readonly] |
|**extraParams** | **String** | Comma-separated list of key-value pairs. |  [optional] |
|**groupPrefix** | **String** | Prefix to prepend to group name. |  [optional] |
|**groupsClaim** | **String** | Claim in OIDC ID token that holds group information. |  [optional] |
|**issuerUri** | **String** | URI for the OIDC provider. This should point to the level below .well-known/openid-configuration. |  [optional] |
|**kubectlRedirectUri** | **String** | Registered redirect uri to redirect users going through OAuth flow using kubectl plugin. |  [optional] |
|**scopes** | **String** | Comma-separated list of identifiers. |  [optional] |
|**userClaim** | **String** | Claim in OIDC ID token that holds username. |  [optional] |
|**userPrefix** | **String** | Prefix to prepend to user name. |  [optional] |



