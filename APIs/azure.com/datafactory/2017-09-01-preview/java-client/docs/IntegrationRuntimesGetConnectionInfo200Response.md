

# IntegrationRuntimesGetConnectionInfo200Response

Connection information for encrypting the on-premises data source credentials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostServiceUri** | **String** | The on-premises integration runtime host URL. |  [optional] [readonly] |
|**identityCertThumbprint** | **String** | The integration runtime SSL certificate thumbprint. Click-Once application uses it to do server validation. |  [optional] [readonly] |
|**isIdentityCertExprired** | **Boolean** | Whether the identity certificate is expired. |  [optional] [readonly] |
|**publicKey** | **String** | The public key for encrypting a credential when transferring the credential to the integration runtime. |  [optional] [readonly] |
|**serviceToken** | **String** | The token generated in service. Callers use this token to authenticate to integration runtime. |  [optional] [readonly] |
|**version** | **String** | The integration runtime version. |  [optional] [readonly] |



