

# Project

Contains properties of a Planning project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this project. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this project. |  [optional] |
|**audienceAgeGroup** | [**AudienceAgeGroupEnum**](#AudienceAgeGroupEnum) | Audience age group of this project. |  [optional] |
|**audienceGender** | [**AudienceGenderEnum**](#AudienceGenderEnum) | Audience gender of this project. |  [optional] |
|**budget** | **String** | Budget of this project in the currency specified by the current account. The value stored in this field represents only the non-fractional amount. For example, for USD, the smallest value that can be represented by this field is 1 US dollar. |  [optional] |
|**clientBillingCode** | **String** | Client billing code of this project. |  [optional] |
|**clientName** | **String** | Name of the project client. |  [optional] |
|**endDate** | **LocalDate** |  |  [optional] |
|**id** | **String** | ID of this project. This is a read-only, auto-generated field. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#project\&quot;. |  [optional] |
|**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**name** | **String** | Name of this project. |  [optional] |
|**overview** | **String** | Overview of this project. |  [optional] |
|**startDate** | **LocalDate** |  |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this project. |  [optional] |
|**targetClicks** | **String** | Number of clicks that the advertiser is targeting. |  [optional] |
|**targetConversions** | **String** | Number of conversions that the advertiser is targeting. |  [optional] |
|**targetCpaNanos** | **String** | CPA that the advertiser is targeting. |  [optional] |
|**targetCpcNanos** | **String** | CPC that the advertiser is targeting. |  [optional] |
|**targetCpmActiveViewNanos** | **String** | vCPM from Active View that the advertiser is targeting. |  [optional] |
|**targetCpmNanos** | **String** | CPM that the advertiser is targeting. |  [optional] |
|**targetImpressions** | **String** | Number of impressions that the advertiser is targeting. |  [optional] |



## Enum: AudienceAgeGroupEnum

| Name | Value |
|---- | -----|
| _18_24 | &quot;PLANNING_AUDIENCE_AGE_18_24&quot; |
| _25_34 | &quot;PLANNING_AUDIENCE_AGE_25_34&quot; |
| _35_44 | &quot;PLANNING_AUDIENCE_AGE_35_44&quot; |
| _45_54 | &quot;PLANNING_AUDIENCE_AGE_45_54&quot; |
| _55_64 | &quot;PLANNING_AUDIENCE_AGE_55_64&quot; |
| _65_OR_MORE | &quot;PLANNING_AUDIENCE_AGE_65_OR_MORE&quot; |
| UNKNOWN | &quot;PLANNING_AUDIENCE_AGE_UNKNOWN&quot; |



## Enum: AudienceGenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;PLANNING_AUDIENCE_GENDER_MALE&quot; |
| FEMALE | &quot;PLANNING_AUDIENCE_GENDER_FEMALE&quot; |



