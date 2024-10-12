# RealTimeApi

All URIs are relative to *https://api.mux.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRealtimeBreakdown**](RealTimeApi.md#getRealtimeBreakdown) | **GET** /data/v1/realtime/metrics/{REALTIME_METRIC_ID}/breakdown | Get Real-Time Breakdown |
| [**getRealtimeHistogramTimeseries**](RealTimeApi.md#getRealtimeHistogramTimeseries) | **GET** /data/v1/realtime/metrics/{REALTIME_HISTOGRAM_METRIC_ID}/histogram-timeseries | Get Real-Time Histogram Timeseries |
| [**getRealtimeTimeseries**](RealTimeApi.md#getRealtimeTimeseries) | **GET** /data/v1/realtime/metrics/{REALTIME_METRIC_ID}/timeseries | Get Real-Time Timeseries |
| [**listRealtimeDimensions**](RealTimeApi.md#listRealtimeDimensions) | **GET** /data/v1/realtime/dimensions | List Real-Time Dimensions |
| [**listRealtimeMetrics**](RealTimeApi.md#listRealtimeMetrics) | **GET** /data/v1/realtime/metrics | List Real-Time Metrics |


<a id="getRealtimeBreakdown"></a>
# **getRealtimeBreakdown**
> GetRealTimeBreakdownResponse getRealtimeBreakdown(REALTIME_METRIC_ID).dimension(dimension).timestamp(timestamp).filters(filters).orderBy(orderBy).orderDirection(orderDirection).execute();

Get Real-Time Breakdown

Gets breakdown information for a specific dimension and metric along with the number of concurrent viewers and negative impact score. This API is now deprecated, please use the &#x60;Get Monitoring Breakdown&#x60; API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mux.com");
    
    // Configure HTTP basic authorization: accessToken
    HttpBasicAuth accessToken = (HttpBasicAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setUsername("YOUR USERNAME");
    accessToken.setPassword("YOUR PASSWORD");

    RealTimeApi apiInstance = new RealTimeApi(defaultClient);
    String REALTIME_METRIC_ID = "current-concurrent-viewers"; // String | ID of the Realtime Metric
    String dimension = "asn"; // String | Dimension the specified value belongs to
    Integer timestamp = 56; // Integer | Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp.
    List<String> filters = Arrays.asList(); // List<String> | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
    String orderBy = "negative_impact"; // String | Value to order the results by
    String orderDirection = "asc"; // String | Sort order.
    try {
      GetRealTimeBreakdownResponse result = apiInstance.getRealtimeBreakdown(REALTIME_METRIC_ID)
            .dimension(dimension)
            .timestamp(timestamp)
            .filters(filters)
            .orderBy(orderBy)
            .orderDirection(orderDirection)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealTimeApi#getRealtimeBreakdown");
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
| **REALTIME_METRIC_ID** | **String**| ID of the Realtime Metric | [enum: current-concurrent-viewers, current-rebuffering-percentage, exits-before-video-start, playback-failure-percentage, current-average-bitrate] |
| **dimension** | **String**| Dimension the specified value belongs to | [optional] [enum: asn, cdn, country, operating_system, player_name, region, stream_type, sub_property_id, video_series, video_title] |
| **timestamp** | **Integer**| Timestamp to limit results by. This value must be provided as a unix timestamp. Defaults to the current unix timestamp. | [optional] |
| **filters** | [**List&lt;String&gt;**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] |
| **orderBy** | **String**| Value to order the results by | [optional] [enum: negative_impact, value, views, field] |
| **orderDirection** | **String**| Sort order. | [optional] [enum: asc, desc] |

### Return type

[**GetRealTimeBreakdownResponse**](GetRealTimeBreakdownResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getRealtimeHistogramTimeseries"></a>
# **getRealtimeHistogramTimeseries**
> GetRealTimeHistogramTimeseriesResponse getRealtimeHistogramTimeseries(REALTIME_HISTOGRAM_METRIC_ID).filters(filters).execute();

Get Real-Time Histogram Timeseries

Gets histogram timeseries information for a specific metric. This API is now deprecated, please use the &#x60;Get Monitoring Histogram Timeseries&#x60; API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mux.com");
    
    // Configure HTTP basic authorization: accessToken
    HttpBasicAuth accessToken = (HttpBasicAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setUsername("YOUR USERNAME");
    accessToken.setPassword("YOUR PASSWORD");

    RealTimeApi apiInstance = new RealTimeApi(defaultClient);
    String REALTIME_HISTOGRAM_METRIC_ID = "video-startup-time"; // String | ID of the Realtime Histogram Metric
    List<String> filters = Arrays.asList(); // List<String> | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
    try {
      GetRealTimeHistogramTimeseriesResponse result = apiInstance.getRealtimeHistogramTimeseries(REALTIME_HISTOGRAM_METRIC_ID)
            .filters(filters)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealTimeApi#getRealtimeHistogramTimeseries");
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
| **REALTIME_HISTOGRAM_METRIC_ID** | **String**| ID of the Realtime Histogram Metric | [enum: video-startup-time] |
| **filters** | [**List&lt;String&gt;**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] |

### Return type

[**GetRealTimeHistogramTimeseriesResponse**](GetRealTimeHistogramTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getRealtimeTimeseries"></a>
# **getRealtimeTimeseries**
> GetRealTimeTimeseriesResponse getRealtimeTimeseries(REALTIME_METRIC_ID).filters(filters).timestamp(timestamp).execute();

Get Real-Time Timeseries

Gets Time series information for a specific metric along with the number of concurrent viewers. This API is now deprecated, please use the &#x60;Get Monitoring Timeseries&#x60; API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mux.com");
    
    // Configure HTTP basic authorization: accessToken
    HttpBasicAuth accessToken = (HttpBasicAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setUsername("YOUR USERNAME");
    accessToken.setPassword("YOUR PASSWORD");

    RealTimeApi apiInstance = new RealTimeApi(defaultClient);
    String REALTIME_METRIC_ID = "current-concurrent-viewers"; // String | ID of the Realtime Metric
    List<String> filters = Arrays.asList(); // List<String> | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US` 
    Integer timestamp = 56; // Integer | Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago.
    try {
      GetRealTimeTimeseriesResponse result = apiInstance.getRealtimeTimeseries(REALTIME_METRIC_ID)
            .filters(filters)
            .timestamp(timestamp)
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealTimeApi#getRealtimeTimeseries");
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
| **REALTIME_METRIC_ID** | **String**| ID of the Realtime Metric | [enum: current-concurrent-viewers, current-rebuffering-percentage, exits-before-video-start, playback-failure-percentage, current-average-bitrate] |
| **filters** | [**List&lt;String&gt;**](String.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Monitoring Dimensions endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] |
| **timestamp** | **Integer**| Timestamp to use as the start of the timeseries data. This value must be provided as a unix timestamp. Defaults to 30 minutes ago. | [optional] |

### Return type

[**GetRealTimeTimeseriesResponse**](GetRealTimeTimeseriesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRealtimeDimensions"></a>
# **listRealtimeDimensions**
> ListRealTimeDimensionsResponse listRealtimeDimensions().execute();

List Real-Time Dimensions

Lists available real-time dimensions. This API is now deprecated, please use the &#x60;List Monitoring Dimensions&#x60; API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mux.com");
    
    // Configure HTTP basic authorization: accessToken
    HttpBasicAuth accessToken = (HttpBasicAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setUsername("YOUR USERNAME");
    accessToken.setPassword("YOUR PASSWORD");

    RealTimeApi apiInstance = new RealTimeApi(defaultClient);
    try {
      ListRealTimeDimensionsResponse result = apiInstance.listRealtimeDimensions()
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealTimeApi#listRealtimeDimensions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRealTimeDimensionsResponse**](ListRealTimeDimensionsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listRealtimeMetrics"></a>
# **listRealtimeMetrics**
> ListRealTimeMetricsResponse listRealtimeMetrics().execute();

List Real-Time Metrics

Lists available real-time metrics. This API is now deprecated, please use the &#x60;List Monitoring Metrics&#x60; API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mux.com");
    
    // Configure HTTP basic authorization: accessToken
    HttpBasicAuth accessToken = (HttpBasicAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setUsername("YOUR USERNAME");
    accessToken.setPassword("YOUR PASSWORD");

    RealTimeApi apiInstance = new RealTimeApi(defaultClient);
    try {
      ListRealTimeMetricsResponse result = apiInstance.listRealtimeMetrics()
            .execute();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealTimeApi#listRealtimeMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListRealTimeMetricsResponse**](ListRealTimeMetricsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

