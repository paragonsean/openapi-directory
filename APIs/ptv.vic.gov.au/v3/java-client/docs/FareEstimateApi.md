# FareEstimateApi

All URIs are relative to *http://timetableapi.ptv.vic.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fareEstimateGetFareEstimateByZone**](FareEstimateApi.md#fareEstimateGetFareEstimateByZone) | **GET** /v3/fare_estimate/min_zone/{minZone}/max_zone/{maxZone} | Estimate a fare by zone |


<a id="fareEstimateGetFareEstimateByZone"></a>
# **fareEstimateGetFareEstimateByZone**
> Object fareEstimateGetFareEstimateByZone(minZone, maxZone, journeyTouchOnUtc, journeyTouchOffUtc, isJourneyInFreeTramZone, travelledRouteTypes, token, devid, signature)

Estimate a fare by zone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FareEstimateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://timetableapi.ptv.vic.gov.au");

    FareEstimateApi apiInstance = new FareEstimateApi(defaultClient);
    Integer minZone = 56; // Integer | Minimum Zone travelled through ie. 1
    Integer maxZone = 56; // Integer | Maximum Zone travelled through id. 6
    OffsetDateTime journeyTouchOnUtc = OffsetDateTime.now(); // OffsetDateTime | JourneyTouchOnUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53).
    OffsetDateTime journeyTouchOffUtc = OffsetDateTime.now(); // OffsetDateTime | JourneyTouchOffUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53).
    Boolean isJourneyInFreeTramZone = true; // Boolean | 
    List<Integer> travelledRouteTypes = Arrays.asList(); // List<Integer> | 
    String token = "token_example"; // String | Please ignore
    String devid = "devid_example"; // String | Your developer id
    String signature = "signature_example"; // String | Authentication signature for request
    try {
      Object result = apiInstance.fareEstimateGetFareEstimateByZone(minZone, maxZone, journeyTouchOnUtc, journeyTouchOffUtc, isJourneyInFreeTramZone, travelledRouteTypes, token, devid, signature);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FareEstimateApi#fareEstimateGetFareEstimateByZone");
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
| **minZone** | **Integer**| Minimum Zone travelled through ie. 1 | |
| **maxZone** | **Integer**| Maximum Zone travelled through id. 6 | |
| **journeyTouchOnUtc** | **OffsetDateTime**| JourneyTouchOnUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53). | [optional] |
| **journeyTouchOffUtc** | **OffsetDateTime**| JourneyTouchOffUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53). | [optional] |
| **isJourneyInFreeTramZone** | **Boolean**|  | [optional] |
| **travelledRouteTypes** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] [enum: 0, 1, 2, 3, 4] |
| **token** | **String**| Please ignore | [optional] |
| **devid** | **String**| Your developer id | [optional] |
| **signature** | **String**| Authentication signature for request | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Resultant set fare estimates |  -  |
| **400** | Invalid Request |  -  |
| **403** | Access Denied |  -  |

