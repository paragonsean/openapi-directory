# DataLakeStoreAccountManagementClient.LocationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsGetCapability**](LocationsApi.md#locationsGetCapability) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataLakeStore/locations/{location}/capability | 



## locationsGetCapability

> CapabilityInformation locationsGetCapability(subscriptionId, location, apiVersion)



Gets subscription-level properties and limits for Data Lake Store specified by resource location.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.LocationsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The resource location without whitespace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.locationsGetCapability(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The resource location without whitespace. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**CapabilityInformation**](CapabilityInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

