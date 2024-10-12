# AzureDigitalTwinsManagementClient.IoTHubIntegrationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**digitalTwinsIoTHubsList**](IoTHubIntegrationApi.md#digitalTwinsIoTHubsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName}/integrationResources | 
[**ioTHubCreateOrUpdate**](IoTHubIntegrationApi.md#ioTHubCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integrationResourceName} | 
[**ioTHubDelete**](IoTHubIntegrationApi.md#ioTHubDelete) | **DELETE** /{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integrationResourceName} | 
[**ioTHubGet**](IoTHubIntegrationApi.md#ioTHubGet) | **GET** /{scope}/providers/Microsoft.DigitalTwins/integrationResources/{integrationResourceName} | 



## digitalTwinsIoTHubsList

> DigitalTwinsIntegrationResourceListResult digitalTwinsIoTHubsList(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get DigitalTwinsInstance IoTHubs.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.IoTHubIntegrationApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
apiInstance.digitalTwinsIoTHubsList(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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

[**DigitalTwinsIntegrationResourceListResult**](DigitalTwinsIntegrationResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTHubCreateOrUpdate

> IntegrationResource ioTHubCreateOrUpdate(scope, integrationResourceName, iotHubDescription)



Creates or Updates an IoTHub Integration with DigitalTwinsInstances.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.IoTHubIntegrationApi();
let scope = "scope_example"; // String | The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
let integrationResourceName = "integrationResourceName_example"; // String | Name of IoTHub and DigitalTwinsInstance integration instance.
let iotHubDescription = new AzureDigitalTwinsManagementClient.IntegrationResource(); // IntegrationResource | The IoTHub metadata.
apiInstance.ioTHubCreateOrUpdate(scope, integrationResourceName, iotHubDescription, (error, data, response) => {
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
 **scope** | **String**| The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}. | 
 **integrationResourceName** | **String**| Name of IoTHub and DigitalTwinsInstance integration instance. | 
 **iotHubDescription** | [**IntegrationResource**](IntegrationResource.md)| The IoTHub metadata. | 

### Return type

[**IntegrationResource**](IntegrationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ioTHubDelete

> ioTHubDelete(scope, integrationResourceName)



Deletes a DigitalTwinsInstance link with IoTHub.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.IoTHubIntegrationApi();
let scope = "scope_example"; // String | The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
let integrationResourceName = "integrationResourceName_example"; // String | Name of IoTHub and DigitalTwinsInstance integration instance.
apiInstance.ioTHubDelete(scope, integrationResourceName, (error, data, response) => {
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
 **scope** | **String**| The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}. | 
 **integrationResourceName** | **String**| Name of IoTHub and DigitalTwinsInstance integration instance. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ioTHubGet

> IntegrationResource ioTHubGet(scope, integrationResourceName)



Gets properties of an IoTHub Integration.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.IoTHubIntegrationApi();
let scope = "scope_example"; // String | The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}.
let integrationResourceName = "integrationResourceName_example"; // String | Name of IoTHub and DigitalTwinsInstance integration instance.
apiInstance.ioTHubGet(scope, integrationResourceName, (error, data, response) => {
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
 **scope** | **String**| The scope of the Digital Twins Integration. The scope has to be an IoTHub resource. For example, /{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IoTHubs/{resourceName}. | 
 **integrationResourceName** | **String**| Name of IoTHub and DigitalTwinsInstance integration instance. | 

### Return type

[**IntegrationResource**](IntegrationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

