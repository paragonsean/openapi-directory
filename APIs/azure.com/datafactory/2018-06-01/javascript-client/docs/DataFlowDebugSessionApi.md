# DataFactoryManagementClient.DataFlowDebugSessionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataFlowDebugSessionAddDataFlow**](DataFlowDebugSessionApi.md#dataFlowDebugSessionAddDataFlow) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/addDataFlowToDebugSession | 
[**dataFlowDebugSessionCreate**](DataFlowDebugSessionApi.md#dataFlowDebugSessionCreate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/createDataFlowDebugSession | 
[**dataFlowDebugSessionDelete**](DataFlowDebugSessionApi.md#dataFlowDebugSessionDelete) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/deleteDataFlowDebugSession | 
[**dataFlowDebugSessionExecuteCommand**](DataFlowDebugSessionApi.md#dataFlowDebugSessionExecuteCommand) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/executeDataFlowDebugCommand | 
[**dataFlowDebugSessionQueryByFactory**](DataFlowDebugSessionApi.md#dataFlowDebugSessionQueryByFactory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryDataFlowDebugSessions | 



## dataFlowDebugSessionAddDataFlow

> AddDataFlowToDebugSessionResponse dataFlowDebugSessionAddDataFlow(subscriptionId, resourceGroupName, factoryName, apiVersion, request)



Add a data flow into debug session.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowDebugSessionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let request = new DataFactoryManagementClient.DataFlowDebugPackage(); // DataFlowDebugPackage | Data flow debug session definition with debug content.
apiInstance.dataFlowDebugSessionAddDataFlow(subscriptionId, resourceGroupName, factoryName, apiVersion, request, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **request** | [**DataFlowDebugPackage**](DataFlowDebugPackage.md)| Data flow debug session definition with debug content. | 

### Return type

[**AddDataFlowToDebugSessionResponse**](AddDataFlowToDebugSessionResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataFlowDebugSessionCreate

> CreateDataFlowDebugSessionResponse dataFlowDebugSessionCreate(subscriptionId, resourceGroupName, factoryName, apiVersion, request)



Creates a data flow debug session.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowDebugSessionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let request = new DataFactoryManagementClient.CreateDataFlowDebugSessionRequest(); // CreateDataFlowDebugSessionRequest | Data flow debug session definition
apiInstance.dataFlowDebugSessionCreate(subscriptionId, resourceGroupName, factoryName, apiVersion, request, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **request** | [**CreateDataFlowDebugSessionRequest**](CreateDataFlowDebugSessionRequest.md)| Data flow debug session definition | 

### Return type

[**CreateDataFlowDebugSessionResponse**](CreateDataFlowDebugSessionResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataFlowDebugSessionDelete

> dataFlowDebugSessionDelete(subscriptionId, resourceGroupName, factoryName, apiVersion, request)



Deletes a data flow debug session.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowDebugSessionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let request = new DataFactoryManagementClient.DeleteDataFlowDebugSessionRequest(); // DeleteDataFlowDebugSessionRequest | Data flow debug session definition for deletion
apiInstance.dataFlowDebugSessionDelete(subscriptionId, resourceGroupName, factoryName, apiVersion, request, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **request** | [**DeleteDataFlowDebugSessionRequest**](DeleteDataFlowDebugSessionRequest.md)| Data flow debug session definition for deletion | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataFlowDebugSessionExecuteCommand

> DataFlowDebugCommandResponse dataFlowDebugSessionExecuteCommand(subscriptionId, resourceGroupName, factoryName, apiVersion, request)



Execute a data flow debug command.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowDebugSessionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let request = new DataFactoryManagementClient.DataFlowDebugCommandRequest(); // DataFlowDebugCommandRequest | Data flow debug command definition.
apiInstance.dataFlowDebugSessionExecuteCommand(subscriptionId, resourceGroupName, factoryName, apiVersion, request, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **request** | [**DataFlowDebugCommandRequest**](DataFlowDebugCommandRequest.md)| Data flow debug command definition. | 

### Return type

[**DataFlowDebugCommandResponse**](DataFlowDebugCommandResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dataFlowDebugSessionQueryByFactory

> QueryDataFlowDebugSessionsResponse dataFlowDebugSessionQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Query all active data flow debug sessions.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.DataFlowDebugSessionApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.dataFlowDebugSessionQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 

### Return type

[**QueryDataFlowDebugSessionsResponse**](QueryDataFlowDebugSessionsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

