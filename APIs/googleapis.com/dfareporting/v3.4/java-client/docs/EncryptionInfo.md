

# EncryptionInfo

A description of how user IDs are encrypted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionEntityId** | **String** | The encryption entity ID. This should match the encryption configuration for ad serving or Data Transfer. |  [optional] |
|**encryptionEntityType** | [**EncryptionEntityTypeEnum**](#EncryptionEntityTypeEnum) | The encryption entity type. This should match the encryption configuration for ad serving or Data Transfer. |  [optional] |
|**encryptionSource** | [**EncryptionSourceEnum**](#EncryptionSourceEnum) | Describes whether the encrypted cookie was received from ad serving (the %m macro) or from Data Transfer. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#encryptionInfo\&quot;. |  [optional] |



## Enum: EncryptionEntityTypeEnum

| Name | Value |
|---- | -----|
| ENCRYPTION_ENTITY_TYPE_UNKNOWN | &quot;ENCRYPTION_ENTITY_TYPE_UNKNOWN&quot; |
| DCM_ACCOUNT | &quot;DCM_ACCOUNT&quot; |
| DCM_ADVERTISER | &quot;DCM_ADVERTISER&quot; |
| DBM_PARTNER | &quot;DBM_PARTNER&quot; |
| DBM_ADVERTISER | &quot;DBM_ADVERTISER&quot; |
| ADWORDS_CUSTOMER | &quot;ADWORDS_CUSTOMER&quot; |
| DFP_NETWORK_CODE | &quot;DFP_NETWORK_CODE&quot; |



## Enum: EncryptionSourceEnum

| Name | Value |
|---- | -----|
| ENCRYPTION_SCOPE_UNKNOWN | &quot;ENCRYPTION_SCOPE_UNKNOWN&quot; |
| AD_SERVING | &quot;AD_SERVING&quot; |
| DATA_TRANSFER | &quot;DATA_TRANSFER&quot; |



