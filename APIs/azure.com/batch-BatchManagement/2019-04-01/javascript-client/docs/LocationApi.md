# BatchManagement.LocationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationGetQuotas**](LocationApi.md#locationGetQuotas) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Batch/locations/{locationName}/quotas | 



## locationGetQuotas

> BatchLocationQuota locationGetQuotas(locationName, apiVersion, subscriptionId)



Gets the Batch service quotas for the specified subscription at the given location.

### Example

```javascript
import BatchManagement from 'batch_management';
let defaultClient = BatchManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BatchManagement.LocationApi();
let locationName = "locationName_example"; // String | The region for which to retrieve Batch service quotas.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
apiInstance.locationGetQuotas(locationName, apiVersion, subscriptionId, (error, data, response) => {
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
 **locationName** | **String**| The region for which to retrieve Batch service quotas. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **subscriptionId** | **String**| The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000) | 

### Return type

[**BatchLocationQuota**](BatchLocationQuota.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

