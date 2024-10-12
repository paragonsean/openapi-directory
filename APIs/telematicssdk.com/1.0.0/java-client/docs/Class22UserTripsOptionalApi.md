# Class22UserTripsOptionalApi

All URIs are relative to *https://api.telematicssdk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**tripsTripDetails_0**](Class22UserTripsOptionalApi.md#tripsTripDetails_0) | **GET** /mobilesdk/stage/track/get_track/v1 | Trips - trip details |


<a id="tripsTripDetails_0"></a>
# **tripsTripDetails_0**
> TripsTripDetails200Response tripsTripDetails_0(trackToken)

Trips - trip details

Trips - trip details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class22UserTripsOptionalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.telematicssdk.com");

    Class22UserTripsOptionalApi apiInstance = new Class22UserTripsOptionalApi(defaultClient);
    String trackToken = ""; // String | 
    try {
      TripsTripDetails200Response result = apiInstance.tripsTripDetails_0(trackToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class22UserTripsOptionalApi#tripsTripDetails_0");
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
| **trackToken** | **String**|  | [optional] |

### Return type

[**TripsTripDetails200Response**](TripsTripDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * CF-Cache-Status -  <br>  * CF-Ray -  <br>  * Code -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * EnableLogging -  <br>  * EnableRealTimeLocation -  <br>  * EnableTracking -  <br>  * Expect-CT -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Powered-By -  <br>  * X-StackifyID -  <br>  * cf-apo-via -  <br>  * cf-request-id -  <br>  |

