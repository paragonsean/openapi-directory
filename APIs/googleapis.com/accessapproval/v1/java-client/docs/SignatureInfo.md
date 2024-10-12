

# SignatureInfo

Information about the digital signature of the resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customerKmsKeyVersion** | **String** | The resource name of the customer CryptoKeyVersion used for signing. |  [optional] |
|**googleKeyAlgorithm** | [**GoogleKeyAlgorithmEnum**](#GoogleKeyAlgorithmEnum) | The hashing algorithm used for signature verification. It will only be present in the case of Google managed keys. |  [optional] |
|**googlePublicKeyPem** | **String** | The public key for the Google default signing, encoded in PEM format. The signature was created using a private key which may be verified using this public key. |  [optional] |
|**serializedApprovalRequest** | **byte[]** | The ApprovalRequest that is serialized without the SignatureInfo message field. This data is used with the hashing algorithm to generate the digital signature, and it can be used for signature verification. |  [optional] |
|**signature** | **byte[]** | The digital signature. |  [optional] |



## Enum: GoogleKeyAlgorithmEnum

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



