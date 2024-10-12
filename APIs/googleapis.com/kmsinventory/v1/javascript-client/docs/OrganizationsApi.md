# KmsInventoryApi.OrganizationsApi

All URIs are relative to *https://kmsinventory.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kmsinventoryOrganizationsProtectedResourcesSearch**](OrganizationsApi.md#kmsinventoryOrganizationsProtectedResourcesSearch) | **GET** /v1/{scope}/protectedResources:search | 



## kmsinventoryOrganizationsProtectedResourcesSearch

> GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse kmsinventoryOrganizationsProtectedResourcesSearch(scope, opts)



Returns metadata about the resources protected by the given Cloud KMS CryptoKey in the given Cloud organization.

### Example

```javascript
import KmsInventoryApi from 'kms_inventory_api';
let defaultClient = KmsInventoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new KmsInventoryApi.OrganizationsApi();
let scope = "scope_example"; // String | Required. Resource name of the organization. Example: organizations/123
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
  'cryptoKey': "cryptoKey_example", // String | Required. The resource name of the CryptoKey.
  'pageSize': 56, // Number | The maximum number of resources to return. The service may return fewer than this value. If unspecified, at most 500 resources will be returned. The maximum value is 500; values above 500 will be coerced to 500.
  'pageToken': "pageToken_example", // String | A page token, received from a previous KeyTrackingService.SearchProtectedResources call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to KeyTrackingService.SearchProtectedResources must match the call that provided the page token.
  'resourceTypes': ["null"] // [String] | Optional. A list of resource types that this request searches for. If empty, it will search all the [trackable resource types](https://cloud.google.com/kms/docs/view-key-usage#tracked-resource-types). Regular expressions are also supported. For example: * `compute.googleapis.com.*` snapshots resources whose type starts with `compute.googleapis.com`. * `.*Image` snapshots resources whose type ends with `Image`. * `.*Image.*` snapshots resources whose type contains `Image`. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported resource type, an INVALID_ARGUMENT error will be returned.
};
apiInstance.kmsinventoryOrganizationsProtectedResourcesSearch(scope, opts, (error, data, response) => {
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
 **scope** | **String**| Required. Resource name of the organization. Example: organizations/123 | 
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
 **cryptoKey** | **String**| Required. The resource name of the CryptoKey. | [optional] 
 **pageSize** | **Number**| The maximum number of resources to return. The service may return fewer than this value. If unspecified, at most 500 resources will be returned. The maximum value is 500; values above 500 will be coerced to 500. | [optional] 
 **pageToken** | **String**| A page token, received from a previous KeyTrackingService.SearchProtectedResources call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to KeyTrackingService.SearchProtectedResources must match the call that provided the page token. | [optional] 
 **resourceTypes** | [**[String]**](String.md)| Optional. A list of resource types that this request searches for. If empty, it will search all the [trackable resource types](https://cloud.google.com/kms/docs/view-key-usage#tracked-resource-types). Regular expressions are also supported. For example: * &#x60;compute.googleapis.com.*&#x60; snapshots resources whose type starts with &#x60;compute.googleapis.com&#x60;. * &#x60;.*Image&#x60; snapshots resources whose type ends with &#x60;Image&#x60;. * &#x60;.*Image.*&#x60; snapshots resources whose type contains &#x60;Image&#x60;. See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported resource type, an INVALID_ARGUMENT error will be returned. | [optional] 

### Return type

[**GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse**](GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

