# YouTubeReportingApi.ReportTypesApi

All URIs are relative to *https://youtubereporting.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**youtubereportingReportTypesList**](ReportTypesApi.md#youtubereportingReportTypesList) | **GET** /v1/reportTypes | 



## youtubereportingReportTypesList

> ListReportTypesResponse youtubereportingReportTypesList(opts)



Lists report types.

### Example

```javascript
import YouTubeReportingApi from 'you_tube_reporting_api';
let defaultClient = YouTubeReportingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new YouTubeReportingApi.ReportTypesApi();
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
  'includeSystemManaged': true, // Boolean | If set to true, also system-managed report types will be returned; otherwise only the report types that can be used to create new reporting jobs will be returned.
  'onBehalfOfContentOwner': "onBehalfOfContentOwner_example", // String | The content owner's external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel).
  'pageSize': 56, // Number | Requested page size. Server may return fewer report types than requested. If unspecified, server will pick an appropriate default.
  'pageToken': "pageToken_example" // String | A token identifying a page of results the server should return. Typically, this is the value of ListReportTypesResponse.next_page_token returned in response to the previous call to the `ListReportTypes` method.
};
apiInstance.youtubereportingReportTypesList(opts, (error, data, response) => {
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
 **includeSystemManaged** | **Boolean**| If set to true, also system-managed report types will be returned; otherwise only the report types that can be used to create new reporting jobs will be returned. | [optional] 
 **onBehalfOfContentOwner** | **String**| The content owner&#39;s external ID on which behalf the user is acting on. If not set, the user is acting for himself (his own channel). | [optional] 
 **pageSize** | **Number**| Requested page size. Server may return fewer report types than requested. If unspecified, server will pick an appropriate default. | [optional] 
 **pageToken** | **String**| A token identifying a page of results the server should return. Typically, this is the value of ListReportTypesResponse.next_page_token returned in response to the previous call to the &#x60;ListReportTypes&#x60; method. | [optional] 

### Return type

[**ListReportTypesResponse**](ListReportTypesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

