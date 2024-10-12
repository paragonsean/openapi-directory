# BusinessProfilePerformanceApi.LocationsApi

All URIs are relative to *https://businessprofileperformance.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries**](LocationsApi.md#businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries) | **GET** /v1/{location}:fetchMultiDailyMetricsTimeSeries | 
[**businessprofileperformanceLocationsGetDailyMetricsTimeSeries**](LocationsApi.md#businessprofileperformanceLocationsGetDailyMetricsTimeSeries) | **GET** /v1/{name}:getDailyMetricsTimeSeries | 
[**businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList**](LocationsApi.md#businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList) | **GET** /v1/{parent}/searchkeywords/impressions/monthly | 



## businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries

> FetchMultiDailyMetricsTimeSeriesResponse businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries(location, opts)



 Returns the values for each date from a given time range and optionally the sub entity type, where applicable, that are associated with the specific daily metrics. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345:fetchMultiDailyMetricsTimeSeries?dailyMetrics&#x3D;WEBSITE_CLICKS&amp;dailyMetrics&#x3D;CALL_CLICKS&amp;daily_range.start_date.year&#x3D;2022&amp;daily_range.start_date.month&#x3D;1&amp;daily_range.start_date.day&#x3D;1&amp;daily_range.end_date.year&#x3D;2022&amp;daily_range.end_date.month&#x3D;3&amp;daily_range.end_date.day&#x3D;31&#x60;

### Example

```javascript
import BusinessProfilePerformanceApi from 'business_profile_performance_api';

let apiInstance = new BusinessProfilePerformanceApi.LocationsApi();
let location = "location_example"; // String | Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'dailyMetrics': ["null"], // [String] | Required. The metrics to retrieve time series for.
  'dailyRangeEndDateDay': 56, // Number | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
  'dailyRangeEndDateMonth': 56, // Number | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
  'dailyRangeEndDateYear': 56, // Number | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
  'dailyRangeStartDateDay': 56, // Number | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
  'dailyRangeStartDateMonth': 56, // Number | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
  'dailyRangeStartDateYear': 56 // Number | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
};
apiInstance.businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries(location, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **String**| Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **dailyMetrics** | [**[String]**](String.md)| Required. The metrics to retrieve time series for. | [optional] 
 **dailyRangeEndDateDay** | **Number**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] 
 **dailyRangeEndDateMonth** | **Number**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] 
 **dailyRangeEndDateYear** | **Number**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] 
 **dailyRangeStartDateDay** | **Number**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] 
 **dailyRangeStartDateMonth** | **Number**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] 
 **dailyRangeStartDateYear** | **Number**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] 

### Return type

[**FetchMultiDailyMetricsTimeSeriesResponse**](FetchMultiDailyMetricsTimeSeriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## businessprofileperformanceLocationsGetDailyMetricsTimeSeries

> GetDailyMetricsTimeSeriesResponse businessprofileperformanceLocationsGetDailyMetricsTimeSeries(name, opts)



 Returns the values for each date from a given time range that are associated with the specific daily metric. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345:getDailyMetricsTimeSeries?dailyMetric&#x3D;WEBSITE_CLICKS&amp;daily_range.start_date.year&#x3D;2022&amp;daily_range.start_date.month&#x3D;1&amp;daily_range.start_date.day&#x3D;1&amp;daily_range.end_date.year&#x3D;2022&amp;daily_range.end_date.month&#x3D;3&amp;daily_range.end_date.day&#x3D;31&#x60;

### Example

```javascript
import BusinessProfilePerformanceApi from 'business_profile_performance_api';

let apiInstance = new BusinessProfilePerformanceApi.LocationsApi();
let name = "name_example"; // String | Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'dailyMetric': "dailyMetric_example", // String | Required. The metric to retrieve time series.
  'dailyRangeEndDateDay': 56, // Number | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
  'dailyRangeEndDateMonth': 56, // Number | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
  'dailyRangeEndDateYear': 56, // Number | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
  'dailyRangeStartDateDay': 56, // Number | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
  'dailyRangeStartDateMonth': 56, // Number | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
  'dailyRangeStartDateYear': 56, // Number | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
  'dailySubEntityTypeDayOfWeek': "dailySubEntityTypeDayOfWeek_example", // String | Represents the day of the week. Eg: MONDAY. Currently supported DailyMetrics = NONE.
  'dailySubEntityTypeTimeOfDayHours': 56, // Number | Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
  'dailySubEntityTypeTimeOfDayMinutes': 56, // Number | Minutes of hour of day. Must be from 0 to 59.
  'dailySubEntityTypeTimeOfDayNanos': 56, // Number | Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.
  'dailySubEntityTypeTimeOfDaySeconds': 56 // Number | Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds.
};
apiInstance.businessprofileperformanceLocationsGetDailyMetricsTimeSeries(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **dailyMetric** | **String**| Required. The metric to retrieve time series. | [optional] 
 **dailyRangeEndDateDay** | **Number**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] 
 **dailyRangeEndDateMonth** | **Number**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] 
 **dailyRangeEndDateYear** | **Number**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] 
 **dailyRangeStartDateDay** | **Number**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] 
 **dailyRangeStartDateMonth** | **Number**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] 
 **dailyRangeStartDateYear** | **Number**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] 
 **dailySubEntityTypeDayOfWeek** | **String**| Represents the day of the week. Eg: MONDAY. Currently supported DailyMetrics &#x3D; NONE. | [optional] 
 **dailySubEntityTypeTimeOfDayHours** | **Number**| Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] 
 **dailySubEntityTypeTimeOfDayMinutes** | **Number**| Minutes of hour of day. Must be from 0 to 59. | [optional] 
 **dailySubEntityTypeTimeOfDayNanos** | **Number**| Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. | [optional] 
 **dailySubEntityTypeTimeOfDaySeconds** | **Number**| Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds. | [optional] 

### Return type

[**GetDailyMetricsTimeSeriesResponse**](GetDailyMetricsTimeSeriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList

> ListSearchKeywordImpressionsMonthlyResponse businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList(parent, opts)



Returns the search keywords used to find a business in search or maps. Each search keyword is accompanied by impressions which are aggregated on a monthly basis. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345/searchkeywords/impressions/monthly?monthly_range.start_month.year&#x3D;2022&amp;monthly_range.start_month.month&#x3D;1&amp;monthly_range.end_month.year&#x3D;2022&amp;monthly_range.end_month.month&#x3D;3&#x60;

### Example

```javascript
import BusinessProfilePerformanceApi from 'business_profile_performance_api';

let apiInstance = new BusinessProfilePerformanceApi.LocationsApi();
let parent = "parent_example"; // String | Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'monthlyRangeEndMonthDay': 56, // Number | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
  'monthlyRangeEndMonthMonth': 56, // Number | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
  'monthlyRangeEndMonthYear': 56, // Number | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
  'monthlyRangeStartMonthDay': 56, // Number | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
  'monthlyRangeStartMonthMonth': 56, // Number | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
  'monthlyRangeStartMonthYear': 56, // Number | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
  'pageSize': 56, // Number | Optional. The number of results requested. The default page size is 100. Page size can be set to a maximum of 100.
  'pageToken': "pageToken_example" // String | Optional. A token indicating the next paginated result to be returned.
};
apiInstance.businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList(parent, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **String**| Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **monthlyRangeEndMonthDay** | **Number**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] 
 **monthlyRangeEndMonthMonth** | **Number**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] 
 **monthlyRangeEndMonthYear** | **Number**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] 
 **monthlyRangeStartMonthDay** | **Number**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] 
 **monthlyRangeStartMonthMonth** | **Number**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] 
 **monthlyRangeStartMonthYear** | **Number**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] 
 **pageSize** | **Number**| Optional. The number of results requested. The default page size is 100. Page size can be set to a maximum of 100. | [optional] 
 **pageToken** | **String**| Optional. A token indicating the next paginated result to be returned. | [optional] 

### Return type

[**ListSearchKeywordImpressionsMonthlyResponse**](ListSearchKeywordImpressionsMonthlyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

