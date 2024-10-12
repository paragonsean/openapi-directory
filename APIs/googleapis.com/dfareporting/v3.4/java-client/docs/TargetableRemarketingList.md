

# TargetableRemarketingList

Contains properties of a targetable remarketing list. Remarketing enables you to create lists of users who have performed specific actions on a site, then target ads to members of those lists. This resource is a read-only view of a remarketing list to be used to faciliate targeting ads to specific lists. Remarketing lists that are owned by your advertisers and those that are shared to your advertisers or account are accessible via this resource. To manage remarketing lists that are owned by your advertisers, use the RemarketingLists resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. |  [optional] |
|**active** | **Boolean** | Whether this targetable remarketing list is active. |  [optional] |
|**advertiserId** | **String** | Dimension value for the advertiser ID that owns this targetable remarketing list. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**description** | **String** | Targetable remarketing list description. |  [optional] |
|**id** | **String** | Targetable remarketing list ID. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#targetableRemarketingList\&quot;. |  [optional] |
|**lifeSpan** | **String** | Number of days that a user should remain in the targetable remarketing list without an impression. |  [optional] |
|**listSize** | **String** | Number of users currently in the list. This is a read-only field. |  [optional] |
|**listSource** | [**ListSourceEnum**](#ListSourceEnum) | Product from which this targetable remarketing list was originated. |  [optional] |
|**name** | **String** | Name of the targetable remarketing list. Is no greater than 128 characters long. |  [optional] |
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



