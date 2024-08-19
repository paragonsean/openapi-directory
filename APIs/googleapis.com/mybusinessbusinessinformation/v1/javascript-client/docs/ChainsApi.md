# MyBusinessBusinessInformationApi.ChainsApi

All URIs are relative to *https://mybusinessbusinessinformation.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mybusinessbusinessinformationChainsSearch**](ChainsApi.md#mybusinessbusinessinformationChainsSearch) | **GET** /v1/chains:search | 



## mybusinessbusinessinformationChainsSearch

> SearchChainsResponse mybusinessbusinessinformationChainsSearch(opts)



Searches the chain based on chain name.

### Example

```javascript
import MyBusinessBusinessInformationApi from 'my_business_business_information_api';

let apiInstance = new MyBusinessBusinessInformationApi.ChainsApi();
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
  'chainName': "chainName_example", // String | Required. Search for a chain by its name. Exact/partial/fuzzy/related queries are supported. Examples: \"walmart\", \"wal-mart\", \"walmmmart\", \"沃尔玛\"
  'pageSize': 56 // Number | The maximum number of matched chains to return from this query. The default is 10. The maximum possible value is 500.
};
apiInstance.mybusinessbusinessinformationChainsSearch(opts, (error, data, response) => {
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
 **chainName** | **String**| Required. Search for a chain by its name. Exact/partial/fuzzy/related queries are supported. Examples: \&quot;walmart\&quot;, \&quot;wal-mart\&quot;, \&quot;walmmmart\&quot;, \&quot;沃尔玛\&quot; | [optional] 
 **pageSize** | **Number**| The maximum number of matched chains to return from this query. The default is 10. The maximum possible value is 500. | [optional] 

### Return type

[**SearchChainsResponse**](SearchChainsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

