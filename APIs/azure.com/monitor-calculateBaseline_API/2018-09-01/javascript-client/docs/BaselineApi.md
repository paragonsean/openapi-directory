# MonitorManagementClient.BaselineApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricBaselineCalculateBaseline**](BaselineApi.md#metricBaselineCalculateBaseline) | **POST** /{resourceUri}/providers/microsoft.insights/calculatebaseline | 



## metricBaselineCalculateBaseline

> CalculateBaselineResponse metricBaselineCalculateBaseline(resourceUri, apiVersion, timeSeriesInformation)



**Lists the baseline values for a resource**.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.BaselineApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource. It has the following structure: subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}. For example: subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let timeSeriesInformation = new MonitorManagementClient.TimeSeriesInformation(); // TimeSeriesInformation | Information that need to be specified to calculate a baseline on a time series.
apiInstance.metricBaselineCalculateBaseline(resourceUri, apiVersion, timeSeriesInformation, (error, data, response) => {
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
 **resourceUri** | **String**| The identifier of the resource. It has the following structure: subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}. For example: subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1 | 
 **apiVersion** | **String**| Client Api Version. | 
 **timeSeriesInformation** | [**TimeSeriesInformation**](TimeSeriesInformation.md)| Information that need to be specified to calculate a baseline on a time series. | 

### Return type

[**CalculateBaselineResponse**](CalculateBaselineResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

