# MyBusinessBusinessInformationApi.GoogleLocationsApi

All URIs are relative to *https://mybusinessbusinessinformation.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessbusinessinformationGoogleLocationsSearch**](GoogleLocationsApi.md#mybusinessbusinessinformationGoogleLocationsSearch) | **POST** /v1/googleLocations:search | 



## mybusinessbusinessinformationGoogleLocationsSearch

> SearchGoogleLocationsResponse mybusinessbusinessinformationGoogleLocationsSearch(opts)



Search all of the possible locations that are a match to the specified request.

### Example

```javascript
import MyBusinessBusinessInformationApi from 'my_business_business_information_api';

let apiInstance = new MyBusinessBusinessInformationApi.GoogleLocationsApi();
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
  'searchGoogleLocationsRequest': new MyBusinessBusinessInformationApi.SearchGoogleLocationsRequest() // SearchGoogleLocationsRequest | 
};
apiInstance.mybusinessbusinessinformationGoogleLocationsSearch(opts, (error, data, response) => {
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
 **searchGoogleLocationsRequest** | [**SearchGoogleLocationsRequest**](SearchGoogleLocationsRequest.md)|  | [optional] 

### Return type

[**SearchGoogleLocationsResponse**](SearchGoogleLocationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

