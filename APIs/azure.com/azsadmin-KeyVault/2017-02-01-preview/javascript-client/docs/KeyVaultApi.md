# KeyVaultManagementClient.KeyVaultApi

All URIs are relative to *https://management.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](KeyVaultApi.md#operationsList) | **GET** /providers/Microsoft.KeyVault.Admin/operations | 



## operationsList

> OperationList operationsList(apiVersion)



Get the list of support rest operations.

### Example

```javascript
import KeyVaultManagementClient from 'key_vault_management_client';
let defaultClient = KeyVaultManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new KeyVaultManagementClient.KeyVaultApi();
let apiVersion = "'2017-02-01-preview'"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2017-02-01-preview&#39;]

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

