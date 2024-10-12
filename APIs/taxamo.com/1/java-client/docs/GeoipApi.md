# GeoipApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locateGivenIP**](GeoipApi.md#locateGivenIP) | **GET** /api/v1/geoip/{ip} | Locate provided IP |
| [**locateMyIP**](GeoipApi.md#locateMyIP) | **GET** /api/v1/geoip | Locate IP |


<a id="locateGivenIP"></a>
# **locateGivenIP**
> LocateGivenIPOut locateGivenIP(ip)

Locate provided IP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    GeoipApi apiInstance = new GeoipApi(defaultClient);
    String ip = "ip_example"; // String | IP address.
    try {
      LocateGivenIPOut result = apiInstance.locateGivenIP(ip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoipApi#locateGivenIP");
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
| **ip** | **String**| IP address. | |

### Return type

[**LocateGivenIPOut**](LocateGivenIPOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="locateMyIP"></a>
# **locateMyIP**
> LocateMyIPOut locateMyIP()

Locate IP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    GeoipApi apiInstance = new GeoipApi(defaultClient);
    try {
      LocateMyIPOut result = apiInstance.locateMyIP();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoipApi#locateMyIP");
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

[**LocateMyIPOut**](LocateMyIPOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

