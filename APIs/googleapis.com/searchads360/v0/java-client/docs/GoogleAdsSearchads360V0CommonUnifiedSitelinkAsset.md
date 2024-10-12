

# GoogleAdsSearchads360V0CommonUnifiedSitelinkAsset

A unified sitelink asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adScheduleTargets** | [**List&lt;GoogleAdsSearchads360V0CommonAdScheduleInfo&gt;**](GoogleAdsSearchads360V0CommonAdScheduleInfo.md) | List of non-overlapping schedules specifying all time intervals for which the asset may serve. There can be a maximum of 6 schedules per day, 42 in total. |  [optional] |
|**description1** | **String** | First line of the description for the sitelink. If set, the length should be between 1 and 35, inclusive, and description2 must also be set. |  [optional] |
|**description2** | **String** | Second line of the description for the sitelink. If set, the length should be between 1 and 35, inclusive, and description1 must also be set. |  [optional] |
|**endDate** | **String** | Last date of when this asset is effective and still serving, in yyyy-MM-dd format. |  [optional] |
|**linkText** | **String** | URL display text for the sitelink. The length of this string should be between 1 and 25, inclusive. |  [optional] |
|**mobilePreferred** | **Boolean** | Whether the preference is for the sitelink asset to be displayed on mobile devices. Applies to Microsoft Ads. |  [optional] |
|**startDate** | **String** | Start date of when this asset is effective and can begin serving, in yyyy-MM-dd format. |  [optional] |
|**trackingId** | **String** | ID used for tracking clicks for the sitelink asset. This is a Yahoo! Japan only field. |  [optional] |
|**useSearcherTimeZone** | **Boolean** | Whether to show the sitelink asset in search user&#39;s time zone. Applies to Microsoft Ads. |  [optional] |



