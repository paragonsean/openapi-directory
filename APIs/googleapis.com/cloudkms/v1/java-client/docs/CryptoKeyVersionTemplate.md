

# CryptoKeyVersionTemplate

A CryptoKeyVersionTemplate specifies the properties to use when creating a new CryptoKeyVersion, either manually with CreateCryptoKeyVersion or automatically as a result of auto-rotation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | Required. Algorithm to use when creating a CryptoKeyVersion based on this template. For backwards compatibility, GOOGLE_SYMMETRIC_ENCRYPTION is implied if both this field is omitted and CryptoKey.purpose is ENCRYPT_DECRYPT. |  [optional] |
|**protectionLevel** | [**ProtectionLevelEnum**](#ProtectionLevelEnum) | ProtectionLevel to use when creating a CryptoKeyVersion based on this template. Immutable. Defaults to SOFTWARE. |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED | &quot;CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED&quot; |
| GOOGLE_SYMMETRIC_ENCRYPTION | &quot;GOOGLE_SYMMETRIC_ENCRYPTION&quot; |
| AES_128_GCM | &quot;AES_128_GCM&quot; |
| AES_256_GCM | &quot;AES_256_GCM&quot; |
| AES_128_CBC | &quot;AES_128_CBC&quot; |
| AES_256_CBC | &quot;AES_256_CBC&quot; |
| AES_128_CTR | &quot;AES_128_CTR&quot; |
| AES_256_CTR | &quot;AES_256_CTR&quot; |
| RSA_SIGN_PSS_2048_SHA256 | &quot;RSA_SIGN_PSS_2048_SHA256&quot; |
| RSA_SIGN_PSS_3072_SHA256 | &quot;RSA_SIGN_PSS_3072_SHA256&quot; |
| RSA_SIGN_PSS_4096_SHA256 | &quot;RSA_SIGN_PSS_4096_SHA256&quot; |
| RSA_SIGN_PSS_4096_SHA512 | &quot;RSA_SIGN_PSS_4096_SHA512&quot; |
| RSA_SIGN_PKCS1_2048_SHA256 | &quot;RSA_SIGN_PKCS1_2048_SHA256&quot; |
| RSA_SIGN_PKCS1_3072_SHA256 | &quot;RSA_SIGN_PKCS1_3072_SHA256&quot; |
| RSA_SIGN_PKCS1_4096_SHA256 | &quot;RSA_SIGN_PKCS1_4096_SHA256&quot; |
| RSA_SIGN_PKCS1_4096_SHA512 | &quot;RSA_SIGN_PKCS1_4096_SHA512&quot; |
| RSA_SIGN_RAW_PKCS1_2048 | &quot;RSA_SIGN_RAW_PKCS1_2048&quot; |
| RSA_SIGN_RAW_PKCS1_3072 | &quot;RSA_SIGN_RAW_PKCS1_3072&quot; |
| RSA_SIGN_RAW_PKCS1_4096 | &quot;RSA_SIGN_RAW_PKCS1_4096&quot; |
| RSA_DECRYPT_OAEP_2048_SHA256 | &quot;RSA_DECRYPT_OAEP_2048_SHA256&quot; |
| RSA_DECRYPT_OAEP_3072_SHA256 | &quot;RSA_DECRYPT_OAEP_3072_SHA256&quot; |
| RSA_DECRYPT_OAEP_4096_SHA256 | &quot;RSA_DECRYPT_OAEP_4096_SHA256&quot; |
| RSA_DECRYPT_OAEP_4096_SHA512 | &quot;RSA_DECRYPT_OAEP_4096_SHA512&quot; |
| RSA_DECRYPT_OAEP_2048_SHA1 | &quot;RSA_DECRYPT_OAEP_2048_SHA1&quot; |
| RSA_DECRYPT_OAEP_3072_SHA1 | &quot;RSA_DECRYPT_OAEP_3072_SHA1&quot; |
| RSA_DECRYPT_OAEP_4096_SHA1 | &quot;RSA_DECRYPT_OAEP_4096_SHA1&quot; |
| EC_SIGN_P256_SHA256 | &quot;EC_SIGN_P256_SHA256&quot; |
| EC_SIGN_P384_SHA384 | &quot;EC_SIGN_P384_SHA384&quot; |
| EC_SIGN_SECP256_K1_SHA256 | &quot;EC_SIGN_SECP256K1_SHA256&quot; |
| HMAC_SHA256 | &quot;HMAC_SHA256&quot; |
| HMAC_SHA1 | &quot;HMAC_SHA1&quot; |
| HMAC_SHA384 | &quot;HMAC_SHA384&quot; |
| HMAC_SHA512 | &quot;HMAC_SHA512&quot; |
| HMAC_SHA224 | &quot;HMAC_SHA224&quot; |
| EXTERNAL_SYMMETRIC_ENCRYPTION | &quot;EXTERNAL_SYMMETRIC_ENCRYPTION&quot; |



## Enum: ProtectionLevelEnum

| Name | Value |
|---- | -----|
| PROTECTION_LEVEL_UNSPECIFIED | &quot;PROTECTION_LEVEL_UNSPECIFIED&quot; |
| SOFTWARE | &quot;SOFTWARE&quot; |
| HSM | &quot;HSM&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |
| EXTERNAL_VPC | &quot;EXTERNAL_VPC&quot; |



