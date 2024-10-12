# FrontDoorManagementClient.FrontDoorsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpointsPurgeContent**](FrontDoorsApi.md#endpointsPurgeContent) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/purge | 
[**frontDoorsCreateOrUpdate**](FrontDoorsApi.md#frontDoorsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName} | 
[**frontDoorsDelete**](FrontDoorsApi.md#frontDoorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName} | 
[**frontDoorsGet**](FrontDoorsApi.md#frontDoorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName} | 
[**frontDoorsList**](FrontDoorsApi.md#frontDoorsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/frontDoors | 
[**frontDoorsListByResourceGroup**](FrontDoorsApi.md#frontDoorsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors | 
[**frontDoorsValidateCustomDomain**](FrontDoorsApi.md#frontDoorsValidateCustomDomain) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/validateCustomDomain | 
[**frontendEndpointsDisableHttps**](FrontDoorsApi.md#frontendEndpointsDisableHttps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/disableHttps | 
[**frontendEndpointsEnableHttps**](FrontDoorsApi.md#frontendEndpointsEnableHttps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName}/enableHttps | 
[**frontendEndpointsGet**](FrontDoorsApi.md#frontendEndpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints/{frontendEndpointName} | 
[**frontendEndpointsListByFrontDoor**](FrontDoorsApi.md#frontendEndpointsListByFrontDoor) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/frontendEndpoints | 
[**rulesEnginesCreateOrUpdate**](FrontDoorsApi.md#rulesEnginesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/rulesEngines/{rulesEngineName} | 
[**rulesEnginesDelete**](FrontDoorsApi.md#rulesEnginesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/rulesEngines/{rulesEngineName} | 
[**rulesEnginesGet**](FrontDoorsApi.md#rulesEnginesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/rulesEngines/{rulesEngineName} | 
[**rulesEnginesListByFrontDoor**](FrontDoorsApi.md#rulesEnginesListByFrontDoor) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/frontDoors/{frontDoorName}/rulesEngines | 



## endpointsPurgeContent

> endpointsPurgeContent(subscriptionId, resourceGroupName, frontDoorName, apiVersion, contentFilePaths)



Removes a content from Front Door.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let apiVersion = "apiVersion_example"; // String | Client API version.
let contentFilePaths = new FrontDoorManagementClient.PurgeParameters(); // PurgeParameters | The path to the content to be purged. Path can be a full URL, e.g. '/pictures/city.png' which removes a single file, or a directory with a wildcard, e.g. '/pictures/_*' which removes all folders and files in the directory.
apiInstance.endpointsPurgeContent(subscriptionId, resourceGroupName, frontDoorName, apiVersion, contentFilePaths, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **apiVersion** | **String**| Client API version. | 
 **contentFilePaths** | [**PurgeParameters**](PurgeParameters.md)| The path to the content to be purged. Path can be a full URL, e.g. &#39;/pictures/city.png&#39; which removes a single file, or a directory with a wildcard, e.g. &#39;/pictures/_*&#39; which removes all folders and files in the directory. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## frontDoorsCreateOrUpdate

> FrontDoor frontDoorsCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, apiVersion, frontDoorParameters)



Creates a new Front Door with a Front Door name under the specified subscription and resource group.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let apiVersion = "apiVersion_example"; // String | Client API version.
let frontDoorParameters = new FrontDoorManagementClient.FrontDoor(); // FrontDoor | Front Door properties needed to create a new Front Door.
apiInstance.frontDoorsCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, apiVersion, frontDoorParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **apiVersion** | **String**| Client API version. | 
 **frontDoorParameters** | [**FrontDoor**](FrontDoor.md)| Front Door properties needed to create a new Front Door. | 

### Return type

[**FrontDoor**](FrontDoor.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## frontDoorsDelete

> frontDoorsDelete(subscriptionId, resourceGroupName, frontDoorName, apiVersion)



Deletes an existing Front Door with the specified parameters.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.frontDoorsDelete(subscriptionId, resourceGroupName, frontDoorName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## frontDoorsGet

> FrontDoor frontDoorsGet(subscriptionId, resourceGroupName, frontDoorName, apiVersion)



Gets a Front Door with the specified Front Door name under the specified subscription and resource group.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.frontDoorsGet(subscriptionId, resourceGroupName, frontDoorName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**FrontDoor**](FrontDoor.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## frontDoorsList

> FrontDoorListResult frontDoorsList(subscriptionId, apiVersion)



Lists all of the Front Doors within an Azure subscription.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.frontDoorsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**FrontDoorListResult**](FrontDoorListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## frontDoorsListByResourceGroup

> FrontDoorListResult frontDoorsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists all of the Front Doors within a resource group under a subscription.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.frontDoorsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**FrontDoorListResult**](FrontDoorListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## frontDoorsValidateCustomDomain

> ValidateCustomDomainOutput frontDoorsValidateCustomDomain(subscriptionId, resourceGroupName, frontDoorName, apiVersion, customDomainProperties)



Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let apiVersion = "apiVersion_example"; // String | Client API version.
let customDomainProperties = new FrontDoorManagementClient.ValidateCustomDomainInput(); // ValidateCustomDomainInput | Custom domain to be validated.
apiInstance.frontDoorsValidateCustomDomain(subscriptionId, resourceGroupName, frontDoorName, apiVersion, customDomainProperties, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **apiVersion** | **String**| Client API version. | 
 **customDomainProperties** | [**ValidateCustomDomainInput**](ValidateCustomDomainInput.md)| Custom domain to be validated. | 

### Return type

[**ValidateCustomDomainOutput**](ValidateCustomDomainOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## frontendEndpointsDisableHttps

> frontendEndpointsDisableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion)



Disables a frontendEndpoint for HTTPS traffic

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let frontendEndpointName = "frontendEndpointName_example"; // String | Name of the Frontend endpoint which is unique within the Front Door.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.frontendEndpointsDisableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **frontendEndpointName** | **String**| Name of the Frontend endpoint which is unique within the Front Door. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## frontendEndpointsEnableHttps

> frontendEndpointsEnableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion, customHttpsConfiguration)



Enables a frontendEndpoint for HTTPS traffic

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let frontendEndpointName = "frontendEndpointName_example"; // String | Name of the Frontend endpoint which is unique within the Front Door.
let apiVersion = "apiVersion_example"; // String | Client API version.
let customHttpsConfiguration = new FrontDoorManagementClient.CustomHttpsConfiguration(); // CustomHttpsConfiguration | The configuration specifying how to enable HTTPS
apiInstance.frontendEndpointsEnableHttps(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion, customHttpsConfiguration, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **frontendEndpointName** | **String**| Name of the Frontend endpoint which is unique within the Front Door. | 
 **apiVersion** | **String**| Client API version. | 
 **customHttpsConfiguration** | [**CustomHttpsConfiguration**](CustomHttpsConfiguration.md)| The configuration specifying how to enable HTTPS | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## frontendEndpointsGet

> FrontendEndpoint frontendEndpointsGet(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion)



Gets a Frontend endpoint with the specified name within the specified Front Door.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let frontendEndpointName = "frontendEndpointName_example"; // String | Name of the Frontend endpoint which is unique within the Front Door.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.frontendEndpointsGet(subscriptionId, resourceGroupName, frontDoorName, frontendEndpointName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **frontendEndpointName** | **String**| Name of the Frontend endpoint which is unique within the Front Door. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**FrontendEndpoint**](FrontendEndpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## frontendEndpointsListByFrontDoor

> FrontendEndpointsListResult frontendEndpointsListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion)



Lists all of the frontend endpoints within a Front Door.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.frontendEndpointsListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**FrontendEndpointsListResult**](FrontendEndpointsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rulesEnginesCreateOrUpdate

> RulesEngine rulesEnginesCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion, rulesEngineParameters)



Creates a new Rules Engine Configuration with the specified name within the specified Front Door.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let rulesEngineName = "rulesEngineName_example"; // String | Name of the Rules Engine which is unique within the Front Door.
let apiVersion = "apiVersion_example"; // String | Client API version.
let rulesEngineParameters = new FrontDoorManagementClient.RulesEngine(); // RulesEngine | Rules Engine Configuration properties needed to create a new Rules Engine Configuration.
apiInstance.rulesEnginesCreateOrUpdate(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion, rulesEngineParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **rulesEngineName** | **String**| Name of the Rules Engine which is unique within the Front Door. | 
 **apiVersion** | **String**| Client API version. | 
 **rulesEngineParameters** | [**RulesEngine**](RulesEngine.md)| Rules Engine Configuration properties needed to create a new Rules Engine Configuration. | 

### Return type

[**RulesEngine**](RulesEngine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rulesEnginesDelete

> rulesEnginesDelete(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion)



Deletes an existing Rules Engine Configuration with the specified parameters.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let rulesEngineName = "rulesEngineName_example"; // String | Name of the Rules Engine which is unique within the Front Door.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.rulesEnginesDelete(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **rulesEngineName** | **String**| Name of the Rules Engine which is unique within the Front Door. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rulesEnginesGet

> RulesEngine rulesEnginesGet(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion)



Gets a Rules Engine Configuration with the specified name within the specified Front Door.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let rulesEngineName = "rulesEngineName_example"; // String | Name of the Rules Engine which is unique within the Front Door.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.rulesEnginesGet(subscriptionId, resourceGroupName, frontDoorName, rulesEngineName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **rulesEngineName** | **String**| Name of the Rules Engine which is unique within the Front Door. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**RulesEngine**](RulesEngine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rulesEnginesListByFrontDoor

> RulesEngineListResult rulesEnginesListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion)



Lists all of the Rules Engine Configurations within a Front Door.

### Example

```javascript
import FrontDoorManagementClient from 'front_door_management_client';
let defaultClient = FrontDoorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FrontDoorManagementClient.FrontDoorsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let frontDoorName = "frontDoorName_example"; // String | Name of the Front Door which is globally unique.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.rulesEnginesListByFrontDoor(subscriptionId, resourceGroupName, frontDoorName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **frontDoorName** | **String**| Name of the Front Door which is globally unique. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**RulesEngineListResult**](RulesEngineListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

