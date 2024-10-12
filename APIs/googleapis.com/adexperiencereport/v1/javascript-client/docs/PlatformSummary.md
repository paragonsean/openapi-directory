# AdExperienceReportApi.PlatformSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**betterAdsStatus** | **String** | The site&#39;s Ad Experience Report status on this platform. | [optional] 
**enforcementTime** | **String** | The time at which [enforcement](https://support.google.com/webtools/answer/7308033) against the site began or will begin on this platform. Not set when the filter_status is OFF. | [optional] 
**filterStatus** | **String** | The site&#39;s [enforcement status](https://support.google.com/webtools/answer/7308033) on this platform. | [optional] 
**lastChangeTime** | **String** | The time at which the site&#39;s status last changed on this platform. | [optional] 
**region** | **[String]** | The site&#39;s regions on this platform. No longer populated, because there is no longer any semantic difference between sites in different regions. | [optional] 
**reportUrl** | **String** | A link to the full Ad Experience Report for the site on this platform.. Not set in ViolatingSitesResponse. Note that you must complete the [Search Console verification process](https://support.google.com/webmasters/answer/9008080) for the site before you can access the full report. | [optional] 
**underReview** | **Boolean** | Whether the site is currently under review on this platform. | [optional] 



## Enum: BetterAdsStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `PASSING` (value: `"PASSING"`)

* `WARNING` (value: `"WARNING"`)

* `FAILING` (value: `"FAILING"`)





## Enum: FilterStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `true` (value: `"true"`)

* `false` (value: `"false"`)

* `PAUSED` (value: `"PAUSED"`)

* `PENDING` (value: `"PENDING"`)





## Enum: [RegionEnum]


* `UNKNOWN` (value: `"REGION_UNKNOWN"`)

* `A` (value: `"REGION_A"`)

* `B` (value: `"REGION_B"`)

* `C` (value: `"REGION_C"`)




