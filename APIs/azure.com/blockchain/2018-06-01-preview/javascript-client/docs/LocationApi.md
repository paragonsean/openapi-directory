# BlockchainManagementClient.LocationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationsCheckNameAvailability**](LocationApi.md#locationsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/locations/{locationName}/checkNameAvailability | 
[**locationsListConsortiums**](LocationApi.md#locationsListConsortiums) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/locations/{locationName}/listConsortiums | 



## locationsCheckNameAvailability

> NameAvailability locationsCheckNameAvailability(locationName, apiVersion, subscriptionId, opts)



To check whether a resource name is available.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.LocationApi();
let locationName = "locationName_example"; // String | Location Name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
let opts = {
  'nameAvailabilityRequest': new BlockchainManagementClient.NameAvailabilityRequest() // NameAvailabilityRequest | Name availability request payload.
};
apiInstance.locationsCheckNameAvailability(locationName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **locationName** | **String**| Location Name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 
 **nameAvailabilityRequest** | [**NameAvailabilityRequest**](NameAvailabilityRequest.md)| Name availability request payload. | [optional] 

### Return type

[**NameAvailability**](NameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## locationsListConsortiums

> ConsortiumCollection locationsListConsortiums(locationName, apiVersion, subscriptionId)



Lists the available consortiums for a subscription.

### Example

```javascript
import BlockchainManagementClient from 'blockchain_management_client';
let defaultClient = BlockchainManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlockchainManagementClient.LocationApi();
let locationName = "locationName_example"; // String | Location Name.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
apiInstance.locationsListConsortiums(locationName, apiVersion, subscriptionId, (error, data, response) => {
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
 **locationName** | **String**| Location Name. | 
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | 

### Return type

[**ConsortiumCollection**](ConsortiumCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

