# VitalsApi

All URIs are relative to *https://playdeveloperreporting.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**playdeveloperreportingVitalsErrorsIssuesSearch**](VitalsApi.md#playdeveloperreportingVitalsErrorsIssuesSearch) | **GET** /v1alpha1/{parent}/errorIssues:search |  |
| [**playdeveloperreportingVitalsErrorsReportsSearch**](VitalsApi.md#playdeveloperreportingVitalsErrorsReportsSearch) | **GET** /v1alpha1/{parent}/errorReports:search |  |
| [**playdeveloperreportingVitalsStuckbackgroundwakelockrateGet**](VitalsApi.md#playdeveloperreportingVitalsStuckbackgroundwakelockrateGet) | **GET** /v1alpha1/{name} |  |
| [**playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery**](VitalsApi.md#playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery) | **POST** /v1alpha1/{name}:query |  |


<a id="playdeveloperreportingVitalsErrorsIssuesSearch"></a>
# **playdeveloperreportingVitalsErrorsIssuesSearch**
> GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse playdeveloperreportingVitalsErrorsIssuesSearch(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, intervalEndTimeDay, intervalEndTimeHours, intervalEndTimeMinutes, intervalEndTimeMonth, intervalEndTimeNanos, intervalEndTimeSeconds, intervalEndTimeTimeZoneId, intervalEndTimeTimeZoneVersion, intervalEndTimeUtcOffset, intervalEndTimeYear, intervalStartTimeDay, intervalStartTimeHours, intervalStartTimeMinutes, intervalStartTimeMonth, intervalStartTimeNanos, intervalStartTimeSeconds, intervalStartTimeTimeZoneId, intervalStartTimeTimeZoneVersion, intervalStartTimeUtcOffset, intervalStartTimeYear, orderBy, pageSize, pageToken)



Searches all error issues in which reports have been grouped.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VitalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://playdeveloperreporting.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VitalsApi apiInstance = new VitalsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Parent resource of the error issues, indicating the application for which they were received. Format: apps/{app}
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
    String filter = "filter_example"; // String | A selection predicate to retrieve only a subset of the issues. Counts in the returned error issues will only reflect occurrences that matched the filter. For filtering basics, please check [AIP-160](https://google.aip.dev/160). ** Supported field names:** * `apiLevel`: Matches error issues that occurred in the requested Android versions (specified as the numeric API level) only. Example: `apiLevel = 28 OR apiLevel = 29`. * `versionCode`: Matches error issues that occurred in the requested app version codes only. Example: `versionCode = 123 OR versionCode = 456`. * `deviceModel`: Matches error issues that occurred in the requested devices. Example: `deviceModel = \"google/walleye\" OR deviceModel = \"google/marlin\"`. * `deviceBrand`: Matches error issues that occurred in the requested device brands. Example: `deviceBrand = \"Google\". * `deviceType`: Matches error issues that occurred in the requested device types. Example: `deviceType = \"PHONE\"`. * `errorIssueType`: Matches error issues of the requested types only. Valid candidates: `CRASH`, `ANR`. Example: `errorIssueType = CRASH OR errorIssueType = ANR`. * `appProcessState`: Matches error issues on the process state of an app, indicating whether an app runs in the foreground (user-visible) or background. Valid candidates: `FOREGROUND`, `BACKGROUND`. Example: `appProcessState = FOREGROUND`. * `isUserPerceived`: Matches error issues that are user-perceived. It is not accompanied by any operators. Example: `isUserPerceived`. ** Supported operators:** * Comparison operators: The only supported comparison operator is equality. The filtered field must appear on the left hand side of the comparison. * Logical Operators: Logical operators `AND` and `OR` can be used to build complex filters following a conjunctive normal form (CNF), i.e., conjunctions of disjunctions. The `OR` operator takes precedence over `AND` so the use of parenthesis is not necessary when building CNF. The `OR` operator is only supported to build disjunctions that apply to the same field, e.g., `versionCode = 123 OR errorIssueType = ANR` is not a valid filter. ** Examples ** Some valid filtering expressions: * `versionCode = 123 AND errorIssueType = ANR` * `versionCode = 123 AND errorIssueType = OR errorIssueType = CRASH` * `versionCode = 123 AND (errorIssueType = OR errorIssueType = CRASH)`
    Integer intervalEndTimeDay = 56; // Integer | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.
    Integer intervalEndTimeHours = 56; // Integer | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
    Integer intervalEndTimeMinutes = 56; // Integer | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.
    Integer intervalEndTimeMonth = 56; // Integer | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.
    Integer intervalEndTimeNanos = 56; // Integer | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.
    Integer intervalEndTimeSeconds = 56; // Integer | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.
    String intervalEndTimeTimeZoneId = "intervalEndTimeTimeZoneId_example"; // String | IANA Time Zone Database time zone, e.g. \"America/New_York\".
    String intervalEndTimeTimeZoneVersion = "intervalEndTimeTimeZoneVersion_example"; // String | Optional. IANA Time Zone Database version number, e.g. \"2019a\".
    String intervalEndTimeUtcOffset = "intervalEndTimeUtcOffset_example"; // String | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.
    Integer intervalEndTimeYear = 56; // Integer | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.
    Integer intervalStartTimeDay = 56; // Integer | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.
    Integer intervalStartTimeHours = 56; // Integer | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
    Integer intervalStartTimeMinutes = 56; // Integer | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.
    Integer intervalStartTimeMonth = 56; // Integer | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.
    Integer intervalStartTimeNanos = 56; // Integer | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.
    Integer intervalStartTimeSeconds = 56; // Integer | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.
    String intervalStartTimeTimeZoneId = "intervalStartTimeTimeZoneId_example"; // String | IANA Time Zone Database time zone, e.g. \"America/New_York\".
    String intervalStartTimeTimeZoneVersion = "intervalStartTimeTimeZoneVersion_example"; // String | Optional. IANA Time Zone Database version number, e.g. \"2019a\".
    String intervalStartTimeUtcOffset = "intervalStartTimeUtcOffset_example"; // String | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.
    Integer intervalStartTimeYear = 56; // Integer | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.
    String orderBy = "orderBy_example"; // String | Specifies a field that will be used to order the results. ** Supported dimensions:** * `errorReportCount`: Orders issues by number of error reports. * `distinctUsers`: Orders issues by number of unique affected users. ** Supported operations:** * `asc` for ascending order. * `desc` for descending order. Format: A field and an operation, e.g., `errorReportCount desc` *Note:* currently only one field is supported at a time.
    Integer pageSize = 56; // Integer | The maximum number of error issues to return. The service may return fewer than this value. If unspecified, at most 50 error issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to the request must match the call that provided the page token.
    try {
      GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse result = apiInstance.playdeveloperreportingVitalsErrorsIssuesSearch(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, intervalEndTimeDay, intervalEndTimeHours, intervalEndTimeMinutes, intervalEndTimeMonth, intervalEndTimeNanos, intervalEndTimeSeconds, intervalEndTimeTimeZoneId, intervalEndTimeTimeZoneVersion, intervalEndTimeUtcOffset, intervalEndTimeYear, intervalStartTimeDay, intervalStartTimeHours, intervalStartTimeMinutes, intervalStartTimeMonth, intervalStartTimeNanos, intervalStartTimeSeconds, intervalStartTimeTimeZoneId, intervalStartTimeTimeZoneVersion, intervalStartTimeUtcOffset, intervalStartTimeYear, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VitalsApi#playdeveloperreportingVitalsErrorsIssuesSearch");
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
| **parent** | **String**| Required. Parent resource of the error issues, indicating the application for which they were received. Format: apps/{app} | |
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
| **filter** | **String**| A selection predicate to retrieve only a subset of the issues. Counts in the returned error issues will only reflect occurrences that matched the filter. For filtering basics, please check [AIP-160](https://google.aip.dev/160). ** Supported field names:** * &#x60;apiLevel&#x60;: Matches error issues that occurred in the requested Android versions (specified as the numeric API level) only. Example: &#x60;apiLevel &#x3D; 28 OR apiLevel &#x3D; 29&#x60;. * &#x60;versionCode&#x60;: Matches error issues that occurred in the requested app version codes only. Example: &#x60;versionCode &#x3D; 123 OR versionCode &#x3D; 456&#x60;. * &#x60;deviceModel&#x60;: Matches error issues that occurred in the requested devices. Example: &#x60;deviceModel &#x3D; \&quot;google/walleye\&quot; OR deviceModel &#x3D; \&quot;google/marlin\&quot;&#x60;. * &#x60;deviceBrand&#x60;: Matches error issues that occurred in the requested device brands. Example: &#x60;deviceBrand &#x3D; \&quot;Google\&quot;. * &#x60;deviceType&#x60;: Matches error issues that occurred in the requested device types. Example: &#x60;deviceType &#x3D; \&quot;PHONE\&quot;&#x60;. * &#x60;errorIssueType&#x60;: Matches error issues of the requested types only. Valid candidates: &#x60;CRASH&#x60;, &#x60;ANR&#x60;. Example: &#x60;errorIssueType &#x3D; CRASH OR errorIssueType &#x3D; ANR&#x60;. * &#x60;appProcessState&#x60;: Matches error issues on the process state of an app, indicating whether an app runs in the foreground (user-visible) or background. Valid candidates: &#x60;FOREGROUND&#x60;, &#x60;BACKGROUND&#x60;. Example: &#x60;appProcessState &#x3D; FOREGROUND&#x60;. * &#x60;isUserPerceived&#x60;: Matches error issues that are user-perceived. It is not accompanied by any operators. Example: &#x60;isUserPerceived&#x60;. ** Supported operators:** * Comparison operators: The only supported comparison operator is equality. The filtered field must appear on the left hand side of the comparison. * Logical Operators: Logical operators &#x60;AND&#x60; and &#x60;OR&#x60; can be used to build complex filters following a conjunctive normal form (CNF), i.e., conjunctions of disjunctions. The &#x60;OR&#x60; operator takes precedence over &#x60;AND&#x60; so the use of parenthesis is not necessary when building CNF. The &#x60;OR&#x60; operator is only supported to build disjunctions that apply to the same field, e.g., &#x60;versionCode &#x3D; 123 OR errorIssueType &#x3D; ANR&#x60; is not a valid filter. ** Examples ** Some valid filtering expressions: * &#x60;versionCode &#x3D; 123 AND errorIssueType &#x3D; ANR&#x60; * &#x60;versionCode &#x3D; 123 AND errorIssueType &#x3D; OR errorIssueType &#x3D; CRASH&#x60; * &#x60;versionCode &#x3D; 123 AND (errorIssueType &#x3D; OR errorIssueType &#x3D; CRASH)&#x60; | [optional] |
| **intervalEndTimeDay** | **Integer**| Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] |
| **intervalEndTimeHours** | **Integer**| Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] |
| **intervalEndTimeMinutes** | **Integer**| Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] |
| **intervalEndTimeMonth** | **Integer**| Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] |
| **intervalEndTimeNanos** | **Integer**| Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] |
| **intervalEndTimeSeconds** | **Integer**| Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] |
| **intervalEndTimeTimeZoneId** | **String**| IANA Time Zone Database time zone, e.g. \&quot;America/New_York\&quot;. | [optional] |
| **intervalEndTimeTimeZoneVersion** | **String**| Optional. IANA Time Zone Database version number, e.g. \&quot;2019a\&quot;. | [optional] |
| **intervalEndTimeUtcOffset** | **String**| UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] |
| **intervalEndTimeYear** | **Integer**| Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] |
| **intervalStartTimeDay** | **Integer**| Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] |
| **intervalStartTimeHours** | **Integer**| Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] |
| **intervalStartTimeMinutes** | **Integer**| Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] |
| **intervalStartTimeMonth** | **Integer**| Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] |
| **intervalStartTimeNanos** | **Integer**| Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] |
| **intervalStartTimeSeconds** | **Integer**| Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] |
| **intervalStartTimeTimeZoneId** | **String**| IANA Time Zone Database time zone, e.g. \&quot;America/New_York\&quot;. | [optional] |
| **intervalStartTimeTimeZoneVersion** | **String**| Optional. IANA Time Zone Database version number, e.g. \&quot;2019a\&quot;. | [optional] |
| **intervalStartTimeUtcOffset** | **String**| UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] |
| **intervalStartTimeYear** | **Integer**| Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] |
| **orderBy** | **String**| Specifies a field that will be used to order the results. ** Supported dimensions:** * &#x60;errorReportCount&#x60;: Orders issues by number of error reports. * &#x60;distinctUsers&#x60;: Orders issues by number of unique affected users. ** Supported operations:** * &#x60;asc&#x60; for ascending order. * &#x60;desc&#x60; for descending order. Format: A field and an operation, e.g., &#x60;errorReportCount desc&#x60; *Note:* currently only one field is supported at a time. | [optional] |
| **pageSize** | **Integer**| The maximum number of error issues to return. The service may return fewer than this value. If unspecified, at most 50 error issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] |
| **pageToken** | **String**| A page token, received from a previous call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to the request must match the call that provided the page token. | [optional] |

### Return type

[**GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse**](GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="playdeveloperreportingVitalsErrorsReportsSearch"></a>
# **playdeveloperreportingVitalsErrorsReportsSearch**
> GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse playdeveloperreportingVitalsErrorsReportsSearch(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, intervalEndTimeDay, intervalEndTimeHours, intervalEndTimeMinutes, intervalEndTimeMonth, intervalEndTimeNanos, intervalEndTimeSeconds, intervalEndTimeTimeZoneId, intervalEndTimeTimeZoneVersion, intervalEndTimeUtcOffset, intervalEndTimeYear, intervalStartTimeDay, intervalStartTimeHours, intervalStartTimeMinutes, intervalStartTimeMonth, intervalStartTimeNanos, intervalStartTimeSeconds, intervalStartTimeTimeZoneId, intervalStartTimeTimeZoneVersion, intervalStartTimeUtcOffset, intervalStartTimeYear, pageSize, pageToken)



Searches all error reports received for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VitalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://playdeveloperreporting.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VitalsApi apiInstance = new VitalsApi(defaultClient);
    String parent = "parent_example"; // String | Required. Parent resource of the reports, indicating the application for which they were received. Format: apps/{app}
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
    String filter = "filter_example"; // String | A selection predicate to retrieve only a subset of the reports. For filtering basics, please check [AIP-160](https://google.aip.dev/160). ** Supported field names:** * `apiLevel`: Matches error reports that occurred in the requested Android versions (specified as the numeric API level) only. Example: `apiLevel = 28 OR apiLevel = 29`. * `versionCode`: Matches error reports that occurred in the requested app version codes only. Example: `versionCode = 123 OR versionCode = 456`. * `deviceModel`: Matches error issues that occurred in the requested devices. Example: `deviceModel = \"google/walleye\" OR deviceModel = \"google/marlin\"`. * `deviceBrand`: Matches error issues that occurred in the requested device brands. Example: `deviceBrand = \"Google\". * `deviceType`: Matches error reports that occurred in the requested device types. Example: `deviceType = \"PHONE\"`. * `errorIssueType`: Matches error reports of the requested types only. Valid candidates: `JAVA_CRASH`, `NATIVE_CRASH`, `ANR`. Example: `errorIssueType = JAVA_CRASH OR errorIssueType = NATIVE_CRASH`. * `errorIssueId`: Matches error reports belonging to the requested error issue ids only. Example: `errorIssueId = 1234 OR errorIssueId = 4567`. * `appProcessState`: Matches error reports on the process state of an app, indicating whether an app runs in the foreground (user-visible) or background. Valid candidates: `FOREGROUND`, `BACKGROUND`. Example: `appProcessState = FOREGROUND`. * `isUserPerceived`: Matches error reports that are user-perceived. It is not accompanied by any operators. Example: `isUserPerceived`. ** Supported operators:** * Comparison operators: The only supported comparison operator is equality. The filtered field must appear on the left hand side of the comparison. * Logical Operators: Logical operators `AND` and `OR` can be used to build complex filters following a conjunctive normal form (CNF), i.e., conjunctions of disjunctions. The `OR` operator takes precedence over `AND` so the use of parenthesis is not necessary when building CNF. The `OR` operator is only supported to build disjunctions that apply to the same field, e.g., `versionCode = 123 OR versionCode = ANR`. The filter expression `versionCode = 123 OR errorIssueType = ANR` is not valid. ** Examples ** Some valid filtering expressions: * `versionCode = 123 AND errorIssueType = ANR` * `versionCode = 123 AND errorIssueType = OR errorIssueType = CRASH` * `versionCode = 123 AND (errorIssueType = OR errorIssueType = CRASH)`
    Integer intervalEndTimeDay = 56; // Integer | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.
    Integer intervalEndTimeHours = 56; // Integer | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
    Integer intervalEndTimeMinutes = 56; // Integer | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.
    Integer intervalEndTimeMonth = 56; // Integer | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.
    Integer intervalEndTimeNanos = 56; // Integer | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.
    Integer intervalEndTimeSeconds = 56; // Integer | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.
    String intervalEndTimeTimeZoneId = "intervalEndTimeTimeZoneId_example"; // String | IANA Time Zone Database time zone, e.g. \"America/New_York\".
    String intervalEndTimeTimeZoneVersion = "intervalEndTimeTimeZoneVersion_example"; // String | Optional. IANA Time Zone Database version number, e.g. \"2019a\".
    String intervalEndTimeUtcOffset = "intervalEndTimeUtcOffset_example"; // String | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.
    Integer intervalEndTimeYear = 56; // Integer | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.
    Integer intervalStartTimeDay = 56; // Integer | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.
    Integer intervalStartTimeHours = 56; // Integer | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
    Integer intervalStartTimeMinutes = 56; // Integer | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.
    Integer intervalStartTimeMonth = 56; // Integer | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.
    Integer intervalStartTimeNanos = 56; // Integer | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.
    Integer intervalStartTimeSeconds = 56; // Integer | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.
    String intervalStartTimeTimeZoneId = "intervalStartTimeTimeZoneId_example"; // String | IANA Time Zone Database time zone, e.g. \"America/New_York\".
    String intervalStartTimeTimeZoneVersion = "intervalStartTimeTimeZoneVersion_example"; // String | Optional. IANA Time Zone Database version number, e.g. \"2019a\".
    String intervalStartTimeUtcOffset = "intervalStartTimeUtcOffset_example"; // String | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.
    Integer intervalStartTimeYear = 56; // Integer | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.
    Integer pageSize = 56; // Integer | The maximum number of reports to return. The service may return fewer than this value. If unspecified, at most 50 reports will be returned. The maximum value is 100; values above 100 will be coerced to 100.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous `SearchErrorReports` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `SearchErrorReports` must match the call that provided the page token.
    try {
      GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse result = apiInstance.playdeveloperreportingVitalsErrorsReportsSearch(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, intervalEndTimeDay, intervalEndTimeHours, intervalEndTimeMinutes, intervalEndTimeMonth, intervalEndTimeNanos, intervalEndTimeSeconds, intervalEndTimeTimeZoneId, intervalEndTimeTimeZoneVersion, intervalEndTimeUtcOffset, intervalEndTimeYear, intervalStartTimeDay, intervalStartTimeHours, intervalStartTimeMinutes, intervalStartTimeMonth, intervalStartTimeNanos, intervalStartTimeSeconds, intervalStartTimeTimeZoneId, intervalStartTimeTimeZoneVersion, intervalStartTimeUtcOffset, intervalStartTimeYear, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VitalsApi#playdeveloperreportingVitalsErrorsReportsSearch");
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
| **parent** | **String**| Required. Parent resource of the reports, indicating the application for which they were received. Format: apps/{app} | |
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
| **filter** | **String**| A selection predicate to retrieve only a subset of the reports. For filtering basics, please check [AIP-160](https://google.aip.dev/160). ** Supported field names:** * &#x60;apiLevel&#x60;: Matches error reports that occurred in the requested Android versions (specified as the numeric API level) only. Example: &#x60;apiLevel &#x3D; 28 OR apiLevel &#x3D; 29&#x60;. * &#x60;versionCode&#x60;: Matches error reports that occurred in the requested app version codes only. Example: &#x60;versionCode &#x3D; 123 OR versionCode &#x3D; 456&#x60;. * &#x60;deviceModel&#x60;: Matches error issues that occurred in the requested devices. Example: &#x60;deviceModel &#x3D; \&quot;google/walleye\&quot; OR deviceModel &#x3D; \&quot;google/marlin\&quot;&#x60;. * &#x60;deviceBrand&#x60;: Matches error issues that occurred in the requested device brands. Example: &#x60;deviceBrand &#x3D; \&quot;Google\&quot;. * &#x60;deviceType&#x60;: Matches error reports that occurred in the requested device types. Example: &#x60;deviceType &#x3D; \&quot;PHONE\&quot;&#x60;. * &#x60;errorIssueType&#x60;: Matches error reports of the requested types only. Valid candidates: &#x60;JAVA_CRASH&#x60;, &#x60;NATIVE_CRASH&#x60;, &#x60;ANR&#x60;. Example: &#x60;errorIssueType &#x3D; JAVA_CRASH OR errorIssueType &#x3D; NATIVE_CRASH&#x60;. * &#x60;errorIssueId&#x60;: Matches error reports belonging to the requested error issue ids only. Example: &#x60;errorIssueId &#x3D; 1234 OR errorIssueId &#x3D; 4567&#x60;. * &#x60;appProcessState&#x60;: Matches error reports on the process state of an app, indicating whether an app runs in the foreground (user-visible) or background. Valid candidates: &#x60;FOREGROUND&#x60;, &#x60;BACKGROUND&#x60;. Example: &#x60;appProcessState &#x3D; FOREGROUND&#x60;. * &#x60;isUserPerceived&#x60;: Matches error reports that are user-perceived. It is not accompanied by any operators. Example: &#x60;isUserPerceived&#x60;. ** Supported operators:** * Comparison operators: The only supported comparison operator is equality. The filtered field must appear on the left hand side of the comparison. * Logical Operators: Logical operators &#x60;AND&#x60; and &#x60;OR&#x60; can be used to build complex filters following a conjunctive normal form (CNF), i.e., conjunctions of disjunctions. The &#x60;OR&#x60; operator takes precedence over &#x60;AND&#x60; so the use of parenthesis is not necessary when building CNF. The &#x60;OR&#x60; operator is only supported to build disjunctions that apply to the same field, e.g., &#x60;versionCode &#x3D; 123 OR versionCode &#x3D; ANR&#x60;. The filter expression &#x60;versionCode &#x3D; 123 OR errorIssueType &#x3D; ANR&#x60; is not valid. ** Examples ** Some valid filtering expressions: * &#x60;versionCode &#x3D; 123 AND errorIssueType &#x3D; ANR&#x60; * &#x60;versionCode &#x3D; 123 AND errorIssueType &#x3D; OR errorIssueType &#x3D; CRASH&#x60; * &#x60;versionCode &#x3D; 123 AND (errorIssueType &#x3D; OR errorIssueType &#x3D; CRASH)&#x60; | [optional] |
| **intervalEndTimeDay** | **Integer**| Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] |
| **intervalEndTimeHours** | **Integer**| Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] |
| **intervalEndTimeMinutes** | **Integer**| Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] |
| **intervalEndTimeMonth** | **Integer**| Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] |
| **intervalEndTimeNanos** | **Integer**| Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] |
| **intervalEndTimeSeconds** | **Integer**| Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] |
| **intervalEndTimeTimeZoneId** | **String**| IANA Time Zone Database time zone, e.g. \&quot;America/New_York\&quot;. | [optional] |
| **intervalEndTimeTimeZoneVersion** | **String**| Optional. IANA Time Zone Database version number, e.g. \&quot;2019a\&quot;. | [optional] |
| **intervalEndTimeUtcOffset** | **String**| UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] |
| **intervalEndTimeYear** | **Integer**| Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] |
| **intervalStartTimeDay** | **Integer**| Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] |
| **intervalStartTimeHours** | **Integer**| Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] |
| **intervalStartTimeMinutes** | **Integer**| Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] |
| **intervalStartTimeMonth** | **Integer**| Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] |
| **intervalStartTimeNanos** | **Integer**| Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] |
| **intervalStartTimeSeconds** | **Integer**| Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] |
| **intervalStartTimeTimeZoneId** | **String**| IANA Time Zone Database time zone, e.g. \&quot;America/New_York\&quot;. | [optional] |
| **intervalStartTimeTimeZoneVersion** | **String**| Optional. IANA Time Zone Database version number, e.g. \&quot;2019a\&quot;. | [optional] |
| **intervalStartTimeUtcOffset** | **String**| UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] |
| **intervalStartTimeYear** | **Integer**| Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] |
| **pageSize** | **Integer**| The maximum number of reports to return. The service may return fewer than this value. If unspecified, at most 50 reports will be returned. The maximum value is 100; values above 100 will be coerced to 100. | [optional] |
| **pageToken** | **String**| A page token, received from a previous &#x60;SearchErrorReports&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;SearchErrorReports&#x60; must match the call that provided the page token. | [optional] |

### Return type

[**GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse**](GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="playdeveloperreportingVitalsStuckbackgroundwakelockrateGet"></a>
# **playdeveloperreportingVitalsStuckbackgroundwakelockrateGet**
> GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet playdeveloperreportingVitalsStuckbackgroundwakelockrateGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Describes the properties of the metric set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VitalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://playdeveloperreporting.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VitalsApi apiInstance = new VitalsApi(defaultClient);
    String name = "name_example"; // String | Required. The resource name. Format: apps/{app}/stuckBackgroundWakelockRateMetricSet
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
    try {
      GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet result = apiInstance.playdeveloperreportingVitalsStuckbackgroundwakelockrateGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VitalsApi#playdeveloperreportingVitalsStuckbackgroundwakelockrateGet");
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
| **name** | **String**| Required. The resource name. Format: apps/{app}/stuckBackgroundWakelockRateMetricSet | |
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

### Return type

[**GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet**](GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery"></a>
# **playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery**
> GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googlePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest)



Queries the metrics in the metric set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VitalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://playdeveloperreporting.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VitalsApi apiInstance = new VitalsApi(defaultClient);
    String name = "name_example"; // String | Required. The resource name. Format: apps/{app}/stuckBackgroundWakelockRateMetricSet
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
    GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest googlePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest = new GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest(); // GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest | 
    try {
      GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse result = apiInstance.playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googlePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VitalsApi#playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery");
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
| **name** | **String**| Required. The resource name. Format: apps/{app}/stuckBackgroundWakelockRateMetricSet | |
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
| **googlePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest** | [**GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest**](GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest.md)|  | [optional] |

### Return type

[**GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse**](GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

