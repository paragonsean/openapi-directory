

# SymmetricEncryptedSecret

This class can be used as the Type for any secret entity represented as Value, ValueCertificateThumbprint, EncryptionAlgorithm. In this case, \"Value\" is a secret and the \"valueThumbprint\" represents the certificate thumbprint of the value. The algorithm field is mainly for future usage to potentially allow different entities encrypted using different algorithms.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionAlgorithm** | [**EncryptionAlgorithmEnum**](#EncryptionAlgorithmEnum) | Algorithm used to encrypt \&quot;Value\&quot; |  |
|**value** | **String** | The value of the secret itself. If the secret is in plaintext or null then EncryptionAlgorithm will be none |  |
|**valueCertificateThumbprint** | **String** | Thumbprint cert that was used to encrypt \&quot;Value\&quot; |  [optional] |



## Enum: EncryptionAlgorithmEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| AES256 | &quot;AES256&quot; |
| RSAES_PKCS1_V_1_5 | &quot;RSAES_PKCS1_v_1_5&quot; |



