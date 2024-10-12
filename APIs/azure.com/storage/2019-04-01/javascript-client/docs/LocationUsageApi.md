# StorageManagementClient.LocationUsageApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usagesListByLocation**](LocationUsageApi.md#usagesListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Storage/locations/{location}/usages | 



## usagesListByLocation

> UsageListResult usagesListByLocation(apiVersion, subscriptionId, location)



Gets the current usage count and the limit for the resources of the location under the subscription.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.LocationUsageApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let location = "location_example"; // String | The location of the Azure Storage resource.
apiInstance.usagesListByLocation(apiVersion, subscriptionId, location, (error, data, response) => {
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
 **location** | **String**| The location of the Azure Storage resource. | 

### Return type

[**UsageListResult**](UsageListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

