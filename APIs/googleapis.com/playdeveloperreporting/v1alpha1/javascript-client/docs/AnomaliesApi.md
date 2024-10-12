# GooglePlayDeveloperReportingApi.AnomaliesApi

All URIs are relative to *https://playdeveloperreporting.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playdeveloperreportingAnomaliesList**](AnomaliesApi.md#playdeveloperreportingAnomaliesList) | **GET** /v1alpha1/{parent}/anomalies | 



## playdeveloperreportingAnomaliesList

> GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponse playdeveloperreportingAnomaliesList(parent, opts)



Lists anomalies in any of the datasets.

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

let apiInstance = new GooglePlayDeveloperReportingApi.AnomaliesApi();
let parent = "parent_example"; // String | Required. Parent app for which anomalies were detected. Format: apps/{app}
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
  'filter': "filter_example", // String | Filtering criteria for anomalies. For basic filter guidance, please check: https://google.aip.dev/160. **Supported functions:** * `activeBetween(startTime, endTime)`: If specified, only list anomalies that were active in between `startTime` (inclusive) and `endTime` (exclusive). Both parameters are expected to conform to an RFC-3339 formatted string (e.g. `2012-04-21T11:30:00-04:00`). UTC offsets are supported. Both `startTime` and `endTime` accept the special value `UNBOUNDED`, to signify intervals with no lower or upper bound, respectively. Examples: * `activeBetween(\"2021-04-21T11:30:00Z\", \"2021-07-21T00:00:00Z\")` * `activeBetween(UNBOUNDED, \"2021-11-21T00:00:00-04:00\")` * `activeBetween(\"2021-07-21T00:00:00-04:00\", UNBOUNDED)`
  'pageSize': 56, // Number | Maximum size of the returned data. If unspecified, at most 10 anomalies will be returned. The maximum value is 100; values above 100 will be coerced to 100.
  'pageToken': "pageToken_example" // String | A page token, received from a previous `ListErrorReports` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListErrorReports` must match the call that provided the page token.
};
apiInstance.playdeveloperreportingAnomaliesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent app for which anomalies were detected. Format: apps/{app} | 
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
 **filter** | **String**| Filtering criteria for anomalies. For basic filter guidance, please check: https://google.aip.dev/160. **Supported functions:** * &#x60;activeBetween(startTime, endTime)&#x60;: If specified, only list anomalies that were active in between &#x60;startTime&#x60; (inclusive) and &#x60;endTime&#x60; (exclusive). Both parameters are expected to conform to an RFC-3339 formatted string (e.g. &#x60;2012-04-21T11:30:00-04:00&#x60;). UTC offsets are supported. Both &#x60;startTime&#x60; and &#x60;endTime&#x60; accept the special value &#x60;UNBOUNDED&#x60;, to signify intervals with no lower or upper bound, respectively. Examples: * &#x60;activeBetween(\&quot;2021-04-21T11:30:00Z\&quot;, \&quot;2021-07-21T00:00:00Z\&quot;)&#x60; * &#x60;activeBetween(UNBOUNDED, \&quot;2021-11-21T00:00:00-04:00\&quot;)&#x60; * &#x60;activeBetween(\&quot;2021-07-21T00:00:00-04:00\&quot;, UNBOUNDED)&#x60; | [optional] 
 **pageSize** | **Number**| Maximum size of the returned data. If unspecified, at most 10 anomalies will be returned. The maximum value is 100; values above 100 will be coerced to 100. | [optional] 
 **pageToken** | **String**| A page token, received from a previous &#x60;ListErrorReports&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListErrorReports&#x60; must match the call that provided the page token. | [optional] 

### Return type

[**GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponse**](GooglePlayDeveloperReportingV1alpha1ListAnomaliesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

