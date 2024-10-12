# ReverseGeocodingApi

All URIs are relative to *https://api.exoapi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reverseGeocodingGet**](ReverseGeocodingApi.md#reverseGeocodingGet) | **GET** /reverse-geocoding |  |


<a id="reverseGeocodingGet"></a>
# **reverseGeocodingGet**
> ReverseGeocodingGet200Response reverseGeocodingGet(lat, lon, locale)



Quickly convert GPS coordinates to human-readable addresses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReverseGeocodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.exoapi.dev");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    ReverseGeocodingApi apiInstance = new ReverseGeocodingApi(defaultClient);
    BigDecimal lat = new BigDecimal(78); // BigDecimal | 
    BigDecimal lon = new BigDecimal(78); // BigDecimal | 
    String locale = "locale_example"; // String | 
    try {
      ReverseGeocodingGet200Response result = apiInstance.reverseGeocodingGet(lat, lon, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReverseGeocodingApi#reverseGeocodingGet");
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
| **lat** | **BigDecimal**|  | |
| **lon** | **BigDecimal**|  | |
| **locale** | **String**|  | [optional] |

### Return type

[**ReverseGeocodingGet200Response**](ReverseGeocodingGet200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 🟢 200 OK |  -  |
| **401** | 🟡 401 Unauthorized |  -  |
| **429** | 🟡 429 Too many requests |  -  |
| **500** | 🔴 500 Internal server error |  -  |

