

# GoogleAnalyticsAdminV1alphaChannelGroup

A resource message representing a Channel Group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the Channel Group. Max length of 256 characters. |  [optional] |
|**displayName** | **String** | Required. The display name of the Channel Group. Max length of 80 characters. |  [optional] |
|**groupingRule** | [**List&lt;GoogleAnalyticsAdminV1alphaGroupingRule&gt;**](GoogleAnalyticsAdminV1alphaGroupingRule.md) | Required. The grouping rules of channels. Maximum number of rules is 50. |  [optional] |
|**name** | **String** | Output only. The resource name for this Channel Group resource. Format: properties/{property}/channelGroups/{channel_group} |  [optional] [readonly] |
|**systemDefined** | **Boolean** | Output only. If true, then this channel group is the Default Channel Group predefined by Google Analytics. Display name and grouping rules cannot be updated for this channel group. |  [optional] [readonly] |



