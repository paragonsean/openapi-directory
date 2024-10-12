# CampaignManager360Api.Project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this project. | [optional] 
**advertiserId** | **String** | Advertiser ID of this project. | [optional] 
**audienceAgeGroup** | **String** | Audience age group of this project. | [optional] 
**audienceGender** | **String** | Audience gender of this project. | [optional] 
**budget** | **String** | Budget of this project in the currency specified by the current account. The value stored in this field represents only the non-fractional amount. For example, for USD, the smallest value that can be represented by this field is 1 US dollar. | [optional] 
**clientBillingCode** | **String** | Client billing code of this project. | [optional] 
**clientName** | **String** | Name of the project client. | [optional] 
**endDate** | **Date** |  | [optional] 
**id** | **String** | ID of this project. This is a read-only, auto-generated field. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#project\&quot;. | [optional] 
**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  | [optional] 
**name** | **String** | Name of this project. | [optional] 
**overview** | **String** | Overview of this project. | [optional] 
**startDate** | **Date** |  | [optional] 
**subaccountId** | **String** | Subaccount ID of this project. | [optional] 
**targetClicks** | **String** | Number of clicks that the advertiser is targeting. | [optional] 
**targetConversions** | **String** | Number of conversions that the advertiser is targeting. | [optional] 
**targetCpaNanos** | **String** | CPA that the advertiser is targeting. | [optional] 
**targetCpcNanos** | **String** | CPC that the advertiser is targeting. | [optional] 
**targetCpmActiveViewNanos** | **String** | vCPM from Active View that the advertiser is targeting. | [optional] 
**targetCpmNanos** | **String** | CPM that the advertiser is targeting. | [optional] 
**targetImpressions** | **String** | Number of impressions that the advertiser is targeting. | [optional] 



## Enum: AudienceAgeGroupEnum


* `18_24` (value: `"PLANNING_AUDIENCE_AGE_18_24"`)

* `25_34` (value: `"PLANNING_AUDIENCE_AGE_25_34"`)

* `35_44` (value: `"PLANNING_AUDIENCE_AGE_35_44"`)

* `45_54` (value: `"PLANNING_AUDIENCE_AGE_45_54"`)

* `55_64` (value: `"PLANNING_AUDIENCE_AGE_55_64"`)

* `65_OR_MORE` (value: `"PLANNING_AUDIENCE_AGE_65_OR_MORE"`)

* `UNKNOWN` (value: `"PLANNING_AUDIENCE_AGE_UNKNOWN"`)





## Enum: AudienceGenderEnum


* `MALE` (value: `"PLANNING_AUDIENCE_GENDER_MALE"`)

* `FEMALE` (value: `"PLANNING_AUDIENCE_GENDER_FEMALE"`)




