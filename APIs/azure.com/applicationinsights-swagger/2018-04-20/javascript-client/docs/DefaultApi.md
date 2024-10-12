# ApplicationInsightsDataPlane.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsGet**](DefaultApi.md#eventsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/events/{eventType}/{eventId} | Get an event
[**eventsGetByType**](DefaultApi.md#eventsGetByType) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/events/{eventType} | Execute OData query
[**eventsGetOdataMetadata**](DefaultApi.md#eventsGetOdataMetadata) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/events/$metadata | Get OData metadata
[**metricsGet**](DefaultApi.md#metricsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/metrics/{metricId} | Retrieve metric data
[**metricsGetMetadata**](DefaultApi.md#metricsGetMetadata) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/metrics/metadata | Retrieve metric metadata
[**queryExecute**](DefaultApi.md#queryExecute) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/query | Execute an Analytics query
[**queryGet**](DefaultApi.md#queryGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/query | Execute an Analytics query



## eventsGet

> EventsResults eventsGet(subscriptionId, resourceGroupName, applicationName, eventType, eventId, apiVersion, opts)

Get an event

Gets the data for a single event

### Example

```javascript
import ApplicationInsightsDataPlane from 'application_insights_data_plane';
let defaultClient = ApplicationInsightsDataPlane.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsDataPlane.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let applicationName = "applicationName_example"; // String | Name of the Application Insights application.
let eventType = "eventType_example"; // String | The type of events to query; either a standard event type (`traces`, `customEvents`, `pageViews`, `requests`, `dependencies`, `exceptions`, `availabilityResults`) or `$all` to query across all event types.
let eventId = "eventId_example"; // String | ID of event.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'timespan': "timespan_example" // String | Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression.
};
apiInstance.eventsGet(subscriptionId, resourceGroupName, applicationName, eventType, eventId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **applicationName** | **String**| Name of the Application Insights application. | 
 **eventType** | **String**| The type of events to query; either a standard event type (&#x60;traces&#x60;, &#x60;customEvents&#x60;, &#x60;pageViews&#x60;, &#x60;requests&#x60;, &#x60;dependencies&#x60;, &#x60;exceptions&#x60;, &#x60;availabilityResults&#x60;) or &#x60;$all&#x60; to query across all event types. | 
 **eventId** | **String**| ID of event. | 
 **apiVersion** | **String**| Client API version. | 
 **timespan** | **String**| Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression. | [optional] 

### Return type

[**EventsResults**](EventsResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsGetByType

> EventsResults eventsGetByType(subscriptionId, resourceGroupName, applicationName, eventType, apiVersion, opts)

Execute OData query

Executes an OData query for events

### Example

```javascript
import ApplicationInsightsDataPlane from 'application_insights_data_plane';
let defaultClient = ApplicationInsightsDataPlane.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsDataPlane.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let applicationName = "applicationName_example"; // String | Name of the Application Insights application.
let eventType = "eventType_example"; // String | The type of events to query; either a standard event type (`traces`, `customEvents`, `pageViews`, `requests`, `dependencies`, `exceptions`, `availabilityResults`) or `$all` to query across all event types.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'timespan': "timespan_example", // String | Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression.
  'filter': "filter_example", // String | An expression used to filter the returned events
  'search': "search_example", // String | A free-text search expression to match for whether a particular event should be returned
  'orderby': "orderby_example", // String | A comma-separated list of properties with \\\"asc\\\" (the default) or \\\"desc\\\" to control the order of returned events
  'select': "select_example", // String | Limits the properties to just those requested on each returned event
  'skip': 56, // Number | The number of items to skip over before returning events
  'top': 56, // Number | The number of events to return
  'format': "format_example", // String | Format for the returned events
  'count': true, // Boolean | Request a count of matching items included with the returned events
  'apply': "apply_example" // String | An expression used for aggregation over returned events
};
apiInstance.eventsGetByType(subscriptionId, resourceGroupName, applicationName, eventType, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **applicationName** | **String**| Name of the Application Insights application. | 
 **eventType** | **String**| The type of events to query; either a standard event type (&#x60;traces&#x60;, &#x60;customEvents&#x60;, &#x60;pageViews&#x60;, &#x60;requests&#x60;, &#x60;dependencies&#x60;, &#x60;exceptions&#x60;, &#x60;availabilityResults&#x60;) or &#x60;$all&#x60; to query across all event types. | 
 **apiVersion** | **String**| Client API version. | 
 **timespan** | **String**| Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression. | [optional] 
 **filter** | **String**| An expression used to filter the returned events | [optional] 
 **search** | **String**| A free-text search expression to match for whether a particular event should be returned | [optional] 
 **orderby** | **String**| A comma-separated list of properties with \\\&quot;asc\\\&quot; (the default) or \\\&quot;desc\\\&quot; to control the order of returned events | [optional] 
 **select** | **String**| Limits the properties to just those requested on each returned event | [optional] 
 **skip** | **Number**| The number of items to skip over before returning events | [optional] 
 **top** | **Number**| The number of events to return | [optional] 
 **format** | **String**| Format for the returned events | [optional] 
 **count** | **Boolean**| Request a count of matching items included with the returned events | [optional] 
 **apply** | **String**| An expression used for aggregation over returned events | [optional] 

### Return type

[**EventsResults**](EventsResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsGetOdataMetadata

> Object eventsGetOdataMetadata(subscriptionId, resourceGroupName, applicationName, apiVersion)

Get OData metadata

Gets OData EDMX metadata describing the event data model

### Example

```javascript
import ApplicationInsightsDataPlane from 'application_insights_data_plane';
let defaultClient = ApplicationInsightsDataPlane.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsDataPlane.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let applicationName = "applicationName_example"; // String | Name of the Application Insights application.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.eventsGetOdataMetadata(subscriptionId, resourceGroupName, applicationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **applicationName** | **String**| Name of the Application Insights application. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml;charset=utf-8


## metricsGet

> MetricsResult metricsGet(subscriptionId, resourceGroupName, applicationName, metricId, apiVersion, opts)

Retrieve metric data

Gets metric values for a single metric

### Example

```javascript
import ApplicationInsightsDataPlane from 'application_insights_data_plane';
let defaultClient = ApplicationInsightsDataPlane.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsDataPlane.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let applicationName = "applicationName_example"; // String | Name of the Application Insights application.
let metricId = "metricId_example"; // String | ID of the metric. This is either a standard AI metric, or an application-specific custom metric.
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'timespan': "timespan_example", // String | The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of `PT12H` (\"last 12 hours\") is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response.
  'interval': "interval_example", // String | The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response.
  'aggregation': ["null"], // [String] | The aggregation to use when computing the metric values. To retrieve more than one aggregation at a time, separate them with a comma. If no aggregation is specified, then the default aggregation for the metric is used.
  'segment': ["null"], // [String] | The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter.
  'top': 56, // Number | The number of segments to return.  This value is only valid when segment is specified.
  'orderby': "orderby_example", // String | The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified.
  'filter': "filter_example" // String | An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving.
};
apiInstance.metricsGet(subscriptionId, resourceGroupName, applicationName, metricId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **applicationName** | **String**| Name of the Application Insights application. | 
 **metricId** | **String**| ID of the metric. This is either a standard AI metric, or an application-specific custom metric. | 
 **apiVersion** | **String**| Client API version. | 
 **timespan** | **String**| The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of &#x60;PT12H&#x60; (\&quot;last 12 hours\&quot;) is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response. | [optional] 
 **interval** | **String**| The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response. | [optional] 
 **aggregation** | [**[String]**](String.md)| The aggregation to use when computing the metric values. To retrieve more than one aggregation at a time, separate them with a comma. If no aggregation is specified, then the default aggregation for the metric is used. | [optional] 
 **segment** | [**[String]**](String.md)| The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter. | [optional] 
 **top** | **Number**| The number of segments to return.  This value is only valid when segment is specified. | [optional] 
 **orderby** | **String**| The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified. | [optional] 
 **filter** | **String**| An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving. | [optional] 

### Return type

[**MetricsResult**](MetricsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## metricsGetMetadata

> Object metricsGetMetadata(subscriptionId, resourceGroupName, applicationName, apiVersion)

Retrieve metric metadata

Gets metadata describing the available metrics

### Example

```javascript
import ApplicationInsightsDataPlane from 'application_insights_data_plane';
let defaultClient = ApplicationInsightsDataPlane.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsDataPlane.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let applicationName = "applicationName_example"; // String | Name of the Application Insights application.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.metricsGetMetadata(subscriptionId, resourceGroupName, applicationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **applicationName** | **String**| Name of the Application Insights application. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryExecute

> QueryResults queryExecute(subscriptionId, resourceGroupName, applicationName, apiVersion, body)

Execute an Analytics query

Executes an Analytics query for data. [Here](https://dev.applicationinsights.io/documentation/Using-the-API/Query) is an example for using POST with an Analytics query.

### Example

```javascript
import ApplicationInsightsDataPlane from 'application_insights_data_plane';
let defaultClient = ApplicationInsightsDataPlane.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsDataPlane.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let applicationName = "applicationName_example"; // String | Name of the Application Insights application.
let apiVersion = "apiVersion_example"; // String | Client API version.
let body = new ApplicationInsightsDataPlane.QueryBody(); // QueryBody | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
apiInstance.queryExecute(subscriptionId, resourceGroupName, applicationName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **applicationName** | **String**| Name of the Application Insights application. | 
 **apiVersion** | **String**| Client API version. | 
 **body** | [**QueryBody**](QueryBody.md)| The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) | 

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryGet

> QueryResults queryGet(subscriptionId, resourceGroupName, applicationName, query, apiVersion, opts)

Execute an Analytics query

Executes an Analytics query for data

### Example

```javascript
import ApplicationInsightsDataPlane from 'application_insights_data_plane';
let defaultClient = ApplicationInsightsDataPlane.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsDataPlane.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let applicationName = "applicationName_example"; // String | Name of the Application Insights application.
let query = "query_example"; // String | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
let apiVersion = "apiVersion_example"; // String | Client API version.
let opts = {
  'timespan': "timespan_example" // String | Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression.
};
apiInstance.queryGet(subscriptionId, resourceGroupName, applicationName, query, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **applicationName** | **String**| Name of the Application Insights application. | 
 **query** | **String**| The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) | 
 **apiVersion** | **String**| Client API version. | 
 **timespan** | **String**| Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression. | [optional] 

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

