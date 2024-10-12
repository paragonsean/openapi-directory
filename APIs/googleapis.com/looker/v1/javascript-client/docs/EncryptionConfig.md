# LookerGoogleCloudCoreApi.EncryptionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kmsKeyName** | **String** | Name of the CMEK key in KMS (input parameter). | [optional] 
**kmsKeyNameVersion** | **String** | Output only. Full name and version of the CMEK key currently in use to encrypt Looker data. Format: &#x60;projects/{project}/locations/{location}/keyRings/{ring}/cryptoKeys/{key}/cryptoKeyVersions/{version}&#x60;. Empty if CMEK is not configured in this instance. | [optional] [readonly] 
**kmsKeyState** | **String** | Output only. Status of the CMEK key. | [optional] [readonly] 



## Enum: KmsKeyStateEnum


* `KMS_KEY_STATE_UNSPECIFIED` (value: `"KMS_KEY_STATE_UNSPECIFIED"`)

* `VALID` (value: `"VALID"`)

* `REVOKED` (value: `"REVOKED"`)




