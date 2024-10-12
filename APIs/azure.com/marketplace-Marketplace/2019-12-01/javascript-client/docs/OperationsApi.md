# MarketplaceRpService.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.Marketplace/operations | 



## operationsList

> OperationListResult operationsList(apiVersion)



Lists all of the available Microsoft.Marketplace REST API operations.

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
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
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

