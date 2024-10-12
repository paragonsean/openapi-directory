# CloudKeyManagementServiceKmsApi.CryptoKeyVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | Output only. The CryptoKeyVersionAlgorithm that this CryptoKeyVersion supports. | [optional] [readonly] 
**attestation** | [**KeyOperationAttestation**](KeyOperationAttestation.md) |  | [optional] 
**createTime** | **String** | Output only. The time at which this CryptoKeyVersion was created. | [optional] [readonly] 
**destroyEventTime** | **String** | Output only. The time this CryptoKeyVersion&#39;s key material was destroyed. Only present if state is DESTROYED. | [optional] [readonly] 
**destroyTime** | **String** | Output only. The time this CryptoKeyVersion&#39;s key material is scheduled for destruction. Only present if state is DESTROY_SCHEDULED. | [optional] [readonly] 
**externalDestructionFailureReason** | **String** | Output only. The root cause of the most recent external destruction failure. Only present if state is EXTERNAL_DESTRUCTION_FAILED. | [optional] [readonly] 
**externalProtectionLevelOptions** | [**ExternalProtectionLevelOptions**](ExternalProtectionLevelOptions.md) |  | [optional] 
**generateTime** | **String** | Output only. The time this CryptoKeyVersion&#39;s key material was generated. | [optional] [readonly] 
**generationFailureReason** | **String** | Output only. The root cause of the most recent generation failure. Only present if state is GENERATION_FAILED. | [optional] [readonly] 
**importFailureReason** | **String** | Output only. The root cause of the most recent import failure. Only present if state is IMPORT_FAILED. | [optional] [readonly] 
**importJob** | **String** | Output only. The name of the ImportJob used in the most recent import of this CryptoKeyVersion. Only present if the underlying key material was imported. | [optional] [readonly] 
**importTime** | **String** | Output only. The time at which this CryptoKeyVersion&#39;s key material was most recently imported. | [optional] [readonly] 
**name** | **String** | Output only. The resource name for this CryptoKeyVersion in the format &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*_/cryptoKeyVersions/_*&#x60;. | [optional] [readonly] 
**protectionLevel** | **String** | Output only. The ProtectionLevel describing how crypto operations are performed with this CryptoKeyVersion. | [optional] [readonly] 
**reimportEligible** | **Boolean** | Output only. Whether or not this key version is eligible for reimport, by being specified as a target in ImportCryptoKeyVersionRequest.crypto_key_version. | [optional] [readonly] 
**state** | **String** | The current state of the CryptoKeyVersion. | [optional] 



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





## Enum: StateEnum


* `CRYPTO_KEY_VERSION_STATE_UNSPECIFIED` (value: `"CRYPTO_KEY_VERSION_STATE_UNSPECIFIED"`)

* `PENDING_GENERATION` (value: `"PENDING_GENERATION"`)

* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)

* `DESTROYED` (value: `"DESTROYED"`)

* `DESTROY_SCHEDULED` (value: `"DESTROY_SCHEDULED"`)

* `PENDING_IMPORT` (value: `"PENDING_IMPORT"`)

* `IMPORT_FAILED` (value: `"IMPORT_FAILED"`)

* `GENERATION_FAILED` (value: `"GENERATION_FAILED"`)

* `PENDING_EXTERNAL_DESTRUCTION` (value: `"PENDING_EXTERNAL_DESTRUCTION"`)

* `EXTERNAL_DESTRUCTION_FAILED` (value: `"EXTERNAL_DESTRUCTION_FAILED"`)




