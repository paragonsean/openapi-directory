# MonitorClient.MetricDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricDefinitionsList**](MetricDefinitionsApi.md#metricDefinitionsList) | **GET** /{resourceUri}/providers/microsoft.insights/metricDefinitions | 



## metricDefinitionsList

> MetricDefinitionCollection metricDefinitionsList(resourceUri, apiVersion, opts)



Lists the metric definitions for the resource.

### Example

```javascript
import MonitorClient from 'monitor_client';
let defaultClient = MonitorClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorClient.MetricDefinitionsApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | Reduces the set of data collected by retrieving particular metric definitions from all the definitions available for the resource.<br>For example, to get just the definition for the 'CPU percentage' counter: $filter=name.value eq '\\Processor(_Total)\\% Processor Time'.<br>Multiple metrics can be retrieved by joining together *'name eq <value>'* clauses separated by *or* logical operators.<br>**NOTE**: No other syntax is allowed.
};
apiInstance.metricDefinitionsList(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **resourceUri** | **String**| The identifier of the resource. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| Reduces the set of data collected by retrieving particular metric definitions from all the definitions available for the resource.&lt;br&gt;For example, to get just the definition for the &#39;CPU percentage&#39; counter: $filter&#x3D;name.value eq &#39;\\Processor(_Total)\\% Processor Time&#39;.&lt;br&gt;Multiple metrics can be retrieved by joining together *&#39;name eq &lt;value&gt;&#39;* clauses separated by *or* logical operators.&lt;br&gt;**NOTE**: No other syntax is allowed. | [optional] 

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

