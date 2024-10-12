# JumpsellerApi.ProductOptionValuesApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsIdOptionsOptionIdValuesCountJsonGet**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesCountJsonGet) | **GET** /products/{id}/options/{option_id}/values/count.json | Count all Product Option Values.
[**productsIdOptionsOptionIdValuesJsonGet**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesJsonGet) | **GET** /products/{id}/options/{option_id}/values.json | Retrieve all Product Option Values.
[**productsIdOptionsOptionIdValuesJsonPost**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesJsonPost) | **POST** /products/{id}/options/{option_id}/values.json | Create a new Product Option Value.
[**productsIdOptionsOptionIdValuesValueIdJsonDelete**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonDelete) | **DELETE** /products/{id}/options/{option_id}/values/{value_id}.json | Delete a Product Option Value.
[**productsIdOptionsOptionIdValuesValueIdJsonGet**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonGet) | **GET** /products/{id}/options/{option_id}/values/{value_id}.json | Retrieve a single Product Option Value.
[**productsIdOptionsOptionIdValuesValueIdJsonPut**](ProductOptionValuesApi.md#productsIdOptionsOptionIdValuesValueIdJsonPut) | **PUT** /products/{id}/options/{option_id}/values/{value_id}.json | Modify an existing Product Option Value.



## productsIdOptionsOptionIdValuesCountJsonGet

> Count productsIdOptionsOptionIdValuesCountJsonGet(login, authtoken, id, optionId)

Count all Product Option Values.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionValuesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
let optionId = 56; // Number | ID of the Product Option
apiInstance.productsIdOptionsOptionIdValuesCountJsonGet(login, authtoken, id, optionId, (error, data, response) => {
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
 **optionId** | **Number**| ID of the Product Option | 

### Return type

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdOptionsOptionIdValuesJsonGet

> [ProductOptionValue] productsIdOptionsOptionIdValuesJsonGet(login, authtoken, id, optionId)

Retrieve all Product Option Values.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionValuesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
let optionId = 56; // Number | ID of the Product Option
apiInstance.productsIdOptionsOptionIdValuesJsonGet(login, authtoken, id, optionId, (error, data, response) => {
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
 **optionId** | **Number**| ID of the Product Option | 

### Return type

[**[ProductOptionValue]**](ProductOptionValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdOptionsOptionIdValuesJsonPost

> ProductOptionValue productsIdOptionsOptionIdValuesJsonPost(login, authtoken, id, optionId, productOptionValueEdit)

Create a new Product Option Value.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionValuesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let optionId = 56; // Number | Id of the Product Option
let productOptionValueEdit = new JumpsellerApi.ProductOptionValueEdit(); // ProductOptionValueEdit | Product Option Value parameters.
apiInstance.productsIdOptionsOptionIdValuesJsonPost(login, authtoken, id, optionId, productOptionValueEdit, (error, data, response) => {
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
 **productOptionValueEdit** | [**ProductOptionValueEdit**](ProductOptionValueEdit.md)| Product Option Value parameters. | 

### Return type

[**ProductOptionValue**](ProductOptionValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsIdOptionsOptionIdValuesValueIdJsonDelete

> String productsIdOptionsOptionIdValuesValueIdJsonDelete(login, authtoken, id, optionId, valueId)

Delete a Product Option Value.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionValuesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let optionId = 56; // Number | Id of the Product Option
let valueId = 56; // Number | ID of the Product Option Value
apiInstance.productsIdOptionsOptionIdValuesValueIdJsonDelete(login, authtoken, id, optionId, valueId, (error, data, response) => {
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
 **valueId** | **Number**| ID of the Product Option Value | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdOptionsOptionIdValuesValueIdJsonGet

> ProductOptionValue productsIdOptionsOptionIdValuesValueIdJsonGet(login, authtoken, id, optionId, valueId)

Retrieve a single Product Option Value.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionValuesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let optionId = 56; // Number | Id of the Product Option
let valueId = 56; // Number | ID of the Product Option Value
apiInstance.productsIdOptionsOptionIdValuesValueIdJsonGet(login, authtoken, id, optionId, valueId, (error, data, response) => {
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
 **valueId** | **Number**| ID of the Product Option Value | 

### Return type

[**ProductOptionValue**](ProductOptionValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdOptionsOptionIdValuesValueIdJsonPut

> ProductOptionValue productsIdOptionsOptionIdValuesValueIdJsonPut(login, authtoken, id, optionId, valueId, productOptionValueEdit)

Modify an existing Product Option Value.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductOptionValuesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let optionId = 56; // Number | Id of the Product Option
let valueId = 56; // Number | Id of the Product Option Value
let productOptionValueEdit = new JumpsellerApi.ProductOptionValueEdit(); // ProductOptionValueEdit | Product option value parameters to change
apiInstance.productsIdOptionsOptionIdValuesValueIdJsonPut(login, authtoken, id, optionId, valueId, productOptionValueEdit, (error, data, response) => {
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
 **valueId** | **Number**| Id of the Product Option Value | 
 **productOptionValueEdit** | [**ProductOptionValueEdit**](ProductOptionValueEdit.md)| Product option value parameters to change | 

### Return type

[**ProductOptionValue**](ProductOptionValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

