# PeeringManagementClient.PeerAsnsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peerAsnsCreateOrUpdate**](PeerAsnsApi.md#peerAsnsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerAsns/{peerAsnName} | 
[**peerAsnsDelete**](PeerAsnsApi.md#peerAsnsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerAsns/{peerAsnName} | 
[**peerAsnsGet**](PeerAsnsApi.md#peerAsnsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerAsns/{peerAsnName} | 
[**peerAsnsListBySubscription**](PeerAsnsApi.md#peerAsnsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerAsns | 



## peerAsnsCreateOrUpdate

> PeerAsn peerAsnsCreateOrUpdate(peerAsnName, subscriptionId, apiVersion, peerAsn)



Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subscription.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeerAsnsApi();
let peerAsnName = "peerAsnName_example"; // String | The peer ASN name.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let peerAsn = new PeeringManagementClient.PeerAsn(); // PeerAsn | The peer ASN.
apiInstance.peerAsnsCreateOrUpdate(peerAsnName, subscriptionId, apiVersion, peerAsn, (error, data, response) => {
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
 **peerAsnName** | **String**| The peer ASN name. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **peerAsn** | [**PeerAsn**](PeerAsn.md)| The peer ASN. | 

### Return type

[**PeerAsn**](PeerAsn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## peerAsnsDelete

> peerAsnsDelete(peerAsnName, subscriptionId, apiVersion)



Deletes an existing peer ASN with the specified name under the given subscription.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeerAsnsApi();
let peerAsnName = "peerAsnName_example"; // String | The peer ASN name.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peerAsnsDelete(peerAsnName, subscriptionId, apiVersion, (error, data, response) => {
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
 **peerAsnName** | **String**| The peer ASN name. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peerAsnsGet

> PeerAsn peerAsnsGet(peerAsnName, subscriptionId, apiVersion)



Gets the peer ASN with the specified name under the given subscription.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeerAsnsApi();
let peerAsnName = "peerAsnName_example"; // String | The peer ASN name.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peerAsnsGet(peerAsnName, subscriptionId, apiVersion, (error, data, response) => {
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
 **peerAsnName** | **String**| The peer ASN name. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeerAsn**](PeerAsn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peerAsnsListBySubscription

> PeerAsnListResult peerAsnsListBySubscription(subscriptionId, apiVersion)



Lists all of the peer ASNs under the given subscription.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeerAsnsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peerAsnsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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

### Return type

[**PeerAsnListResult**](PeerAsnListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

