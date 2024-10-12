# DefaultApi

All URIs are relative to *https://quickchart.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartGet**](DefaultApi.md#chartGet) | **GET** /chart | Generate a chart (GET) |
| [**chartPost**](DefaultApi.md#chartPost) | **POST** /chart | Generate a chart (POST) |
| [**qrGet**](DefaultApi.md#qrGet) | **GET** /qr | Generate a QR code (GET) |
| [**qrPost**](DefaultApi.md#qrPost) | **POST** /qr | Generate a QR code (POST) |


<a id="chartGet"></a>
# **chartGet**
> File chartGet(chart, width, height, format, backgroundColor)

Generate a chart (GET)

Generate a chart based on the provided parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quickchart.io");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String chart = "chart_example"; // String | The chart configuration in Chart.js format (JSON or Javascript).
    Integer width = 56; // Integer | The width of the chart in pixels.
    Integer height = 56; // Integer | The height of the chart in pixels.
    String format = "format_example"; // String | The output format of the chart, 'png', 'jpg', 'svg', or 'webp'.
    String backgroundColor = "backgroundColor_example"; // String | The background color of the chart.
    try {
      File result = apiInstance.chartGet(chart, width, height, format, backgroundColor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#chartGet");
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
| **chart** | **String**| The chart configuration in Chart.js format (JSON or Javascript). | [optional] |
| **width** | **Integer**| The width of the chart in pixels. | [optional] |
| **height** | **Integer**| The height of the chart in pixels. | [optional] |
| **format** | **String**| The output format of the chart, &#39;png&#39;, &#39;jpg&#39;, &#39;svg&#39;, or &#39;webp&#39;. | [optional] |
| **backgroundColor** | **String**| The background color of the chart. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, image/png, image/svg+xml, image/webp

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A generated chart image. |  -  |

<a id="chartPost"></a>
# **chartPost**
> File chartPost(chartPostRequest)

Generate a chart (POST)

Generate a chart based on the provided configuration in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quickchart.io");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ChartPostRequest chartPostRequest = new ChartPostRequest(); // ChartPostRequest | 
    try {
      File result = apiInstance.chartPost(chartPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#chartPost");
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
| **chartPostRequest** | [**ChartPostRequest**](ChartPostRequest.md)|  | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/jpeg, image/png, image/svg+xml, image/webp

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A generated chart image. |  -  |

<a id="qrGet"></a>
# **qrGet**
> File qrGet(text, width, height, format, margin)

Generate a QR code (GET)

Generate a QR code based on the provided parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quickchart.io");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String text = "text_example"; // String | The text to be encoded in the QR code.
    Integer width = 56; // Integer | The width of the QR code in pixels.
    Integer height = 56; // Integer | The height of the QR code in pixels.
    String format = "format_example"; // String | The output format of the QR code, e.g., 'png' or 'svg'.
    Integer margin = 56; // Integer | The margin around the QR code in pixels.
    try {
      File result = apiInstance.qrGet(text, width, height, format, margin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#qrGet");
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
| **text** | **String**| The text to be encoded in the QR code. | [optional] |
| **width** | **Integer**| The width of the QR code in pixels. | [optional] |
| **height** | **Integer**| The height of the QR code in pixels. | [optional] |
| **format** | **String**| The output format of the QR code, e.g., &#39;png&#39; or &#39;svg&#39;. | [optional] |
| **margin** | **Integer**| The margin around the QR code in pixels. | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/svg+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A generated QR code image. |  -  |

<a id="qrPost"></a>
# **qrPost**
> File qrPost(qrPostRequest)

Generate a QR code (POST)

Generate a QR code based on the provided configuration in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://quickchart.io");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    QrPostRequest qrPostRequest = new QrPostRequest(); // QrPostRequest | 
    try {
      File result = apiInstance.qrPost(qrPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#qrPost");
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
| **qrPostRequest** | [**QrPostRequest**](QrPostRequest.md)|  | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png, image/svg+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A generated QR code image. |  -  |

