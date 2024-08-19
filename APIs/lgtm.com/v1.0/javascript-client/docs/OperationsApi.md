# LgtmApiSpecification.OperationsApi

All URIs are relative to *https://lgtm.com/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOperation**](OperationsApi.md#getOperation) | **GET** /operations/{operation-id} | Get operation status



## getOperation

> Operation getOperation(operationId)

Get operation status

Track progress of a long-running operation using the operations identifier returned when you  created the operation. For example, by triggering the analysis of a commit, or the code review of a patch. For both LGTM.com and LGTM Enterprise, you must include an access token with the &#x60;operations:read&#x60; scope. 

### Example

```javascript
import LgtmApiSpecification from 'lgtm_api_specification';
let defaultClient = LgtmApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: access-token
let access-token = defaultClient.authentications['access-token'];
access-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new LgtmApiSpecification.OperationsApi();
let operationId = 789; // Number | The operation identifier returned on creating the task.
apiInstance.getOperation(operationId, (error, data, response) => {
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
 **operationId** | **Number**| The operation identifier returned on creating the task. | 

### Return type

[**Operation**](Operation.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

