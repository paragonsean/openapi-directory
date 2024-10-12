# DefaultApi

All URIs are relative to *https://api.openuv.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**forecastGet**](DefaultApi.md#forecastGet) | **GET** /forecast |  |
| [**protectionGet**](DefaultApi.md#protectionGet) | **GET** /protection |  |
| [**uvGet**](DefaultApi.md#uvGet) | **GET** /uv |  |


<a id="forecastGet"></a>
# **forecastGet**
> List&lt;Set&lt;Forecast&gt;&gt; forecastGet(lat, lng, xAccessToken, alt, ozone, dt)



Get hourly UV Index Forecast by location and date. Optional altitude, ozone level and datetime could be provided.

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
    defaultClient.setBasePath("https://api.openuv.io/api/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BigDecimal lat = new BigDecimal("78.67"); // BigDecimal | latitude, from -90.00 to 90.00
    BigDecimal lng = new BigDecimal("115.67"); // BigDecimal | longitude, from -180.00 to 180.00
    String xAccessToken = "xAccessToken_example"; // String | This header is used to send data that contains your OpenUV API key
    BigDecimal alt = new BigDecimal("1050"); // BigDecimal | Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
    BigDecimal ozone = new BigDecimal("304.5"); // BigDecimal | Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
    OffsetDateTime dt = OffsetDateTime.parse("2018-02-04T04:39:06.467Z"); // OffsetDateTime | UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time.
    try {
      List<Set<Forecast>> result = apiInstance.forecastGet(lat, lng, xAccessToken, alt, ozone, dt);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#forecastGet");
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
| **lat** | **BigDecimal**| latitude, from -90.00 to 90.00 | |
| **lng** | **BigDecimal**| longitude, from -180.00 to 180.00 | |
| **xAccessToken** | **String**| This header is used to send data that contains your OpenUV API key | |
| **alt** | **BigDecimal**| Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. | [optional] |
| **ozone** | **BigDecimal**| Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. | [optional] |
| **dt** | **OffsetDateTime**| UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. | [optional] |

### Return type

[**List&lt;Set&lt;Forecast&gt;&gt;**](Set.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="protectionGet"></a>
# **protectionGet**
> ProtectionResult protectionGet(lat, lng, from, to, xAccessToken, alt, ozone)



Get daily protection time by location, UV Index from and UV Index to with 10 minutes accuracy. Optional altitide and ozone level could be provided.

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
    defaultClient.setBasePath("https://api.openuv.io/api/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BigDecimal lat = new BigDecimal("78.67"); // BigDecimal | latitude, from -90.00 to 90.00
    BigDecimal lng = new BigDecimal("115.67"); // BigDecimal | longitude, from -180.00 to 180.00
    BigDecimal from = new BigDecimal("2.5"); // BigDecimal | UV Index from value for protection datetime lookup. From 0 to 40.
    BigDecimal to = new BigDecimal("3.6"); // BigDecimal | UV Index to value for protection datetime lookup. From 0 to 40.
    String xAccessToken = "xAccessToken_example"; // String | This header is used to send data that contains your OpenUV API key
    BigDecimal alt = new BigDecimal("1050"); // BigDecimal | Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
    BigDecimal ozone = new BigDecimal("304.5"); // BigDecimal | Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
    try {
      ProtectionResult result = apiInstance.protectionGet(lat, lng, from, to, xAccessToken, alt, ozone);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#protectionGet");
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
| **lat** | **BigDecimal**| latitude, from -90.00 to 90.00 | |
| **lng** | **BigDecimal**| longitude, from -180.00 to 180.00 | |
| **from** | **BigDecimal**| UV Index from value for protection datetime lookup. From 0 to 40. | |
| **to** | **BigDecimal**| UV Index to value for protection datetime lookup. From 0 to 40. | |
| **xAccessToken** | **String**| This header is used to send data that contains your OpenUV API key | |
| **alt** | **BigDecimal**| Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. | [optional] |
| **ozone** | **BigDecimal**| Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. | [optional] |

### Return type

[**ProtectionResult**](ProtectionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="uvGet"></a>
# **uvGet**
> UvIndexResult uvGet(lat, lng, xAccessToken, alt, ozone, dt)



Get real-time UV Index by location. Optional altitude, ozone level and datetime could be provided.

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
    defaultClient.setBasePath("https://api.openuv.io/api/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    BigDecimal lat = new BigDecimal("78.67"); // BigDecimal | latitude, from -90.00 to 90.00
    BigDecimal lng = new BigDecimal("115.67"); // BigDecimal | longitude, from -180.00 to 180.00
    String xAccessToken = "xAccessToken_example"; // String | This header is used to send data that contains your OpenUV API key
    BigDecimal alt = new BigDecimal("1050"); // BigDecimal | Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value.
    BigDecimal ozone = new BigDecimal("304.5"); // BigDecimal | Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default.
    OffsetDateTime dt = OffsetDateTime.parse("2018-02-04T04:39:06.467Z"); // OffsetDateTime | UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time.
    try {
      UvIndexResult result = apiInstance.uvGet(lat, lng, xAccessToken, alt, ozone, dt);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#uvGet");
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
| **lat** | **BigDecimal**| latitude, from -90.00 to 90.00 | |
| **lng** | **BigDecimal**| longitude, from -180.00 to 180.00 | |
| **xAccessToken** | **String**| This header is used to send data that contains your OpenUV API key | |
| **alt** | **BigDecimal**| Altitude in meters, from 0 to 10000m, 0m by default. If provided the altitude correction factor will be applied to clear sky sea level UV Index value. | [optional] |
| **ozone** | **BigDecimal**| Ozone in du (Dobson Units), from 100 to 550du, the latest forecast from OMI dataset is used by default. | [optional] |
| **dt** | **OffsetDateTime**| UTC datetime in ISO-8601 format, now by default. Use that parameter to get UV Index Forecast for any point in time. | [optional] |

### Return type

[**UvIndexResult**](UvIndexResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

