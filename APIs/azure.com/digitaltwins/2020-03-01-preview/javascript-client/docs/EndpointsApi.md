# AzureDigitalTwinsManagementClient.EndpointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**digitalTwinsEndpointCreateOrUpdate**](EndpointsApi.md#digitalTwinsEndpointCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/endpoints/{endpointName} | 
[**digitalTwinsEndpointDelete**](EndpointsApi.md#digitalTwinsEndpointDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/endpoints/{endpointName} | 
[**digitalTwinsEndpointGet**](EndpointsApi.md#digitalTwinsEndpointGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/endpoints/{endpointName} | 
[**digitalTwinsEndpointList**](EndpointsApi.md#digitalTwinsEndpointList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/endpoints | 



## digitalTwinsEndpointCreateOrUpdate

> DigitalTwinsEndpointResource digitalTwinsEndpointCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName, endpointDescription)



Create or update DigitalTwinsInstance endpoint.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.EndpointsApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
let endpointName = "endpointName_example"; // String | Name of Endpoint Resource.
let endpointDescription = new AzureDigitalTwinsManagementClient.DigitalTwinsEndpointResource(); // DigitalTwinsEndpointResource | The DigitalTwinsInstance endpoint metadata and security metadata.
apiInstance.digitalTwinsEndpointCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName, endpointDescription, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 
 **resourceName** | **String**| The name of the DigitalTwinsInstance. | 
 **endpointName** | **String**| Name of Endpoint Resource. | 
 **endpointDescription** | [**DigitalTwinsEndpointResource**](DigitalTwinsEndpointResource.md)| The DigitalTwinsInstance endpoint metadata and security metadata. | 

### Return type

[**DigitalTwinsEndpointResource**](DigitalTwinsEndpointResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## digitalTwinsEndpointDelete

> digitalTwinsEndpointDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName)



Delete a DigitalTwinsInstance endpoint.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.EndpointsApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
let endpointName = "endpointName_example"; // String | Name of Endpoint Resource.
apiInstance.digitalTwinsEndpointDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 
 **resourceName** | **String**| The name of the DigitalTwinsInstance. | 
 **endpointName** | **String**| Name of Endpoint Resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## digitalTwinsEndpointGet

> DigitalTwinsEndpointResource digitalTwinsEndpointGet(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName)



Get DigitalTwinsInstances Endpoint.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.EndpointsApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
let endpointName = "endpointName_example"; // String | Name of Endpoint Resource.
apiInstance.digitalTwinsEndpointGet(apiVersion, subscriptionId, resourceGroupName, resourceName, endpointName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 
 **resourceName** | **String**| The name of the DigitalTwinsInstance. | 
 **endpointName** | **String**| Name of Endpoint Resource. | 

### Return type

[**DigitalTwinsEndpointResource**](DigitalTwinsEndpointResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## digitalTwinsEndpointList

> DigitalTwinsEndpointResourceListResult digitalTwinsEndpointList(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get DigitalTwinsInstance Endpoints.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.EndpointsApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
apiInstance.digitalTwinsEndpointList(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 
 **resourceName** | **String**| The name of the DigitalTwinsInstance. | 

### Return type

[**DigitalTwinsEndpointResourceListResult**](DigitalTwinsEndpointResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

