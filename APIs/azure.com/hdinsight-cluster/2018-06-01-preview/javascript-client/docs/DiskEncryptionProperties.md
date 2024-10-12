# HdInsightManagementClient.DiskEncryptionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionAlgorithm** | **String** | Algorithm identifier for encryption, default RSA-OAEP. | [optional] 
**keyName** | **String** | Key name that is used for enabling disk encryption. | [optional] 
**keyVersion** | **String** | Specific key version that is used for enabling disk encryption. | [optional] 
**msiResourceId** | **String** | Resource ID of Managed Identity that is used to access the key vault. | [optional] 
**vaultUri** | **String** | Base key vault URI where the customers key is located eg. https://myvault.vault.azure.net | [optional] 



## Enum: EncryptionAlgorithmEnum


* `RSA-OAEP` (value: `"RSA-OAEP"`)

* `RSA-OAEP-256` (value: `"RSA-OAEP-256"`)

* `RSA1_5` (value: `"RSA1_5"`)




