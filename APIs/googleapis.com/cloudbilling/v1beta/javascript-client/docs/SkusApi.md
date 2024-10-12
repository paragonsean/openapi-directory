# CloudBillingApi.SkusApi

All URIs are relative to *https://cloudbilling.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cloudbillingSkusPriceGet**](SkusApi.md#cloudbillingSkusPriceGet) | **GET** /v1beta/{name} | 
[**cloudbillingSkusPricesList**](SkusApi.md#cloudbillingSkusPricesList) | **GET** /v1beta/{parent}/prices | 



## cloudbillingSkusPriceGet

> GoogleCloudBillingPricesV1betaPrice cloudbillingSkusPriceGet(name, opts)



Gets the latest price for the given SKU.

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

let apiInstance = new CloudBillingApi.SkusApi();
let name = "name_example"; // String | Required. Name of the latest price to retrieve. Format: skus/{sku}/price
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
  'currencyCode': "currencyCode_example" // String | Optional. ISO-4217 currency code for the price. If not specified, USD will be used.
};
apiInstance.cloudbillingSkusPriceGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Name of the latest price to retrieve. Format: skus/{sku}/price | 
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
 **currencyCode** | **String**| Optional. ISO-4217 currency code for the price. If not specified, USD will be used. | [optional] 

### Return type

[**GoogleCloudBillingPricesV1betaPrice**](GoogleCloudBillingPricesV1betaPrice.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cloudbillingSkusPricesList

> GoogleCloudBillingPricesV1betaListPricesResponse cloudbillingSkusPricesList(parent, opts)



Lists the latest prices for all SKUs.

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

let apiInstance = new CloudBillingApi.SkusApi();
let parent = "parent_example"; // String | Required. To list the prices for all SKUs, use `-` as the SKU ID. Format: `skus/-` Specifying a specific SKU ID returns a collection with one Price object for the SKU.
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
  'currencyCode': "currencyCode_example", // String | Optional. ISO-4217 currency code for the price. If not specified, USD will be used.
  'pageSize': 56, // Number | Optional. Maximum number of prices to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000.
  'pageToken': "pageToken_example" // String | Optional. Page token received from a previous ListPrices call to retrieve the next page of results. If this field is empty, the first page is returned.
};
apiInstance.cloudbillingSkusPricesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. To list the prices for all SKUs, use &#x60;-&#x60; as the SKU ID. Format: &#x60;skus/-&#x60; Specifying a specific SKU ID returns a collection with one Price object for the SKU. | 
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
 **currencyCode** | **String**| Optional. ISO-4217 currency code for the price. If not specified, USD will be used. | [optional] 
 **pageSize** | **Number**| Optional. Maximum number of prices to return. Results may return fewer than this value. Default value is 50 and maximum value is 5000. | [optional] 
 **pageToken** | **String**| Optional. Page token received from a previous ListPrices call to retrieve the next page of results. If this field is empty, the first page is returned. | [optional] 

### Return type

[**GoogleCloudBillingPricesV1betaListPricesResponse**](GoogleCloudBillingPricesV1betaListPricesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

