# JumpsellerApi.ProductCustomFieldsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsIdFieldsCountJsonGet**](ProductCustomFieldsApi.md#productsIdFieldsCountJsonGet) | **GET** /products/{id}/fields/count.json | Count all Product Custom Fields.
[**productsIdFieldsJsonGet**](ProductCustomFieldsApi.md#productsIdFieldsJsonGet) | **GET** /products/{id}/fields.json | Retrieve all Product Custom Fields
[**productsIdFieldsJsonPost**](ProductCustomFieldsApi.md#productsIdFieldsJsonPost) | **POST** /products/{id}/fields.json | Add an existing Custom Field to a Product.
[**productsProductIdFieldsFieldIdJsonDelete**](ProductCustomFieldsApi.md#productsProductIdFieldsFieldIdJsonDelete) | **DELETE** /products/{product_id}/fields/{field_id}.json | Delete value of Product Custom Field
[**productsProductIdFieldsFieldIdJsonPut**](ProductCustomFieldsApi.md#productsProductIdFieldsFieldIdJsonPut) | **PUT** /products/{product_id}/fields/{field_id}.json | Update value of Product Custom Field



## productsIdFieldsCountJsonGet

> Count productsIdFieldsCountJsonGet(login, authtoken, id)

Count all Product Custom Fields.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | ID of the Product
apiInstance.productsIdFieldsCountJsonGet(login, authtoken, id, (error, data, response) => {
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


## productsIdFieldsJsonGet

> [ProductCustomField] productsIdFieldsJsonGet(login, authtoken, id)

Retrieve all Product Custom Fields

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
apiInstance.productsIdFieldsJsonGet(login, authtoken, id, (error, data, response) => {
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

### Return type

[**[ProductCustomField]**](ProductCustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsIdFieldsJsonPost

> Product productsIdFieldsJsonPost(login, authtoken, id, addProductCustomField)

Add an existing Custom Field to a Product.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Product
let addProductCustomField = new JumpsellerApi.AddProductCustomField(); // AddProductCustomField | Product Custom Field parameters.
apiInstance.productsIdFieldsJsonPost(login, authtoken, id, addProductCustomField, (error, data, response) => {
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
 **addProductCustomField** | [**AddProductCustomField**](AddProductCustomField.md)| Product Custom Field parameters. | 

### Return type

[**Product**](Product.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsProductIdFieldsFieldIdJsonDelete

> MessageObject productsProductIdFieldsFieldIdJsonDelete(login, authtoken, productId, fieldId)

Delete value of Product Custom Field

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let productId = 56; // Number | Id of the Product.
let fieldId = 56; // Number | Id of the Custom Field Value.
apiInstance.productsProductIdFieldsFieldIdJsonDelete(login, authtoken, productId, fieldId, (error, data, response) => {
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
 **productId** | **Number**| Id of the Product. | 
 **fieldId** | **Number**| Id of the Custom Field Value. | 

### Return type

[**MessageObject**](MessageObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsProductIdFieldsFieldIdJsonPut

> ProductCustomField productsProductIdFieldsFieldIdJsonPut(login, authtoken, productId, fieldId)

Update value of Product Custom Field

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ProductCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let productId = 56; // Number | Id of the Product.
let fieldId = 56; // Number | Id of the Custom Field Value.
apiInstance.productsProductIdFieldsFieldIdJsonPut(login, authtoken, productId, fieldId, (error, data, response) => {
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
 **productId** | **Number**| Id of the Product. | 
 **fieldId** | **Number**| Id of the Custom Field Value. | 

### Return type

[**ProductCustomField**](ProductCustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

