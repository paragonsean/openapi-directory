

# DiskEncryptionProperties

The disk encryption properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionAlgorithm** | [**EncryptionAlgorithmEnum**](#EncryptionAlgorithmEnum) | Algorithm identifier for encryption, default RSA-OAEP. |  [optional] |
|**keyName** | **String** | Key name that is used for enabling disk encryption. |  [optional] |
|**keyVersion** | **String** | Specific key version that is used for enabling disk encryption. |  [optional] |
|**msiResourceId** | **String** | Resource ID of Managed Identity that is used to access the key vault. |  [optional] |
|**vaultUri** | **String** | Base key vault URI where the customers key is located eg. https://myvault.vault.azure.net |  [optional] |



## Enum: EncryptionAlgorithmEnum

| Name | Value |
|---- | -----|
| RSA_OAEP | &quot;RSA-OAEP&quot; |
| RSA_OAEP_256 | &quot;RSA-OAEP-256&quot; |
| RSA1_5 | &quot;RSA1_5&quot; |



