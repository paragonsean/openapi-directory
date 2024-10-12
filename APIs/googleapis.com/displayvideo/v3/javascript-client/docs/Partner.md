# DisplayVideo360Api.Partner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adServerConfig** | [**PartnerAdServerConfig**](PartnerAdServerConfig.md) |  | [optional] 
**billingConfig** | [**PartnerBillingConfig**](PartnerBillingConfig.md) |  | [optional] 
**dataAccessConfig** | [**PartnerDataAccessConfig**](PartnerDataAccessConfig.md) |  | [optional] 
**displayName** | **String** | The display name of the partner. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**entityStatus** | **String** | Output only. The status of the partner. | [optional] [readonly] 
**exchangeConfig** | [**ExchangeConfig**](ExchangeConfig.md) |  | [optional] 
**generalConfig** | [**PartnerGeneralConfig**](PartnerGeneralConfig.md) |  | [optional] 
**name** | **String** | Output only. The resource name of the partner. | [optional] [readonly] 
**partnerId** | **String** | Output only. The unique ID of the partner. Assigned by the system. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when the partner was last updated. Assigned by the system. | [optional] [readonly] 



## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)




