# RecoveryServicesClient.RecoveryServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recoveryServicesCheckNameAvailability**](RecoveryServicesApi.md#recoveryServicesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/locations/{location}/checkNameAvailability | API to check for resource name availability.  A name is available if no other resource exists that has the same SubscriptionId, Resource Name and Type  or if one or more such resources exist, each of these must be GC&#39;d and their time of deletion be more than 24 Hours Ago



## recoveryServicesCheckNameAvailability

> CheckNameAvailabilityResultResource recoveryServicesCheckNameAvailability(subscriptionId, resourceGroupName, apiVersion, location, input)

API to check for resource name availability.  A name is available if no other resource exists that has the same SubscriptionId, Resource Name and Type  or if one or more such resources exist, each of these must be GC&#39;d and their time of deletion be more than 24 Hours Ago

### Example

```javascript
import RecoveryServicesClient from 'recovery_services_client';
let defaultClient = RecoveryServicesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesClient.RecoveryServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let location = "location_example"; // String | Location of the resource
let input = new RecoveryServicesClient.CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | Contains information about Resource type and Resource name
apiInstance.recoveryServicesCheckNameAvailability(subscriptionId, resourceGroupName, apiVersion, location, input, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **apiVersion** | **String**| Client Api Version. | 
 **location** | **String**| Location of the resource | 
 **input** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| Contains information about Resource type and Resource name | 

### Return type

[**CheckNameAvailabilityResultResource**](CheckNameAvailabilityResultResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

