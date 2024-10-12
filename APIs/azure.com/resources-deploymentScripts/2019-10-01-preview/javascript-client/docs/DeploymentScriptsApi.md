# DeploymentScriptsClient.DeploymentScriptsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploymentScriptsCreate**](DeploymentScriptsApi.md#deploymentScriptsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName} | 
[**deploymentScriptsDelete**](DeploymentScriptsApi.md#deploymentScriptsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName} | 
[**deploymentScriptsGet**](DeploymentScriptsApi.md#deploymentScriptsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName} | 
[**deploymentScriptsGetLogs**](DeploymentScriptsApi.md#deploymentScriptsGetLogs) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}/logs | 
[**deploymentScriptsGetLogsDefault**](DeploymentScriptsApi.md#deploymentScriptsGetLogsDefault) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName}/logs/default | 
[**deploymentScriptsListByResourceGroup**](DeploymentScriptsApi.md#deploymentScriptsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts | 
[**deploymentScriptsListBySubscription**](DeploymentScriptsApi.md#deploymentScriptsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Resources/deploymentScripts | 
[**deploymentScriptsUpdate**](DeploymentScriptsApi.md#deploymentScriptsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Resources/deploymentScripts/{scriptName} | 



## deploymentScriptsCreate

> DeploymentScript deploymentScriptsCreate(subscriptionId, resourceGroupName, scriptName, apiVersion, deploymentScript)



Creates a deployment script.

### Example

```javascript
import DeploymentScriptsClient from 'deployment_scripts_client';
let defaultClient = DeploymentScriptsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentScriptsClient.DeploymentScriptsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let scriptName = "scriptName_example"; // String | Name of the deployment script.
let apiVersion = "apiVersion_example"; // String | Client Api version.
let deploymentScript = new DeploymentScriptsClient.DeploymentScript(); // DeploymentScript | Deployment script supplied to the operation.
apiInstance.deploymentScriptsCreate(subscriptionId, resourceGroupName, scriptName, apiVersion, deploymentScript, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **scriptName** | **String**| Name of the deployment script. | 
 **apiVersion** | **String**| Client Api version. | 
 **deploymentScript** | [**DeploymentScript**](DeploymentScript.md)| Deployment script supplied to the operation. | 

### Return type

[**DeploymentScript**](DeploymentScript.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentScriptsDelete

> deploymentScriptsDelete(subscriptionId, resourceGroupName, scriptName, apiVersion)



Deletes a deployment script. When operation completes, status code 200 returned without content.

### Example

```javascript
import DeploymentScriptsClient from 'deployment_scripts_client';
let defaultClient = DeploymentScriptsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentScriptsClient.DeploymentScriptsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let scriptName = "scriptName_example"; // String | Name of the deployment script.
let apiVersion = "apiVersion_example"; // String | Client Api version.
apiInstance.deploymentScriptsDelete(subscriptionId, resourceGroupName, scriptName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **scriptName** | **String**| Name of the deployment script. | 
 **apiVersion** | **String**| Client Api version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentScriptsGet

> DeploymentScript deploymentScriptsGet(subscriptionId, resourceGroupName, scriptName, apiVersion)



Gets a deployment script with a given name.

### Example

```javascript
import DeploymentScriptsClient from 'deployment_scripts_client';
let defaultClient = DeploymentScriptsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentScriptsClient.DeploymentScriptsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let scriptName = "scriptName_example"; // String | Name of the deployment script.
let apiVersion = "apiVersion_example"; // String | Client Api version.
apiInstance.deploymentScriptsGet(subscriptionId, resourceGroupName, scriptName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **scriptName** | **String**| Name of the deployment script. | 
 **apiVersion** | **String**| Client Api version. | 

### Return type

[**DeploymentScript**](DeploymentScript.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentScriptsGetLogs

> ScriptLogsList deploymentScriptsGetLogs(subscriptionId, resourceGroupName, scriptName, apiVersion)



Gets deployment script logs for a given deployment script name.

### Example

```javascript
import DeploymentScriptsClient from 'deployment_scripts_client';
let defaultClient = DeploymentScriptsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentScriptsClient.DeploymentScriptsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let scriptName = "scriptName_example"; // String | Name of the deployment script.
let apiVersion = "apiVersion_example"; // String | Client Api version.
apiInstance.deploymentScriptsGetLogs(subscriptionId, resourceGroupName, scriptName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **scriptName** | **String**| Name of the deployment script. | 
 **apiVersion** | **String**| Client Api version. | 

### Return type

[**ScriptLogsList**](ScriptLogsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentScriptsGetLogsDefault

> ScriptLog deploymentScriptsGetLogsDefault(subscriptionId, resourceGroupName, scriptName, apiVersion)



Gets deployment script logs for a given deployment script name.

### Example

```javascript
import DeploymentScriptsClient from 'deployment_scripts_client';
let defaultClient = DeploymentScriptsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentScriptsClient.DeploymentScriptsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let scriptName = "scriptName_example"; // String | Name of the deployment script.
let apiVersion = "apiVersion_example"; // String | Client Api version.
apiInstance.deploymentScriptsGetLogsDefault(subscriptionId, resourceGroupName, scriptName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **scriptName** | **String**| Name of the deployment script. | 
 **apiVersion** | **String**| Client Api version. | 

### Return type

[**ScriptLog**](ScriptLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentScriptsListByResourceGroup

> DeploymentScriptListResult deploymentScriptsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Lists deployments scripts.

### Example

```javascript
import DeploymentScriptsClient from 'deployment_scripts_client';
let defaultClient = DeploymentScriptsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentScriptsClient.DeploymentScriptsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api version.
apiInstance.deploymentScriptsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api version. | 

### Return type

[**DeploymentScriptListResult**](DeploymentScriptListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentScriptsListBySubscription

> DeploymentScriptListResult deploymentScriptsListBySubscription(subscriptionId, apiVersion)



Lists all deployment scripts for a given subscription.

### Example

```javascript
import DeploymentScriptsClient from 'deployment_scripts_client';
let defaultClient = DeploymentScriptsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentScriptsClient.DeploymentScriptsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api version.
apiInstance.deploymentScriptsListBySubscription(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api version. | 

### Return type

[**DeploymentScriptListResult**](DeploymentScriptListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deploymentScriptsUpdate

> DeploymentScript deploymentScriptsUpdate(subscriptionId, resourceGroupName, scriptName, apiVersion, opts)



Updates deployment script tags with specified values.

### Example

```javascript
import DeploymentScriptsClient from 'deployment_scripts_client';
let defaultClient = DeploymentScriptsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DeploymentScriptsClient.DeploymentScriptsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id which forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let scriptName = "scriptName_example"; // String | Name of the deployment script.
let apiVersion = "apiVersion_example"; // String | Client Api version.
let opts = {
  'deploymentScript': new DeploymentScriptsClient.DeploymentScriptUpdateParameter() // DeploymentScriptUpdateParameter | Deployment script resource with the tags to be updated.
};
apiInstance.deploymentScriptsUpdate(subscriptionId, resourceGroupName, scriptName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id which forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **scriptName** | **String**| Name of the deployment script. | 
 **apiVersion** | **String**| Client Api version. | 
 **deploymentScript** | [**DeploymentScriptUpdateParameter**](DeploymentScriptUpdateParameter.md)| Deployment script resource with the tags to be updated. | [optional] 

### Return type

[**DeploymentScript**](DeploymentScript.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

