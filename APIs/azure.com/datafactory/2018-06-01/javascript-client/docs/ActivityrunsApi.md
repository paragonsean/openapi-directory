# DataFactoryManagementClient.ActivityrunsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activityRunsQueryByPipelineRun**](ActivityrunsApi.md#activityRunsQueryByPipelineRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelineruns/{runId}/queryActivityruns | 



## activityRunsQueryByPipelineRun

> ActivityRunsQueryResponse activityRunsQueryByPipelineRun(subscriptionId, resourceGroupName, factoryName, runId, apiVersion, filterParameters)



Query activity runs based on input filter conditions.

### Example

```javascript
import DataFactoryManagementClient from 'data_factory_management_client';
let defaultClient = DataFactoryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataFactoryManagementClient.ActivityrunsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let factoryName = "factoryName_example"; // String | The factory name.
let runId = "runId_example"; // String | The pipeline run identifier.
let apiVersion = "apiVersion_example"; // String | The API version.
let filterParameters = new DataFactoryManagementClient.RunFilterParameters(); // RunFilterParameters | Parameters to filter the activity runs.
apiInstance.activityRunsQueryByPipelineRun(subscriptionId, resourceGroupName, factoryName, runId, apiVersion, filterParameters, (error, data, response) => {
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
 **runId** | **String**| The pipeline run identifier. | 
 **apiVersion** | **String**| The API version. | 
 **filterParameters** | [**RunFilterParameters**](RunFilterParameters.md)| Parameters to filter the activity runs. | 

### Return type

[**ActivityRunsQueryResponse**](ActivityRunsQueryResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

