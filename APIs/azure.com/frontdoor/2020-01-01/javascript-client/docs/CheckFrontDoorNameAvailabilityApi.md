# FrontDoorManagementClient.CheckFrontDoorNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkFrontDoorNameAvailability**](CheckFrontDoorNameAvailabilityApi.md#checkFrontDoorNameAvailability) | **POST** /providers/Microsoft.Network/checkFrontDoorNameAvailability | 



## checkFrontDoorNameAvailability

> CheckNameAvailabilityOutput checkFrontDoorNameAvailability(apiVersion, checkFrontDoorNameAvailabilityInput)



Check the availability of a Front Door resource name.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.CheckFrontDoorNameAvailabilityApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let checkFrontDoorNameAvailabilityInput = new FrontDoorManagementClient.CheckNameAvailabilityInput(); // CheckNameAvailabilityInput | Input to check.
apiInstance.checkFrontDoorNameAvailability(apiVersion, checkFrontDoorNameAvailabilityInput, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **checkFrontDoorNameAvailabilityInput** | [**CheckNameAvailabilityInput**](CheckNameAvailabilityInput.md)| Input to check. | 

### Return type

[**CheckNameAvailabilityOutput**](CheckNameAvailabilityOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

