# ServiceFabricClientApis.ComposeDeploymentApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createComposeDeployment**](ComposeDeploymentApi.md#createComposeDeployment) | **PUT** /ComposeDeployments/$/Create | Creates a Service Fabric compose deployment.
[**getComposeDeploymentStatus**](ComposeDeploymentApi.md#getComposeDeploymentStatus) | **GET** /ComposeDeployments/{deploymentName} | Gets information about a Service Fabric compose deployment.
[**getComposeDeploymentStatusList**](ComposeDeploymentApi.md#getComposeDeploymentStatusList) | **GET** /ComposeDeployments | Gets the list of compose deployments created in the Service Fabric cluster.
[**getComposeDeploymentUpgradeProgress**](ComposeDeploymentApi.md#getComposeDeploymentUpgradeProgress) | **GET** /ComposeDeployments/{deploymentName}/$/GetUpgradeProgress | Gets details for the latest upgrade performed on this Service Fabric compose deployment.
[**removeComposeDeployment**](ComposeDeploymentApi.md#removeComposeDeployment) | **POST** /ComposeDeployments/{deploymentName}/$/Delete | Deletes an existing Service Fabric compose deployment from cluster.
[**startComposeDeploymentUpgrade**](ComposeDeploymentApi.md#startComposeDeploymentUpgrade) | **POST** /ComposeDeployments/{deploymentName}/$/Upgrade | Starts upgrading a compose deployment in the Service Fabric cluster.
[**startRollbackComposeDeploymentUpgrade**](ComposeDeploymentApi.md#startRollbackComposeDeploymentUpgrade) | **POST** /ComposeDeployments/{deploymentName}/$/RollbackUpgrade | Starts rolling back a compose deployment upgrade in the Service Fabric cluster.



## createComposeDeployment

> createComposeDeployment(apiVersion, createComposeDeploymentDescription, opts)

Creates a Service Fabric compose deployment.

Compose is a file format that describes multi-container applications. This API allows deploying container based applications defined in compose format in a Service Fabric cluster. Once the deployment is created, its status can be tracked via the &#x60;GetComposeDeploymentStatus&#x60; API.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ComposeDeploymentApi();
let apiVersion = "'6.0-preview'"; // String | The version of the API. This parameter is required and its value must be '\"6.0-preview'.
let createComposeDeploymentDescription = new ServiceFabricClientApis.CreateComposeDeploymentDescription(); // CreateComposeDeploymentDescription | Describes the compose deployment that needs to be created.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.createComposeDeployment(apiVersion, createComposeDeploymentDescription, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;\&quot;6.0-preview&#39;. | [default to &#39;6.0-preview&#39;]
 **createComposeDeploymentDescription** | [**CreateComposeDeploymentDescription**](CreateComposeDeploymentDescription.md)| Describes the compose deployment that needs to be created. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComposeDeploymentStatus

> ComposeDeploymentStatusInfo getComposeDeploymentStatus(apiVersion, deploymentName, opts)

Gets information about a Service Fabric compose deployment.

Returns the status of the compose deployment that was created or in the process of being created in the Service Fabric cluster and whose name matches the one specified as the parameter. The response includes the name, status, and other details about the deployment.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ComposeDeploymentApi();
let apiVersion = "'6.0-preview'"; // String | The version of the API. This parameter is required and its value must be '\"6.0-preview'.
let deploymentName = "deploymentName_example"; // String | The identity of the deployment.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getComposeDeploymentStatus(apiVersion, deploymentName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;\&quot;6.0-preview&#39;. | [default to &#39;6.0-preview&#39;]
 **deploymentName** | **String**| The identity of the deployment. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ComposeDeploymentStatusInfo**](ComposeDeploymentStatusInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComposeDeploymentStatusList

> PagedComposeDeploymentStatusInfoList getComposeDeploymentStatusList(apiVersion, opts)

Gets the list of compose deployments created in the Service Fabric cluster.

Gets the status about the compose deployments that were created or in the process of being created in the Service Fabric cluster. The response includes the name, status, and other details about the compose deployments. If the list of deployments do not fit in a page, one page of results is returned as well as a continuation token, which can be used to get the next page.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ComposeDeploymentApi();
let apiVersion = "'6.0-preview'"; // String | The version of the API. This parameter is required and its value must be '\"6.0-preview'.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0, // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getComposeDeploymentStatusList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;\&quot;6.0-preview&#39;. | [default to &#39;6.0-preview&#39;]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedComposeDeploymentStatusInfoList**](PagedComposeDeploymentStatusInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComposeDeploymentUpgradeProgress

> ComposeDeploymentUpgradeProgressInfo getComposeDeploymentUpgradeProgress(apiVersion, deploymentName, opts)

Gets details for the latest upgrade performed on this Service Fabric compose deployment.

Returns the information about the state of the compose deployment upgrade along with details to aid debugging application health issues.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ComposeDeploymentApi();
let apiVersion = "'6.0-preview'"; // String | The version of the API. This parameter is required and its value must be '\"6.0-preview'.
let deploymentName = "deploymentName_example"; // String | The identity of the deployment.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getComposeDeploymentUpgradeProgress(apiVersion, deploymentName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;\&quot;6.0-preview&#39;. | [default to &#39;6.0-preview&#39;]
 **deploymentName** | **String**| The identity of the deployment. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**ComposeDeploymentUpgradeProgressInfo**](ComposeDeploymentUpgradeProgressInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeComposeDeployment

> removeComposeDeployment(apiVersion, deploymentName, opts)

Deletes an existing Service Fabric compose deployment from cluster.

Deletes an existing Service Fabric compose deployment.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ComposeDeploymentApi();
let apiVersion = "'6.0-preview'"; // String | The version of the API. This parameter is required and its value must be '\"6.0-preview'.
let deploymentName = "deploymentName_example"; // String | The identity of the deployment.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.removeComposeDeployment(apiVersion, deploymentName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;\&quot;6.0-preview&#39;. | [default to &#39;6.0-preview&#39;]
 **deploymentName** | **String**| The identity of the deployment. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startComposeDeploymentUpgrade

> startComposeDeploymentUpgrade(apiVersion, deploymentName, composeDeploymentUpgradeDescription, opts)

Starts upgrading a compose deployment in the Service Fabric cluster.

Validates the supplied upgrade parameters and starts upgrading the deployment if the parameters are valid.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ComposeDeploymentApi();
let apiVersion = "'6.0-preview'"; // String | The version of the API. This parameter is required and its value must be '\"6.0-preview'.
let deploymentName = "deploymentName_example"; // String | The identity of the deployment.
let composeDeploymentUpgradeDescription = new ServiceFabricClientApis.ComposeDeploymentUpgradeDescription(); // ComposeDeploymentUpgradeDescription | Parameters for upgrading compose deployment.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.startComposeDeploymentUpgrade(apiVersion, deploymentName, composeDeploymentUpgradeDescription, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;\&quot;6.0-preview&#39;. | [default to &#39;6.0-preview&#39;]
 **deploymentName** | **String**| The identity of the deployment. | 
 **composeDeploymentUpgradeDescription** | [**ComposeDeploymentUpgradeDescription**](ComposeDeploymentUpgradeDescription.md)| Parameters for upgrading compose deployment. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startRollbackComposeDeploymentUpgrade

> startRollbackComposeDeploymentUpgrade(apiVersion, deploymentName, opts)

Starts rolling back a compose deployment upgrade in the Service Fabric cluster.

Rollback a service fabric compose deployment upgrade.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.ComposeDeploymentApi();
let apiVersion = "'6.4-preview'"; // String | The version of the API. This parameter is required and its value must be '6.4-preview'.
let deploymentName = "deploymentName_example"; // String | The identity of the deployment.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.startRollbackComposeDeploymentUpgrade(apiVersion, deploymentName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;. | [default to &#39;6.4-preview&#39;]
 **deploymentName** | **String**| The identity of the deployment. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

