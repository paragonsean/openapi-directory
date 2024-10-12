

# EncryptionConfig

Encryption configuration (i.e. CMEK).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyName** | **String** | Name of the CMEK key in KMS (input parameter). |  [optional] |
|**kmsKeyNameVersion** | **String** | Output only. Full name and version of the CMEK key currently in use to encrypt Looker data. Format: &#x60;projects/{project}/locations/{location}/keyRings/{ring}/cryptoKeys/{key}/cryptoKeyVersions/{version}&#x60;. Empty if CMEK is not configured in this instance. |  [optional] [readonly] |
|**kmsKeyState** | [**KmsKeyStateEnum**](#KmsKeyStateEnum) | Output only. Status of the CMEK key. |  [optional] [readonly] |



## Enum: KmsKeyStateEnum

| Name | Value |
|---- | -----|
| KMS_KEY_STATE_UNSPECIFIED | &quot;KMS_KEY_STATE_UNSPECIFIED&quot; |
| VALID | &quot;VALID&quot; |
| REVOKED | &quot;REVOKED&quot; |



