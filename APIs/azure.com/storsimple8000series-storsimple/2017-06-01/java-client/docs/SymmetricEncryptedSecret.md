

# SymmetricEncryptedSecret

Represents the secrets encrypted using Symmetric Encryption Key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionAlgorithm** | [**EncryptionAlgorithmEnum**](#EncryptionAlgorithmEnum) | The algorithm used to encrypt the \&quot;Value\&quot;. |  |
|**value** | **String** | The value of the secret itself. If the secret is in plaintext or null then EncryptionAlgorithm will be none. |  |
|**valueCertificateThumbprint** | **String** | The thumbprint of the cert that was used to encrypt \&quot;Value\&quot;. |  [optional] |



## Enum: EncryptionAlgorithmEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AES256 | &quot;AES256&quot; |
| RSAES_PKCS1_V_1_5 | &quot;RSAES_PKCS1_v_1_5&quot; |



