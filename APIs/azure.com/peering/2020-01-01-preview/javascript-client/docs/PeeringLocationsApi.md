# PeeringManagementClient.PeeringLocationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peeringLocationsList**](PeeringLocationsApi.md#peeringLocationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peeringLocations | 



## peeringLocationsList

> PeeringLocationListResult peeringLocationsList(kind, subscriptionId, apiVersion, opts)



Lists all of the available peering locations for the specified kind of peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringLocationsApi();
let kind = "kind_example"; // String | The kind of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'directPeeringType': "directPeeringType_example" // String | The type of direct peering.
};
apiInstance.peeringLocationsList(kind, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **kind** | **String**| The kind of the peering. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **directPeeringType** | **String**| The type of direct peering. | [optional] 

### Return type

[**PeeringLocationListResult**](PeeringLocationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

