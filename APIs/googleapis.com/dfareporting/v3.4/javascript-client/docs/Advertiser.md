# CampaignManager360Api.Advertiser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this advertiser.This is a read-only field that can be left blank. | [optional] 
**advertiserGroupId** | **String** | ID of the advertiser group this advertiser belongs to. You can group advertisers for reporting purposes, allowing you to see aggregated information for all advertisers in each group. | [optional] 
**clickThroughUrlSuffix** | **String** | Suffix added to click-through URL of ad creative associations under this advertiser. Must be less than 129 characters long. | [optional] 
**defaultClickThroughEventTagId** | **String** | ID of the click-through event tag to apply by default to the landing pages of this advertiser&#39;s campaigns. | [optional] 
**defaultEmail** | **String** | Default email address used in sender field for tag emails. | [optional] 
**floodlightConfigurationId** | **String** | Floodlight configuration ID of this advertiser. The floodlight configuration ID will be created automatically, so on insert this field should be left blank. This field can be set to another advertiser&#39;s floodlight configuration ID in order to share that advertiser&#39;s floodlight configuration with this advertiser, so long as: - This advertiser&#39;s original floodlight configuration is not already associated with floodlight activities or floodlight activity groups. - This advertiser&#39;s original floodlight configuration is not already shared with another advertiser.  | [optional] 
**floodlightConfigurationIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**id** | **String** | ID of this advertiser. This is a read-only, auto-generated field. | [optional] 
**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#advertiser\&quot;. | [optional] 
**name** | **String** | Name of this advertiser. This is a required field and must be less than 256 characters long and unique among advertisers of the same account. | [optional] 
**originalFloodlightConfigurationId** | **String** | Original floodlight configuration before any sharing occurred. Set the floodlightConfigurationId of this advertiser to originalFloodlightConfigurationId to unshare the advertiser&#39;s current floodlight configuration. You cannot unshare an advertiser&#39;s floodlight configuration if the shared configuration has activities associated with any campaign or placement. | [optional] 
**status** | **String** | Status of this advertiser. | [optional] 
**subaccountId** | **String** | Subaccount ID of this advertiser.This is a read-only field that can be left blank. | [optional] 
**suspended** | **Boolean** | Suspension status of this advertiser. | [optional] 



## Enum: StatusEnum


* `APPROVED` (value: `"APPROVED"`)

* `ON_HOLD` (value: `"ON_HOLD"`)




