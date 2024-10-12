# KeyServ.ProductsApiApi

All URIs are relative to *https://keyserv.solutions*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsApiCount**](ProductsApiApi.md#productsApiCount) | **POST** /v1/ProductsApi/Count | 
[**productsApiDeleteProduct**](ProductsApiApi.md#productsApiDeleteProduct) | **DELETE** /v1/ProductsApi/{serial} | 
[**productsApiDeleteProduct2**](ProductsApiApi.md#productsApiDeleteProduct2) | **POST** /v1/ProductsApi/{serial} | 
[**productsApiFind**](ProductsApiApi.md#productsApiFind) | **POST** /v1/ProductsApi/Find | 
[**productsApiList**](ProductsApiApi.md#productsApiList) | **POST** /v1/ProductsApi/List | 
[**productsApiPatchProduct**](ProductsApiApi.md#productsApiPatchProduct) | **PATCH** /v1/ProductsApi | 
[**productsApiPatchProduct2**](ProductsApiApi.md#productsApiPatchProduct2) | **POST** /v1/ProductsApi | 
[**productsApiSave**](ProductsApiApi.md#productsApiSave) | **POST** /v1/ProductsApi/Save | 



## productsApiCount

> ProductsApiCount200Response productsApiCount(productsApiCountRequest)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.ProductsApiApi();
let productsApiCountRequest = new KeyServ.ProductsApiCountRequest(); // ProductsApiCountRequest | 
apiInstance.productsApiCount(productsApiCountRequest, (error, data, response) => {
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
 **productsApiCountRequest** | [**ProductsApiCountRequest**](ProductsApiCountRequest.md)|  | 

### Return type

[**ProductsApiCount200Response**](ProductsApiCount200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsApiDeleteProduct

> productsApiDeleteProduct(xApiKey, serial)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.ProductsApiApi();
let xApiKey = "xApiKey_example"; // String | 
let serial = "serial_example"; // String | 
apiInstance.productsApiDeleteProduct(xApiKey, serial, (error, data, response) => {
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
 **xApiKey** | **String**|  | 
 **serial** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsApiDeleteProduct2

> productsApiDeleteProduct2(xApiKey, serial)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.ProductsApiApi();
let xApiKey = "xApiKey_example"; // String | 
let serial = "serial_example"; // String | 
apiInstance.productsApiDeleteProduct2(xApiKey, serial, (error, data, response) => {
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
 **xApiKey** | **String**|  | 
 **serial** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsApiFind

> ProductsApiFind200Response productsApiFind(productsApiFindRequest, opts)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.ProductsApiApi();
let productsApiFindRequest = new KeyServ.ProductsApiFindRequest(); // ProductsApiFindRequest | 
let opts = {
  'page': 56 // Number | 
};
apiInstance.productsApiFind(productsApiFindRequest, opts, (error, data, response) => {
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
 **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | 
 **page** | **Number**|  | [optional] 

### Return type

[**ProductsApiFind200Response**](ProductsApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsApiList

> [ProductView] productsApiList(productsApiCountRequest, opts)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.ProductsApiApi();
let productsApiCountRequest = new KeyServ.ProductsApiCountRequest(); // ProductsApiCountRequest | 
let opts = {
  'page': 56 // Number | 
};
apiInstance.productsApiList(productsApiCountRequest, opts, (error, data, response) => {
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
 **productsApiCountRequest** | [**ProductsApiCountRequest**](ProductsApiCountRequest.md)|  | 
 **page** | **Number**|  | [optional] 

### Return type

[**[ProductView]**](ProductView.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsApiPatchProduct

> productsApiPatchProduct(productsApiPatchProduct2Request)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.ProductsApiApi();
let productsApiPatchProduct2Request = new KeyServ.ProductsApiPatchProduct2Request(); // ProductsApiPatchProduct2Request | 
apiInstance.productsApiPatchProduct(productsApiPatchProduct2Request, (error, data, response) => {
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
 **productsApiPatchProduct2Request** | [**ProductsApiPatchProduct2Request**](ProductsApiPatchProduct2Request.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productsApiPatchProduct2

> productsApiPatchProduct2(productsApiPatchProduct2Request)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.ProductsApiApi();
let productsApiPatchProduct2Request = new KeyServ.ProductsApiPatchProduct2Request(); // ProductsApiPatchProduct2Request | 
apiInstance.productsApiPatchProduct2(productsApiPatchProduct2Request, (error, data, response) => {
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
 **productsApiPatchProduct2Request** | [**ProductsApiPatchProduct2Request**](ProductsApiPatchProduct2Request.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## productsApiSave

> ProductsApiFind200Response productsApiSave(productsApiPatchProduct2Request)



### Example

```javascript
import KeyServ from 'key_serv';

let apiInstance = new KeyServ.ProductsApiApi();
let productsApiPatchProduct2Request = new KeyServ.ProductsApiPatchProduct2Request(); // ProductsApiPatchProduct2Request | 
apiInstance.productsApiSave(productsApiPatchProduct2Request, (error, data, response) => {
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
 **productsApiPatchProduct2Request** | [**ProductsApiPatchProduct2Request**](ProductsApiPatchProduct2Request.md)|  | 

### Return type

[**ProductsApiFind200Response**](ProductsApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

