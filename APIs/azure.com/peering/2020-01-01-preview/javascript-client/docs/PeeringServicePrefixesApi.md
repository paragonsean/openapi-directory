# PeeringManagementClient.PeeringServicePrefixesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prefixesCreateOrUpdate**](PeeringServicePrefixesApi.md#prefixesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} | 
[**prefixesDelete**](PeeringServicePrefixesApi.md#prefixesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} | 
[**prefixesGet**](PeeringServicePrefixesApi.md#prefixesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} | 
[**prefixesListByPeeringService**](PeeringServicePrefixesApi.md#prefixesListByPeeringService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes | 



## prefixesCreateOrUpdate

> PeeringServicePrefix prefixesCreateOrUpdate(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, peeringServicePrefix)



Creates a new prefix with the specified name under the given subscription, resource group and peering service.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicePrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
let prefixName = "prefixName_example"; // String | The name of the prefix.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let peeringServicePrefix = new PeeringManagementClient.PeeringServicePrefix(); // PeeringServicePrefix | The properties needed to create a prefix.
apiInstance.prefixesCreateOrUpdate(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, peeringServicePrefix, (error, data, response) => {
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
 **peeringServiceName** | **String**| The name of the peering service. | 
 **prefixName** | **String**| The name of the prefix. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **peeringServicePrefix** | [**PeeringServicePrefix**](PeeringServicePrefix.md)| The properties needed to create a prefix. | 

### Return type

[**PeeringServicePrefix**](PeeringServicePrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## prefixesDelete

> prefixesDelete(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion)



Deletes an existing prefix with the specified name under the given subscription, resource group and peering service.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicePrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
let prefixName = "prefixName_example"; // String | The name of the prefix.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.prefixesDelete(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, (error, data, response) => {
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
 **peeringServiceName** | **String**| The name of the peering service. | 
 **prefixName** | **String**| The name of the prefix. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## prefixesGet

> PeeringServicePrefix prefixesGet(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, opts)



Gets an existing prefix with the specified name under the given subscription, resource group and peering service.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicePrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
let prefixName = "prefixName_example"; // String | The name of the prefix.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'expand': "expand_example" // String | The properties to be expanded.
};
apiInstance.prefixesGet(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **peeringServiceName** | **String**| The name of the peering service. | 
 **prefixName** | **String**| The name of the prefix. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **expand** | **String**| The properties to be expanded. | [optional] 

### Return type

[**PeeringServicePrefix**](PeeringServicePrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## prefixesListByPeeringService

> PeeringServicePrefixListResult prefixesListByPeeringService(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, opts)



Lists all prefixes under the given subscription, resource group and peering service.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicePrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'expand': "expand_example" // String | The properties to be expanded.
};
apiInstance.prefixesListByPeeringService(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **peeringServiceName** | **String**| The name of the peering service. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **expand** | **String**| The properties to be expanded. | [optional] 

### Return type

[**PeeringServicePrefixListResult**](PeeringServicePrefixListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

