# ApiV100.ProductApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productApiAll**](ProductApi.md#productApiAll) | **GET** /api/product/all | Return all products for the account
[**productApiDelete**](ProductApi.md#productApiDelete) | **POST** /api/product/delete | Delete an existing product
[**productApiDetails**](ProductApi.md#productApiDetails) | **GET** /api/product/details | Return product details
[**productApiNew**](ProductApi.md#productApiNew) | **POST** /api/product/new | Create a product
[**productApiUpdate**](ProductApi.md#productApiUpdate) | **POST** /api/product/update | Update an existing product



## productApiAll

> ListResultProductDetailsApiModel productApiAll(xAuthKey, xAuthSecret, opts)

Return all products for the account

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ProductApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let opts = {
  'queryOptionsPage': 56, // Number | 
  'queryOptionsPageSize': 56 // Number | 
};
apiInstance.productApiAll(xAuthKey, xAuthSecret, opts, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **queryOptionsPage** | **Number**|  | [optional] 
 **queryOptionsPageSize** | **Number**|  | [optional] 

### Return type

[**ListResultProductDetailsApiModel**](ListResultProductDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## productApiDelete

> Number productApiDelete(xAuthKey, xAuthSecret, productDeleteApiModel)

Delete an existing product

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ProductApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let productDeleteApiModel = new ApiV100.ProductDeleteApiModel(); // ProductDeleteApiModel | 
apiInstance.productApiDelete(xAuthKey, xAuthSecret, productDeleteApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **productDeleteApiModel** | [**ProductDeleteApiModel**](ProductDeleteApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## productApiDetails

> ProductFullDetailsApiModel productApiDetails(id, xAuthKey, xAuthSecret)

Return product details

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ProductApi();
let id = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.productApiDetails(id, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **id** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**ProductFullDetailsApiModel**](ProductFullDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## productApiNew

> Number productApiNew(xAuthKey, xAuthSecret, productCreateApiModel)

Create a product

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ProductApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let productCreateApiModel = new ApiV100.ProductCreateApiModel(); // ProductCreateApiModel | 
apiInstance.productApiNew(xAuthKey, xAuthSecret, productCreateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **productCreateApiModel** | [**ProductCreateApiModel**](ProductCreateApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## productApiUpdate

> productApiUpdate(xAuthKey, xAuthSecret, productUpdateApiModel)

Update an existing product

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.ProductApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let productUpdateApiModel = new ApiV100.ProductUpdateApiModel(); // ProductUpdateApiModel | 
apiInstance.productApiUpdate(xAuthKey, xAuthSecret, productUpdateApiModel, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **productUpdateApiModel** | [**ProductUpdateApiModel**](ProductUpdateApiModel.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: Not defined

