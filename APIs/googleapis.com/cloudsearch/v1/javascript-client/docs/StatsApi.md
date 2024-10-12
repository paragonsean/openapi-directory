# CloudSearchApi.StatsApi

All URIs are relative to *https://cloudsearch.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudsearchStatsGetIndex**](StatsApi.md#cloudsearchStatsGetIndex) | **GET** /v1/stats/index | 
[**cloudsearchStatsGetQuery**](StatsApi.md#cloudsearchStatsGetQuery) | **GET** /v1/stats/query | 
[**cloudsearchStatsGetSearchapplication**](StatsApi.md#cloudsearchStatsGetSearchapplication) | **GET** /v1/stats/searchapplication | 
[**cloudsearchStatsGetSession**](StatsApi.md#cloudsearchStatsGetSession) | **GET** /v1/stats/session | 
[**cloudsearchStatsGetUser**](StatsApi.md#cloudsearchStatsGetUser) | **GET** /v1/stats/user | 
[**cloudsearchStatsIndexDatasourcesGet**](StatsApi.md#cloudsearchStatsIndexDatasourcesGet) | **GET** /v1/stats/index/{name} | 
[**cloudsearchStatsQuerySearchapplicationsGet**](StatsApi.md#cloudsearchStatsQuerySearchapplicationsGet) | **GET** /v1/stats/query/{name} | 
[**cloudsearchStatsSessionSearchapplicationsGet**](StatsApi.md#cloudsearchStatsSessionSearchapplicationsGet) | **GET** /v1/stats/session/{name} | 
[**cloudsearchStatsUserSearchapplicationsGet**](StatsApi.md#cloudsearchStatsUserSearchapplicationsGet) | **GET** /v1/stats/user/{name} | 



## cloudsearchStatsGetIndex

> GetCustomerIndexStatsResponse cloudsearchStatsGetIndex(opts)



Gets indexed item statistics aggreggated across all data sources. This API only returns statistics for previous dates; it doesn&#39;t return statistics for the current day. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
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
  'fromDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'fromDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'fromDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'toDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'toDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'toDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsGetIndex(opts, (error, data, response) => {
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
 **fromDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **fromDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **fromDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **toDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **toDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **toDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetCustomerIndexStatsResponse**](GetCustomerIndexStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchStatsGetQuery

> GetCustomerQueryStatsResponse cloudsearchStatsGetQuery(opts)



Get the query statistics for customer. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
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
  'fromDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'fromDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'fromDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'toDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'toDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'toDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsGetQuery(opts, (error, data, response) => {
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
 **fromDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **fromDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **fromDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **toDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **toDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **toDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetCustomerQueryStatsResponse**](GetCustomerQueryStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchStatsGetSearchapplication

> GetCustomerSearchApplicationStatsResponse cloudsearchStatsGetSearchapplication(opts)



Get search application stats for customer. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
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
  'endDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'endDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'endDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'startDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'startDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'startDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsGetSearchapplication(opts, (error, data, response) => {
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
 **endDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **endDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **endDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **startDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **startDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **startDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetCustomerSearchApplicationStatsResponse**](GetCustomerSearchApplicationStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchStatsGetSession

> GetCustomerSessionStatsResponse cloudsearchStatsGetSession(opts)



Get the # of search sessions, % of successful sessions with a click query statistics for customer. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
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
  'fromDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'fromDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'fromDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'toDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'toDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'toDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsGetSession(opts, (error, data, response) => {
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
 **fromDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **fromDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **fromDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **toDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **toDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **toDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetCustomerSessionStatsResponse**](GetCustomerSessionStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchStatsGetUser

> GetCustomerUserStatsResponse cloudsearchStatsGetUser(opts)



Get the users statistics for customer. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
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
  'fromDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'fromDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'fromDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'toDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'toDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'toDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsGetUser(opts, (error, data, response) => {
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
 **fromDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **fromDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **fromDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **toDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **toDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **toDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetCustomerUserStatsResponse**](GetCustomerUserStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchStatsIndexDatasourcesGet

> GetDataSourceIndexStatsResponse cloudsearchStatsIndexDatasourcesGet(name, opts)



Gets indexed item statistics for a single data source. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
let name = "name_example"; // String | The resource id of the data source to retrieve statistics for, in the following format: \"datasources/{source_id}\"
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
  'fromDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'fromDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'fromDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'toDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'toDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'toDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsIndexDatasourcesGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource id of the data source to retrieve statistics for, in the following format: \&quot;datasources/{source_id}\&quot; | 
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
 **fromDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **fromDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **fromDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **toDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **toDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **toDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetDataSourceIndexStatsResponse**](GetDataSourceIndexStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchStatsQuerySearchapplicationsGet

> GetSearchApplicationQueryStatsResponse cloudsearchStatsQuerySearchapplicationsGet(name, opts)



Get the query statistics for search application. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
let name = "name_example"; // String | The resource id of the search application query stats, in the following format: searchapplications/{application_id}
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
  'fromDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'fromDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'fromDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'toDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'toDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'toDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsQuerySearchapplicationsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource id of the search application query stats, in the following format: searchapplications/{application_id} | 
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
 **fromDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **fromDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **fromDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **toDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **toDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **toDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetSearchApplicationQueryStatsResponse**](GetSearchApplicationQueryStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchStatsSessionSearchapplicationsGet

> GetSearchApplicationSessionStatsResponse cloudsearchStatsSessionSearchapplicationsGet(name, opts)



Get the # of search sessions, % of successful sessions with a click query statistics for search application. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
let name = "name_example"; // String | The resource id of the search application session stats, in the following format: searchapplications/{application_id}
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
  'fromDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'fromDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'fromDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'toDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'toDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'toDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsSessionSearchapplicationsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource id of the search application session stats, in the following format: searchapplications/{application_id} | 
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
 **fromDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **fromDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **fromDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **toDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **toDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **toDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetSearchApplicationSessionStatsResponse**](GetSearchApplicationSessionStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudsearchStatsUserSearchapplicationsGet

> GetSearchApplicationUserStatsResponse cloudsearchStatsUserSearchapplicationsGet(name, opts)



Get the users statistics for search application. **Note:** This API requires a standard end user account to execute.

### Example

```javascript
import CloudSearchApi from 'cloud_search_api';
let defaultClient = CloudSearchApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudSearchApi.StatsApi();
let name = "name_example"; // String | The resource id of the search application session stats, in the following format: searchapplications/{application_id}
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
  'fromDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'fromDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'fromDateYear': 56, // Number | Year of date. Must be from 1 to 9999.
  'toDateDay': 56, // Number | Day of month. Must be from 1 to 31 and valid for the year and month.
  'toDateMonth': 56, // Number | Month of date. Must be from 1 to 12.
  'toDateYear': 56 // Number | Year of date. Must be from 1 to 9999.
};
apiInstance.cloudsearchStatsUserSearchapplicationsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource id of the search application session stats, in the following format: searchapplications/{application_id} | 
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
 **fromDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **fromDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **fromDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 
 **toDateDay** | **Number**| Day of month. Must be from 1 to 31 and valid for the year and month. | [optional] 
 **toDateMonth** | **Number**| Month of date. Must be from 1 to 12. | [optional] 
 **toDateYear** | **Number**| Year of date. Must be from 1 to 9999. | [optional] 

### Return type

[**GetSearchApplicationUserStatsResponse**](GetSearchApplicationUserStatsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

