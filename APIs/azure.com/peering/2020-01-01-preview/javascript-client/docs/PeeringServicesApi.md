# PeeringManagementClient.PeeringServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peeringServicesCreateOrUpdate**](PeeringServicesApi.md#peeringServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName} | 
[**peeringServicesDelete**](PeeringServicesApi.md#peeringServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName} | 
[**peeringServicesGet**](PeeringServicesApi.md#peeringServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName} | 
[**peeringServicesListByResourceGroup**](PeeringServicesApi.md#peeringServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices | 
[**peeringServicesListBySubscription**](PeeringServicesApi.md#peeringServicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/peeringServices | 
[**peeringServicesUpdate**](PeeringServicesApi.md#peeringServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Peering/peeringServices/{peeringServiceName} | 



## peeringServicesCreateOrUpdate

> PeeringService peeringServicesCreateOrUpdate(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, peeringService)



Creates a new peering service or updates an existing peering with the specified name under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let peeringService = new PeeringManagementClient.PeeringService(); // PeeringService | The properties needed to create or update a peering service.
apiInstance.peeringServicesCreateOrUpdate(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, peeringService, (error, data, response) => {
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
 **peeringService** | [**PeeringService**](PeeringService.md)| The properties needed to create or update a peering service. | 

### Return type

[**PeeringService**](PeeringService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## peeringServicesDelete

> peeringServicesDelete(resourceGroupName, peeringServiceName, subscriptionId, apiVersion)



Deletes an existing peering service with the specified name under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringServicesDelete(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringServicesGet

> PeeringService peeringServicesGet(resourceGroupName, peeringServiceName, subscriptionId, apiVersion)



Gets an existing peering service with the specified name under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringServiceName = "peeringServiceName_example"; // String | The name of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringServicesGet(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, (error, data, response) => {
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
 **peeringServiceName** | **String**| The name of the peering. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PeeringService**](PeeringService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringServicesListByResourceGroup

> PeeringServiceListResult peeringServicesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Lists all of the peering services under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringServicesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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

[**PeeringServiceListResult**](PeeringServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringServicesListBySubscription

> PeeringServiceListResult peeringServicesListBySubscription(subscriptionId, apiVersion)



Lists all of the peerings under the given subscription.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.peeringServicesListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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

[**PeeringServiceListResult**](PeeringServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peeringServicesUpdate

> PeeringService peeringServicesUpdate(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, tags)



Updates tags for a peering service with the specified name under the given subscription and resource group.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.PeeringServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let peeringServiceName = "peeringServiceName_example"; // String | The name of the peering service.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let tags = new PeeringManagementClient.ResourceTags(); // ResourceTags | The resource tags.
apiInstance.peeringServicesUpdate(resourceGroupName, peeringServiceName, subscriptionId, apiVersion, tags, (error, data, response) => {
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
 **tags** | [**ResourceTags**](ResourceTags.md)| The resource tags. | 

### Return type

[**PeeringService**](PeeringService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

