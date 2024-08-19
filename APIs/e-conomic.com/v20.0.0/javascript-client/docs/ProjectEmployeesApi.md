# VismaEConomicOpenApi.ProjectEmployeesApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createProjectEmployee**](ProjectEmployeesApi.md#createProjectEmployee) | **POST** /project-employees | Create a single Project employee
[**deleteProjectEmployeeById**](ProjectEmployeesApi.md#deleteProjectEmployeeById) | **DELETE** /project-employees/{number} | Delete single Project employee
[**getAllProjectEmployees**](ProjectEmployeesApi.md#getAllProjectEmployees) | **GET** /project-employees | Retrieve all Project employees
[**getNumberOfProjectEmployees**](ProjectEmployeesApi.md#getNumberOfProjectEmployees) | **GET** /project-employees/count | Retrieve the number of Project employees
[**getPageOfProjectEmployees**](ProjectEmployeesApi.md#getPageOfProjectEmployees) | **GET** /project-employees/paged | Retrieve a page of Project employees
[**getProjectEmployeeById**](ProjectEmployeesApi.md#getProjectEmployeeById) | **GET** /project-employees/{number} | Retrieve single Project employee
[**updateProjectEmployee**](ProjectEmployeesApi.md#updateProjectEmployee) | **PUT** /project-employees | Update a single Project employee



## createProjectEmployee

> CreatedResult createProjectEmployee(opts)

Create a single Project employee

Use this endpoint to create a single Project employee.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeesApi();
let opts = {
  'projectEmployee': new VismaEConomicOpenApi.ProjectEmployee() // ProjectEmployee | 
};
apiInstance.createProjectEmployee(opts, (error, data, response) => {
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
 **projectEmployee** | [**ProjectEmployee**](ProjectEmployee.md)|  | [optional] 

### Return type

[**CreatedResult**](CreatedResult.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## deleteProjectEmployeeById

> deleteProjectEmployeeById(number)

Delete single Project employee

Use this endpoint to delete a single Project employee by id/number.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeesApi();
let number = 56; // Number | 
apiInstance.deleteProjectEmployeeById(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllProjectEmployees

> ProjectEmployeeCursorResults getAllProjectEmployees(opts)

Retrieve all Project employees

Use this endpoint to retrieve all Project employees in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeesApi();
let opts = {
  'cursor': "cursor_example", // String | 
  'filter': "filter_example" // String | 
};
apiInstance.getAllProjectEmployees(opts, (error, data, response) => {
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
 **cursor** | **String**|  | [optional] 
 **filter** | **String**|  | [optional] 

### Return type

[**ProjectEmployeeCursorResults**](ProjectEmployeeCursorResults.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumberOfProjectEmployees

> Number getNumberOfProjectEmployees(opts)

Retrieve the number of Project employees

Call this endpoint to get the number of Project employees. You can use a filtering as well.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeesApi();
let opts = {
  'filter': "filter_example" // String | 
};
apiInstance.getNumberOfProjectEmployees(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 

### Return type

**Number**

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPageOfProjectEmployees

> [ProjectEmployee] getPageOfProjectEmployees(opts)

Retrieve a page of Project employees

Use this endpoint to load a page of Project employees.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeesApi();
let opts = {
  'filter': "filter_example", // String | 
  'sort': "sort_example", // String | 
  'pageSize': 20, // Number | 
  'skipPages': 0 // Number | 
};
apiInstance.getPageOfProjectEmployees(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **pageSize** | **Number**|  | [optional] [default to 20]
 **skipPages** | **Number**|  | [optional] [default to 0]

### Return type

[**[ProjectEmployee]**](ProjectEmployee.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectEmployeeById

> ProjectEmployee getProjectEmployeeById(number)

Retrieve single Project employee

Use this endpoint to load a single Project employee by id/number.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeesApi();
let number = 56; // Number | 
apiInstance.getProjectEmployeeById(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

[**ProjectEmployee**](ProjectEmployee.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateProjectEmployee

> updateProjectEmployee(opts)

Update a single Project employee

Use this endpoint to update a single Project employee.

### Example

```javascript
import VismaEConomicOpenApi from 'visma_e_conomic_open_api';
let defaultClient = VismaEConomicOpenApi.ApiClient.instance;
// Configure API key authorization: X-AgreementGrantToken
let X-AgreementGrantToken = defaultClient.authentications['X-AgreementGrantToken'];
X-AgreementGrantToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AgreementGrantToken.apiKeyPrefix = 'Token';
// Configure API key authorization: X-AppSecretToken
let X-AppSecretToken = defaultClient.authentications['X-AppSecretToken'];
X-AppSecretToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-AppSecretToken.apiKeyPrefix = 'Token';

let apiInstance = new VismaEConomicOpenApi.ProjectEmployeesApi();
let opts = {
  'projectEmployee': new VismaEConomicOpenApi.ProjectEmployee() // ProjectEmployee | 
};
apiInstance.updateProjectEmployee(opts, (error, data, response) => {
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
 **projectEmployee** | [**ProjectEmployee**](ProjectEmployee.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

