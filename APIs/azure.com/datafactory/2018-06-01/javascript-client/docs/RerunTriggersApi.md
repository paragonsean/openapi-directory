# DataFactoryManagementClient.RerunTriggersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rerunTriggersCancel**](RerunTriggersApi.md#rerunTriggersCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers/{rerunTriggerName}/cancel | 
[**rerunTriggersCreate**](RerunTriggersApi.md#rerunTriggersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers/{rerunTriggerName} | 
[**rerunTriggersListByTrigger**](RerunTriggersApi.md#rerunTriggersListByTrigger) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers | 
[**rerunTriggersStart**](RerunTriggersApi.md#rerunTriggersStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers/{rerunTriggerName}/start | 
[**rerunTriggersStop**](RerunTriggersApi.md#rerunTriggersStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/rerunTriggers/{rerunTriggerName}/stop | 



## rerunTriggersCancel

> rerunTriggersCancel(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion)



Cancels a trigger.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.RerunTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let triggerName = "triggerName_example"; // String | The trigger name.
let rerunTriggerName = "rerunTriggerName_example"; // String | The rerun trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rerunTriggersCancel(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **triggerName** | **String**| The trigger name. | 
 **rerunTriggerName** | **String**| The rerun trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rerunTriggersCreate

> TriggerResource rerunTriggersCreate(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion, rerunTumblingWindowTriggerActionParameters)



Creates a rerun trigger.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.RerunTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let triggerName = "triggerName_example"; // String | The trigger name.
let rerunTriggerName = "rerunTriggerName_example"; // String | The rerun trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
let rerunTumblingWindowTriggerActionParameters = new DataFactoryManagementClient.RerunTumblingWindowTriggerActionParameters(); // RerunTumblingWindowTriggerActionParameters | Rerun tumbling window trigger action parameters.
apiInstance.rerunTriggersCreate(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion, rerunTumblingWindowTriggerActionParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **triggerName** | **String**| The trigger name. | 
 **rerunTriggerName** | **String**| The rerun trigger name. | 
 **apiVersion** | **String**| The API version. | 
 **rerunTumblingWindowTriggerActionParameters** | [**RerunTumblingWindowTriggerActionParameters**](RerunTumblingWindowTriggerActionParameters.md)| Rerun tumbling window trigger action parameters. | 

### Return type

[**TriggerResource**](TriggerResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rerunTriggersListByTrigger

> RerunTriggerListResponse rerunTriggersListByTrigger(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion)



Lists rerun triggers by an original trigger name.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.RerunTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let triggerName = "triggerName_example"; // String | The trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rerunTriggersListByTrigger(subscriptionId, resourceGroupName, factoryName, triggerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **triggerName** | **String**| The trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**RerunTriggerListResponse**](RerunTriggerListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rerunTriggersStart

> rerunTriggersStart(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion)



Starts a trigger.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.RerunTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let triggerName = "triggerName_example"; // String | The trigger name.
let rerunTriggerName = "rerunTriggerName_example"; // String | The rerun trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rerunTriggersStart(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **triggerName** | **String**| The trigger name. | 
 **rerunTriggerName** | **String**| The rerun trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rerunTriggersStop

> rerunTriggersStop(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion)



Stops a trigger.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.RerunTriggersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let triggerName = "triggerName_example"; // String | The trigger name.
let rerunTriggerName = "rerunTriggerName_example"; // String | The rerun trigger name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rerunTriggersStop(subscriptionId, resourceGroupName, factoryName, triggerName, rerunTriggerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **factoryName** | **String**| The factory name. | 
 **triggerName** | **String**| The trigger name. | 
 **rerunTriggerName** | **String**| The rerun trigger name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

