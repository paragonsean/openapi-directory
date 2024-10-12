# CampaignManager360Api.EncryptionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionEntityId** | **String** | The encryption entity ID. This should match the encryption configuration for ad serving or Data Transfer. | [optional] 
**encryptionEntityType** | **String** | The encryption entity type. This should match the encryption configuration for ad serving or Data Transfer. | [optional] 
**encryptionSource** | **String** | Describes whether the encrypted cookie was received from ad serving (the %m macro) or from Data Transfer. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#encryptionInfo\&quot;. | [optional] 



## Enum: EncryptionEntityTypeEnum


* `ENCRYPTION_ENTITY_TYPE_UNKNOWN` (value: `"ENCRYPTION_ENTITY_TYPE_UNKNOWN"`)

* `DCM_ACCOUNT` (value: `"DCM_ACCOUNT"`)

* `DCM_ADVERTISER` (value: `"DCM_ADVERTISER"`)

* `DBM_PARTNER` (value: `"DBM_PARTNER"`)

* `DBM_ADVERTISER` (value: `"DBM_ADVERTISER"`)

* `ADWORDS_CUSTOMER` (value: `"ADWORDS_CUSTOMER"`)

* `DFP_NETWORK_CODE` (value: `"DFP_NETWORK_CODE"`)





## Enum: EncryptionSourceEnum


* `ENCRYPTION_SCOPE_UNKNOWN` (value: `"ENCRYPTION_SCOPE_UNKNOWN"`)

* `AD_SERVING` (value: `"AD_SERVING"`)

* `DATA_TRANSFER` (value: `"DATA_TRANSFER"`)




