# PositionApi

All URIs are relative to *http://demo.waterlinked.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**positionAcousticFiltered**](PositionApi.md#positionAcousticFiltered) | **GET** /api/v1/position/acoustic/filtered | AcousticFiltered position |
| [**positionAcousticRaw**](PositionApi.md#positionAcousticRaw) | **GET** /api/v1/position/acoustic/raw | AcousticRaw position |
| [**positionGet**](PositionApi.md#positionGet) | **GET** /api/v1/position/global | Get position |
| [**positionGetMaster**](PositionApi.md#positionGetMaster) | **GET** /api/v1/position/master | GetMaster position |


<a id="positionAcousticFiltered"></a>
# **positionAcousticFiltered**
> WaterlinkedAccousticPosition positionAcousticFiltered()

AcousticFiltered position

Get current Kalman filtered acoustic position relative to master acoustics. Expected update frequency: 4 Hz

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PositionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PositionApi apiInstance = new PositionApi(defaultClient);
    try {
      WaterlinkedAccousticPosition result = apiInstance.positionAcousticFiltered();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PositionApi#positionAcousticFiltered");
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

[**WaterlinkedAccousticPosition**](WaterlinkedAccousticPosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.accoustic.position+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="positionAcousticRaw"></a>
# **positionAcousticRaw**
> WaterlinkedAccousticPosition positionAcousticRaw()

AcousticRaw position

Get current unfiltered acoustic position relative to master acoustics. Expected update frequency: 4 Hz

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PositionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PositionApi apiInstance = new PositionApi(defaultClient);
    try {
      WaterlinkedAccousticPosition result = apiInstance.positionAcousticRaw();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PositionApi#positionAcousticRaw");
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

[**WaterlinkedAccousticPosition**](WaterlinkedAccousticPosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.accoustic.position+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="positionGet"></a>
# **positionGet**
> WlSatellitePosition positionGet()

Get position

Get current global position of locator. Locator position is calculated from the current acoustic position and the global position of the master electronics. Expected update frequency: 4 Hz

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PositionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PositionApi apiInstance = new PositionApi(defaultClient);
    try {
      WlSatellitePosition result = apiInstance.positionGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PositionApi#positionGet");
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

[**WlSatellitePosition**](WlSatellitePosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.wl.satellite.position+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="positionGetMaster"></a>
# **positionGetMaster**
> WlSatellitePosition positionGetMaster()

GetMaster position

Get current global position of master electronics. Expected update frequency: 1 Hz

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PositionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    PositionApi apiInstance = new PositionApi(defaultClient);
    try {
      WlSatellitePosition result = apiInstance.positionGetMaster();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PositionApi#positionGetMaster");
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

[**WlSatellitePosition**](WlSatellitePosition.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.wl.satellite.position+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

