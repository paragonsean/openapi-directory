# LogicManagementClient.WorkflowAccessKeysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflowAccessKeysCreateOrUpdate**](WorkflowAccessKeysApi.md#workflowAccessKeysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName} | 
[**workflowAccessKeysDelete**](WorkflowAccessKeysApi.md#workflowAccessKeysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName} | 
[**workflowAccessKeysGet**](WorkflowAccessKeysApi.md#workflowAccessKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName} | 
[**workflowAccessKeysList**](WorkflowAccessKeysApi.md#workflowAccessKeysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys | 
[**workflowAccessKeysListSecretKeys**](WorkflowAccessKeysApi.md#workflowAccessKeysListSecretKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName}/list | 
[**workflowAccessKeysRegenerateSecretKey**](WorkflowAccessKeysApi.md#workflowAccessKeysRegenerateSecretKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/accessKeys/{accessKeyName}/regenerate | 



## workflowAccessKeysCreateOrUpdate

> WorkflowAccessKey workflowAccessKeysCreateOrUpdate(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, workflowAccesskey)



Creates or updates a workflow access key.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowAccessKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
let apiVersion = "apiVersion_example"; // String | The API version.
let workflowAccesskey = new LogicManagementClient.WorkflowAccessKey(); // WorkflowAccessKey | The workflow access key.
apiInstance.workflowAccessKeysCreateOrUpdate(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, workflowAccesskey, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **workflowName** | **String**| The workflow name. | 
 **accessKeyName** | **String**| The workflow access key name. | 
 **apiVersion** | **String**| The API version. | 
 **workflowAccesskey** | [**WorkflowAccessKey**](WorkflowAccessKey.md)| The workflow access key. | 

### Return type

[**WorkflowAccessKey**](WorkflowAccessKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## workflowAccessKeysDelete

> workflowAccessKeysDelete(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion)



Deletes a workflow access key.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowAccessKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowAccessKeysDelete(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **workflowName** | **String**| The workflow name. | 
 **accessKeyName** | **String**| The workflow access key name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workflowAccessKeysGet

> WorkflowAccessKey workflowAccessKeysGet(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion)



Gets a workflow access key.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowAccessKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowAccessKeysGet(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **workflowName** | **String**| The workflow name. | 
 **accessKeyName** | **String**| The workflow access key name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowAccessKey**](WorkflowAccessKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## workflowAccessKeysList

> WorkflowAccessKeyListResult workflowAccessKeysList(subscriptionId, resourceGroupName, workflowName, apiVersion, opts)



Gets a list of workflow access keys.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowAccessKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56 // Number | The number of items to be included in the result.
};
apiInstance.workflowAccessKeysList(subscriptionId, resourceGroupName, workflowName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **workflowName** | **String**| The workflow name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 

### Return type

[**WorkflowAccessKeyListResult**](WorkflowAccessKeyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## workflowAccessKeysListSecretKeys

> WorkflowSecretKeys workflowAccessKeysListSecretKeys(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion)



Lists secret keys.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowAccessKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.workflowAccessKeysListSecretKeys(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **workflowName** | **String**| The workflow name. | 
 **accessKeyName** | **String**| The workflow access key name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**WorkflowSecretKeys**](WorkflowSecretKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## workflowAccessKeysRegenerateSecretKey

> WorkflowSecretKeys workflowAccessKeysRegenerateSecretKey(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, parameters)



Regenerates secret key.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.WorkflowAccessKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let workflowName = "workflowName_example"; // String | The workflow name.
let accessKeyName = "accessKeyName_example"; // String | The workflow access key name.
let apiVersion = "apiVersion_example"; // String | The API version.
let parameters = new LogicManagementClient.RegenerateSecretKeyParameters(); // RegenerateSecretKeyParameters | The parameters.
apiInstance.workflowAccessKeysRegenerateSecretKey(subscriptionId, resourceGroupName, workflowName, accessKeyName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **workflowName** | **String**| The workflow name. | 
 **accessKeyName** | **String**| The workflow access key name. | 
 **apiVersion** | **String**| The API version. | 
 **parameters** | [**RegenerateSecretKeyParameters**](RegenerateSecretKeyParameters.md)| The parameters. | 

### Return type

[**WorkflowSecretKeys**](WorkflowSecretKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

