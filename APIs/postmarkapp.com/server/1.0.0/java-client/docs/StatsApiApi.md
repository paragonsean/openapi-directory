# StatsApiApi

All URIs are relative to *http://api.postmarkapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBounceCounts**](StatsApiApi.md#getBounceCounts) | **GET** /stats/outbound/bounces | Get bounce counts |
| [**getOutboundClickCounts**](StatsApiApi.md#getOutboundClickCounts) | **GET** /stats/outbound/clicks | Get click counts |
| [**getOutboundClickCountsByBrowserFamily**](StatsApiApi.md#getOutboundClickCountsByBrowserFamily) | **GET** /stats/outbound/clicks/browserfamilies | Get browser usage by family |
| [**getOutboundClickCountsByLocation**](StatsApiApi.md#getOutboundClickCountsByLocation) | **GET** /stats/outbound/clicks/location | Get clicks by body location |
| [**getOutboundClickCountsByPlatform**](StatsApiApi.md#getOutboundClickCountsByPlatform) | **GET** /stats/outbound/clicks/platforms | Get browser plaform usage |
| [**getOutboundOpenCounts**](StatsApiApi.md#getOutboundOpenCounts) | **GET** /stats/outbound/opens | Get email open counts |
| [**getOutboundOpenCountsByEmailClient**](StatsApiApi.md#getOutboundOpenCountsByEmailClient) | **GET** /stats/outbound/opens/emailclients | Get email client usage |
| [**getOutboundOpenCountsByPlatform**](StatsApiApi.md#getOutboundOpenCountsByPlatform) | **GET** /stats/outbound/opens/platforms | Get email platform usage |
| [**getOutboundOverviewStatistics**](StatsApiApi.md#getOutboundOverviewStatistics) | **GET** /stats/outbound | Get outbound overview |
| [**getSentCounts**](StatsApiApi.md#getSentCounts) | **GET** /stats/outbound/sends | Get sent counts |
| [**getSpamComplaints**](StatsApiApi.md#getSpamComplaints) | **GET** /stats/outbound/spam | Get spam complaints |
| [**getTrackedEmailCounts**](StatsApiApi.md#getTrackedEmailCounts) | **GET** /stats/outbound/tracked | Get tracked email counts |


<a id="getBounceCounts"></a>
# **getBounceCounts**
> GetBounceCounts200Response getBounceCounts(xPostmarkServerToken, tag, fromdate, todate)

Get bounce counts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      GetBounceCounts200Response result = apiInstance.getBounceCounts(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getBounceCounts");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**GetBounceCounts200Response**](GetBounceCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundClickCounts"></a>
# **getOutboundClickCounts**
> Object getOutboundClickCounts(xPostmarkServerToken, tag, fromdate, todate)

Get click counts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      Object result = apiInstance.getOutboundClickCounts(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getOutboundClickCounts");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundClickCountsByBrowserFamily"></a>
# **getOutboundClickCountsByBrowserFamily**
> Object getOutboundClickCountsByBrowserFamily(xPostmarkServerToken, tag, fromdate, todate)

Get browser usage by family

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      Object result = apiInstance.getOutboundClickCountsByBrowserFamily(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getOutboundClickCountsByBrowserFamily");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundClickCountsByLocation"></a>
# **getOutboundClickCountsByLocation**
> Object getOutboundClickCountsByLocation(xPostmarkServerToken, tag, fromdate, todate)

Get clicks by body location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      Object result = apiInstance.getOutboundClickCountsByLocation(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getOutboundClickCountsByLocation");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundClickCountsByPlatform"></a>
# **getOutboundClickCountsByPlatform**
> Object getOutboundClickCountsByPlatform(xPostmarkServerToken, tag, fromdate, todate)

Get browser plaform usage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      Object result = apiInstance.getOutboundClickCountsByPlatform(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getOutboundClickCountsByPlatform");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundOpenCounts"></a>
# **getOutboundOpenCounts**
> GetOutboundOpenCounts200Response getOutboundOpenCounts(xPostmarkServerToken, tag, fromdate, todate)

Get email open counts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      GetOutboundOpenCounts200Response result = apiInstance.getOutboundOpenCounts(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getOutboundOpenCounts");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**GetOutboundOpenCounts200Response**](GetOutboundOpenCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundOpenCountsByEmailClient"></a>
# **getOutboundOpenCountsByEmailClient**
> GetOutboundOpenCountsByEmailClient200Response getOutboundOpenCountsByEmailClient(xPostmarkServerToken, tag, fromdate, todate)

Get email client usage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      GetOutboundOpenCountsByEmailClient200Response result = apiInstance.getOutboundOpenCountsByEmailClient(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getOutboundOpenCountsByEmailClient");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**GetOutboundOpenCountsByEmailClient200Response**](GetOutboundOpenCountsByEmailClient200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundOpenCountsByPlatform"></a>
# **getOutboundOpenCountsByPlatform**
> GetOutboundOpenCountsByPlatform200Response getOutboundOpenCountsByPlatform(xPostmarkServerToken, tag, fromdate, todate)

Get email platform usage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      GetOutboundOpenCountsByPlatform200Response result = apiInstance.getOutboundOpenCountsByPlatform(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getOutboundOpenCountsByPlatform");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**GetOutboundOpenCountsByPlatform200Response**](GetOutboundOpenCountsByPlatform200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getOutboundOverviewStatistics"></a>
# **getOutboundOverviewStatistics**
> OutboundOverviewStatsResponse getOutboundOverviewStatistics(xPostmarkServerToken, tag, fromdate, todate)

Get outbound overview

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      OutboundOverviewStatsResponse result = apiInstance.getOutboundOverviewStatistics(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getOutboundOverviewStatistics");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**OutboundOverviewStatsResponse**](OutboundOverviewStatsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getSentCounts"></a>
# **getSentCounts**
> SentCountsResponse getSentCounts(xPostmarkServerToken, tag, fromdate, todate)

Get sent counts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      SentCountsResponse result = apiInstance.getSentCounts(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getSentCounts");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**SentCountsResponse**](SentCountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getSpamComplaints"></a>
# **getSpamComplaints**
> GetSpamComplaints200Response getSpamComplaints(xPostmarkServerToken, tag, fromdate, todate)

Get spam complaints

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats up to the date specified. e.g. `2014-02-01`
    try {
      GetSpamComplaints200Response result = apiInstance.getSpamComplaints(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getSpamComplaints");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats up to the date specified. e.g. &#x60;2014-02-01&#x60; | [optional] |

### Return type

[**GetSpamComplaints200Response**](GetSpamComplaints200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

<a id="getTrackedEmailCounts"></a>
# **getTrackedEmailCounts**
> GetTrackedEmailCounts200Response getTrackedEmailCounts(xPostmarkServerToken, tag, fromdate, todate)

Get tracked email counts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.postmarkapp.com");

    StatsApiApi apiInstance = new StatsApiApi(defaultClient);
    String xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
    String tag = "tag_example"; // String | Filter by tag
    LocalDate fromdate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    LocalDate todate = LocalDate.now(); // LocalDate | Filter stats starting from the date specified. e.g. `2014-01-01`
    try {
      GetTrackedEmailCounts200Response result = apiInstance.getTrackedEmailCounts(xPostmarkServerToken, tag, fromdate, todate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApiApi#getTrackedEmailCounts");
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
| **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | |
| **tag** | **String**| Filter by tag | [optional] |
| **fromdate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |
| **todate** | **LocalDate**| Filter stats starting from the date specified. e.g. &#x60;2014-01-01&#x60; | [optional] |

### Return type

[**GetTrackedEmailCounts200Response**](GetTrackedEmailCounts200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **422** | An error was generated due to incorrect use of the API. See the Message associated with this response for more information. |  -  |
| **500** | Indicates an internal server error occurred. |  -  |

