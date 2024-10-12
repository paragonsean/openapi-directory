# PeeringManagementClient.PeeringRegisteredAsnsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registeredAsnsCreateOrUpdate**](PeeringRegisteredAsnsApi.md#registeredAsnsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredAsns/{registeredAsnName} | 
[**registeredAsnsDelete**](PeeringRegisteredAsnsApi.md#registeredAsnsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredAsns/{registeredAsnName} | 
[**registeredAsnsGet**](PeeringRegisteredAsnsApi.md#registeredAsnsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredAsns/{registeredAsnName} | 
[**registeredAsnsListByPeering**](PeeringRegisteredAsnsApi.md#registeredAsnsListByPeering) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName}/registeredAsns | 



## registeredAsnsCreateOrUpdate

> PeeringRegisteredAsn registeredAsnsCreateOrUpdate(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion, registeredAsn)



Creates a new registered ASN with the specified name under the given subscription, resource group and peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringRegisteredAsnsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let registeredAsnName = "registeredAsnName_example"; // String | The name of the ASN.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let registeredAsn = new PeeringManagementClient.PeeringRegisteredAsn(); // PeeringRegisteredAsn | The properties needed to create a registered ASN.
apiInstance.registeredAsnsCreateOrUpdate(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion, registeredAsn, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **peeringName** | **String**| The name of the peering. | 
 **registeredAsnName** | **String**| The name of the ASN. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **registeredAsn** | [**PeeringRegisteredAsn**](PeeringRegisteredAsn.md)| The properties needed to create a registered ASN. | 

### Return type

[**PeeringRegisteredAsn**](PeeringRegisteredAsn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registeredAsnsDelete

> registeredAsnsDelete(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion)



Deletes an existing registered ASN with the specified name under the given subscription, resource group and peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringRegisteredAsnsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let registeredAsnName = "registeredAsnName_example"; // String | The name of the registered ASN.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.registeredAsnsDelete(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The name of the resource group. | 
 **peeringName** | **String**| The name of the peering. | 
 **registeredAsnName** | **String**| The name of the registered ASN. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registeredAsnsGet

> PeeringRegisteredAsn registeredAsnsGet(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion)



Gets an existing registered ASN with the specified name under the given subscription, resource group and peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringRegisteredAsnsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let registeredAsnName = "registeredAsnName_example"; // String | The name of the registered ASN.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.registeredAsnsGet(resourceGroupName, peeringName, registeredAsnName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **peeringName** | **String**| The name of the peering. | 
 **registeredAsnName** | **String**| The name of the registered ASN. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeeringRegisteredAsn**](PeeringRegisteredAsn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## registeredAsnsListByPeering

> PeeringRegisteredAsnListResult registeredAsnsListByPeering(resourceGroupName, peeringName, subscriptionId, apiVersion)



Lists all registered ASNs under the given subscription, resource group and peering.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringRegisteredAsnsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.registeredAsnsListByPeering(resourceGroupName, peeringName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **peeringName** | **String**| The name of the peering. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeeringRegisteredAsnListResult**](PeeringRegisteredAsnListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

