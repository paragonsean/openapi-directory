# StorSimpleManagementClient.AsymmetricEncryptedSecret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionAlgorithm** | **String** | Algorithm used to encrypt \&quot;Value\&quot; | 
**encryptionCertificateThumbprint** | **String** | Thumbprint certificate that was used to encrypt \&quot;Value\&quot; | [optional] 
**value** | **String** | The value of the secret itself. If the secret is in plaintext then EncryptionAlgorithm will be none and EncryptionCertThumbprint will be null. | 



## Enum: EncryptionAlgorithmEnum


* `None` (value: `"None"`)

* `AES256` (value: `"AES256"`)

* `RSAES_PKCS1_v_1_5` (value: `"RSAES_PKCS1_v_1_5"`)




