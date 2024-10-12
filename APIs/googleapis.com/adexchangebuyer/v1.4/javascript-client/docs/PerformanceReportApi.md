# AdExchangeBuyerApi.PerformanceReportApi

All URIs are relative to *https://www.googleapis.com/adexchangebuyer/v1.4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adexchangebuyerPerformanceReportList**](PerformanceReportApi.md#adexchangebuyerPerformanceReportList) | **GET** /performancereport | 



## adexchangebuyerPerformanceReportList

> PerformanceReportList adexchangebuyerPerformanceReportList(accountId, endDateTime, startDateTime, opts)



Retrieves the authenticated user&#39;s list of performance metrics.

### Example

```javascript
import AdExchangeBuyerApi from 'ad_exchange_buyer_api';
let defaultClient = AdExchangeBuyerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdExchangeBuyerApi.PerformanceReportApi();
let accountId = "accountId_example"; // String | The account id to get the reports.
let endDateTime = "endDateTime_example"; // String | The end time of the report in ISO 8601 timestamp format using UTC.
let startDateTime = "startDateTime_example"; // String | The start time of the report in ISO 8601 timestamp format using UTC.
let opts = {
  'alt': "alt_example", // String | Data format for the response.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
  'userIp': "userIp_example", // String | Deprecated. Please use quotaUser instead.
  'maxResults': 56, // Number | Maximum number of entries returned on one result page. If not set, the default is 100. Optional.
  'pageToken': "pageToken_example" // String | A continuation token, used to page through performance reports. To retrieve the next page, set this parameter to the value of \"nextPageToken\" from the previous response. Optional.
};
apiInstance.adexchangebuyerPerformanceReportList(accountId, endDateTime, startDateTime, opts, (error, data, response) => {
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
 **accountId** | **String**| The account id to get the reports. | 
 **endDateTime** | **String**| The end time of the report in ISO 8601 timestamp format using UTC. | 
 **startDateTime** | **String**| The start time of the report in ISO 8601 timestamp format using UTC. | 
 **alt** | **String**| Data format for the response. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] 
 **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] 
 **maxResults** | **Number**| Maximum number of entries returned on one result page. If not set, the default is 100. Optional. | [optional] 
 **pageToken** | **String**| A continuation token, used to page through performance reports. To retrieve the next page, set this parameter to the value of \&quot;nextPageToken\&quot; from the previous response. Optional. | [optional] 

### Return type

[**PerformanceReportList**](PerformanceReportList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

