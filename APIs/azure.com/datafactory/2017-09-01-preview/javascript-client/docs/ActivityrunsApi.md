# DataFactoryManagementClient.ActivityrunsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activityRunsListByPipelineRun**](ActivityrunsApi.md#activityRunsListByPipelineRun) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelineruns/{runId}/activityruns | 



## activityRunsListByPipelineRun

> ActivityRunsListResponse activityRunsListByPipelineRun(subscriptionId, resourceGroupName, factoryName, runId, apiVersion, startTime, endTime, opts)



List activity runs based on input filter conditions.

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
let startTime = new Date("2013-10-20T19:20:30+01:00"); // Date | The start time of activity runs in ISO8601 format.
let endTime = new Date("2013-10-20T19:20:30+01:00"); // Date | The end time of activity runs in ISO8601 format.
let opts = {
  'status': "status_example", // String | The status of the pipeline run.
  'activityName': "activityName_example", // String | The name of the activity.
  'linkedServiceName': "linkedServiceName_example" // String | The linked service name.
};
apiInstance.activityRunsListByPipelineRun(subscriptionId, resourceGroupName, factoryName, runId, apiVersion, startTime, endTime, opts, (error, data, response) => {
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
 **startTime** | **Date**| The start time of activity runs in ISO8601 format. | 
 **endTime** | **Date**| The end time of activity runs in ISO8601 format. | 
 **status** | **String**| The status of the pipeline run. | [optional] 
 **activityName** | **String**| The name of the activity. | [optional] 
 **linkedServiceName** | **String**| The linked service name. | [optional] 

### Return type

[**ActivityRunsListResponse**](ActivityRunsListResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

