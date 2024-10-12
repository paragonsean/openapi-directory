# DataFactoryManagementClient.TriggerrunsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triggerRunsQueryByFactory**](TriggerrunsApi.md#triggerRunsQueryByFactory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryTriggerRuns | 
[**triggerRunsRerun**](TriggerrunsApi.md#triggerRunsRerun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/triggerRuns/{runId}/rerun | 



## triggerRunsQueryByFactory

> TriggerRunsQueryResponse triggerRunsQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, filterParameters)



Query trigger runs.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.TriggerrunsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let apiVersion = "apiVersion_example"; // String | The API version.
let filterParameters = new DataFactoryManagementClient.RunFilterParameters(); // RunFilterParameters | Parameters to filter the pipeline run.
apiInstance.triggerRunsQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, filterParameters, (error, data, response) => {
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
 **filterParameters** | [**RunFilterParameters**](RunFilterParameters.md)| Parameters to filter the pipeline run. | 

### Return type

[**TriggerRunsQueryResponse**](TriggerRunsQueryResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## triggerRunsRerun

> triggerRunsRerun(subscriptionId, resourceGroupName, factoryName, triggerName, runId, apiVersion)



Rerun single trigger instance by runId.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.TriggerrunsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let triggerName = "triggerName_example"; // String | The trigger name.
let runId = "runId_example"; // String | The pipeline run identifier.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.triggerRunsRerun(subscriptionId, resourceGroupName, factoryName, triggerName, runId, apiVersion, (error, data, response) => {
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
 **runId** | **String**| The pipeline run identifier. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

