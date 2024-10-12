# MonitorManagementClient.MetricApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**baselinesList_0**](MetricApi.md#baselinesList_0) | **GET** /{resourceUri}/providers/microsoft.insights/metricBaselines | 



## baselinesList_0

> MetricBaselinesResponse baselinesList_0(resourceUri, apiVersion, opts)



**Lists the metric baseline values for a resource**.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.MetricApi();
let resourceUri = "resourceUri_example"; // String | The identifier of the resource.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'metricnames': "metricnames_example", // String | The names of the metrics (comma separated) to retrieve.
  'metricnamespace': "metricnamespace_example", // String | Metric namespace to query metric definitions for.
  'timespan': "timespan_example", // String | The timespan of the query. It is a string with the following format 'startDateTime_ISO/endDateTime_ISO'.
  'interval': "interval_example", // String | The interval (i.e. timegrain) of the query.
  'aggregation': "aggregation_example", // String | The list of aggregation types (comma separated) to retrieve.
  'sensitivities': "sensitivities_example", // String | The list of sensitivities (comma separated) to retrieve.
  'filter': "filter_example", // String | The **$filter** is used to reduce the set of metric data returned.<br>Example:<br>Metric contains metadata A, B and C.<br>- Return all time series of C where A = a1 and B = b1 or b2<br>**$filter=A eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**<br>- Invalid variant:<br>**$filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B = ‘b2’**<br>This is invalid because the logical or operator cannot separate two different metadata names.<br>- Return all time series where A = a1, B = b1 and C = c1:<br>**$filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**<br>- Return all time series where A = a1<br>**$filter=A eq ‘a1’ and B eq ‘*’ and C eq ‘*’**.
  'resultType': "resultType_example" // String | Allows retrieving only metadata of the baseline. On data request all information is retrieved.
};
apiInstance.baselinesList_0(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **metricnames** | **String**| The names of the metrics (comma separated) to retrieve. | [optional] 
 **metricnamespace** | **String**| Metric namespace to query metric definitions for. | [optional] 
 **timespan** | **String**| The timespan of the query. It is a string with the following format &#39;startDateTime_ISO/endDateTime_ISO&#39;. | [optional] 
 **interval** | **String**| The interval (i.e. timegrain) of the query. | [optional] 
 **aggregation** | **String**| The list of aggregation types (comma separated) to retrieve. | [optional] 
 **sensitivities** | **String**| The list of sensitivities (comma separated) to retrieve. | [optional] 
 **filter** | **String**| The **$filter** is used to reduce the set of metric data returned.&lt;br&gt;Example:&lt;br&gt;Metric contains metadata A, B and C.&lt;br&gt;- Return all time series of C where A &#x3D; a1 and B &#x3D; b1 or b2&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**&lt;br&gt;- Invalid variant:&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B &#x3D; ‘b2’**&lt;br&gt;This is invalid because the logical or operator cannot separate two different metadata names.&lt;br&gt;- Return all time series where A &#x3D; a1, B &#x3D; b1 and C &#x3D; c1:&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**&lt;br&gt;- Return all time series where A &#x3D; a1&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘*’ and C eq ‘*’**. | [optional] 
 **resultType** | **String**| Allows retrieving only metadata of the baseline. On data request all information is retrieved. | [optional] 

### Return type

[**MetricBaselinesResponse**](MetricBaselinesResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

