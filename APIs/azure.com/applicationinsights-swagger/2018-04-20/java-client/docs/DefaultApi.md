# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsGet**](DefaultApi.md#eventsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/events/{eventType}/{eventId} | Get an event |
| [**eventsGetByType**](DefaultApi.md#eventsGetByType) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/events/{eventType} | Execute OData query |
| [**eventsGetOdataMetadata**](DefaultApi.md#eventsGetOdataMetadata) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/events/$metadata | Get OData metadata |
| [**metricsGet**](DefaultApi.md#metricsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/metrics/{metricId} | Retrieve metric data |
| [**metricsGetMetadata**](DefaultApi.md#metricsGetMetadata) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/metrics/metadata | Retrieve metric metadata |
| [**queryExecute**](DefaultApi.md#queryExecute) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/query | Execute an Analytics query |
| [**queryGet**](DefaultApi.md#queryGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Insights/components/{applicationName}/query | Execute an Analytics query |


<a id="eventsGet"></a>
# **eventsGet**
> EventsResults eventsGet(subscriptionId, resourceGroupName, applicationName, eventType, eventId, apiVersion, timespan)

Get an event

Gets the data for a single event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String applicationName = "applicationName_example"; // String | Name of the Application Insights application.
    String eventType = "$all"; // String | The type of events to query; either a standard event type (`traces`, `customEvents`, `pageViews`, `requests`, `dependencies`, `exceptions`, `availabilityResults`) or `$all` to query across all event types.
    String eventId = "eventId_example"; // String | ID of event.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String timespan = "timespan_example"; // String | Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression.
    try {
      EventsResults result = apiInstance.eventsGet(subscriptionId, resourceGroupName, applicationName, eventType, eventId, apiVersion, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#eventsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **applicationName** | **String**| Name of the Application Insights application. | |
| **eventType** | **String**| The type of events to query; either a standard event type (&#x60;traces&#x60;, &#x60;customEvents&#x60;, &#x60;pageViews&#x60;, &#x60;requests&#x60;, &#x60;dependencies&#x60;, &#x60;exceptions&#x60;, &#x60;availabilityResults&#x60;) or &#x60;$all&#x60; to query across all event types. | [enum: $all, traces, customEvents, pageViews, browserTimings, requests, dependencies, exceptions, availabilityResults, performanceCounters, customMetrics] |
| **eventId** | **String**| ID of event. | |
| **apiVersion** | **String**| Client API version. | |
| **timespan** | **String**| Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression. | [optional] |

### Return type

[**EventsResults**](EventsResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | An error response object. |  -  |

<a id="eventsGetByType"></a>
# **eventsGetByType**
> EventsResults eventsGetByType(subscriptionId, resourceGroupName, applicationName, eventType, apiVersion, timespan, $filter, $search, $orderby, $select, $skip, $top, $format, $count, $apply)

Execute OData query

Executes an OData query for events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String applicationName = "applicationName_example"; // String | Name of the Application Insights application.
    String eventType = "$all"; // String | The type of events to query; either a standard event type (`traces`, `customEvents`, `pageViews`, `requests`, `dependencies`, `exceptions`, `availabilityResults`) or `$all` to query across all event types.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String timespan = "timespan_example"; // String | Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression.
    String $filter = "$filter_example"; // String | An expression used to filter the returned events
    String $search = "$search_example"; // String | A free-text search expression to match for whether a particular event should be returned
    String $orderby = "$orderby_example"; // String | A comma-separated list of properties with \\\"asc\\\" (the default) or \\\"desc\\\" to control the order of returned events
    String $select = "$select_example"; // String | Limits the properties to just those requested on each returned event
    Integer $skip = 56; // Integer | The number of items to skip over before returning events
    Integer $top = 56; // Integer | The number of events to return
    String $format = "$format_example"; // String | Format for the returned events
    Boolean $count = true; // Boolean | Request a count of matching items included with the returned events
    String $apply = "$apply_example"; // String | An expression used for aggregation over returned events
    try {
      EventsResults result = apiInstance.eventsGetByType(subscriptionId, resourceGroupName, applicationName, eventType, apiVersion, timespan, $filter, $search, $orderby, $select, $skip, $top, $format, $count, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#eventsGetByType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **applicationName** | **String**| Name of the Application Insights application. | |
| **eventType** | **String**| The type of events to query; either a standard event type (&#x60;traces&#x60;, &#x60;customEvents&#x60;, &#x60;pageViews&#x60;, &#x60;requests&#x60;, &#x60;dependencies&#x60;, &#x60;exceptions&#x60;, &#x60;availabilityResults&#x60;) or &#x60;$all&#x60; to query across all event types. | [enum: $all, traces, customEvents, pageViews, browserTimings, requests, dependencies, exceptions, availabilityResults, performanceCounters, customMetrics] |
| **apiVersion** | **String**| Client API version. | |
| **timespan** | **String**| Optional. The timespan over which to retrieve events. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the Odata expression. | [optional] |
| **$filter** | **String**| An expression used to filter the returned events | [optional] |
| **$search** | **String**| A free-text search expression to match for whether a particular event should be returned | [optional] |
| **$orderby** | **String**| A comma-separated list of properties with \\\&quot;asc\\\&quot; (the default) or \\\&quot;desc\\\&quot; to control the order of returned events | [optional] |
| **$select** | **String**| Limits the properties to just those requested on each returned event | [optional] |
| **$skip** | **Integer**| The number of items to skip over before returning events | [optional] |
| **$top** | **Integer**| The number of events to return | [optional] |
| **$format** | **String**| Format for the returned events | [optional] |
| **$count** | **Boolean**| Request a count of matching items included with the returned events | [optional] |
| **$apply** | **String**| An expression used for aggregation over returned events | [optional] |

### Return type

[**EventsResults**](EventsResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | An error response object. |  -  |

<a id="eventsGetOdataMetadata"></a>
# **eventsGetOdataMetadata**
> Object eventsGetOdataMetadata(subscriptionId, resourceGroupName, applicationName, apiVersion)

Get OData metadata

Gets OData EDMX metadata describing the event data model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String applicationName = "applicationName_example"; // String | Name of the Application Insights application.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      Object result = apiInstance.eventsGetOdataMetadata(subscriptionId, resourceGroupName, applicationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#eventsGetOdataMetadata");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **applicationName** | **String**| Name of the Application Insights application. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml;charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | An error response object. |  -  |

<a id="metricsGet"></a>
# **metricsGet**
> MetricsResult metricsGet(subscriptionId, resourceGroupName, applicationName, metricId, apiVersion, timespan, interval, aggregation, segment, top, orderby, filter)

Retrieve metric data

Gets metric values for a single metric

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String applicationName = "applicationName_example"; // String | Name of the Application Insights application.
    String metricId = "requests/count"; // String | ID of the metric. This is either a standard AI metric, or an application-specific custom metric.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String timespan = "timespan_example"; // String | The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of `PT12H` (\"last 12 hours\") is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response.
    String interval = "interval_example"; // String | The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response.
    List<String> aggregation = Arrays.asList(); // List<String> | The aggregation to use when computing the metric values. To retrieve more than one aggregation at a time, separate them with a comma. If no aggregation is specified, then the default aggregation for the metric is used.
    List<String> segment = Arrays.asList(); // List<String> | The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter.
    Integer top = 56; // Integer | The number of segments to return.  This value is only valid when segment is specified.
    String orderby = "orderby_example"; // String | The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified.
    String filter = "filter_example"; // String | An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving.
    try {
      MetricsResult result = apiInstance.metricsGet(subscriptionId, resourceGroupName, applicationName, metricId, apiVersion, timespan, interval, aggregation, segment, top, orderby, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#metricsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **applicationName** | **String**| Name of the Application Insights application. | |
| **metricId** | **String**| ID of the metric. This is either a standard AI metric, or an application-specific custom metric. | [enum: requests/count, requests/duration, requests/failed, users/count, users/authenticated, pageViews/count, pageViews/duration, client/processingDuration, client/receiveDuration, client/networkDuration, client/sendDuration, client/totalDuration, dependencies/count, dependencies/failed, dependencies/duration, exceptions/count, exceptions/browser, exceptions/server, sessions/count, performanceCounters/requestExecutionTime, performanceCounters/requestsPerSecond, performanceCounters/requestsInQueue, performanceCounters/memoryAvailableBytes, performanceCounters/exceptionsPerSecond, performanceCounters/processCpuPercentage, performanceCounters/processIOBytesPerSecond, performanceCounters/processPrivateBytes, performanceCounters/processorCpuPercentage, availabilityResults/availabilityPercentage, availabilityResults/duration, billing/telemetryCount, customEvents/count] |
| **apiVersion** | **String**| Client API version. | |
| **timespan** | **String**| The timespan over which to retrieve metric values. This is an ISO8601 time period value. If timespan is omitted, a default time range of &#x60;PT12H&#x60; (\&quot;last 12 hours\&quot;) is used. The actual timespan that is queried may be adjusted by the server based. In all cases, the actual time span used for the query is included in the response. | [optional] |
| **interval** | **String**| The time interval to use when retrieving metric values. This is an ISO8601 duration. If interval is omitted, the metric value is aggregated across the entire timespan. If interval is supplied, the server may adjust the interval to a more appropriate size based on the timespan used for the query. In all cases, the actual interval used for the query is included in the response. | [optional] |
| **aggregation** | [**List&lt;String&gt;**](String.md)| The aggregation to use when computing the metric values. To retrieve more than one aggregation at a time, separate them with a comma. If no aggregation is specified, then the default aggregation for the metric is used. | [optional] [enum: min, max, avg, sum, count, unique] |
| **segment** | [**List&lt;String&gt;**](String.md)| The name of the dimension to segment the metric values by. This dimension must be applicable to the metric you are retrieving. To segment by more than one dimension at a time, separate them with a comma (,). In this case, the metric data will be segmented in the order the dimensions are listed in the parameter. | [optional] [enum: applicationBuild, applicationVersion, authenticatedOrAnonymousTraffic, browser, browserVersion, city, cloudRoleName, cloudServiceName, continent, countryOrRegion, deploymentId, deploymentUnit, deviceType, environment, hostingLocation, instanceName] |
| **top** | **Integer**| The number of segments to return.  This value is only valid when segment is specified. | [optional] |
| **orderby** | **String**| The aggregation function and direction to sort the segments by.  This value is only valid when segment is specified. | [optional] |
| **filter** | **String**| An expression used to filter the results.  This value should be a valid OData filter expression where the keys of each clause should be applicable dimensions for the metric you are retrieving. | [optional] |

### Return type

[**MetricsResult**](MetricsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | An error response object. |  -  |

<a id="metricsGetMetadata"></a>
# **metricsGetMetadata**
> Object metricsGetMetadata(subscriptionId, resourceGroupName, applicationName, apiVersion)

Retrieve metric metadata

Gets metadata describing the available metrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String applicationName = "applicationName_example"; // String | Name of the Application Insights application.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      Object result = apiInstance.metricsGetMetadata(subscriptionId, resourceGroupName, applicationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#metricsGetMetadata");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **applicationName** | **String**| Name of the Application Insights application. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful responses |  -  |
| **0** | An error response object. |  -  |

<a id="queryExecute"></a>
# **queryExecute**
> QueryResults queryExecute(subscriptionId, resourceGroupName, applicationName, apiVersion, body)

Execute an Analytics query

Executes an Analytics query for data. [Here](https://dev.applicationinsights.io/documentation/Using-the-API/Query) is an example for using POST with an Analytics query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String applicationName = "applicationName_example"; // String | Name of the Application Insights application.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    QueryBody body = new QueryBody(); // QueryBody | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
    try {
      QueryResults result = apiInstance.queryExecute(subscriptionId, resourceGroupName, applicationName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queryExecute");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **applicationName** | **String**| Name of the Application Insights application. | |
| **apiVersion** | **String**| Client API version. | |
| **body** | [**QueryBody**](QueryBody.md)| The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) | |

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | An error response object. |  -  |

<a id="queryGet"></a>
# **queryGet**
> QueryResults queryGet(subscriptionId, resourceGroupName, applicationName, query, apiVersion, timespan)

Execute an Analytics query

Executes an Analytics query for data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String applicationName = "applicationName_example"; // String | Name of the Application Insights application.
    String query = "query_example"; // String | The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/)
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String timespan = "timespan_example"; // String | Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression.
    try {
      QueryResults result = apiInstance.queryGet(subscriptionId, resourceGroupName, applicationName, query, apiVersion, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#queryGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **applicationName** | **String**| Name of the Application Insights application. | |
| **query** | **String**| The Analytics query. Learn more about the [Analytics query syntax](https://azure.microsoft.com/documentation/articles/app-insights-analytics-reference/) | |
| **apiVersion** | **String**| Client API version. | |
| **timespan** | **String**| Optional. The timespan over which to query data. This is an ISO8601 time period value.  This timespan is applied in addition to any that are specified in the query expression. | [optional] |

### Return type

[**QueryResults**](QueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | An error response object. |  -  |

