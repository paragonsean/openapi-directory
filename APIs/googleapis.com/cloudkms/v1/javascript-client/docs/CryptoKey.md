# CloudKeyManagementServiceKmsApi.CryptoKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time at which this CryptoKey was created. | [optional] [readonly] 
**cryptoKeyBackend** | **String** | Immutable. The resource name of the backend environment where the key material for all CryptoKeyVersions associated with this CryptoKey reside and where all related cryptographic operations are performed. Only applicable if CryptoKeyVersions have a ProtectionLevel of EXTERNAL_VPC, with the resource name in the format &#x60;projects/_*_/locations/_*_/ekmConnections/_*&#x60;. Note, this list is non-exhaustive and may apply to additional ProtectionLevels in the future. | [optional] 
**destroyScheduledDuration** | **String** | Immutable. The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 24 hours. | [optional] 
**importOnly** | **Boolean** | Immutable. Whether this key may contain imported versions only. | [optional] 
**labels** | **{String: String}** | Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys). | [optional] 
**name** | **String** | Output only. The resource name for this CryptoKey in the format &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*&#x60;. | [optional] [readonly] 
**nextRotationTime** | **String** | At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted. | [optional] 
**primary** | [**CryptoKeyVersion**](CryptoKeyVersion.md) |  | [optional] 
**purpose** | **String** | Immutable. The immutable purpose of this CryptoKey. | [optional] 
**rotationPeriod** | **String** | next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted. | [optional] 
**versionTemplate** | [**CryptoKeyVersionTemplate**](CryptoKeyVersionTemplate.md) |  | [optional] 



## Enum: PurposeEnum


* `CRYPTO_KEY_PURPOSE_UNSPECIFIED` (value: `"CRYPTO_KEY_PURPOSE_UNSPECIFIED"`)

* `ENCRYPT_DECRYPT` (value: `"ENCRYPT_DECRYPT"`)

* `ASYMMETRIC_SIGN` (value: `"ASYMMETRIC_SIGN"`)

* `ASYMMETRIC_DECRYPT` (value: `"ASYMMETRIC_DECRYPT"`)

* `RAW_ENCRYPT_DECRYPT` (value: `"RAW_ENCRYPT_DECRYPT"`)

* `MAC` (value: `"MAC"`)




