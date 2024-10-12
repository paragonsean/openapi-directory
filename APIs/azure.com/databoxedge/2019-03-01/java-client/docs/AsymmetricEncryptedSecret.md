

# AsymmetricEncryptedSecret

Represent the secrets intended for encryption with asymmetric key pair.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionAlgorithm** | [**EncryptionAlgorithmEnum**](#EncryptionAlgorithmEnum) | The algorithm used to encrypt \&quot;Value\&quot;. |  |
|**encryptionCertThumbprint** | **String** | Thumbprint certificate used to encrypt \\\&quot;Value\\\&quot;. If the value is unencrypted, it will be null. |  [optional] |
|**value** | **String** | The value of the secret. |  |



## Enum: EncryptionAlgorithmEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AES256 | &quot;AES256&quot; |
| RSAES_PKCS1_V_1_5 | &quot;RSAES_PKCS1_v_1_5&quot; |



