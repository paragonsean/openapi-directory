# CampaignManager360Api.CreativeGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this creative group. This is a read-only field that can be left blank. | [optional] 
**advertiserId** | **String** | Advertiser ID of this creative group. This is a required field on insertion. | [optional] 
**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**groupNumber** | **Number** | Subgroup of the creative group. Assign your creative groups to a subgroup in order to filter or manage them more easily. This field is required on insertion and is read-only after insertion. Acceptable values are 1 to 2, inclusive. | [optional] 
**id** | **String** | ID of this creative group. This is a read-only, auto-generated field. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#creativeGroup\&quot;. | [optional] 
**name** | **String** | Name of this creative group. This is a required field and must be less than 256 characters long and unique among creative groups of the same advertiser. | [optional] 
**subaccountId** | **String** | Subaccount ID of this creative group. This is a read-only field that can be left blank. | [optional] 


