# Egm2008Api

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiEgm2008EndpointsEGM2008CalculateAnomaly**](Egm2008Api.md#appApiEgm2008EndpointsEGM2008CalculateAnomaly) | **GET** /egm2008/gravity_anomaly | Calculate gravity anomaly values  |
| [**appApiEgm2008EndpointsEGM2008CalculateHeight**](Egm2008Api.md#appApiEgm2008EndpointsEGM2008CalculateHeight) | **GET** /egm2008/geoid_height | Calculate the geoid height  |


<a id="appApiEgm2008EndpointsEGM2008CalculateAnomaly"></a>
# **appApiEgm2008EndpointsEGM2008CalculateAnomaly**
> Anomaly appApiEgm2008EndpointsEGM2008CalculateAnomaly(latitude, longitude)

Calculate gravity anomaly values 

for a given latitude / longitude. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Egm2008Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    Egm2008Api apiInstance = new Egm2008Api(defaultClient);
    BigDecimal latitude = new BigDecimal("-45"); // BigDecimal | Geographic latitude (-90 to 90 deg).
    BigDecimal longitude = new BigDecimal("45"); // BigDecimal | Geographic longitude (-180 to 180 deg).
    try {
      Anomaly result = apiInstance.appApiEgm2008EndpointsEGM2008CalculateAnomaly(latitude, longitude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Egm2008Api#appApiEgm2008EndpointsEGM2008CalculateAnomaly");
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
| **latitude** | **BigDecimal**| Geographic latitude (-90 to 90 deg). | |
| **longitude** | **BigDecimal**| Geographic longitude (-180 to 180 deg). | |

### Return type

[**Anomaly**](Anomaly.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful anomaly calculation |  -  |

<a id="appApiEgm2008EndpointsEGM2008CalculateHeight"></a>
# **appApiEgm2008EndpointsEGM2008CalculateHeight**
> Height appApiEgm2008EndpointsEGM2008CalculateHeight(latitude, longitude)

Calculate the geoid height 

for a given latitude / longitude.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Egm2008Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    Egm2008Api apiInstance = new Egm2008Api(defaultClient);
    BigDecimal latitude = new BigDecimal("-45"); // BigDecimal | Geographic latitude (-90 to 90 deg).
    BigDecimal longitude = new BigDecimal("45"); // BigDecimal | Geographic longitude (-180 to 180 deg).
    try {
      Height result = apiInstance.appApiEgm2008EndpointsEGM2008CalculateHeight(latitude, longitude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Egm2008Api#appApiEgm2008EndpointsEGM2008CalculateHeight");
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
| **latitude** | **BigDecimal**| Geographic latitude (-90 to 90 deg). | |
| **longitude** | **BigDecimal**| Geographic longitude (-180 to 180 deg). | |

### Return type

[**Height**](Height.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful geoid height calculation |  -  |

