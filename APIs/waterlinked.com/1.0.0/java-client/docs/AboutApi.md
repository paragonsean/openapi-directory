# AboutApi

All URIs are relative to *http://demo.waterlinked.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aboutApiVersion**](AboutApi.md#aboutApiVersion) | **GET** /api/ | ApiVersion about |
| [**aboutFactoryReset**](AboutApi.md#aboutFactoryReset) | **POST** /api/v1/about/factoryreset | FactoryReset about |
| [**aboutGet**](AboutApi.md#aboutGet) | **GET** /api/v1/about | Get about |
| [**aboutLED**](AboutApi.md#aboutLED) | **GET** /api/v1/about/led | LED about |
| [**aboutStatus**](AboutApi.md#aboutStatus) | **GET** /api/v1/about/status | Status about |
| [**aboutTemperature**](AboutApi.md#aboutTemperature) | **GET** /api/v1/about/temperature | Temperature about |


<a id="aboutApiVersion"></a>
# **aboutApiVersion**
> WupdaterApiversion aboutApiVersion()

ApiVersion about

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AboutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    AboutApi apiInstance = new AboutApi(defaultClient);
    try {
      WupdaterApiversion result = apiInstance.aboutApiVersion();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AboutApi#aboutApiVersion");
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

[**WupdaterApiversion**](WupdaterApiversion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.wupdater.apiversion

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="aboutFactoryReset"></a>
# **aboutFactoryReset**
> WaterlinkedOperationResponse aboutFactoryReset()

FactoryReset about

Reset all settings on master electronics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AboutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    AboutApi apiInstance = new AboutApi(defaultClient);
    try {
      WaterlinkedOperationResponse result = apiInstance.aboutFactoryReset();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AboutApi#aboutFactoryReset");
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

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="aboutGet"></a>
# **aboutGet**
> WaterlinkedAbout aboutGet()

Get about

Get about information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AboutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    AboutApi apiInstance = new AboutApi(defaultClient);
    try {
      WaterlinkedAbout result = apiInstance.aboutGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AboutApi#aboutGet");
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

[**WaterlinkedAbout**](WaterlinkedAbout.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.about+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="aboutLED"></a>
# **aboutLED**
> aboutLED()

LED about

Flash LED1 on master electronics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AboutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    AboutApi apiInstance = new AboutApi(defaultClient);
    try {
      apiInstance.aboutLED();
    } catch (ApiException e) {
      System.err.println("Exception when calling AboutApi#aboutLED");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not Found |  -  |

<a id="aboutStatus"></a>
# **aboutStatus**
> WaterlinkedStatus aboutStatus()

Status about

Get current IMU and GPS status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AboutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    AboutApi apiInstance = new AboutApi(defaultClient);
    try {
      WaterlinkedStatus result = apiInstance.aboutStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AboutApi#aboutStatus");
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

[**WaterlinkedStatus**](WaterlinkedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.status+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="aboutTemperature"></a>
# **aboutTemperature**
> WaterlinkedTemperature aboutTemperature()

Temperature about

Get board temperature

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AboutApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    AboutApi apiInstance = new AboutApi(defaultClient);
    try {
      WaterlinkedTemperature result = apiInstance.aboutTemperature();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AboutApi#aboutTemperature");
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

[**WaterlinkedTemperature**](WaterlinkedTemperature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.temperature+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

