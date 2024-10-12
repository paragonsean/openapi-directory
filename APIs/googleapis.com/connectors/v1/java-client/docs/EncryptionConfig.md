

# EncryptionConfig

Regional encryption config for CMEK details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionType** | [**EncryptionTypeEnum**](#EncryptionTypeEnum) | Optional. Encryption type for the region. |  [optional] |
|**kmsKeyName** | **String** | Optional. KMS crypto key. This field accepts identifiers of the form &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/ {crypto_key}&#x60; |  [optional] |



## Enum: EncryptionTypeEnum

| Name | Value |
|---- | -----|
| ENCRYPTION_TYPE_UNSPECIFIED | &quot;ENCRYPTION_TYPE_UNSPECIFIED&quot; |
| GMEK | &quot;GMEK&quot; |
| CMEK | &quot;CMEK&quot; |



