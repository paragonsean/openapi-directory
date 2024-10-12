# BlockchainManagementClient.OperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](OperationApi.md#operationsList) | **GET** /providers/Microsoft.Blockchain/operations | 



## operationsList

> ResourceProviderOperationCollection operationsList(apiVersion)



Lists the available operations of Microsoft.Blockchain resource provider.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.OperationApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
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
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**ResourceProviderOperationCollection**](ResourceProviderOperationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

