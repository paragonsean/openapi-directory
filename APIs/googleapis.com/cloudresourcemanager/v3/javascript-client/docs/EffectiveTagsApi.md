# CloudResourceManagerApi.EffectiveTagsApi

All URIs are relative to *https://cloudresourcemanager.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudresourcemanagerEffectiveTagsList**](EffectiveTagsApi.md#cloudresourcemanagerEffectiveTagsList) | **GET** /v3/effectiveTags | 



## cloudresourcemanagerEffectiveTagsList

> ListEffectiveTagsResponse cloudresourcemanagerEffectiveTagsList(opts)



Return a list of effective tags for the given Google Cloud resource, as specified in &#x60;parent&#x60;.

### Example

```javascript
import CloudResourceManagerApi from 'cloud_resource_manager_api';
let defaultClient = CloudResourceManagerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudResourceManagerApi.EffectiveTagsApi();
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
  'pageSize': 56, // Number | Optional. The maximum number of effective tags to return in the response. The server allows a maximum of 300 effective tags to return in a single page. If unspecified, the server will use 100 as the default.
  'pageToken': "pageToken_example", // String | Optional. A pagination token returned from a previous call to `ListEffectiveTags` that indicates from where this listing should continue.
  'parent': "parent_example" // String | Required. The full resource name of a resource for which you want to list the effective tags. E.g. \"//cloudresourcemanager.googleapis.com/projects/123\"
};
apiInstance.cloudresourcemanagerEffectiveTagsList(opts, (error, data, response) => {
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
 **pageSize** | **Number**| Optional. The maximum number of effective tags to return in the response. The server allows a maximum of 300 effective tags to return in a single page. If unspecified, the server will use 100 as the default. | [optional] 
 **pageToken** | **String**| Optional. A pagination token returned from a previous call to &#x60;ListEffectiveTags&#x60; that indicates from where this listing should continue. | [optional] 
 **parent** | **String**| Required. The full resource name of a resource for which you want to list the effective tags. E.g. \&quot;//cloudresourcemanager.googleapis.com/projects/123\&quot; | [optional] 

### Return type

[**ListEffectiveTagsResponse**](ListEffectiveTagsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

