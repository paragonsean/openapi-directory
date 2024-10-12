# FabricAdminClient.NetworkFabricOperationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkFabricOperationsGet**](NetworkFabricOperationsApi.md#networkFabricOperationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/System.{location}/providers/{provider}/fabricLocations/{location}/networkOperationResults/{networkOperationResult} | 



## networkFabricOperationsGet

> OperationStatus networkFabricOperationsGet(subscriptionId, location, provider, networkOperationResult, apiVersion)



Get the status of a network fabric operation.

### Example

```javascript
import FabricAdminClient from 'fabric_admin_client';
let defaultClient = FabricAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FabricAdminClient.NetworkFabricOperationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Location of the resource.
let provider = "provider_example"; // String | Name of the provider.
let networkOperationResult = "networkOperationResult_example"; // String | Id of a network fabric operation.
let apiVersion = "'2016-05-01'"; // String | Client Api Version.
apiInstance.networkFabricOperationsGet(subscriptionId, location, provider, networkOperationResult, apiVersion, (error, data, response) => {
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
 **networkOperationResult** | **String**| Id of a network fabric operation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-05-01&#39;]

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

