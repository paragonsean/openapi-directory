# CampaignManager360Api.TargetableRemarketingList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. | [optional] 
**active** | **Boolean** | Whether this targetable remarketing list is active. | [optional] 
**advertiserId** | **String** | Dimension value for the advertiser ID that owns this targetable remarketing list. | [optional] 
**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**description** | **String** | Targetable remarketing list description. | [optional] 
**id** | **String** | Targetable remarketing list ID. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#targetableRemarketingList\&quot;. | [optional] 
**lifeSpan** | **String** | Number of days that a user should remain in the targetable remarketing list without an impression. | [optional] 
**listSize** | **String** | Number of users currently in the list. This is a read-only field. | [optional] 
**listSource** | **String** | Product from which this targetable remarketing list was originated. | [optional] 
**name** | **String** | Name of the targetable remarketing list. Is no greater than 128 characters long. | [optional] 
**subaccountId** | **String** | Subaccount ID of this remarketing list. This is a read-only, auto-generated field that is only returned in GET requests. | [optional] 



## Enum: ListSourceEnum


* `OTHER` (value: `"REMARKETING_LIST_SOURCE_OTHER"`)

* `ADX` (value: `"REMARKETING_LIST_SOURCE_ADX"`)

* `DFP` (value: `"REMARKETING_LIST_SOURCE_DFP"`)

* `XFP` (value: `"REMARKETING_LIST_SOURCE_XFP"`)

* `DFA` (value: `"REMARKETING_LIST_SOURCE_DFA"`)

* `GA` (value: `"REMARKETING_LIST_SOURCE_GA"`)

* `YOUTUBE` (value: `"REMARKETING_LIST_SOURCE_YOUTUBE"`)

* `DBM` (value: `"REMARKETING_LIST_SOURCE_DBM"`)

* `GPLUS` (value: `"REMARKETING_LIST_SOURCE_GPLUS"`)

* `DMP` (value: `"REMARKETING_LIST_SOURCE_DMP"`)

* `PLAY_STORE` (value: `"REMARKETING_LIST_SOURCE_PLAY_STORE"`)




