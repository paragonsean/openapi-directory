# AzureReservation.OperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationList**](OperationApi.md#operationList) | **GET** /providers/Microsoft.Capacity/operations | Get operations.



## operationList

> OperationList operationList(apiVersion)

Get operations.

List all the operations.

### Example

```javascript
import AzureReservation from 'azure_reservation';

let apiInstance = new AzureReservation.OperationApi();
let apiVersion = "apiVersion_example"; // String | Supported version.
apiInstance.operationList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Supported version. | 

### Return type

[**OperationList**](OperationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

