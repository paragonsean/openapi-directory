# CloudKeyManagementServiceKmsApi.PublicKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | The Algorithm associated with this key. | [optional] 
**name** | **String** | The name of the CryptoKeyVersion public key. Provided here for verification. NOTE: This field is in Beta. | [optional] 
**pem** | **String** | A public key encoded in PEM format, populated only when GetPublicKey returns one key. For more information, see the [RFC 7468](https://tools.ietf.org/html/rfc7468) sections for [General Considerations](https://tools.ietf.org/html/rfc7468#section-2) and [Textual Encoding of Subject Public Key Info] (https://tools.ietf.org/html/rfc7468#section-13). | [optional] 
**pemCrc32c** | **String** | Integrity verification field: A CRC32C checksum of the returned PublicKey.pem. It is only populated when GetPublicKey returns one key. An integrity check of PublicKey.pem can be performed by computing the CRC32C checksum of PublicKey.pem and comparing your results to this field. Discard the response in case of non-matching checksum values, and perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type. NOTE: This field is in Beta. | [optional] 
**protectionLevel** | **String** | The ProtectionLevel of the CryptoKeyVersion public key. | [optional] 



## Enum: AlgorithmEnum


* `CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED` (value: `"CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED"`)

* `GOOGLE_SYMMETRIC_ENCRYPTION` (value: `"GOOGLE_SYMMETRIC_ENCRYPTION"`)

* `AES_128_GCM` (value: `"AES_128_GCM"`)

* `AES_256_GCM` (value: `"AES_256_GCM"`)

* `AES_128_CBC` (value: `"AES_128_CBC"`)

* `AES_256_CBC` (value: `"AES_256_CBC"`)

* `AES_128_CTR` (value: `"AES_128_CTR"`)

* `AES_256_CTR` (value: `"AES_256_CTR"`)

* `RSA_SIGN_PSS_2048_SHA256` (value: `"RSA_SIGN_PSS_2048_SHA256"`)

* `RSA_SIGN_PSS_3072_SHA256` (value: `"RSA_SIGN_PSS_3072_SHA256"`)

* `RSA_SIGN_PSS_4096_SHA256` (value: `"RSA_SIGN_PSS_4096_SHA256"`)

* `RSA_SIGN_PSS_4096_SHA512` (value: `"RSA_SIGN_PSS_4096_SHA512"`)

* `RSA_SIGN_PKCS1_2048_SHA256` (value: `"RSA_SIGN_PKCS1_2048_SHA256"`)

* `RSA_SIGN_PKCS1_3072_SHA256` (value: `"RSA_SIGN_PKCS1_3072_SHA256"`)

* `RSA_SIGN_PKCS1_4096_SHA256` (value: `"RSA_SIGN_PKCS1_4096_SHA256"`)

* `RSA_SIGN_PKCS1_4096_SHA512` (value: `"RSA_SIGN_PKCS1_4096_SHA512"`)

* `RSA_SIGN_RAW_PKCS1_2048` (value: `"RSA_SIGN_RAW_PKCS1_2048"`)

* `RSA_SIGN_RAW_PKCS1_3072` (value: `"RSA_SIGN_RAW_PKCS1_3072"`)

* `RSA_SIGN_RAW_PKCS1_4096` (value: `"RSA_SIGN_RAW_PKCS1_4096"`)

* `RSA_DECRYPT_OAEP_2048_SHA256` (value: `"RSA_DECRYPT_OAEP_2048_SHA256"`)

* `RSA_DECRYPT_OAEP_3072_SHA256` (value: `"RSA_DECRYPT_OAEP_3072_SHA256"`)

* `RSA_DECRYPT_OAEP_4096_SHA256` (value: `"RSA_DECRYPT_OAEP_4096_SHA256"`)

* `RSA_DECRYPT_OAEP_4096_SHA512` (value: `"RSA_DECRYPT_OAEP_4096_SHA512"`)

* `RSA_DECRYPT_OAEP_2048_SHA1` (value: `"RSA_DECRYPT_OAEP_2048_SHA1"`)

* `RSA_DECRYPT_OAEP_3072_SHA1` (value: `"RSA_DECRYPT_OAEP_3072_SHA1"`)

* `RSA_DECRYPT_OAEP_4096_SHA1` (value: `"RSA_DECRYPT_OAEP_4096_SHA1"`)

* `EC_SIGN_P256_SHA256` (value: `"EC_SIGN_P256_SHA256"`)

* `EC_SIGN_P384_SHA384` (value: `"EC_SIGN_P384_SHA384"`)

* `EC_SIGN_SECP256K1_SHA256` (value: `"EC_SIGN_SECP256K1_SHA256"`)

* `HMAC_SHA256` (value: `"HMAC_SHA256"`)

* `HMAC_SHA1` (value: `"HMAC_SHA1"`)

* `HMAC_SHA384` (value: `"HMAC_SHA384"`)

* `HMAC_SHA512` (value: `"HMAC_SHA512"`)

* `HMAC_SHA224` (value: `"HMAC_SHA224"`)

* `EXTERNAL_SYMMETRIC_ENCRYPTION` (value: `"EXTERNAL_SYMMETRIC_ENCRYPTION"`)





## Enum: ProtectionLevelEnum


* `PROTECTION_LEVEL_UNSPECIFIED` (value: `"PROTECTION_LEVEL_UNSPECIFIED"`)

* `SOFTWARE` (value: `"SOFTWARE"`)

* `HSM` (value: `"HSM"`)

* `EXTERNAL` (value: `"EXTERNAL"`)

* `EXTERNAL_VPC` (value: `"EXTERNAL_VPC"`)




