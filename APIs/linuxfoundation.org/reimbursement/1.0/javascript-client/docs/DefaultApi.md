# ReimbursementsApi.DefaultApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenseAction**](DefaultApi.md#expenseAction) | **POST** /expense/{action}/{reportId} | Expense Action
[**healthCheck**](DefaultApi.md#healthCheck) | **GET** /health | Get API Health Status
[**resetPolicy**](DefaultApi.md#resetPolicy) | **POST** /reset | Reset Policy
[**tagPolicy**](DefaultApi.md#tagPolicy) | **POST** /tag | Tag Policy



## expenseAction

> expenseAction(action, reportId)

Expense Action

approves or rejects expense report

### Example

```javascript
import ReimbursementsApi from 'reimbursements_api';
let defaultClient = ReimbursementsApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ReimbursementsApi.DefaultApi();
let action = "action_example"; // String | 
let reportId = "reportId_example"; // String | 
apiInstance.expenseAction(action, reportId, (error, data, response) => {
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
 **action** | **String**|  | 
 **reportId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## healthCheck

> Health healthCheck()

Get API Health Status

### Example

```javascript
import ReimbursementsApi from 'reimbursements_api';

let apiInstance = new ReimbursementsApi.DefaultApi();
apiInstance.healthCheck((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Health**](Health.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetPolicy

> resetPolicy(body)

Reset Policy

Reset an existing policy to match with templatePolicy

### Example

```javascript
import ReimbursementsApi from 'reimbursements_api';
let defaultClient = ReimbursementsApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ReimbursementsApi.DefaultApi();
let body = new ReimbursementsApi.PolicyResetInput(); // PolicyResetInput | 
apiInstance.resetPolicy(body, (error, data, response) => {
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
 **body** | [**PolicyResetInput**](PolicyResetInput.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagPolicy

> tagPolicy(body)

Tag Policy

Tag adds a tag to the policy

### Example

```javascript
import ReimbursementsApi from 'reimbursements_api';
let defaultClient = ReimbursementsApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ReimbursementsApi.DefaultApi();
let body = new ReimbursementsApi.PolicyTagInput(); // PolicyTagInput | 
apiInstance.tagPolicy(body, (error, data, response) => {
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
 **body** | [**PolicyTagInput**](PolicyTagInput.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

