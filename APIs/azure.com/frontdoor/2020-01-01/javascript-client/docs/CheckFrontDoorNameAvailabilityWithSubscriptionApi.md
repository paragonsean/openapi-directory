# FrontDoorManagementClient.CheckFrontDoorNameAvailabilityWithSubscriptionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkFrontDoorNameAvailabilityWithSubscription**](CheckFrontDoorNameAvailabilityWithSubscriptionApi.md#checkFrontDoorNameAvailabilityWithSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Network/checkFrontDoorNameAvailability | 



## checkFrontDoorNameAvailabilityWithSubscription

> CheckNameAvailabilityOutput checkFrontDoorNameAvailabilityWithSubscription(subscriptionId, apiVersion, checkFrontDoorNameAvailabilityInput)



Check the availability of a Front Door subdomain.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.CheckFrontDoorNameAvailabilityWithSubscriptionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let checkFrontDoorNameAvailabilityInput = new FrontDoorManagementClient.CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
apiInstance.checkFrontDoorNameAvailabilityWithSubscription(subscriptionId, apiVersion, checkFrontDoorNameAvailabilityInput, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **checkFrontDoorNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check. | 

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

