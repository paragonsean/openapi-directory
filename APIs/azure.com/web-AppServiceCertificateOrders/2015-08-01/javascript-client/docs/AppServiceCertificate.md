# AppServiceCertificateOrdersApiClient.AppServiceCertificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyVaultId** | **String** | Key Vault resource Id. | [optional] 
**keyVaultSecretName** | **String** | Key Vault secret name. | [optional] 
**provisioningState** | **String** | Status of the Key Vault secret. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Initialized` (value: `"Initialized"`)

* `WaitingOnCertificateOrder` (value: `"WaitingOnCertificateOrder"`)

* `Succeeded` (value: `"Succeeded"`)

* `CertificateOrderFailed` (value: `"CertificateOrderFailed"`)

* `OperationNotPermittedOnKeyVault` (value: `"OperationNotPermittedOnKeyVault"`)

* `AzureServiceUnauthorizedToAccessKeyVault` (value: `"AzureServiceUnauthorizedToAccessKeyVault"`)

* `KeyVaultDoesNotExist` (value: `"KeyVaultDoesNotExist"`)

* `KeyVaultSecretDoesNotExist` (value: `"KeyVaultSecretDoesNotExist"`)

* `UnknownError` (value: `"UnknownError"`)

* `ExternalPrivateKey` (value: `"ExternalPrivateKey"`)

* `Unknown` (value: `"Unknown"`)




