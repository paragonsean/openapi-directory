

# GoogleAdsSearchads360V0CommonUnifiedCalloutAsset

A unified callout asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adScheduleTargets** | [**List&lt;GoogleAdsSearchads360V0CommonAdScheduleInfo&gt;**](GoogleAdsSearchads360V0CommonAdScheduleInfo.md) | List of non-overlapping schedules specifying all time intervals for which the asset may serve. There can be a maximum of 6 schedules per day, 42 in total. |  [optional] |
|**calloutText** | **String** | The callout text. The length of this string should be between 1 and 25, inclusive. |  [optional] |
|**endDate** | **String** | Last date of when this asset is effective and still serving, in yyyy-MM-dd format. |  [optional] |
|**startDate** | **String** | Start date of when this asset is effective and can begin serving, in yyyy-MM-dd format. |  [optional] |
|**useSearcherTimeZone** | **Boolean** | Whether to show the asset in search user&#39;s time zone. Applies to Microsoft Ads. |  [optional] |



