# MonitorClient.MetricsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metricsList**](MetricsApi.md#metricsList) | **GET** /{resourceUri}/providers/microsoft.insights/metrics | 



## metricsList

> MetricCollection metricsList(resourceUri, apiVersion, opts)



Lists the metric values for a resource.

### Example

```javascript
import MonitorClient from 'monitor_client';
let defaultClient = MonitorClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorClient.MetricsApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | Reduces the set of data collected.<br>The filter is optional. If present it must contain a list of metric names to retrieve of the form: *(name.value eq 'metricName' [or name.value eq 'metricName' or ...])*. Optionally, the filter can contain conditions for the following attributes *aggregationType*, *startTime*, *endTime*, and *timeGrain* of the form *attributeName operator value*. Where operator is one of *ne*, *eq*, *gt*, *lt*.<br>Several conditions can be combined with parentheses and logical operators, e.g: *and*, *or*.<br>Some example filter expressions are:<br>- $filter=(name.value eq 'RunsSucceeded') and aggregationType eq 'Total' and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1M',<br>- $filter=(name.value eq 'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq 'Average') and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1H',<br>- $filter=(name.value eq 'ActionsCompleted' or name.value eq 'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq 'Average') and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1M'.<br><br>**NOTE**: When a metrics query comes in with multiple metrics, but with no aggregation types defined, the service will pick the Primary aggregation type of the first metrics to be used as the default aggregation type for all the metrics.
};
apiInstance.metricsList(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| Reduces the set of data collected.&lt;br&gt;The filter is optional. If present it must contain a list of metric names to retrieve of the form: *(name.value eq &#39;metricName&#39; [or name.value eq &#39;metricName&#39; or ...])*. Optionally, the filter can contain conditions for the following attributes *aggregationType*, *startTime*, *endTime*, and *timeGrain* of the form *attributeName operator value*. Where operator is one of *ne*, *eq*, *gt*, *lt*.&lt;br&gt;Several conditions can be combined with parentheses and logical operators, e.g: *and*, *or*.&lt;br&gt;Some example filter expressions are:&lt;br&gt;- $filter&#x3D;(name.value eq &#39;RunsSucceeded&#39;) and aggregationType eq &#39;Total&#39; and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1M&#39;,&lt;br&gt;- $filter&#x3D;(name.value eq &#39;RunsSucceeded&#39;) and (aggregationType eq &#39;Total&#39; or aggregationType eq &#39;Average&#39;) and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1H&#39;,&lt;br&gt;- $filter&#x3D;(name.value eq &#39;ActionsCompleted&#39; or name.value eq &#39;RunsSucceeded&#39;) and (aggregationType eq &#39;Total&#39; or aggregationType eq &#39;Average&#39;) and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1M&#39;.&lt;br&gt;&lt;br&gt;**NOTE**: When a metrics query comes in with multiple metrics, but with no aggregation types defined, the service will pick the Primary aggregation type of the first metrics to be used as the default aggregation type for all the metrics. | [optional] 

### Return type

[**MetricCollection**](MetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

