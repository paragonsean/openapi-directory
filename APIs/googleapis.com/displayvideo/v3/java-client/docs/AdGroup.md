

# AdGroup

A single ad group associated with a line item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adGroupFormat** | [**AdGroupFormatEnum**](#AdGroupFormatEnum) | The format of the ads in the ad group. |  [optional] |
|**adGroupId** | **String** | The unique ID of the ad group. Assigned by the system. |  [optional] |
|**advertiserId** | **String** | The unique ID of the advertiser the ad group belongs to. |  [optional] |
|**bidStrategy** | [**BiddingStrategy**](BiddingStrategy.md) |  |  [optional] |
|**displayName** | **String** | The display name of the ad group. Must be UTF-8 encoded with a maximum size of 255 bytes. |  [optional] |
|**entityStatus** | [**EntityStatusEnum**](#EntityStatusEnum) | Controls whether or not the ad group can spend its budget and bid on inventory. If the ad group&#39;s parent line item is not active, the ad group can&#39;t spend its budget even if its own status is &#x60;ENTITY_STATUS_ACTIVE&#x60;. |  [optional] |
|**lineItemId** | **String** | The unique ID of the line item that the ad group belongs to. |  [optional] |
|**name** | **String** | The resource name of the ad group. |  [optional] |
|**productFeedData** | [**ProductFeedData**](ProductFeedData.md) |  |  [optional] |
|**targetingExpansion** | [**TargetingExpansionConfig**](TargetingExpansionConfig.md) |  |  [optional] |



## Enum: AdGroupFormatEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AD_GROUP_FORMAT_UNSPECIFIED&quot; |
| IN_STREAM | &quot;AD_GROUP_FORMAT_IN_STREAM&quot; |
| VIDEO_DISCOVERY | &quot;AD_GROUP_FORMAT_VIDEO_DISCOVERY&quot; |
| BUMPER | &quot;AD_GROUP_FORMAT_BUMPER&quot; |
| NON_SKIPPABLE_IN_STREAM | &quot;AD_GROUP_FORMAT_NON_SKIPPABLE_IN_STREAM&quot; |
| AUDIO | &quot;AD_GROUP_FORMAT_AUDIO&quot; |
| RESPONSIVE | &quot;AD_GROUP_FORMAT_RESPONSIVE&quot; |
| REACH | &quot;AD_GROUP_FORMAT_REACH&quot; |
| MASTHEAD | &quot;AD_GROUP_FORMAT_MASTHEAD&quot; |



## Enum: EntityStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_STATUS_UNSPECIFIED&quot; |
| ACTIVE | &quot;ENTITY_STATUS_ACTIVE&quot; |
| ARCHIVED | &quot;ENTITY_STATUS_ARCHIVED&quot; |
| DRAFT | &quot;ENTITY_STATUS_DRAFT&quot; |
| PAUSED | &quot;ENTITY_STATUS_PAUSED&quot; |
| SCHEDULED_FOR_DELETION | &quot;ENTITY_STATUS_SCHEDULED_FOR_DELETION&quot; |



