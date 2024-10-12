# EngagementFabric.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.EngagementFabric/operations | List operation of EngagementFabric resources



## operationsList

> OperationList operationsList(apiVersion)

List operation of EngagementFabric resources

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.OperationsApi();
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API version | 

### Return type

[**OperationList**](OperationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

