# PeeringManagementClient.CheckServiceProviderAvailabilityApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkServiceProviderAvailability**](CheckServiceProviderAvailabilityApi.md#checkServiceProviderAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/CheckServiceProviderAvailability | 



## checkServiceProviderAvailability

> String checkServiceProviderAvailability(subscriptionId, apiVersion, checkServiceProviderAvailabilityInput)



Checks if the peering service provider is present within 1000 miles of customer&#39;s location

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.CheckServiceProviderAvailabilityApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let checkServiceProviderAvailabilityInput = new PeeringManagementClient.CheckServiceProviderAvailabilityInput(); // CheckServiceProviderAvailabilityInput | The CheckServiceProviderAvailabilityInput indicating customer location and service provider.
apiInstance.checkServiceProviderAvailability(subscriptionId, apiVersion, checkServiceProviderAvailabilityInput, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **checkServiceProviderAvailabilityInput** | [**CheckServiceProviderAvailabilityInput**](CheckServiceProviderAvailabilityInput.md)| The CheckServiceProviderAvailabilityInput indicating customer location and service provider. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

