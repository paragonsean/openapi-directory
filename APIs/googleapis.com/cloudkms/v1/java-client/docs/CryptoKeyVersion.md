

# CryptoKeyVersion

A CryptoKeyVersion represents an individual cryptographic key, and the associated key material. An ENABLED version can be used for cryptographic operations. For security reasons, the raw cryptographic key material represented by a CryptoKeyVersion can never be viewed or exported. It can only be used to encrypt, decrypt, or sign data when an authorized user or application invokes Cloud KMS.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | Output only. The CryptoKeyVersionAlgorithm that this CryptoKeyVersion supports. |  [optional] [readonly] |
|**attestation** | [**KeyOperationAttestation**](KeyOperationAttestation.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which this CryptoKeyVersion was created. |  [optional] [readonly] |
|**destroyEventTime** | **String** | Output only. The time this CryptoKeyVersion&#39;s key material was destroyed. Only present if state is DESTROYED. |  [optional] [readonly] |
|**destroyTime** | **String** | Output only. The time this CryptoKeyVersion&#39;s key material is scheduled for destruction. Only present if state is DESTROY_SCHEDULED. |  [optional] [readonly] |
|**externalDestructionFailureReason** | **String** | Output only. The root cause of the most recent external destruction failure. Only present if state is EXTERNAL_DESTRUCTION_FAILED. |  [optional] [readonly] |
|**externalProtectionLevelOptions** | [**ExternalProtectionLevelOptions**](ExternalProtectionLevelOptions.md) |  |  [optional] |
|**generateTime** | **String** | Output only. The time this CryptoKeyVersion&#39;s key material was generated. |  [optional] [readonly] |
|**generationFailureReason** | **String** | Output only. The root cause of the most recent generation failure. Only present if state is GENERATION_FAILED. |  [optional] [readonly] |
|**importFailureReason** | **String** | Output only. The root cause of the most recent import failure. Only present if state is IMPORT_FAILED. |  [optional] [readonly] |
|**importJob** | **String** | Output only. The name of the ImportJob used in the most recent import of this CryptoKeyVersion. Only present if the underlying key material was imported. |  [optional] [readonly] |
|**importTime** | **String** | Output only. The time at which this CryptoKeyVersion&#39;s key material was most recently imported. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name for this CryptoKeyVersion in the format &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*_/cryptoKeyVersions/_*&#x60;. |  [optional] [readonly] |
|**protectionLevel** | [**ProtectionLevelEnum**](#ProtectionLevelEnum) | Output only. The ProtectionLevel describing how crypto operations are performed with this CryptoKeyVersion. |  [optional] [readonly] |
|**reimportEligible** | **Boolean** | Output only. Whether or not this key version is eligible for reimport, by being specified as a target in ImportCryptoKeyVersionRequest.crypto_key_version. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the CryptoKeyVersion. |  [optional] |



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



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CRYPTO_KEY_VERSION_STATE_UNSPECIFIED | &quot;CRYPTO_KEY_VERSION_STATE_UNSPECIFIED&quot; |
| PENDING_GENERATION | &quot;PENDING_GENERATION&quot; |
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| DESTROYED | &quot;DESTROYED&quot; |
| DESTROY_SCHEDULED | &quot;DESTROY_SCHEDULED&quot; |
| PENDING_IMPORT | &quot;PENDING_IMPORT&quot; |
| IMPORT_FAILED | &quot;IMPORT_FAILED&quot; |
| GENERATION_FAILED | &quot;GENERATION_FAILED&quot; |
| PENDING_EXTERNAL_DESTRUCTION | &quot;PENDING_EXTERNAL_DESTRUCTION&quot; |
| EXTERNAL_DESTRUCTION_FAILED | &quot;EXTERNAL_DESTRUCTION_FAILED&quot; |



