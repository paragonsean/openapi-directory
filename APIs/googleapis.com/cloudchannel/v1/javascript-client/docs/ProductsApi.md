# CloudChannelApi.ProductsApi

All URIs are relative to *https://cloudchannel.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudchannelProductsList**](ProductsApi.md#cloudchannelProductsList) | **GET** /v1/products | 
[**cloudchannelProductsSkusList**](ProductsApi.md#cloudchannelProductsSkusList) | **GET** /v1/{parent}/skus | 



## cloudchannelProductsList

> GoogleCloudChannelV1ListProductsResponse cloudchannelProductsList(opts)



Lists the Products the reseller is authorized to sell. Possible error codes: * INVALID_ARGUMENT: Required request parameters are missing or invalid.

### Example

```javascript
import CloudChannelApi from 'cloud_channel_api';
let defaultClient = CloudChannelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudChannelApi.ProductsApi();
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
  'account': "account_example", // String | Required. The resource name of the reseller account. Format: accounts/{account_id}.
  'languageCode': "languageCode_example", // String | Optional. The BCP-47 language code. For example, \"en-US\". The response will localize in the corresponding language code, if specified. The default value is \"en-US\".
  'pageSize': 56, // Number | Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 Products. The maximum value is 1000; the server will coerce values above 1000.
  'pageToken': "pageToken_example" // String | Optional. A token for a page of results other than the first page.
};
apiInstance.cloudchannelProductsList(opts, (error, data, response) => {
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
 **account** | **String**| Required. The resource name of the reseller account. Format: accounts/{account_id}. | [optional] 
 **languageCode** | **String**| Optional. The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;. | [optional] 
 **pageSize** | **Number**| Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 Products. The maximum value is 1000; the server will coerce values above 1000. | [optional] 
 **pageToken** | **String**| Optional. A token for a page of results other than the first page. | [optional] 

### Return type

[**GoogleCloudChannelV1ListProductsResponse**](GoogleCloudChannelV1ListProductsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudchannelProductsSkusList

> GoogleCloudChannelV1ListSkusResponse cloudchannelProductsSkusList(parent, opts)



Lists the SKUs for a product the reseller is authorized to sell. Possible error codes: * INVALID_ARGUMENT: Required request parameters are missing or invalid.

### Example

```javascript
import CloudChannelApi from 'cloud_channel_api';
let defaultClient = CloudChannelApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CloudChannelApi.ProductsApi();
let parent = "parent_example"; // String | Required. The resource name of the Product to list SKUs for. Parent uses the format: products/{product_id}. Supports products/- to retrieve SKUs for all products.
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
  'account': "account_example", // String | Required. Resource name of the reseller. Format: accounts/{account_id}.
  'languageCode': "languageCode_example", // String | Optional. The BCP-47 language code. For example, \"en-US\". The response will localize in the corresponding language code, if specified. The default value is \"en-US\".
  'pageSize': 56, // Number | Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000.
  'pageToken': "pageToken_example" // String | Optional. A token for a page of results other than the first page. Optional.
};
apiInstance.cloudchannelProductsSkusList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the Product to list SKUs for. Parent uses the format: products/{product_id}. Supports products/- to retrieve SKUs for all products. | 
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
 **account** | **String**| Required. Resource name of the reseller. Format: accounts/{account_id}. | [optional] 
 **languageCode** | **String**| Optional. The BCP-47 language code. For example, \&quot;en-US\&quot;. The response will localize in the corresponding language code, if specified. The default value is \&quot;en-US\&quot;. | [optional] 
 **pageSize** | **Number**| Optional. Requested page size. Server might return fewer results than requested. If unspecified, returns at most 100 SKUs. The maximum value is 1000; the server will coerce values above 1000. | [optional] 
 **pageToken** | **String**| Optional. A token for a page of results other than the first page. Optional. | [optional] 

### Return type

[**GoogleCloudChannelV1ListSkusResponse**](GoogleCloudChannelV1ListSkusResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

