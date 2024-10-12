# Apacta.ProductVariantsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsProductIdVariantsGet**](ProductVariantsApi.md#productsProductIdVariantsGet) | **GET** /products/{product_id}/variants | Get a product&#39;s variants
[**productsProductIdVariantsPost**](ProductVariantsApi.md#productsProductIdVariantsPost) | **POST** /products/{product_id}/variants | Add a new variant to a product
[**productsProductIdVariantsVariantTypeVariantIdDelete**](ProductVariantsApi.md#productsProductIdVariantsVariantTypeVariantIdDelete) | **DELETE** /products/{product_id}/variants/{variant_type}/{variant_id} | Delete a product variant



## productsProductIdVariantsGet

> ProductsProductIdVariantsGet200Response productsProductIdVariantsGet(productId)

Get a product&#39;s variants

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ProductVariantsApi();
let productId = "productId_example"; // String | 
apiInstance.productsProductIdVariantsGet(productId, (error, data, response) => {
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
 **productId** | **String**|  | 

### Return type

[**ProductsProductIdVariantsGet200Response**](ProductsProductIdVariantsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsProductIdVariantsPost

> EmptySuccessResponse productsProductIdVariantsPost(productId, ratio, variantId, variantType, opts)

Add a new variant to a product

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

let apiInstance = new Apacta.ProductVariantsApi();
let productId = "productId_example"; // String | 
let ratio = 3.4; // Number | 
let variantId = "variantId_example"; // String | 
let variantType = "variantType_example"; // String | 
let opts = {
  'name': "name_example" // String | Filters by name
};
apiInstance.productsProductIdVariantsPost(productId, ratio, variantId, variantType, opts, (error, data, response) => {
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
 **productId** | **String**|  | 
 **ratio** | **Number**|  | 
 **variantId** | **String**|  | 
 **variantType** | **String**|  | 
 **name** | **String**| Filters by name | [optional] 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## productsProductIdVariantsVariantTypeVariantIdDelete

> EmptySuccessResponse productsProductIdVariantsVariantTypeVariantIdDelete(productId, variantType, variantId)

Delete a product variant

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.ProductVariantsApi();
let productId = "productId_example"; // String | 
let variantType = "variantType_example"; // String | 
let variantId = "variantId_example"; // String | 
apiInstance.productsProductIdVariantsVariantTypeVariantIdDelete(productId, variantType, variantId, (error, data, response) => {
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
 **productId** | **String**|  | 
 **variantType** | **String**|  | 
 **variantId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

