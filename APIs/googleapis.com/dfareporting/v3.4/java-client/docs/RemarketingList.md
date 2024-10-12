

# RemarketingList

Contains properties of a remarketing list. Remarketing enables you to create lists of users who have performed specific actions on a site, then target ads to members of those lists. This resource can be used to manage remarketing lists that are owned by your advertisers. To see all remarketing lists that are visible to your advertisers, including those that are shared to your advertiser or account, use the TargetableRemarketingLists resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. |  [optional] |
|**active** | **Boolean** | Whether this remarketing list is active. |  [optional] |
|**advertiserId** | **String** | Dimension value for the advertiser ID that owns this remarketing list. This is a required field. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**description** | **String** | Remarketing list description. |  [optional] |
|**id** | **String** | Remarketing list ID. This is a read-only, auto-generated field. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#remarketingList\&quot;. |  [optional] |
|**lifeSpan** | **String** | Number of days that a user should remain in the remarketing list without an impression. Acceptable values are 1 to 540, inclusive. |  [optional] |
|**listPopulationRule** | [**ListPopulationRule**](ListPopulationRule.md) |  |  [optional] |
|**listSize** | **String** | Number of users currently in the list. This is a read-only field. |  [optional] |
|**listSource** | [**ListSourceEnum**](#ListSourceEnum) | Product from which this remarketing list was originated. |  [optional] |
|**name** | **String** | Name of the remarketing list. This is a required field. Must be no greater than 128 characters long. |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. |  [optional] |



## Enum: ListSourceEnum

| Name | Value |
|---- | -----|
| OTHER | &quot;REMARKETING_LIST_SOURCE_OTHER&quot; |
| ADX | &quot;REMARKETING_LIST_SOURCE_ADX&quot; |
| DFP | &quot;REMARKETING_LIST_SOURCE_DFP&quot; |
| XFP | &quot;REMARKETING_LIST_SOURCE_XFP&quot; |
| DFA | &quot;REMARKETING_LIST_SOURCE_DFA&quot; |
| GA | &quot;REMARKETING_LIST_SOURCE_GA&quot; |
| YOUTUBE | &quot;REMARKETING_LIST_SOURCE_YOUTUBE&quot; |
| DBM | &quot;REMARKETING_LIST_SOURCE_DBM&quot; |
| GPLUS | &quot;REMARKETING_LIST_SOURCE_GPLUS&quot; |
| DMP | &quot;REMARKETING_LIST_SOURCE_DMP&quot; |
| PLAY_STORE | &quot;REMARKETING_LIST_SOURCE_PLAY_STORE&quot; |



