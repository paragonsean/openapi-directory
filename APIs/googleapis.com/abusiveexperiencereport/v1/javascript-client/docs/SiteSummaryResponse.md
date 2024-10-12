# AbusiveExperienceReportApi.SiteSummaryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abusiveStatus** | **String** | The site&#39;s Abusive Experience Report status. | [optional] 
**enforcementTime** | **String** | The time at which [enforcement](https://support.google.com/webtools/answer/7538608) against the site began or will begin. Not set when the filter_status is OFF. | [optional] 
**filterStatus** | **String** | The site&#39;s [enforcement status](https://support.google.com/webtools/answer/7538608). | [optional] 
**lastChangeTime** | **String** | The time at which the site&#39;s status last changed. | [optional] 
**reportUrl** | **String** | A link to the full Abusive Experience Report for the site. Not set in ViolatingSitesResponse. Note that you must complete the [Search Console verification process](https://support.google.com/webmasters/answer/9008080) for the site before you can access the full report. | [optional] 
**reviewedSite** | **String** | The name of the reviewed site, e.g. &#x60;google.com&#x60;. | [optional] 
**underReview** | **Boolean** | Whether the site is currently under review. | [optional] 



## Enum: AbusiveStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `PASSING` (value: `"PASSING"`)

* `FAILING` (value: `"FAILING"`)





## Enum: FilterStatusEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `true` (value: `"true"`)

* `false` (value: `"false"`)

* `PAUSED` (value: `"PAUSED"`)

* `PENDING` (value: `"PENDING"`)




