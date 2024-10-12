# ReportsApi

All URIs are relative to *https://demo.traccar.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsEventsGet**](ReportsApi.md#reportsEventsGet) | **GET** /reports/events | Fetch a list of Events within the time period for the Devices or Groups |
| [**reportsRouteGet**](ReportsApi.md#reportsRouteGet) | **GET** /reports/route | Fetch a list of Positions within the time period for the Devices or Groups |
| [**reportsStopsGet**](ReportsApi.md#reportsStopsGet) | **GET** /reports/stops | Fetch a list of ReportStops within the time period for the Devices or Groups |
| [**reportsSummaryGet**](ReportsApi.md#reportsSummaryGet) | **GET** /reports/summary | Fetch a list of ReportSummary within the time period for the Devices or Groups |
| [**reportsTripsGet**](ReportsApi.md#reportsTripsGet) | **GET** /reports/trips | Fetch a list of ReportTrips within the time period for the Devices or Groups |


<a id="reportsEventsGet"></a>
# **reportsEventsGet**
> List&lt;Event&gt; reportsEventsGet(from, to, deviceId, groupId, type)

Fetch a list of Events within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    List<Integer> deviceId = Arrays.asList(); // List<Integer> | 
    List<Integer> groupId = Arrays.asList(); // List<Integer> | 
    List<String> type = Arrays.asList(); // List<String> | % can be used to return events of all types
    try {
      List<Event> result = apiInstance.reportsEventsGet(from, to, deviceId, groupId, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsEventsGet");
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
| **from** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **to** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **deviceId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **groupId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **type** | [**List&lt;String&gt;**](String.md)| % can be used to return events of all types | [optional] |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reportsRouteGet"></a>
# **reportsRouteGet**
> List&lt;Position&gt; reportsRouteGet(from, to, deviceId, groupId)

Fetch a list of Positions within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    List<Integer> deviceId = Arrays.asList(); // List<Integer> | 
    List<Integer> groupId = Arrays.asList(); // List<Integer> | 
    try {
      List<Position> result = apiInstance.reportsRouteGet(from, to, deviceId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsRouteGet");
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
| **from** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **to** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **deviceId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **groupId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**List&lt;Position&gt;**](Position.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reportsStopsGet"></a>
# **reportsStopsGet**
> List&lt;ReportStops&gt; reportsStopsGet(from, to, deviceId, groupId)

Fetch a list of ReportStops within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    List<Integer> deviceId = Arrays.asList(); // List<Integer> | 
    List<Integer> groupId = Arrays.asList(); // List<Integer> | 
    try {
      List<ReportStops> result = apiInstance.reportsStopsGet(from, to, deviceId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsStopsGet");
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
| **from** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **to** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **deviceId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **groupId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**List&lt;ReportStops&gt;**](ReportStops.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reportsSummaryGet"></a>
# **reportsSummaryGet**
> List&lt;ReportSummary&gt; reportsSummaryGet(from, to, deviceId, groupId)

Fetch a list of ReportSummary within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    List<Integer> deviceId = Arrays.asList(); // List<Integer> | 
    List<Integer> groupId = Arrays.asList(); // List<Integer> | 
    try {
      List<ReportSummary> result = apiInstance.reportsSummaryGet(from, to, deviceId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsSummaryGet");
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
| **from** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **to** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **deviceId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **groupId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**List&lt;ReportSummary&gt;**](ReportSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reportsTripsGet"></a>
# **reportsTripsGet**
> List&lt;ReportTrips&gt; reportsTripsGet(from, to, deviceId, groupId)

Fetch a list of ReportTrips within the time period for the Devices or Groups

At least one _deviceId_ or one _groupId_ must be passed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    List<Integer> deviceId = Arrays.asList(); // List<Integer> | 
    List<Integer> groupId = Arrays.asList(); // List<Integer> | 
    try {
      List<ReportTrips> result = apiInstance.reportsTripsGet(from, to, deviceId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsTripsGet");
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
| **from** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **to** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **deviceId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **groupId** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |

### Return type

[**List&lt;ReportTrips&gt;**](ReportTrips.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

