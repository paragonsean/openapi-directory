# AzureDigitalTwinsManagementClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.DigitalTwins/operations | 



## operationsList

> OperationListResult operationsList(apiVersion)



Lists all of the available DigitalTwins service REST API operations.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.OperationsApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

