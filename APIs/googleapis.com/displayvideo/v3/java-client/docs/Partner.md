

# Partner

A single partner in Display & Video 360 (DV360).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adServerConfig** | [**PartnerAdServerConfig**](PartnerAdServerConfig.md) |  |  [optional] |
|**billingConfig** | [**PartnerBillingConfig**](PartnerBillingConfig.md) |  |  [optional] |
|**dataAccessConfig** | [**PartnerDataAccessConfig**](PartnerDataAccessConfig.md) |  |  [optional] |
|**displayName** | **String** | The display name of the partner. Must be UTF-8 encoded with a maximum size of 240 bytes. |  [optional] |
|**entityStatus** | [**EntityStatusEnum**](#EntityStatusEnum) | Output only. The status of the partner. |  [optional] [readonly] |
|**exchangeConfig** | [**ExchangeConfig**](ExchangeConfig.md) |  |  [optional] |
|**generalConfig** | [**PartnerGeneralConfig**](PartnerGeneralConfig.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of the partner. |  [optional] [readonly] |
|**partnerId** | **String** | Output only. The unique ID of the partner. Assigned by the system. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when the partner was last updated. Assigned by the system. |  [optional] [readonly] |



## Enum: EntityStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ENTITY_STATUS_ACTIVE&quot; |
| ARCHIVED | &quot;ENTITY_STATUS_ARCHIVED&quot; |
| DRAFT | &quot;ENTITY_STATUS_DRAFT&quot; |
| PAUSED | &quot;ENTITY_STATUS_PAUSED&quot; |
| SCHEDULED_FOR_DELETION | &quot;ENTITY_STATUS_SCHEDULED_FOR_DELETION&quot; |



