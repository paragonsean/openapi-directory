# JumpsellerApi.TaxesApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**taxesIdJsonGet**](TaxesApi.md#taxesIdJsonGet) | **GET** /taxes/{id}.json | Retrieve a single Tax information.
[**taxesJsonGet**](TaxesApi.md#taxesJsonGet) | **GET** /taxes.json | Retrieve all Taxes.
[**taxesJsonPost**](TaxesApi.md#taxesJsonPost) | **POST** /taxes.json | Create a new Tax.



## taxesIdJsonGet

> Tax taxesIdJsonGet(login, authtoken, id)

Retrieve a single Tax information.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.TaxesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Tax
apiInstance.taxesIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Tax | 

### Return type

[**Tax**](Tax.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taxesJsonGet

> [Tax] taxesJsonGet(login, authtoken)

Retrieve all Taxes.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.TaxesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.taxesJsonGet(login, authtoken, (error, data, response) => {
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

### Return type

[**[Tax]**](Tax.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## taxesJsonPost

> Tax taxesJsonPost(login, authtoken, taxEdit)

Create a new Tax.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.TaxesApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let taxEdit = new JumpsellerApi.TaxEdit(); // TaxEdit | Tax parameters.
apiInstance.taxesJsonPost(login, authtoken, taxEdit, (error, data, response) => {
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
 **taxEdit** | [**TaxEdit**](TaxEdit.md)| Tax parameters. | 

### Return type

[**Tax**](Tax.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

