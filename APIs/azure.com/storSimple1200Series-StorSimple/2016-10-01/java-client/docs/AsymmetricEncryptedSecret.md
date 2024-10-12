

# AsymmetricEncryptedSecret

This class can be used as the Type for any secret entity represented as Password, CertThumbprint, Algorithm. This class is intended to be used when the secret is encrypted with an asymmetric key pair. The encryptionAlgorithm field is mainly for future usage to potentially allow different entities encrypted using different algorithms.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionAlgorithm** | [**EncryptionAlgorithmEnum**](#EncryptionAlgorithmEnum) | Algorithm used to encrypt \&quot;Value\&quot; |  |
|**encryptionCertificateThumbprint** | **String** | Thumbprint certificate that was used to encrypt \&quot;Value\&quot; |  [optional] |
|**value** | **String** | The value of the secret itself. If the secret is in plaintext then EncryptionAlgorithm will be none and EncryptionCertThumbprint will be null. |  |



## Enum: EncryptionAlgorithmEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AES256 | &quot;AES256&quot; |
| RSAES_PKCS1_V_1_5 | &quot;RSAES_PKCS1_v_1_5&quot; |



