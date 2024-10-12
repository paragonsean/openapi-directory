# PeeringManagementClient.PeeringServicePrefixesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peeringServicePrefixesCreateOrUpdate**](PeeringServicePrefixesApi.md#peeringServicePrefixesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} | 
[**peeringServicePrefixesDelete**](PeeringServicePrefixesApi.md#peeringServicePrefixesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} | 
[**peeringServicePrefixesGet**](PeeringServicePrefixesApi.md#peeringServicePrefixesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes/{prefixName} | 
[**prefixesListByPeeringService**](PeeringServicePrefixesApi.md#prefixesListByPeeringService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName}/prefixes | 



## peeringServicePrefixesCreateOrUpdate

> PeeringServicePrefix peeringServicePrefixesCreateOrUpdate(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, peeringServicePrefix)



Creates or updates the peering prefix.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicePrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let peeringServiceName = "peeringServiceName_example"; // String | The peering service name.
let prefixName = "prefixName_example"; // String | The prefix name
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let peeringServicePrefix = new PeeringManagementClient.PeeringServicePrefix(); // PeeringServicePrefix | The IP prefix for an peering
apiInstance.peeringServicePrefixesCreateOrUpdate(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, peeringServicePrefix, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **peeringServiceName** | **String**| The peering service name. | 
 **prefixName** | **String**| The prefix name | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **peeringServicePrefix** | [**PeeringServicePrefix**](PeeringServicePrefix.md)| The IP prefix for an peering | 

### Return type

[**PeeringServicePrefix**](PeeringServicePrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## peeringServicePrefixesDelete

> peeringServicePrefixesDelete(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion)



removes the peering prefix.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicePrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let peeringServiceName = "peeringServiceName_example"; // String | The peering service name.
let prefixName = "prefixName_example"; // String | The prefix name
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringServicePrefixesDelete(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **peeringServiceName** | **String**| The peering service name. | 
 **prefixName** | **String**| The prefix name | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringServicePrefixesGet

> PeeringServicePrefix peeringServicePrefixesGet(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion)



Gets the peering service prefix.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicePrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let peeringServiceName = "peeringServiceName_example"; // String | The peering service name.
let prefixName = "prefixName_example"; // String | The prefix name.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringServicePrefixesGet(resourceGroupName, peeringServiceName, prefixName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **peeringServiceName** | **String**| The peering service name. | 
 **prefixName** | **String**| The prefix name. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeeringServicePrefix**](PeeringServicePrefix.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## prefixesListByPeeringService

> PeeringServicePrefixListResult prefixesListByPeeringService(resourceGroupName, peeringServiceName, subscriptionId, apiVersion)



Lists the peerings prefix in the resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicePrefixesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let peeringServiceName = "peeringServiceName_example"; // String | The peering service name.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.prefixesListByPeeringService(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **peeringServiceName** | **String**| The peering service name. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeeringServicePrefixListResult**](PeeringServicePrefixListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

