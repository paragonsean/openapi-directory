

# AppServiceCertificate

Key Vault container for a certificate that is purchased through Azure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyVaultId** | **String** | Key Vault resource Id. |  [optional] |
|**keyVaultSecretName** | **String** | Key Vault secret name. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Status of the Key Vault secret. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| INITIALIZED | &quot;Initialized&quot; |
| WAITING_ON_CERTIFICATE_ORDER | &quot;WaitingOnCertificateOrder&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CERTIFICATE_ORDER_FAILED | &quot;CertificateOrderFailed&quot; |
| OPERATION_NOT_PERMITTED_ON_KEY_VAULT | &quot;OperationNotPermittedOnKeyVault&quot; |
| AZURE_SERVICE_UNAUTHORIZED_TO_ACCESS_KEY_VAULT | &quot;AzureServiceUnauthorizedToAccessKeyVault&quot; |
| KEY_VAULT_DOES_NOT_EXIST | &quot;KeyVaultDoesNotExist&quot; |
| KEY_VAULT_SECRET_DOES_NOT_EXIST | &quot;KeyVaultSecretDoesNotExist&quot; |
| UNKNOWN_ERROR | &quot;UnknownError&quot; |
| EXTERNAL_PRIVATE_KEY | &quot;ExternalPrivateKey&quot; |
| UNKNOWN | &quot;Unknown&quot; |



