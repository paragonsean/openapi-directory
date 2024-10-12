# LocationsApi

All URIs are relative to *https://businessprofileperformance.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries**](LocationsApi.md#businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries) | **GET** /v1/{location}:fetchMultiDailyMetricsTimeSeries |  |
| [**businessprofileperformanceLocationsGetDailyMetricsTimeSeries**](LocationsApi.md#businessprofileperformanceLocationsGetDailyMetricsTimeSeries) | **GET** /v1/{name}:getDailyMetricsTimeSeries |  |
| [**businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList**](LocationsApi.md#businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList) | **GET** /v1/{parent}/searchkeywords/impressions/monthly |  |


<a id="businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries"></a>
# **businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries**
> FetchMultiDailyMetricsTimeSeriesResponse businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries(location, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, dailyMetrics, dailyRangeEndDateDay, dailyRangeEndDateMonth, dailyRangeEndDateYear, dailyRangeStartDateDay, dailyRangeStartDateMonth, dailyRangeStartDateYear)



 Returns the values for each date from a given time range and optionally the sub entity type, where applicable, that are associated with the specific daily metrics. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345:fetchMultiDailyMetricsTimeSeries?dailyMetrics&#x3D;WEBSITE_CLICKS&amp;dailyMetrics&#x3D;CALL_CLICKS&amp;daily_range.start_date.year&#x3D;2022&amp;daily_range.start_date.month&#x3D;1&amp;daily_range.start_date.day&#x3D;1&amp;daily_range.end_date.year&#x3D;2022&amp;daily_range.end_date.month&#x3D;3&amp;daily_range.end_date.day&#x3D;31&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://businessprofileperformance.googleapis.com");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String location = "location_example"; // String | Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    List<String> dailyMetrics = Arrays.asList(); // List<String> | Required. The metrics to retrieve time series for.
    Integer dailyRangeEndDateDay = 56; // Integer | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
    Integer dailyRangeEndDateMonth = 56; // Integer | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    Integer dailyRangeEndDateYear = 56; // Integer | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    Integer dailyRangeStartDateDay = 56; // Integer | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
    Integer dailyRangeStartDateMonth = 56; // Integer | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    Integer dailyRangeStartDateYear = 56; // Integer | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    try {
      FetchMultiDailyMetricsTimeSeriesResponse result = apiInstance.businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries(location, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, dailyMetrics, dailyRangeEndDateDay, dailyRangeEndDateMonth, dailyRangeEndDateYear, dailyRangeStartDateDay, dailyRangeStartDateMonth, dailyRangeStartDateYear);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#businessprofileperformanceLocationsFetchMultiDailyMetricsTimeSeries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **location** | **String**| Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **dailyMetrics** | [**List&lt;String&gt;**](String.md)| Required. The metrics to retrieve time series for. | [optional] [enum: DAILY_METRIC_UNKNOWN, BUSINESS_IMPRESSIONS_DESKTOP_MAPS, BUSINESS_IMPRESSIONS_DESKTOP_SEARCH, BUSINESS_IMPRESSIONS_MOBILE_MAPS, BUSINESS_IMPRESSIONS_MOBILE_SEARCH, BUSINESS_CONVERSATIONS, BUSINESS_DIRECTION_REQUESTS, CALL_CLICKS, WEBSITE_CLICKS, BUSINESS_BOOKINGS, BUSINESS_FOOD_ORDERS, BUSINESS_FOOD_MENU_CLICKS] |
| **dailyRangeEndDateDay** | **Integer**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] |
| **dailyRangeEndDateMonth** | **Integer**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] |
| **dailyRangeEndDateYear** | **Integer**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] |
| **dailyRangeStartDateDay** | **Integer**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] |
| **dailyRangeStartDateMonth** | **Integer**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] |
| **dailyRangeStartDateYear** | **Integer**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] |

### Return type

[**FetchMultiDailyMetricsTimeSeriesResponse**](FetchMultiDailyMetricsTimeSeriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="businessprofileperformanceLocationsGetDailyMetricsTimeSeries"></a>
# **businessprofileperformanceLocationsGetDailyMetricsTimeSeries**
> GetDailyMetricsTimeSeriesResponse businessprofileperformanceLocationsGetDailyMetricsTimeSeries(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, dailyMetric, dailyRangeEndDateDay, dailyRangeEndDateMonth, dailyRangeEndDateYear, dailyRangeStartDateDay, dailyRangeStartDateMonth, dailyRangeStartDateYear, dailySubEntityTypeDayOfWeek, dailySubEntityTypeTimeOfDayHours, dailySubEntityTypeTimeOfDayMinutes, dailySubEntityTypeTimeOfDayNanos, dailySubEntityTypeTimeOfDaySeconds)



 Returns the values for each date from a given time range that are associated with the specific daily metric. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345:getDailyMetricsTimeSeries?dailyMetric&#x3D;WEBSITE_CLICKS&amp;daily_range.start_date.year&#x3D;2022&amp;daily_range.start_date.month&#x3D;1&amp;daily_range.start_date.day&#x3D;1&amp;daily_range.end_date.year&#x3D;2022&amp;daily_range.end_date.month&#x3D;3&amp;daily_range.end_date.day&#x3D;31&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://businessprofileperformance.googleapis.com");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String name = "name_example"; // String | Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String dailyMetric = "DAILY_METRIC_UNKNOWN"; // String | Required. The metric to retrieve time series.
    Integer dailyRangeEndDateDay = 56; // Integer | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
    Integer dailyRangeEndDateMonth = 56; // Integer | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    Integer dailyRangeEndDateYear = 56; // Integer | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    Integer dailyRangeStartDateDay = 56; // Integer | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
    Integer dailyRangeStartDateMonth = 56; // Integer | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    Integer dailyRangeStartDateYear = 56; // Integer | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    String dailySubEntityTypeDayOfWeek = "DAY_OF_WEEK_UNSPECIFIED"; // String | Represents the day of the week. Eg: MONDAY. Currently supported DailyMetrics = NONE.
    Integer dailySubEntityTypeTimeOfDayHours = 56; // Integer | Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
    Integer dailySubEntityTypeTimeOfDayMinutes = 56; // Integer | Minutes of hour of day. Must be from 0 to 59.
    Integer dailySubEntityTypeTimeOfDayNanos = 56; // Integer | Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.
    Integer dailySubEntityTypeTimeOfDaySeconds = 56; // Integer | Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds.
    try {
      GetDailyMetricsTimeSeriesResponse result = apiInstance.businessprofileperformanceLocationsGetDailyMetricsTimeSeries(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, dailyMetric, dailyRangeEndDateDay, dailyRangeEndDateMonth, dailyRangeEndDateYear, dailyRangeStartDateDay, dailyRangeStartDateMonth, dailyRangeStartDateYear, dailySubEntityTypeDayOfWeek, dailySubEntityTypeTimeOfDayHours, dailySubEntityTypeTimeOfDayMinutes, dailySubEntityTypeTimeOfDayNanos, dailySubEntityTypeTimeOfDaySeconds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#businessprofileperformanceLocationsGetDailyMetricsTimeSeries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **dailyMetric** | **String**| Required. The metric to retrieve time series. | [optional] [enum: DAILY_METRIC_UNKNOWN, BUSINESS_IMPRESSIONS_DESKTOP_MAPS, BUSINESS_IMPRESSIONS_DESKTOP_SEARCH, BUSINESS_IMPRESSIONS_MOBILE_MAPS, BUSINESS_IMPRESSIONS_MOBILE_SEARCH, BUSINESS_CONVERSATIONS, BUSINESS_DIRECTION_REQUESTS, CALL_CLICKS, WEBSITE_CLICKS, BUSINESS_BOOKINGS, BUSINESS_FOOD_ORDERS, BUSINESS_FOOD_MENU_CLICKS] |
| **dailyRangeEndDateDay** | **Integer**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] |
| **dailyRangeEndDateMonth** | **Integer**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] |
| **dailyRangeEndDateYear** | **Integer**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] |
| **dailyRangeStartDateDay** | **Integer**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] |
| **dailyRangeStartDateMonth** | **Integer**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] |
| **dailyRangeStartDateYear** | **Integer**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] |
| **dailySubEntityTypeDayOfWeek** | **String**| Represents the day of the week. Eg: MONDAY. Currently supported DailyMetrics &#x3D; NONE. | [optional] [enum: DAY_OF_WEEK_UNSPECIFIED, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY] |
| **dailySubEntityTypeTimeOfDayHours** | **Integer**| Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] |
| **dailySubEntityTypeTimeOfDayMinutes** | **Integer**| Minutes of hour of day. Must be from 0 to 59. | [optional] |
| **dailySubEntityTypeTimeOfDayNanos** | **Integer**| Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999. | [optional] |
| **dailySubEntityTypeTimeOfDaySeconds** | **Integer**| Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds. | [optional] |

### Return type

[**GetDailyMetricsTimeSeriesResponse**](GetDailyMetricsTimeSeriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList"></a>
# **businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList**
> ListSearchKeywordImpressionsMonthlyResponse businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, monthlyRangeEndMonthDay, monthlyRangeEndMonthMonth, monthlyRangeEndMonthYear, monthlyRangeStartMonthDay, monthlyRangeStartMonthMonth, monthlyRangeStartMonthYear, pageSize, pageToken)



Returns the search keywords used to find a business in search or maps. Each search keyword is accompanied by impressions which are aggregated on a monthly basis. Example request: &#x60;GET https://businessprofileperformance.googleapis.com/v1/locations/12345/searchkeywords/impressions/monthly?monthly_range.start_month.year&#x3D;2022&amp;monthly_range.start_month.month&#x3D;1&amp;monthly_range.end_month.year&#x3D;2022&amp;monthly_range.end_month.month&#x3D;3&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://businessprofileperformance.googleapis.com");

    LocationsApi apiInstance = new LocationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer monthlyRangeEndMonthDay = 56; // Integer | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
    Integer monthlyRangeEndMonthMonth = 56; // Integer | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    Integer monthlyRangeEndMonthYear = 56; // Integer | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    Integer monthlyRangeStartMonthDay = 56; // Integer | Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.
    Integer monthlyRangeStartMonthMonth = 56; // Integer | Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.
    Integer monthlyRangeStartMonthYear = 56; // Integer | Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.
    Integer pageSize = 56; // Integer | Optional. The number of results requested. The default page size is 100. Page size can be set to a maximum of 100.
    String pageToken = "pageToken_example"; // String | Optional. A token indicating the next paginated result to be returned.
    try {
      ListSearchKeywordImpressionsMonthlyResponse result = apiInstance.businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, monthlyRangeEndMonthDay, monthlyRangeEndMonthMonth, monthlyRangeEndMonthYear, monthlyRangeStartMonthDay, monthlyRangeStartMonthMonth, monthlyRangeStartMonthYear, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocationsApi#businessprofileperformanceLocationsSearchkeywordsImpressionsMonthlyList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The location for which the time series should be fetched. Format: locations/{location_id} where location_id is an unobfuscated listing id. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **monthlyRangeEndMonthDay** | **Integer**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] |
| **monthlyRangeEndMonthMonth** | **Integer**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] |
| **monthlyRangeEndMonthYear** | **Integer**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] |
| **monthlyRangeStartMonthDay** | **Integer**| Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn&#39;t significant. | [optional] |
| **monthlyRangeStartMonthMonth** | **Integer**| Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day. | [optional] |
| **monthlyRangeStartMonthYear** | **Integer**| Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year. | [optional] |
| **pageSize** | **Integer**| Optional. The number of results requested. The default page size is 100. Page size can be set to a maximum of 100. | [optional] |
| **pageToken** | **String**| Optional. A token indicating the next paginated result to be returned. | [optional] |

### Return type

[**ListSearchKeywordImpressionsMonthlyResponse**](ListSearchKeywordImpressionsMonthlyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

