# DisplayVideo360Api.Campaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiserId** | **String** | Output only. The unique ID of the advertiser the campaign belongs to. | [optional] [readonly] 
**campaignBudgets** | [**[CampaignBudget]**](CampaignBudget.md) | The list of budgets available to this campaign. If this field is not set, the campaign uses an unlimited budget. | [optional] 
**campaignFlight** | [**CampaignFlight**](CampaignFlight.md) |  | [optional] 
**campaignGoal** | [**CampaignGoal**](CampaignGoal.md) |  | [optional] 
**campaignId** | **String** | Output only. The unique ID of the campaign. Assigned by the system. | [optional] [readonly] 
**displayName** | **String** | Required. The display name of the campaign. Must be UTF-8 encoded with a maximum size of 240 bytes. | [optional] 
**entityStatus** | **String** | Required. Controls whether or not the insertion orders under this campaign can spend their budgets and bid on inventory. * Accepted values are &#x60;ENTITY_STATUS_ACTIVE&#x60;, &#x60;ENTITY_STATUS_ARCHIVED&#x60;, and &#x60;ENTITY_STATUS_PAUSED&#x60;. * For CreateCampaign method, &#x60;ENTITY_STATUS_ARCHIVED&#x60; is not allowed. | [optional] 
**frequencyCap** | [**FrequencyCap**](FrequencyCap.md) |  | [optional] 
**name** | **String** | Output only. The resource name of the campaign. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when the campaign was last updated. Assigned by the system. | [optional] [readonly] 



## Enum: EntityStatusEnum


* `UNSPECIFIED` (value: `"ENTITY_STATUS_UNSPECIFIED"`)

* `ACTIVE` (value: `"ENTITY_STATUS_ACTIVE"`)

* `ARCHIVED` (value: `"ENTITY_STATUS_ARCHIVED"`)

* `DRAFT` (value: `"ENTITY_STATUS_DRAFT"`)

* `PAUSED` (value: `"ENTITY_STATUS_PAUSED"`)

* `SCHEDULED_FOR_DELETION` (value: `"ENTITY_STATUS_SCHEDULED_FOR_DELETION"`)




