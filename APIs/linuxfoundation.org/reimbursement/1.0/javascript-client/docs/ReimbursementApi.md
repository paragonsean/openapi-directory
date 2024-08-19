# ReimbursementsApi.ReimbursementApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createReimbursement**](ReimbursementApi.md#createReimbursement) | **POST** /reimbursement/{projectId} | Create Reimbursement
[**updateReimbursement**](ReimbursementApi.md#updateReimbursement) | **PATCH** /reimbursement/{projectId} | Update Reimbursement



## createReimbursement

> createReimbursement(projectId, body)

Create Reimbursement

Create a new Reimbursement policy

### Example

```javascript
import ReimbursementsApi from 'reimbursements_api';
let defaultClient = ReimbursementsApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ReimbursementsApi.ReimbursementApi();
let projectId = "projectId_example"; // String | 
let body = new ReimbursementsApi.CreateReimbursementRequest(); // CreateReimbursementRequest | 
apiInstance.createReimbursement(projectId, body, (error, data, response) => {
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
 **projectId** | **String**|  | 
 **body** | [**CreateReimbursementRequest**](CreateReimbursementRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateReimbursement

> updateReimbursement(projectId, body)

Update Reimbursement

Update an existing Reimbursement policy

### Example

```javascript
import ReimbursementsApi from 'reimbursements_api';
let defaultClient = ReimbursementsApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ReimbursementsApi.ReimbursementApi();
let projectId = "projectId_example"; // String | 
let body = new ReimbursementsApi.PolicyUpdateInput(); // PolicyUpdateInput | 
apiInstance.updateReimbursement(projectId, body, (error, data, response) => {
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
 **projectId** | **String**|  | 
 **body** | [**PolicyUpdateInput**](PolicyUpdateInput.md)|  | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

