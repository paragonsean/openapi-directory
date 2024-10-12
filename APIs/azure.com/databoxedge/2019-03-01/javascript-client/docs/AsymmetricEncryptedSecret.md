# DataBoxEdgeManagementClient.AsymmetricEncryptedSecret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionAlgorithm** | **String** | The algorithm used to encrypt \&quot;Value\&quot;. | 
**encryptionCertThumbprint** | **String** | Thumbprint certificate used to encrypt \\\&quot;Value\\\&quot;. If the value is unencrypted, it will be null. | [optional] 
**value** | **String** | The value of the secret. | 



## Enum: EncryptionAlgorithmEnum


* `None` (value: `"None"`)

* `AES256` (value: `"AES256"`)

* `RSAES_PKCS1_v_1_5` (value: `"RSAES_PKCS1_v_1_5"`)




