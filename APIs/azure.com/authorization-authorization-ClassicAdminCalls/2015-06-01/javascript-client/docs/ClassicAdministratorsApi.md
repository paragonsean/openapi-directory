# AuthorizationManagementClient.ClassicAdministratorsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classicAdministratorsList**](ClassicAdministratorsApi.md#classicAdministratorsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/classicAdministrators | 



## classicAdministratorsList

> ClassicAdministratorListResult classicAdministratorsList(apiVersion, subscriptionId)



Gets service administrator, account administrator, and co-administrators for the subscription.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.ClassicAdministratorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.classicAdministratorsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ClassicAdministratorListResult**](ClassicAdministratorListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

