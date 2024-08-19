# JumpsellerApi.ProductOptionsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsIdOptionsCountJsonGet**](ProductOptionsApi.md#productsIdOptionsCountJsonGet) | **GET** /products/{id}/options/count.json | Count all Product Options.
[**productsIdOptionsJsonGet**](ProductOptionsApi.md#productsIdOptionsJsonGet) | **GET** /products/{id}/options.json | Retrieve all Product Options.
[**productsIdOptionsJsonPost**](ProductOptionsApi.md#productsIdOptionsJsonPost) | **POST** /products/{id}/options.json | Create a new Product Option.
[**productsIdOptionsOptionIdJsonDelete**](ProductOptionsApi.md#productsIdOptionsOptionIdJsonDelete) | **DELETE** /products/{id}/options/{option_id}.json | Delete a Product Option.
[**productsIdOptionsOptionIdJsonGet**](ProductOptionsApi.md#productsIdOptionsOptionIdJsonGet) | **GET** /products/{id}/options/{option_id}.json | Retrieve a single Product Option.
[**productsIdOptionsOptionIdJsonPut**](ProductOptionsApi.md#productsIdOptionsOptionIdJsonPut) | **PUT** /products/{id}/options/{option_id}.json | Modify an existing Product Option.



## productsIdOptionsCountJsonGet

> Count productsIdOptionsCountJsonGet(login, authtoken, id)

Count all Product Options.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdOptionsCountJsonGet(login, authtoken, id, (error, data, response) => {
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


## productsIdOptionsJsonGet

> [ProductOption] productsIdOptionsJsonGet(login, authtoken, id)

Retrieve all Product Options.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdOptionsJsonGet(login, authtoken, id, (error, data, response) => {
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

[**[ProductOption]**](ProductOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdOptionsJsonPost

> ProductOption productsIdOptionsJsonPost(login, authtoken, id, productOptionEdit)

Create a new Product Option.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let productOptionEdit = new JumpsellerApi.ProductOptionEdit(); // ProductOptionEdit | Product Option parameters.
apiInstance.productsIdOptionsJsonPost(login, authtoken, id, productOptionEdit, (error, data, response) => {
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
 **productOptionEdit** | [**ProductOptionEdit**](ProductOptionEdit.md)| Product Option parameters. | 

### Return type

[**ProductOption**](ProductOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsIdOptionsOptionIdJsonDelete

> String productsIdOptionsOptionIdJsonDelete(login, authtoken, id, optionId)

Delete a Product Option.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let optionId = 56; // Number | Id of the Product Option
apiInstance.productsIdOptionsOptionIdJsonDelete(login, authtoken, id, optionId, (error, data, response) => {
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
 **optionId** | **Number**| Id of the Product Option | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdOptionsOptionIdJsonGet

> ProductOption productsIdOptionsOptionIdJsonGet(login, authtoken, id, optionId)

Retrieve a single Product Option.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let optionId = 56; // Number | Id of the Product Option
apiInstance.productsIdOptionsOptionIdJsonGet(login, authtoken, id, optionId, (error, data, response) => {
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
 **optionId** | **Number**| Id of the Product Option | 

### Return type

[**ProductOption**](ProductOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdOptionsOptionIdJsonPut

> ProductOption productsIdOptionsOptionIdJsonPut(login, authtoken, id, optionId, productOptionEdit)

Modify an existing Product Option.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let optionId = 56; // Number | Id of the Product Option
let productOptionEdit = new JumpsellerApi.ProductOptionEdit(); // ProductOptionEdit | Product option parameters to change
apiInstance.productsIdOptionsOptionIdJsonPut(login, authtoken, id, optionId, productOptionEdit, (error, data, response) => {
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
 **optionId** | **Number**| Id of the Product Option | 
 **productOptionEdit** | [**ProductOptionEdit**](ProductOptionEdit.md)| Product option parameters to change | 

### Return type

[**ProductOption**](ProductOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

