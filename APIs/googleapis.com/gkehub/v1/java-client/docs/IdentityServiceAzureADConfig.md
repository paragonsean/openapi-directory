

# IdentityServiceAzureADConfig

Configuration for the AzureAD Auth flow.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | ID for the registered client application that makes authentication requests to the Azure AD identity provider. |  [optional] |
|**clientSecret** | **String** | Input only. Unencrypted AzureAD client secret will be passed to the GKE Hub CLH. |  [optional] |
|**encryptedClientSecret** | **byte[]** | Output only. Encrypted AzureAD client secret. |  [optional] [readonly] |
|**kubectlRedirectUri** | **String** | The redirect URL that kubectl uses for authorization. |  [optional] |
|**tenant** | **String** | Kind of Azure AD account to be authenticated. Supported values are or for accounts belonging to a specific tenant. |  [optional] |



