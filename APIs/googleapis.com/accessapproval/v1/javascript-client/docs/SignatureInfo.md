# AccessApprovalApi.SignatureInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customerKmsKeyVersion** | **String** | The resource name of the customer CryptoKeyVersion used for signing. | [optional] 
**googleKeyAlgorithm** | **String** | The hashing algorithm used for signature verification. It will only be present in the case of Google managed keys. | [optional] 
**googlePublicKeyPem** | **String** | The public key for the Google default signing, encoded in PEM format. The signature was created using a private key which may be verified using this public key. | [optional] 
**serializedApprovalRequest** | **Blob** | The ApprovalRequest that is serialized without the SignatureInfo message field. This data is used with the hashing algorithm to generate the digital signature, and it can be used for signature verification. | [optional] 
**signature** | **Blob** | The digital signature. | [optional] 



## Enum: GoogleKeyAlgorithmEnum


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




