# CloudBillingApi.SkuGroupsApi

All URIs are relative to *https://cloudbilling.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudbillingSkuGroupsList**](SkuGroupsApi.md#cloudbillingSkuGroupsList) | **GET** /v1beta/skuGroups | 
[**cloudbillingSkuGroupsSkusList**](SkuGroupsApi.md#cloudbillingSkuGroupsSkusList) | **GET** /v1beta/{parent}/skus | 



## cloudbillingSkuGroupsList

> GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponse cloudbillingSkuGroupsList(opts)



Lists all publicly listed SKU groups.

### Example

```javascript
import CloudBillingApi from 'cloud_billing_api';
let defaultClient = CloudBillingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudBillingApi.SkuGroupsApi();
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
  'pageSize': 56, // Number | Maximum number of SKU groups to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
  'pageToken': "pageToken_example" // String | Page token received from a previous ListSkuGroups call to retrieve the next page of results. If this field is empty, the first page is returned.
};
apiInstance.cloudbillingSkuGroupsList(opts, (error, data, response) => {
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
 **pageSize** | **Number**| Maximum number of SKU groups to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000. | [optional] 
 **pageToken** | **String**| Page token received from a previous ListSkuGroups call to retrieve the next page of results. If this field is empty, the first page is returned. | [optional] 

### Return type

[**GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponse**](GoogleCloudBillingSkugroupsV1betaListSkuGroupsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudbillingSkuGroupsSkusList

> GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponse cloudbillingSkuGroupsSkusList(parent, opts)



Lists all publicly listed SKUs contained by a publicly listed SKU group.

### Example

```javascript
import CloudBillingApi from 'cloud_billing_api';
let defaultClient = CloudBillingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudBillingApi.SkuGroupsApi();
let parent = "parent_example"; // String | Required. The SkuGroup to list SkuGroupSku from. Format: skuGroups/{sku_group}
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
  'pageSize': 56, // Number | Maximum number of SKU group SKUs to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
  'pageToken': "pageToken_example" // String | Page token received from a previous ListSkuGroupSkus call to retrieve the next page of results. If this field is empty, the first page is returned.
};
apiInstance.cloudbillingSkuGroupsSkusList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The SkuGroup to list SkuGroupSku from. Format: skuGroups/{sku_group} | 
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
 **pageSize** | **Number**| Maximum number of SKU group SKUs to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000. | [optional] 
 **pageToken** | **String**| Page token received from a previous ListSkuGroupSkus call to retrieve the next page of results. If this field is empty, the first page is returned. | [optional] 

### Return type

[**GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponse**](GoogleCloudBillingSkugroupskusV1betaListSkuGroupSkusResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

