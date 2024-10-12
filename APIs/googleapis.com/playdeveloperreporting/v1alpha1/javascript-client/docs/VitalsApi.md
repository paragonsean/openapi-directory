# GooglePlayDeveloperReportingApi.VitalsApi

All URIs are relative to *https://playdeveloperreporting.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playdeveloperreportingVitalsErrorsIssuesSearch**](VitalsApi.md#playdeveloperreportingVitalsErrorsIssuesSearch) | **GET** /v1alpha1/{parent}/errorIssues:search | 
[**playdeveloperreportingVitalsErrorsReportsSearch**](VitalsApi.md#playdeveloperreportingVitalsErrorsReportsSearch) | **GET** /v1alpha1/{parent}/errorReports:search | 
[**playdeveloperreportingVitalsStuckbackgroundwakelockrateGet**](VitalsApi.md#playdeveloperreportingVitalsStuckbackgroundwakelockrateGet) | **GET** /v1alpha1/{name} | 
[**playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery**](VitalsApi.md#playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery) | **POST** /v1alpha1/{name}:query | 



## playdeveloperreportingVitalsErrorsIssuesSearch

> GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse playdeveloperreportingVitalsErrorsIssuesSearch(parent, opts)



Searches all error issues in which reports have been grouped.

### Example

```javascript
import GooglePlayDeveloperReportingApi from 'google_play_developer_reporting_api';
let defaultClient = GooglePlayDeveloperReportingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloperReportingApi.VitalsApi();
let parent = "parent_example"; // String | Required. Parent resource of the error issues, indicating the application for which they were received. Format: apps/{app}
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
  'filter': "filter_example", // String | A selection predicate to retrieve only a subset of the issues. Counts in the returned error issues will only reflect occurrences that matched the filter. For filtering basics, please check [AIP-160](https://google.aip.dev/160). ** Supported field names:** * `apiLevel`: Matches error issues that occurred in the requested Android versions (specified as the numeric API level) only. Example: `apiLevel = 28 OR apiLevel = 29`. * `versionCode`: Matches error issues that occurred in the requested app version codes only. Example: `versionCode = 123 OR versionCode = 456`. * `deviceModel`: Matches error issues that occurred in the requested devices. Example: `deviceModel = \"google/walleye\" OR deviceModel = \"google/marlin\"`. * `deviceBrand`: Matches error issues that occurred in the requested device brands. Example: `deviceBrand = \"Google\". * `deviceType`: Matches error issues that occurred in the requested device types. Example: `deviceType = \"PHONE\"`. * `errorIssueType`: Matches error issues of the requested types only. Valid candidates: `CRASH`, `ANR`. Example: `errorIssueType = CRASH OR errorIssueType = ANR`. * `appProcessState`: Matches error issues on the process state of an app, indicating whether an app runs in the foreground (user-visible) or background. Valid candidates: `FOREGROUND`, `BACKGROUND`. Example: `appProcessState = FOREGROUND`. * `isUserPerceived`: Matches error issues that are user-perceived. It is not accompanied by any operators. Example: `isUserPerceived`. ** Supported operators:** * Comparison operators: The only supported comparison operator is equality. The filtered field must appear on the left hand side of the comparison. * Logical Operators: Logical operators `AND` and `OR` can be used to build complex filters following a conjunctive normal form (CNF), i.e., conjunctions of disjunctions. The `OR` operator takes precedence over `AND` so the use of parenthesis is not necessary when building CNF. The `OR` operator is only supported to build disjunctions that apply to the same field, e.g., `versionCode = 123 OR errorIssueType = ANR` is not a valid filter. ** Examples ** Some valid filtering expressions: * `versionCode = 123 AND errorIssueType = ANR` * `versionCode = 123 AND errorIssueType = OR errorIssueType = CRASH` * `versionCode = 123 AND (errorIssueType = OR errorIssueType = CRASH)`
  'intervalEndTimeDay': 56, // Number | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.
  'intervalEndTimeHours': 56, // Number | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
  'intervalEndTimeMinutes': 56, // Number | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.
  'intervalEndTimeMonth': 56, // Number | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.
  'intervalEndTimeNanos': 56, // Number | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.
  'intervalEndTimeSeconds': 56, // Number | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.
  'intervalEndTimeTimeZoneId': "intervalEndTimeTimeZoneId_example", // String | IANA Time Zone Database time zone, e.g. \"America/New_York\".
  'intervalEndTimeTimeZoneVersion': "intervalEndTimeTimeZoneVersion_example", // String | Optional. IANA Time Zone Database version number, e.g. \"2019a\".
  'intervalEndTimeUtcOffset': "intervalEndTimeUtcOffset_example", // String | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.
  'intervalEndTimeYear': 56, // Number | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.
  'intervalStartTimeDay': 56, // Number | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.
  'intervalStartTimeHours': 56, // Number | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
  'intervalStartTimeMinutes': 56, // Number | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.
  'intervalStartTimeMonth': 56, // Number | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.
  'intervalStartTimeNanos': 56, // Number | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.
  'intervalStartTimeSeconds': 56, // Number | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.
  'intervalStartTimeTimeZoneId': "intervalStartTimeTimeZoneId_example", // String | IANA Time Zone Database time zone, e.g. \"America/New_York\".
  'intervalStartTimeTimeZoneVersion': "intervalStartTimeTimeZoneVersion_example", // String | Optional. IANA Time Zone Database version number, e.g. \"2019a\".
  'intervalStartTimeUtcOffset': "intervalStartTimeUtcOffset_example", // String | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.
  'intervalStartTimeYear': 56, // Number | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.
  'orderBy': "orderBy_example", // String | Specifies a field that will be used to order the results. ** Supported dimensions:** * `errorReportCount`: Orders issues by number of error reports. * `distinctUsers`: Orders issues by number of unique affected users. ** Supported operations:** * `asc` for ascending order. * `desc` for descending order. Format: A field and an operation, e.g., `errorReportCount desc` *Note:* currently only one field is supported at a time.
  'pageSize': 56, // Number | The maximum number of error issues to return. The service may return fewer than this value. If unspecified, at most 50 error issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.
  'pageToken': "pageToken_example" // String | A page token, received from a previous call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to the request must match the call that provided the page token.
};
apiInstance.playdeveloperreportingVitalsErrorsIssuesSearch(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource of the error issues, indicating the application for which they were received. Format: apps/{app} | 
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
 **filter** | **String**| A selection predicate to retrieve only a subset of the issues. Counts in the returned error issues will only reflect occurrences that matched the filter. For filtering basics, please check [AIP-160](https://google.aip.dev/160). ** Supported field names:** * &#x60;apiLevel&#x60;: Matches error issues that occurred in the requested Android versions (specified as the numeric API level) only. Example: &#x60;apiLevel &#x3D; 28 OR apiLevel &#x3D; 29&#x60;. * &#x60;versionCode&#x60;: Matches error issues that occurred in the requested app version codes only. Example: &#x60;versionCode &#x3D; 123 OR versionCode &#x3D; 456&#x60;. * &#x60;deviceModel&#x60;: Matches error issues that occurred in the requested devices. Example: &#x60;deviceModel &#x3D; \&quot;google/walleye\&quot; OR deviceModel &#x3D; \&quot;google/marlin\&quot;&#x60;. * &#x60;deviceBrand&#x60;: Matches error issues that occurred in the requested device brands. Example: &#x60;deviceBrand &#x3D; \&quot;Google\&quot;. * &#x60;deviceType&#x60;: Matches error issues that occurred in the requested device types. Example: &#x60;deviceType &#x3D; \&quot;PHONE\&quot;&#x60;. * &#x60;errorIssueType&#x60;: Matches error issues of the requested types only. Valid candidates: &#x60;CRASH&#x60;, &#x60;ANR&#x60;. Example: &#x60;errorIssueType &#x3D; CRASH OR errorIssueType &#x3D; ANR&#x60;. * &#x60;appProcessState&#x60;: Matches error issues on the process state of an app, indicating whether an app runs in the foreground (user-visible) or background. Valid candidates: &#x60;FOREGROUND&#x60;, &#x60;BACKGROUND&#x60;. Example: &#x60;appProcessState &#x3D; FOREGROUND&#x60;. * &#x60;isUserPerceived&#x60;: Matches error issues that are user-perceived. It is not accompanied by any operators. Example: &#x60;isUserPerceived&#x60;. ** Supported operators:** * Comparison operators: The only supported comparison operator is equality. The filtered field must appear on the left hand side of the comparison. * Logical Operators: Logical operators &#x60;AND&#x60; and &#x60;OR&#x60; can be used to build complex filters following a conjunctive normal form (CNF), i.e., conjunctions of disjunctions. The &#x60;OR&#x60; operator takes precedence over &#x60;AND&#x60; so the use of parenthesis is not necessary when building CNF. The &#x60;OR&#x60; operator is only supported to build disjunctions that apply to the same field, e.g., &#x60;versionCode &#x3D; 123 OR errorIssueType &#x3D; ANR&#x60; is not a valid filter. ** Examples ** Some valid filtering expressions: * &#x60;versionCode &#x3D; 123 AND errorIssueType &#x3D; ANR&#x60; * &#x60;versionCode &#x3D; 123 AND errorIssueType &#x3D; OR errorIssueType &#x3D; CRASH&#x60; * &#x60;versionCode &#x3D; 123 AND (errorIssueType &#x3D; OR errorIssueType &#x3D; CRASH)&#x60; | [optional] 
 **intervalEndTimeDay** | **Number**| Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] 
 **intervalEndTimeHours** | **Number**| Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] 
 **intervalEndTimeMinutes** | **Number**| Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] 
 **intervalEndTimeMonth** | **Number**| Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] 
 **intervalEndTimeNanos** | **Number**| Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] 
 **intervalEndTimeSeconds** | **Number**| Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] 
 **intervalEndTimeTimeZoneId** | **String**| IANA Time Zone Database time zone, e.g. \&quot;America/New_York\&quot;. | [optional] 
 **intervalEndTimeTimeZoneVersion** | **String**| Optional. IANA Time Zone Database version number, e.g. \&quot;2019a\&quot;. | [optional] 
 **intervalEndTimeUtcOffset** | **String**| UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] 
 **intervalEndTimeYear** | **Number**| Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] 
 **intervalStartTimeDay** | **Number**| Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] 
 **intervalStartTimeHours** | **Number**| Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] 
 **intervalStartTimeMinutes** | **Number**| Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] 
 **intervalStartTimeMonth** | **Number**| Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] 
 **intervalStartTimeNanos** | **Number**| Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] 
 **intervalStartTimeSeconds** | **Number**| Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] 
 **intervalStartTimeTimeZoneId** | **String**| IANA Time Zone Database time zone, e.g. \&quot;America/New_York\&quot;. | [optional] 
 **intervalStartTimeTimeZoneVersion** | **String**| Optional. IANA Time Zone Database version number, e.g. \&quot;2019a\&quot;. | [optional] 
 **intervalStartTimeUtcOffset** | **String**| UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] 
 **intervalStartTimeYear** | **Number**| Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] 
 **orderBy** | **String**| Specifies a field that will be used to order the results. ** Supported dimensions:** * &#x60;errorReportCount&#x60;: Orders issues by number of error reports. * &#x60;distinctUsers&#x60;: Orders issues by number of unique affected users. ** Supported operations:** * &#x60;asc&#x60; for ascending order. * &#x60;desc&#x60; for descending order. Format: A field and an operation, e.g., &#x60;errorReportCount desc&#x60; *Note:* currently only one field is supported at a time. | [optional] 
 **pageSize** | **Number**| The maximum number of error issues to return. The service may return fewer than this value. If unspecified, at most 50 error issues will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. | [optional] 
 **pageToken** | **String**| A page token, received from a previous call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to the request must match the call that provided the page token. | [optional] 

### Return type

[**GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse**](GooglePlayDeveloperReportingV1alpha1SearchErrorIssuesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playdeveloperreportingVitalsErrorsReportsSearch

> GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse playdeveloperreportingVitalsErrorsReportsSearch(parent, opts)



Searches all error reports received for an app.

### Example

```javascript
import GooglePlayDeveloperReportingApi from 'google_play_developer_reporting_api';
let defaultClient = GooglePlayDeveloperReportingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloperReportingApi.VitalsApi();
let parent = "parent_example"; // String | Required. Parent resource of the reports, indicating the application for which they were received. Format: apps/{app}
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
  'filter': "filter_example", // String | A selection predicate to retrieve only a subset of the reports. For filtering basics, please check [AIP-160](https://google.aip.dev/160). ** Supported field names:** * `apiLevel`: Matches error reports that occurred in the requested Android versions (specified as the numeric API level) only. Example: `apiLevel = 28 OR apiLevel = 29`. * `versionCode`: Matches error reports that occurred in the requested app version codes only. Example: `versionCode = 123 OR versionCode = 456`. * `deviceModel`: Matches error issues that occurred in the requested devices. Example: `deviceModel = \"google/walleye\" OR deviceModel = \"google/marlin\"`. * `deviceBrand`: Matches error issues that occurred in the requested device brands. Example: `deviceBrand = \"Google\". * `deviceType`: Matches error reports that occurred in the requested device types. Example: `deviceType = \"PHONE\"`. * `errorIssueType`: Matches error reports of the requested types only. Valid candidates: `JAVA_CRASH`, `NATIVE_CRASH`, `ANR`. Example: `errorIssueType = JAVA_CRASH OR errorIssueType = NATIVE_CRASH`. * `errorIssueId`: Matches error reports belonging to the requested error issue ids only. Example: `errorIssueId = 1234 OR errorIssueId = 4567`. * `appProcessState`: Matches error reports on the process state of an app, indicating whether an app runs in the foreground (user-visible) or background. Valid candidates: `FOREGROUND`, `BACKGROUND`. Example: `appProcessState = FOREGROUND`. * `isUserPerceived`: Matches error reports that are user-perceived. It is not accompanied by any operators. Example: `isUserPerceived`. ** Supported operators:** * Comparison operators: The only supported comparison operator is equality. The filtered field must appear on the left hand side of the comparison. * Logical Operators: Logical operators `AND` and `OR` can be used to build complex filters following a conjunctive normal form (CNF), i.e., conjunctions of disjunctions. The `OR` operator takes precedence over `AND` so the use of parenthesis is not necessary when building CNF. The `OR` operator is only supported to build disjunctions that apply to the same field, e.g., `versionCode = 123 OR versionCode = ANR`. The filter expression `versionCode = 123 OR errorIssueType = ANR` is not valid. ** Examples ** Some valid filtering expressions: * `versionCode = 123 AND errorIssueType = ANR` * `versionCode = 123 AND errorIssueType = OR errorIssueType = CRASH` * `versionCode = 123 AND (errorIssueType = OR errorIssueType = CRASH)`
  'intervalEndTimeDay': 56, // Number | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.
  'intervalEndTimeHours': 56, // Number | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
  'intervalEndTimeMinutes': 56, // Number | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.
  'intervalEndTimeMonth': 56, // Number | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.
  'intervalEndTimeNanos': 56, // Number | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.
  'intervalEndTimeSeconds': 56, // Number | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.
  'intervalEndTimeTimeZoneId': "intervalEndTimeTimeZoneId_example", // String | IANA Time Zone Database time zone, e.g. \"America/New_York\".
  'intervalEndTimeTimeZoneVersion': "intervalEndTimeTimeZoneVersion_example", // String | Optional. IANA Time Zone Database version number, e.g. \"2019a\".
  'intervalEndTimeUtcOffset': "intervalEndTimeUtcOffset_example", // String | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.
  'intervalEndTimeYear': 56, // Number | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.
  'intervalStartTimeDay': 56, // Number | Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.
  'intervalStartTimeHours': 56, // Number | Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \"24:00:00\" for scenarios like business closing time.
  'intervalStartTimeMinutes': 56, // Number | Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.
  'intervalStartTimeMonth': 56, // Number | Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.
  'intervalStartTimeNanos': 56, // Number | Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.
  'intervalStartTimeSeconds': 56, // Number | Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.
  'intervalStartTimeTimeZoneId': "intervalStartTimeTimeZoneId_example", // String | IANA Time Zone Database time zone, e.g. \"America/New_York\".
  'intervalStartTimeTimeZoneVersion': "intervalStartTimeTimeZoneVersion_example", // String | Optional. IANA Time Zone Database version number, e.g. \"2019a\".
  'intervalStartTimeUtcOffset': "intervalStartTimeUtcOffset_example", // String | UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.
  'intervalStartTimeYear': 56, // Number | Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.
  'pageSize': 56, // Number | The maximum number of reports to return. The service may return fewer than this value. If unspecified, at most 50 reports will be returned. The maximum value is 100; values above 100 will be coerced to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `SearchErrorReports` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `SearchErrorReports` must match the call that provided the page token.
};
apiInstance.playdeveloperreportingVitalsErrorsReportsSearch(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource of the reports, indicating the application for which they were received. Format: apps/{app} | 
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
 **filter** | **String**| A selection predicate to retrieve only a subset of the reports. For filtering basics, please check [AIP-160](https://google.aip.dev/160). ** Supported field names:** * &#x60;apiLevel&#x60;: Matches error reports that occurred in the requested Android versions (specified as the numeric API level) only. Example: &#x60;apiLevel &#x3D; 28 OR apiLevel &#x3D; 29&#x60;. * &#x60;versionCode&#x60;: Matches error reports that occurred in the requested app version codes only. Example: &#x60;versionCode &#x3D; 123 OR versionCode &#x3D; 456&#x60;. * &#x60;deviceModel&#x60;: Matches error issues that occurred in the requested devices. Example: &#x60;deviceModel &#x3D; \&quot;google/walleye\&quot; OR deviceModel &#x3D; \&quot;google/marlin\&quot;&#x60;. * &#x60;deviceBrand&#x60;: Matches error issues that occurred in the requested device brands. Example: &#x60;deviceBrand &#x3D; \&quot;Google\&quot;. * &#x60;deviceType&#x60;: Matches error reports that occurred in the requested device types. Example: &#x60;deviceType &#x3D; \&quot;PHONE\&quot;&#x60;. * &#x60;errorIssueType&#x60;: Matches error reports of the requested types only. Valid candidates: &#x60;JAVA_CRASH&#x60;, &#x60;NATIVE_CRASH&#x60;, &#x60;ANR&#x60;. Example: &#x60;errorIssueType &#x3D; JAVA_CRASH OR errorIssueType &#x3D; NATIVE_CRASH&#x60;. * &#x60;errorIssueId&#x60;: Matches error reports belonging to the requested error issue ids only. Example: &#x60;errorIssueId &#x3D; 1234 OR errorIssueId &#x3D; 4567&#x60;. * &#x60;appProcessState&#x60;: Matches error reports on the process state of an app, indicating whether an app runs in the foreground (user-visible) or background. Valid candidates: &#x60;FOREGROUND&#x60;, &#x60;BACKGROUND&#x60;. Example: &#x60;appProcessState &#x3D; FOREGROUND&#x60;. * &#x60;isUserPerceived&#x60;: Matches error reports that are user-perceived. It is not accompanied by any operators. Example: &#x60;isUserPerceived&#x60;. ** Supported operators:** * Comparison operators: The only supported comparison operator is equality. The filtered field must appear on the left hand side of the comparison. * Logical Operators: Logical operators &#x60;AND&#x60; and &#x60;OR&#x60; can be used to build complex filters following a conjunctive normal form (CNF), i.e., conjunctions of disjunctions. The &#x60;OR&#x60; operator takes precedence over &#x60;AND&#x60; so the use of parenthesis is not necessary when building CNF. The &#x60;OR&#x60; operator is only supported to build disjunctions that apply to the same field, e.g., &#x60;versionCode &#x3D; 123 OR versionCode &#x3D; ANR&#x60;. The filter expression &#x60;versionCode &#x3D; 123 OR errorIssueType &#x3D; ANR&#x60; is not valid. ** Examples ** Some valid filtering expressions: * &#x60;versionCode &#x3D; 123 AND errorIssueType &#x3D; ANR&#x60; * &#x60;versionCode &#x3D; 123 AND errorIssueType &#x3D; OR errorIssueType &#x3D; CRASH&#x60; * &#x60;versionCode &#x3D; 123 AND (errorIssueType &#x3D; OR errorIssueType &#x3D; CRASH)&#x60; | [optional] 
 **intervalEndTimeDay** | **Number**| Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] 
 **intervalEndTimeHours** | **Number**| Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] 
 **intervalEndTimeMinutes** | **Number**| Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] 
 **intervalEndTimeMonth** | **Number**| Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] 
 **intervalEndTimeNanos** | **Number**| Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] 
 **intervalEndTimeSeconds** | **Number**| Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] 
 **intervalEndTimeTimeZoneId** | **String**| IANA Time Zone Database time zone, e.g. \&quot;America/New_York\&quot;. | [optional] 
 **intervalEndTimeTimeZoneVersion** | **String**| Optional. IANA Time Zone Database version number, e.g. \&quot;2019a\&quot;. | [optional] 
 **intervalEndTimeUtcOffset** | **String**| UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] 
 **intervalEndTimeYear** | **Number**| Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] 
 **intervalStartTimeDay** | **Number**| Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day. | [optional] 
 **intervalStartTimeHours** | **Number**| Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value \&quot;24:00:00\&quot; for scenarios like business closing time. | [optional] 
 **intervalStartTimeMinutes** | **Number**| Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0. | [optional] 
 **intervalStartTimeMonth** | **Number**| Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month. | [optional] 
 **intervalStartTimeNanos** | **Number**| Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0. | [optional] 
 **intervalStartTimeSeconds** | **Number**| Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds. | [optional] 
 **intervalStartTimeTimeZoneId** | **String**| IANA Time Zone Database time zone, e.g. \&quot;America/New_York\&quot;. | [optional] 
 **intervalStartTimeTimeZoneVersion** | **String**| Optional. IANA Time Zone Database version number, e.g. \&quot;2019a\&quot;. | [optional] 
 **intervalStartTimeUtcOffset** | **String**| UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }. | [optional] 
 **intervalStartTimeYear** | **Number**| Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year. | [optional] 
 **pageSize** | **Number**| The maximum number of reports to return. The service may return fewer than this value. If unspecified, at most 50 reports will be returned. The maximum value is 100; values above 100 will be coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;SearchErrorReports&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;SearchErrorReports&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse**](GooglePlayDeveloperReportingV1alpha1SearchErrorReportsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playdeveloperreportingVitalsStuckbackgroundwakelockrateGet

> GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet playdeveloperreportingVitalsStuckbackgroundwakelockrateGet(name, opts)



Describes the properties of the metric set.

### Example

```javascript
import GooglePlayDeveloperReportingApi from 'google_play_developer_reporting_api';
let defaultClient = GooglePlayDeveloperReportingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloperReportingApi.VitalsApi();
let name = "name_example"; // String | Required. The resource name. Format: apps/{app}/stuckBackgroundWakelockRateMetricSet
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
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.playdeveloperreportingVitalsStuckbackgroundwakelockrateGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The resource name. Format: apps/{app}/stuckBackgroundWakelockRateMetricSet | 
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

### Return type

[**GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet**](GooglePlayDeveloperReportingV1alpha1StuckBackgroundWakelockRateMetricSet.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery

> GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery(name, opts)



Queries the metrics in the metric set.

### Example

```javascript
import GooglePlayDeveloperReportingApi from 'google_play_developer_reporting_api';
let defaultClient = GooglePlayDeveloperReportingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GooglePlayDeveloperReportingApi.VitalsApi();
let name = "name_example"; // String | Required. The resource name. Format: apps/{app}/stuckBackgroundWakelockRateMetricSet
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
  'googlePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest': new GooglePlayDeveloperReportingApi.GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest() // GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest | 
};
apiInstance.playdeveloperreportingVitalsStuckbackgroundwakelockrateQuery(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The resource name. Format: apps/{app}/stuckBackgroundWakelockRateMetricSet | 
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
 **googlePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest** | [**GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest**](GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetRequest.md)|  | [optional] 

### Return type

[**GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse**](GooglePlayDeveloperReportingV1alpha1QueryStuckBackgroundWakelockRateMetricSetResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

