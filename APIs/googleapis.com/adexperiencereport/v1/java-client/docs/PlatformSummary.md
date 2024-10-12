

# PlatformSummary

A site's Ad Experience Report summary on a single platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**betterAdsStatus** | [**BetterAdsStatusEnum**](#BetterAdsStatusEnum) | The site&#39;s Ad Experience Report status on this platform. |  [optional] |
|**enforcementTime** | **String** | The time at which [enforcement](https://support.google.com/webtools/answer/7308033) against the site began or will begin on this platform. Not set when the filter_status is OFF. |  [optional] |
|**filterStatus** | [**FilterStatusEnum**](#FilterStatusEnum) | The site&#39;s [enforcement status](https://support.google.com/webtools/answer/7308033) on this platform. |  [optional] |
|**lastChangeTime** | **String** | The time at which the site&#39;s status last changed on this platform. |  [optional] |
|**region** | [**List&lt;RegionEnum&gt;**](#List&lt;RegionEnum&gt;) | The site&#39;s regions on this platform. No longer populated, because there is no longer any semantic difference between sites in different regions. |  [optional] |
|**reportUrl** | **String** | A link to the full Ad Experience Report for the site on this platform.. Not set in ViolatingSitesResponse. Note that you must complete the [Search Console verification process](https://support.google.com/webmasters/answer/9008080) for the site before you can access the full report. |  [optional] |
|**underReview** | **Boolean** | Whether the site is currently under review on this platform. |  [optional] |



## Enum: BetterAdsStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| PASSING | &quot;PASSING&quot; |
| WARNING | &quot;WARNING&quot; |
| FAILING | &quot;FAILING&quot; |



## Enum: FilterStatusEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| TRUE | &quot;true&quot; |
| FALSE | &quot;false&quot; |
| PAUSED | &quot;PAUSED&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: List&lt;RegionEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;REGION_UNKNOWN&quot; |
| A | &quot;REGION_A&quot; |
| B | &quot;REGION_B&quot; |
| C | &quot;REGION_C&quot; |



