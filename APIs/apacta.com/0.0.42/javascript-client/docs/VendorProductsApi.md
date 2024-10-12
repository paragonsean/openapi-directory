# Apacta.VendorProductsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendorProductsGet**](VendorProductsApi.md#vendorProductsGet) | **GET** /vendor_products | List vendor products
[**vendorProductsVendorProductIdGet**](VendorProductsApi.md#vendorProductsVendorProductIdGet) | **GET** /vendor_products/{vendor_product_id} | View single vendor product



## vendorProductsGet

> VendorProductsGet200Response vendorProductsGet(opts)

List vendor products

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.VendorProductsApi();
let opts = {
  'name': "name_example", // String | Used to filter on the `name` of the vendor products
  'productNumber': "productNumber_example", // String | Used to filter on the `product_number` of the vendor products
  'barcode': "barcode_example", // String | Used to filter on the `barcode` of the vendor products
  'vendorId': "vendorId_example" // String | Used to filter on the `vendor_id` of the vendor products
};
apiInstance.vendorProductsGet(opts, (error, data, response) => {
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
 **name** | **String**| Used to filter on the &#x60;name&#x60; of the vendor products | [optional] 
 **productNumber** | **String**| Used to filter on the &#x60;product_number&#x60; of the vendor products | [optional] 
 **barcode** | **String**| Used to filter on the &#x60;barcode&#x60; of the vendor products | [optional] 
 **vendorId** | **String**| Used to filter on the &#x60;vendor_id&#x60; of the vendor products | [optional] 

### Return type

[**VendorProductsGet200Response**](VendorProductsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## vendorProductsVendorProductIdGet

> VendorProductsVendorProductIdGet200Response vendorProductsVendorProductIdGet(vendorProductId)

View single vendor product

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.VendorProductsApi();
let vendorProductId = "vendorProductId_example"; // String | 
apiInstance.vendorProductsVendorProductIdGet(vendorProductId, (error, data, response) => {
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
 **vendorProductId** | **String**|  | 

### Return type

[**VendorProductsVendorProductIdGet200Response**](VendorProductsVendorProductIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

