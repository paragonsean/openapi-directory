# AzureBotService.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.BotService/operations | 



## operationsList

> OperationEntityListResult operationsList(apiVersion)



Lists all the available BotService operations.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.OperationsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 

### Return type

[**OperationEntityListResult**](OperationEntityListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

