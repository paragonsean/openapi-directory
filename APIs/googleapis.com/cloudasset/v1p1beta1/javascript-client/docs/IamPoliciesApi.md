# CloudAssetApi.IamPoliciesApi

All URIs are relative to *https://cloudasset.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudassetIamPoliciesSearchAll**](IamPoliciesApi.md#cloudassetIamPoliciesSearchAll) | **GET** /v1p1beta1/{scope}/iamPolicies:searchAll | 



## cloudassetIamPoliciesSearchAll

> SearchAllIamPoliciesResponse cloudassetIamPoliciesSearchAll(scope, opts)



Searches all the IAM policies within a given accessible Resource Manager scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the IAM policies within a scope, even if they don&#39;t have &#x60;.getIamPolicy&#x60; permission of all the IAM policies. Callers should have &#x60;cloud.assets.SearchAllIamPolicies&#x60; permission on the requested scope, otherwise the request will be rejected.

### Example

```javascript
import CloudAssetApi from 'cloud_asset_api';
let defaultClient = CloudAssetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudAssetApi.IamPoliciesApi();
let scope = "scope_example"; // String | Required. The relative name of an asset. The search is limited to the resources within the `scope`. The allowed value must be: * Organization number (such as \"organizations/123\") * Folder number (such as \"folders/1234\") * Project number (such as \"projects/12345\") * Project ID (such as \"projects/abc\")
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
  'pageSize': 56, // Number | Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned.
  'pageToken': "pageToken_example", // String | Optional. If present, retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters must be identical to those in the previous call.
  'query': "query_example" // String | Optional. The query statement. Examples: * \"policy:myuser@mydomain.com\" * \"policy:(myuser@mydomain.com viewer)\"
};
apiInstance.cloudassetIamPoliciesSearchAll(scope, opts, (error, data, response) => {
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
 **scope** | **String**| Required. The relative name of an asset. The search is limited to the resources within the &#x60;scope&#x60;. The allowed value must be: * Organization number (such as \&quot;organizations/123\&quot;) * Folder number (such as \&quot;folders/1234\&quot;) * Project number (such as \&quot;projects/12345\&quot;) * Project ID (such as \&quot;projects/abc\&quot;) | 
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
 **pageSize** | **Number**| Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as &#x60;next_page_token&#x60; is returned. | [optional] 
 **pageToken** | **String**| Optional. If present, retrieve the next batch of results from the preceding call to this method. &#x60;page_token&#x60; must be the value of &#x60;next_page_token&#x60; from the previous response. The values of all other method parameters must be identical to those in the previous call. | [optional] 
 **query** | **String**| Optional. The query statement. Examples: * \&quot;policy:myuser@mydomain.com\&quot; * \&quot;policy:(myuser@mydomain.com viewer)\&quot; | [optional] 

### Return type

[**SearchAllIamPoliciesResponse**](SearchAllIamPoliciesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

