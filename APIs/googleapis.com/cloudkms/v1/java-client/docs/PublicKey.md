

# PublicKey

The public keys for a given CryptoKeyVersion. Obtained via GetPublicKey.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | The Algorithm associated with this key. |  [optional] |
|**name** | **String** | The name of the CryptoKeyVersion public key. Provided here for verification. NOTE: This field is in Beta. |  [optional] |
|**pem** | **String** | A public key encoded in PEM format, populated only when GetPublicKey returns one key. For more information, see the [RFC 7468](https://tools.ietf.org/html/rfc7468) sections for [General Considerations](https://tools.ietf.org/html/rfc7468#section-2) and [Textual Encoding of Subject Public Key Info] (https://tools.ietf.org/html/rfc7468#section-13). |  [optional] |
|**pemCrc32c** | **String** | Integrity verification field: A CRC32C checksum of the returned PublicKey.pem. It is only populated when GetPublicKey returns one key. An integrity check of PublicKey.pem can be performed by computing the CRC32C checksum of PublicKey.pem and comparing your results to this field. Discard the response in case of non-matching checksum values, and perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type. NOTE: This field is in Beta. |  [optional] |
|**protectionLevel** | [**ProtectionLevelEnum**](#ProtectionLevelEnum) | The ProtectionLevel of the CryptoKeyVersion public key. |  [optional] |



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



