# JumpsellerApi.ProductDigitalProductsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsIdDigitalProductsCountJsonGet**](ProductDigitalProductsApi.md#productsIdDigitalProductsCountJsonGet) | **GET** /products/{id}/digital_products/count.json | Count all Product DigitalProducts.
[**productsIdDigitalProductsDigitalProductIdJsonDelete**](ProductDigitalProductsApi.md#productsIdDigitalProductsDigitalProductIdJsonDelete) | **DELETE** /products/{id}/digital_products/{digital_product_id}.json | Delete a Product DigitalProduct.
[**productsIdDigitalProductsDigitalProductIdJsonGet**](ProductDigitalProductsApi.md#productsIdDigitalProductsDigitalProductIdJsonGet) | **GET** /products/{id}/digital_products/{digital_product_id}.json | Retrieve a single Product DigitalProduct.
[**productsIdDigitalProductsJsonGet**](ProductDigitalProductsApi.md#productsIdDigitalProductsJsonGet) | **GET** /products/{id}/digital_products.json | Retrieve all Product DigitalProducts.
[**productsIdDigitalProductsJsonPost**](ProductDigitalProductsApi.md#productsIdDigitalProductsJsonPost) | **POST** /products/{id}/digital_products.json | Create a new Product DigitalProduct.



## productsIdDigitalProductsCountJsonGet

> Count productsIdDigitalProductsCountJsonGet(login, authtoken, id)

Count all Product DigitalProducts.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductDigitalProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdDigitalProductsCountJsonGet(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| ID of the Product | 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdDigitalProductsDigitalProductIdJsonDelete

> String productsIdDigitalProductsDigitalProductIdJsonDelete(login, authtoken, id, digitalProductId)

Delete a Product DigitalProduct.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductDigitalProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let digitalProductId = 56; // Number | Id of the Product DigitalProduct
apiInstance.productsIdDigitalProductsDigitalProductIdJsonDelete(login, authtoken, id, digitalProductId, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Product | 
 **digitalProductId** | **Number**| Id of the Product DigitalProduct | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdDigitalProductsDigitalProductIdJsonGet

> DigitalProduct productsIdDigitalProductsDigitalProductIdJsonGet(login, authtoken, id, digitalProductId)

Retrieve a single Product DigitalProduct.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductDigitalProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let digitalProductId = 56; // Number | Id of the Product DigitalProduct
apiInstance.productsIdDigitalProductsDigitalProductIdJsonGet(login, authtoken, id, digitalProductId, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Product | 
 **digitalProductId** | **Number**| Id of the Product DigitalProduct | 

### Return type

[**DigitalProduct**](DigitalProduct.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdDigitalProductsJsonGet

> [DigitalProduct] productsIdDigitalProductsJsonGet(login, authtoken, id)

Retrieve all Product DigitalProducts.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductDigitalProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdDigitalProductsJsonGet(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| ID of the Product | 

### Return type

[**[DigitalProduct]**](DigitalProduct.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdDigitalProductsJsonPost

> DigitalProduct productsIdDigitalProductsJsonPost(login, authtoken, id, digitalProductEdit)

Create a new Product DigitalProduct.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductDigitalProductsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let digitalProductEdit = new JumpsellerApi.DigitalProductEdit(); // DigitalProductEdit | Product DigitalProduct parameters.
apiInstance.productsIdDigitalProductsJsonPost(login, authtoken, id, digitalProductEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the Product | 
 **digitalProductEdit** | [**DigitalProductEdit**](DigitalProductEdit.md)| Product DigitalProduct parameters. | 

### Return type

[**DigitalProduct**](DigitalProduct.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

