# DisplayVideo360Api.Advertiser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adServerConfig** | [**AdvertiserAdServerConfig**](AdvertiserAdServerConfig.md) |  | [optional] 
**advertiserId** | **String** | Output only. The unique ID of the advertiser. Assigned by the system. | [optional] [readonly] 
**creativeConfig** | [**AdvertiserCreativeConfig**](AdvertiserCreativeConfig.md) |  | [optional] 
**dataAccessConfig** | [**AdvertiserDataAccessConfig**](AdvertiserDataAccessConfig.md) |  | [optional] 
**displayName** | **String** | Required. The display name of the advertiser. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**entityStatus** | **String** | Required. Controls whether or not insertion orders and line items of the advertiser can spend their budgets and bid on inventory. * Accepted values are &#x60;ENTITY_STATUS_ACTIVE&#x60;, &#x60;ENTITY_STATUS_PAUSED&#x60; and &#x60;ENTITY_STATUS_SCHEDULED_FOR_DELETION&#x60;. * If set to &#x60;ENTITY_STATUS_SCHEDULED_FOR_DELETION&#x60;, the advertiser will be deleted 30 days from when it was first scheduled for deletion. | [optional] 
**generalConfig** | [**AdvertiserGeneralConfig**](AdvertiserGeneralConfig.md) |  | [optional] 
**integrationDetails** | [**IntegrationDetails**](IntegrationDetails.md) |  | [optional] 
**name** | **String** | Output only. The resource name of the advertiser. | [optional] [readonly] 
**partnerId** | **String** | Required. Immutable. The unique ID of the partner that the advertiser belongs to. | [optional] 
**prismaEnabled** | **Boolean** | Whether integration with Mediaocean (Prisma) is enabled. By enabling this, you agree to the following: On behalf of my company, I authorize Mediaocean (Prisma) to send budget segment plans to Google, and I authorize Google to send corresponding reporting and invoices from DV360 to Mediaocean for the purposes of budget planning, billing, and reconciliation for this advertiser. | [optional] 
**servingConfig** | [**AdvertiserTargetingConfig**](AdvertiserTargetingConfig.md) |  | [optional] 
**updateTime** | **String** | Output only. The timestamp when the advertiser was last updated. Assigned by the system. | [optional] [readonly] 



## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)




