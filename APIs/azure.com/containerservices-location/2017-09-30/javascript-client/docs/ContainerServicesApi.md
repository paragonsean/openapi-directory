# ContainerServiceClient.ContainerServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**containerServicesListOrchestrators**](ContainerServicesApi.md#containerServicesListOrchestrators) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerService/locations/{location}/orchestrators | Gets a list of supported orchestrators in the specified subscription.



## containerServicesListOrchestrators

> OrchestratorVersionProfileListResult containerServicesListOrchestrators(apiVersion, subscriptionId, location, opts)

Gets a list of supported orchestrators in the specified subscription.

Gets a list of supported orchestrators in the specified subscription. The operation returns properties of each orchestrator including version and available upgrades.

### Example

```javascript
import ContainerServiceClient from 'container_service_client';
let defaultClient = ContainerServiceClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerServiceClient.ContainerServicesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The name of a supported Azure region.
let opts = {
  'resourceType': "resourceType_example" // String | resource type for which the list of orchestrators needs to be returned
};
apiInstance.containerServicesListOrchestrators(apiVersion, subscriptionId, location, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The name of a supported Azure region. | 
 **resourceType** | **String**| resource type for which the list of orchestrators needs to be returned | [optional] 

### Return type

[**OrchestratorVersionProfileListResult**](OrchestratorVersionProfileListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

