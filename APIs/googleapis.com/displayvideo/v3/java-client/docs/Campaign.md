

# Campaign

A single campaign.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiserId** | **String** | Output only. The unique ID of the advertiser the campaign belongs to. |  [optional] [readonly] |
|**campaignBudgets** | [**List&lt;CampaignBudget&gt;**](CampaignBudget.md) | The list of budgets available to this campaign. If this field is not set, the campaign uses an unlimited budget. |  [optional] |
|**campaignFlight** | [**CampaignFlight**](CampaignFlight.md) |  |  [optional] |
|**campaignGoal** | [**CampaignGoal**](CampaignGoal.md) |  |  [optional] |
|**campaignId** | **String** | Output only. The unique ID of the campaign. Assigned by the system. |  [optional] [readonly] |
|**displayName** | **String** | Required. The display name of the campaign. Must be UTF-8 encoded with a maximum size of 240 bytes. |  [optional] |
|**entityStatus** | [**EntityStatusEnum**](#EntityStatusEnum) | Required. Controls whether or not the insertion orders under this campaign can spend their budgets and bid on inventory. * Accepted values are &#x60;ENTITY_STATUS_ACTIVE&#x60;, &#x60;ENTITY_STATUS_ARCHIVED&#x60;, and &#x60;ENTITY_STATUS_PAUSED&#x60;. * For CreateCampaign method, &#x60;ENTITY_STATUS_ARCHIVED&#x60; is not allowed. |  [optional] |
|**frequencyCap** | [**FrequencyCap**](FrequencyCap.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of the campaign. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when the campaign was last updated. Assigned by the system. |  [optional] [readonly] |



## Enum: EntityStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ENTITY_STATUS_ACTIVE&quot; |
| ARCHIVED | &quot;ENTITY_STATUS_ARCHIVED&quot; |
| DRAFT | &quot;ENTITY_STATUS_DRAFT&quot; |
| PAUSED | &quot;ENTITY_STATUS_PAUSED&quot; |
| SCHEDULED_FOR_DELETION | &quot;ENTITY_STATUS_SCHEDULED_FOR_DELETION&quot; |



