# DynamicsTelemetry.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.DynamicsTelemetry/operations | 



## operationsList

> [Operation] operationsList()



### Example

```javascript
import DynamicsTelemetry from 'dynamics_telemetry';

let apiInstance = new DynamicsTelemetry.OperationsApi();
apiInstance.operationsList((error, data, response) => {
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

[**[Operation]**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

