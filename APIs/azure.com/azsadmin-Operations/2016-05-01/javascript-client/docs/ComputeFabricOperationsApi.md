# FabricAdminClient.ComputeFabricOperationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**computeFabricOperationsGet**](ComputeFabricOperationsApi.md#computeFabricOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/System.{location}/providers/{provider}/fabricLocations/{location}/computeOperationResults/{computeOperationResult} | 



## computeFabricOperationsGet

> OperationStatus computeFabricOperationsGet(subscriptionId, location, provider, computeOperationResult, apiVersion)



Get the status of a compute fabric operation.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.ComputeFabricOperationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let provider = "provider_example"; // String | Name of the provider.
let computeOperationResult = "computeOperationResult_example"; // String | Id of a compute fabric operation.
let apiVersion = "'2016-05-01'"; // String | Client Api Version.
apiInstance.computeFabricOperationsGet(subscriptionId, location, provider, computeOperationResult, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Location of the resource. | 
 **provider** | **String**| Name of the provider. | 
 **computeOperationResult** | **String**| Id of a compute fabric operation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

