# SearchAds360ReportingApi.GoogleAdsSearchads360V0CommonUnifiedCallAsset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adScheduleTargets** | [**[GoogleAdsSearchads360V0CommonAdScheduleInfo]**](GoogleAdsSearchads360V0CommonAdScheduleInfo.md) | List of non-overlapping schedules specifying all time intervals for which the asset may serve. There can be a maximum of 6 schedules per day, 42 in total. | [optional] 
**callConversionAction** | **String** | The conversion action to attribute a call conversion to. If not set, the default conversion action is used. This field only has effect if call_conversion_reporting_state is set to USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION. | [optional] 
**callConversionReportingState** | **String** | Output only. Indicates whether this CallAsset should use its own call conversion setting, follow the account level setting, or disable call conversion. | [optional] [readonly] 
**callOnly** | **Boolean** | Whether the call only shows the phone number without a link to the website. Applies to Microsoft Ads. | [optional] 
**callTrackingEnabled** | **Boolean** | Whether the call should be enabled on call tracking. Applies to Microsoft Ads. | [optional] 
**countryCode** | **String** | Two-letter country code of the phone number. Examples: &#39;US&#39;, &#39;us&#39;. | [optional] 
**endDate** | **String** | Last date of when this asset is effective and still serving, in yyyy-MM-dd format. | [optional] 
**phoneNumber** | **String** | The advertiser&#39;s raw phone number. Examples: &#39;1234567890&#39;, &#39;(123)456-7890&#39; | [optional] 
**startDate** | **String** | Start date of when this asset is effective and can begin serving, in yyyy-MM-dd format. | [optional] 
**useSearcherTimeZone** | **Boolean** | Whether to show the call extension in search user&#39;s time zone. Applies to Microsoft Ads. | [optional] 



## Enum: CallConversionReportingStateEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `DISABLED` (value: `"DISABLED"`)

* `USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION` (value: `"USE_ACCOUNT_LEVEL_CALL_CONVERSION_ACTION"`)

* `USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION` (value: `"USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION"`)




