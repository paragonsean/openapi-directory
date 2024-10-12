# JumpsellerApi.CustomerAdditionalFieldsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customersIdFieldsFieldIdDelete**](CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdDelete) | **DELETE** /customers/{id}/fields/{field_id} | Delete a Customer Additional Field.
[**customersIdFieldsFieldIdGet**](CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdGet) | **GET** /customers/{id}/fields/{field_id} | Retrieve a single Customer Additional Field.
[**customersIdFieldsFieldIdPut**](CustomerAdditionalFieldsApi.md#customersIdFieldsFieldIdPut) | **PUT** /customers/{id}/fields/{field_id} | Update a Customer Additional Field.
[**customersIdFieldsGet**](CustomerAdditionalFieldsApi.md#customersIdFieldsGet) | **GET** /customers/{id}/fields | Retrieves the Customer Additional Field of a Customer.
[**customersIdFieldsPost**](CustomerAdditionalFieldsApi.md#customersIdFieldsPost) | **POST** /customers/{id}/fields | Adds Customer Additional Fields to a Customer.



## customersIdFieldsFieldIdDelete

> String customersIdFieldsFieldIdDelete(login, authtoken, id, fieldId)

Delete a Customer Additional Field.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerAdditionalFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Customer
let fieldId = 56; // Number | Id of the Customer Additional Field
apiInstance.customersIdFieldsFieldIdDelete(login, authtoken, id, fieldId, (error, data, response) => {
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
 **id** | **Number**| Id of the Customer | 
 **fieldId** | **Number**| Id of the Customer Additional Field | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersIdFieldsFieldIdGet

> CustomerAdditionalField customersIdFieldsFieldIdGet(login, authtoken, id, fieldId)

Retrieve a single Customer Additional Field.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerAdditionalFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Customer
let fieldId = 56; // Number | Id of the Customer Additional Field
apiInstance.customersIdFieldsFieldIdGet(login, authtoken, id, fieldId, (error, data, response) => {
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
 **id** | **Number**| Id of the Customer | 
 **fieldId** | **Number**| Id of the Customer Additional Field | 

### Return type

[**CustomerAdditionalField**](CustomerAdditionalField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersIdFieldsFieldIdPut

> CustomerAdditionalField customersIdFieldsFieldIdPut(login, authtoken, id, fieldId, customerAdditionalFieldEdit)

Update a Customer Additional Field.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerAdditionalFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Customer
let fieldId = 56; // Number | Id of the Customer Additional Field
let customerAdditionalFieldEdit = new JumpsellerApi.CustomerAdditionalFieldEdit(); // CustomerAdditionalFieldEdit | Customer Additional Field parameters.
apiInstance.customersIdFieldsFieldIdPut(login, authtoken, id, fieldId, customerAdditionalFieldEdit, (error, data, response) => {
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
 **id** | **Number**| Id of the Customer | 
 **fieldId** | **Number**| Id of the Customer Additional Field | 
 **customerAdditionalFieldEdit** | [**CustomerAdditionalFieldEdit**](CustomerAdditionalFieldEdit.md)| Customer Additional Field parameters. | 

### Return type

[**CustomerAdditionalField**](CustomerAdditionalField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customersIdFieldsGet

> [CustomerAdditionalField] customersIdFieldsGet(login, authtoken, id)

Retrieves the Customer Additional Field of a Customer.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerAdditionalFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Customer
apiInstance.customersIdFieldsGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Customer | 

### Return type

[**[CustomerAdditionalField]**](CustomerAdditionalField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customersIdFieldsPost

> CustomerAdditionalField customersIdFieldsPost(login, authtoken, id, customerAdditionalFieldEdit)

Adds Customer Additional Fields to a Customer.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomerAdditionalFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Customer
let customerAdditionalFieldEdit = new JumpsellerApi.CustomerAdditionalFieldEdit(); // CustomerAdditionalFieldEdit | Customer Additional Field parameters.
apiInstance.customersIdFieldsPost(login, authtoken, id, customerAdditionalFieldEdit, (error, data, response) => {
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
 **id** | **Number**| Id of the Customer | 
 **customerAdditionalFieldEdit** | [**CustomerAdditionalFieldEdit**](CustomerAdditionalFieldEdit.md)| Customer Additional Field parameters. | 

### Return type

[**CustomerAdditionalField**](CustomerAdditionalField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

