# ContentApiForShopping.ProductstatusesApi

All URIs are relative to *https://shoppingcontent.googleapis.com/content/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentProductstatusesCustombatch**](ProductstatusesApi.md#contentProductstatusesCustombatch) | **POST** /productstatuses/batch | 
[**contentProductstatusesGet**](ProductstatusesApi.md#contentProductstatusesGet) | **GET** /{merchantId}/productstatuses/{productId} | 
[**contentProductstatusesList**](ProductstatusesApi.md#contentProductstatusesList) | **GET** /{merchantId}/productstatuses | 



## contentProductstatusesCustombatch

> ProductstatusesCustomBatchResponse contentProductstatusesCustombatch(opts)



Gets the statuses of multiple products in a single request.

### Example

```javascript
import ContentApiForShopping from 'content_api_for_shopping';
let defaultClient = ContentApiForShopping.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentApiForShopping.ProductstatusesApi();
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
  'includeAttributes': true, // Boolean | Flag to include full product data in the results of this request. The default value is false.
  'productstatusesCustomBatchRequest': new ContentApiForShopping.ProductstatusesCustomBatchRequest() // ProductstatusesCustomBatchRequest | 
};
apiInstance.contentProductstatusesCustombatch(opts, (error, data, response) => {
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
 **includeAttributes** | **Boolean**| Flag to include full product data in the results of this request. The default value is false. | [optional] 
 **productstatusesCustomBatchRequest** | [**ProductstatusesCustomBatchRequest**](ProductstatusesCustomBatchRequest.md)|  | [optional] 

### Return type

[**ProductstatusesCustomBatchResponse**](ProductstatusesCustomBatchResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contentProductstatusesGet

> ProductStatus contentProductstatusesGet(merchantId, productId, opts)



Gets the status of a product from your Merchant Center account.

### Example

```javascript
import ContentApiForShopping from 'content_api_for_shopping';
let defaultClient = ContentApiForShopping.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentApiForShopping.ProductstatusesApi();
let merchantId = "merchantId_example"; // String | The ID of the account that contains the product. This account cannot be a multi-client account.
let productId = "productId_example"; // String | The REST ID of the product.
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
  'destinations': ["null"], // [String] | If set, only issues for the specified destinations are returned, otherwise only issues for the Shopping destination.
  'includeAttributes': true // Boolean | Flag to include full product data in the result of this get request. The default value is false.
};
apiInstance.contentProductstatusesGet(merchantId, productId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The ID of the account that contains the product. This account cannot be a multi-client account. | 
 **productId** | **String**| The REST ID of the product. | 
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
 **destinations** | [**[String]**](String.md)| If set, only issues for the specified destinations are returned, otherwise only issues for the Shopping destination. | [optional] 
 **includeAttributes** | **Boolean**| Flag to include full product data in the result of this get request. The default value is false. | [optional] 

### Return type

[**ProductStatus**](ProductStatus.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contentProductstatusesList

> ProductstatusesListResponse contentProductstatusesList(merchantId, opts)



Lists the statuses of the products in your Merchant Center account.

### Example

```javascript
import ContentApiForShopping from 'content_api_for_shopping';
let defaultClient = ContentApiForShopping.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentApiForShopping.ProductstatusesApi();
let merchantId = "merchantId_example"; // String | The ID of the account that contains the products. This account cannot be a multi-client account.
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
  'destinations': ["null"], // [String] | If set, only issues for the specified destinations are returned, otherwise only issues for the Shopping destination.
  'includeAttributes': true, // Boolean | Flag to include full product data in the results of the list request. The default value is false.
  'includeInvalidInsertedItems': true, // Boolean | Flag to include the invalid inserted items in the result of the list request. By default the invalid items are not shown (the default value is false).
  'maxResults': 56, // Number | The maximum number of product statuses to return in the response, used for paging.
  'pageToken': "pageToken_example" // String | The token returned by the previous request.
};
apiInstance.contentProductstatusesList(merchantId, opts, (error, data, response) => {
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
 **merchantId** | **String**| The ID of the account that contains the products. This account cannot be a multi-client account. | 
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
 **destinations** | [**[String]**](String.md)| If set, only issues for the specified destinations are returned, otherwise only issues for the Shopping destination. | [optional] 
 **includeAttributes** | **Boolean**| Flag to include full product data in the results of the list request. The default value is false. | [optional] 
 **includeInvalidInsertedItems** | **Boolean**| Flag to include the invalid inserted items in the result of the list request. By default the invalid items are not shown (the default value is false). | [optional] 
 **maxResults** | **Number**| The maximum number of product statuses to return in the response, used for paging. | [optional] 
 **pageToken** | **String**| The token returned by the previous request. | [optional] 

### Return type

[**ProductstatusesListResponse**](ProductstatusesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

