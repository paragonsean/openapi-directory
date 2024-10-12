# PeeringManagementClient.PeeringsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peeringsCreateOrUpdate**](PeeringsApi.md#peeringsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName} | 
[**peeringsDelete**](PeeringsApi.md#peeringsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName} | 
[**peeringsGet**](PeeringsApi.md#peeringsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName} | 
[**peeringsListByResourceGroup**](PeeringsApi.md#peeringsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings | 
[**peeringsListBySubscription**](PeeringsApi.md#peeringsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peerings | 
[**peeringsUpdate**](PeeringsApi.md#peeringsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peerings/{peeringName} | 



## peeringsCreateOrUpdate

> Peering peeringsCreateOrUpdate(resourceGroupName, peeringName, subscriptionId, apiVersion, peering)



Creates a new peering or updates an existing peering with the specified name under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let peering = new PeeringManagementClient.Peering(); // Peering | The properties needed to create or update a peering.
apiInstance.peeringsCreateOrUpdate(resourceGroupName, peeringName, subscriptionId, apiVersion, peering, (error, data, response) => {
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
 **peering** | [**Peering**](Peering.md)| The properties needed to create or update a peering. | 

### Return type

[**Peering**](Peering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## peeringsDelete

> peeringsDelete(resourceGroupName, peeringName, subscriptionId, apiVersion)



Deletes an existing peering with the specified name under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringsDelete(resourceGroupName, peeringName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringsGet

> Peering peeringsGet(resourceGroupName, peeringName, subscriptionId, apiVersion)



Gets an existing peering with the specified name under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringsGet(resourceGroupName, peeringName, subscriptionId, apiVersion, (error, data, response) => {
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

[**Peering**](Peering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringsListByResourceGroup

> PeeringListResult peeringsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Lists all of the peerings under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeeringListResult**](PeeringListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringsListBySubscription

> PeeringListResult peeringsListBySubscription(subscriptionId, apiVersion)



Lists all of the peerings under the given subscription.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringsApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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

[**PeeringListResult**](PeeringListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringsUpdate

> Peering peeringsUpdate(resourceGroupName, peeringName, subscriptionId, apiVersion, tags)



Updates tags for a peering with the specified name under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringName = "peeringName_example"; // String | The name of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let tags = new PeeringManagementClient.ResourceTags(); // ResourceTags | The resource tags.
apiInstance.peeringsUpdate(resourceGroupName, peeringName, subscriptionId, apiVersion, tags, (error, data, response) => {
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
 **tags** | [**ResourceTags**](ResourceTags.md)| The resource tags. | 

### Return type

[**Peering**](Peering.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

