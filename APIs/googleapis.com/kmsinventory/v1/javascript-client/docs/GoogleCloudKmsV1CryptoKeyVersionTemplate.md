# KmsInventoryApi.GoogleCloudKmsV1CryptoKeyVersionTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | Required. Algorithm to use when creating a CryptoKeyVersion based on this template. For backwards compatibility, GOOGLE_SYMMETRIC_ENCRYPTION is implied if both this field is omitted and CryptoKey.purpose is ENCRYPT_DECRYPT. | [optional] 
**protectionLevel** | **String** | ProtectionLevel to use when creating a CryptoKeyVersion based on this template. Immutable. Defaults to SOFTWARE. | [optional] 



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




