# JumpsellerApi.ProductVariantsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsIdVariantsCountJsonGet**](ProductVariantsApi.md#productsIdVariantsCountJsonGet) | **GET** /products/{id}/variants/count.json | Count all Product Variants.
[**productsIdVariantsJsonGet**](ProductVariantsApi.md#productsIdVariantsJsonGet) | **GET** /products/{id}/variants.json | Retrieve all Product Variants.
[**productsIdVariantsJsonPost**](ProductVariantsApi.md#productsIdVariantsJsonPost) | **POST** /products/{id}/variants.json | Create a new Product Variant.
[**productsIdVariantsVariantIdJsonGet**](ProductVariantsApi.md#productsIdVariantsVariantIdJsonGet) | **GET** /products/{id}/variants/{variant_id}.json | Retrieve a single Product Variant.
[**productsIdVariantsVariantIdJsonPut**](ProductVariantsApi.md#productsIdVariantsVariantIdJsonPut) | **PUT** /products/{id}/variants/{variant_id}.json | Modify an existing Product Variant.



## productsIdVariantsCountJsonGet

> Count productsIdVariantsCountJsonGet(login, authtoken, id)

Count all Product Variants.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductVariantsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdVariantsCountJsonGet(login, authtoken, id, (error, data, response) => {
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


## productsIdVariantsJsonGet

> [Variant] productsIdVariantsJsonGet(login, authtoken, id)

Retrieve all Product Variants.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductVariantsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdVariantsJsonGet(login, authtoken, id, (error, data, response) => {
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

[**[Variant]**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdVariantsJsonPost

> Variant productsIdVariantsJsonPost(login, authtoken, id, variantEdit)

Create a new Product Variant.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductVariantsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let variantEdit = new JumpsellerApi.VariantEdit(); // VariantEdit | Product Variant parameters.
apiInstance.productsIdVariantsJsonPost(login, authtoken, id, variantEdit, (error, data, response) => {
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
 **variantEdit** | [**VariantEdit**](VariantEdit.md)| Product Variant parameters. | 

### Return type

[**Variant**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsIdVariantsVariantIdJsonGet

> Variant productsIdVariantsVariantIdJsonGet(login, authtoken, id, variantId)

Retrieve a single Product Variant.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductVariantsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let variantId = 56; // Number | Id of the Product Variant
apiInstance.productsIdVariantsVariantIdJsonGet(login, authtoken, id, variantId, (error, data, response) => {
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
 **variantId** | **Number**| Id of the Product Variant | 

### Return type

[**Variant**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdVariantsVariantIdJsonPut

> Variant productsIdVariantsVariantIdJsonPut(login, authtoken, id, variantId, variantEdit)

Modify an existing Product Variant.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductVariantsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let variantId = 56; // Number | Id of the Product Variant
let variantEdit = new JumpsellerApi.VariantEdit(); // VariantEdit | Product Variant parameters to change
apiInstance.productsIdVariantsVariantIdJsonPut(login, authtoken, id, variantId, variantEdit, (error, data, response) => {
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
 **variantId** | **Number**| Id of the Product Variant | 
 **variantEdit** | [**VariantEdit**](VariantEdit.md)| Product Variant parameters to change | 

### Return type

[**Variant**](Variant.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

