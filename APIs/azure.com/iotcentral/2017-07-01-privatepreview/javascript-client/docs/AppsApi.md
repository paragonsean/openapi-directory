# IotCentralClient.AppsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsCheckNameAvailability**](AppsApi.md#appsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.IoTCentral/checkNameAvailability | 
[**appsCreateOrUpdate**](AppsApi.md#appsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps/{resourceName} | 
[**appsDelete**](AppsApi.md#appsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps/{resourceName} | 
[**appsGet**](AppsApi.md#appsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps/{resourceName} | 
[**appsListByResourceGroup**](AppsApi.md#appsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps | 
[**appsListBySubscription**](AppsApi.md#appsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.IoTCentral/IoTApps | 
[**appsUpdate**](AppsApi.md#appsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IoTCentral/IoTApps/{resourceName} | 



## appsCheckNameAvailability

> AppNameAvailabilityInfo appsCheckNameAvailability(apiVersion, subscriptionId, operationInputs)



Check if an IoT Central application name is available.

### Example

```javascript
import IotCentralClient from 'iot_central_client';
let defaultClient = IotCentralClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotCentralClient.AppsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let operationInputs = new IotCentralClient.OperationInputs(); // OperationInputs | Set the name parameter in the OperationInputs structure to the name of the IoT Central application to check.
apiInstance.appsCheckNameAvailability(apiVersion, subscriptionId, operationInputs, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **operationInputs** | [**OperationInputs**](OperationInputs.md)| Set the name parameter in the OperationInputs structure to the name of the IoT Central application to check. | 

### Return type

[**AppNameAvailabilityInfo**](AppNameAvailabilityInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsCreateOrUpdate

> App appsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, app)



Create or update the metadata of an IoT Central application. The usual pattern to modify a property is to retrieve the IoT Central application metadata and security metadata, and then combine them with the modified values in a new body to update the IoT Central application.

### Example

```javascript
import IotCentralClient from 'iot_central_client';
let defaultClient = IotCentralClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotCentralClient.AppsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
let resourceName = "resourceName_example"; // String | The ARM resource name of the IoT Central application.
let app = new IotCentralClient.App(); // App | The IoT Central application metadata and security metadata.
apiInstance.appsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, app, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | 
 **resourceName** | **String**| The ARM resource name of the IoT Central application. | 
 **app** | [**App**](App.md)| The IoT Central application metadata and security metadata. | 

### Return type

[**App**](App.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsDelete

> appsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Delete an IoT Central application.

### Example

```javascript
import IotCentralClient from 'iot_central_client';
let defaultClient = IotCentralClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotCentralClient.AppsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
let resourceName = "resourceName_example"; // String | The ARM resource name of the IoT Central application.
apiInstance.appsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | 
 **resourceName** | **String**| The ARM resource name of the IoT Central application. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGet

> App appsGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get the metadata of an IoT Central application.

### Example

```javascript
import IotCentralClient from 'iot_central_client';
let defaultClient = IotCentralClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotCentralClient.AppsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
let resourceName = "resourceName_example"; // String | The ARM resource name of the IoT Central application.
apiInstance.appsGet(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | 
 **resourceName** | **String**| The ARM resource name of the IoT Central application. | 

### Return type

[**App**](App.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListByResourceGroup

> AppListResult appsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the IoT Central Applications in a resource group.

### Example

```javascript
import IotCentralClient from 'iot_central_client';
let defaultClient = IotCentralClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotCentralClient.AppsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
apiInstance.appsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | 

### Return type

[**AppListResult**](AppListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListBySubscription

> AppListResult appsListBySubscription(apiVersion, subscriptionId)



Get all IoT Central Applications in a subscription.

### Example

```javascript
import IotCentralClient from 'iot_central_client';
let defaultClient = IotCentralClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotCentralClient.AppsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
apiInstance.appsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 

### Return type

[**AppListResult**](AppListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsUpdate

> App appsUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, appPatch)



Update the metadata of an IoT Central application.

### Example

```javascript
import IotCentralClient from 'iot_central_client';
let defaultClient = IotCentralClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotCentralClient.AppsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT Central application.
let resourceName = "resourceName_example"; // String | The ARM resource name of the IoT Central application.
let appPatch = new IotCentralClient.AppPatch(); // AppPatch | The IoT Central application metadata and security metadata.
apiInstance.appsUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, appPatch, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT Central application. | 
 **resourceName** | **String**| The ARM resource name of the IoT Central application. | 
 **appPatch** | [**AppPatch**](AppPatch.md)| The IoT Central application metadata and security metadata. | 

### Return type

[**App**](App.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

