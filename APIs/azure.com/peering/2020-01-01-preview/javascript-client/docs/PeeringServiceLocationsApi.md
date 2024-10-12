# PeeringManagementClient.PeeringServiceLocationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peeringServiceLocationsList**](PeeringServiceLocationsApi.md#peeringServiceLocationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peeringServiceLocations | 



## peeringServiceLocationsList

> PeeringServiceLocationListResult peeringServiceLocationsList(subscriptionId, apiVersion, opts)



Lists all of the available locations for peering service.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServiceLocationsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'country': "country_example" // String | The country of interest, in which the locations are to be present.
};
apiInstance.peeringServiceLocationsList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **country** | **String**| The country of interest, in which the locations are to be present. | [optional] 

### Return type

[**PeeringServiceLocationListResult**](PeeringServiceLocationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

