# Wgs84ToOsgb36Api

All URIs are relative to *http://quicksold.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**wgs84ToOsgb36UsingGET**](Wgs84ToOsgb36Api.md#wgs84ToOsgb36UsingGET) | **GET** /v1/wgs84ToOsgb36/{latitude}/{longitude} | wgs84ToOsgb36 |


<a id="wgs84ToOsgb36UsingGET"></a>
# **wgs84ToOsgb36UsingGET**
> ModelApiResponse wgs84ToOsgb36UsingGET(latitude, longitude)

wgs84ToOsgb36

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Wgs84ToOsgb36Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://quicksold.co.uk");

    Wgs84ToOsgb36Api apiInstance = new Wgs84ToOsgb36Api(defaultClient);
    String latitude = "latitude_example"; // String | latitude
    String longitude = "longitude_example"; // String | longitude
    try {
      ModelApiResponse result = apiInstance.wgs84ToOsgb36UsingGET(latitude, longitude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Wgs84ToOsgb36Api#wgs84ToOsgb36UsingGET");
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
| **latitude** | **String**| latitude | |
| **longitude** | **String**| longitude | |

### Return type

[**ModelApiResponse**](ModelApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

