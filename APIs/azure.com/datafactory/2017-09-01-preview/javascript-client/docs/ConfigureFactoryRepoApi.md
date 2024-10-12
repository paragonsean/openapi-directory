# DataFactoryManagementClient.ConfigureFactoryRepoApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**factoriesConfigureFactoryRepo**](ConfigureFactoryRepoApi.md#factoriesConfigureFactoryRepo) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/configureFactoryRepo | 



## factoriesConfigureFactoryRepo

> Factory factoriesConfigureFactoryRepo(subscriptionId, locationId, apiVersion, factoryRepoUpdate)



Updates a factory&#39;s repo information.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.ConfigureFactoryRepoApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let locationId = "locationId_example"; // String | The location identifier.
let apiVersion = "apiVersion_example"; // String | The API version.
let factoryRepoUpdate = new DataFactoryManagementClient.FactoryRepoUpdate(); // FactoryRepoUpdate | Update factory repo request definition.
apiInstance.factoriesConfigureFactoryRepo(subscriptionId, locationId, apiVersion, factoryRepoUpdate, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **locationId** | **String**| The location identifier. | 
 **apiVersion** | **String**| The API version. | 
 **factoryRepoUpdate** | [**FactoryRepoUpdate**](FactoryRepoUpdate.md)| Update factory repo request definition. | 

### Return type

[**Factory**](Factory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

