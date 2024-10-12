# YieldableRatesApi

All URIs are relative to *https://api.hetras-certification.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**yieldableRatesSavePrices**](YieldableRatesApi.md#yieldableRatesSavePrices) | **PUT** /api/hotel/v0/hotels/{hotelId}/yieldable_rateplans/{rateplanCode}/$rates | Saves Yieldable Rate Prices for existing Yieldable Rateplan. |


<a id="yieldableRatesSavePrices"></a>
# **yieldableRatesSavePrices**
> Object yieldableRatesSavePrices(appId, appKey, hotelId, rateplanCode, yieldableRatePrices)

Saves Yieldable Rate Prices for existing Yieldable Rateplan.

Saves Yieldable Rate Prices for existing Yieldable Rateplan. The rateplan has been created before and with this End Point we               create or update the rate prices. If the Yieldable rateplan prices exist it updates them with the new price if not it creates new price entries.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.YieldableRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetras-certification.net");

    YieldableRatesApi apiInstance = new YieldableRatesApi(defaultClient);
    String appId = "appId_example"; // String | Application identifier
    String appKey = "appKey_example"; // String | Application key.
    Integer hotelId = 56; // Integer | Specifies the hotelId which identifies Hotel for which the operation will be performed.
    String rateplanCode = "rateplanCode_example"; // String | Specifies the rateplanCode for which the operation will be performed.
    List<YieldableRateTimeSlice> yieldableRatePrices = Arrays.asList(); // List<YieldableRateTimeSlice> | Specifies the the Yieldable rateplan and prices details to be created or updated.
    try {
      Object result = apiInstance.yieldableRatesSavePrices(appId, appKey, hotelId, rateplanCode, yieldableRatePrices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling YieldableRatesApi#yieldableRatesSavePrices");
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
| **appId** | **String**| Application identifier | |
| **appKey** | **String**| Application key. | |
| **hotelId** | **Integer**| Specifies the hotelId which identifies Hotel for which the operation will be performed. | |
| **rateplanCode** | **String**| Specifies the rateplanCode for which the operation will be performed. | |
| **yieldableRatePrices** | [**List&lt;YieldableRateTimeSlice&gt;**](YieldableRateTimeSlice.md)| Specifies the the Yieldable rateplan and prices details to be created or updated. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Saving the Yieldable rateplan prices was successful. You will get back the confirmation. |  -  |
| **400** | Bad request. Request body erroneous. |  -  |
| **401** | You provided wrong credentials, or you reached your API limit. |  -  |
| **403** | The application does not have access to the requested resource. |  -  |
| **404** | Not Found. The server has not found anything matching the Request-URI. |  -  |
| **422** | The request failed to validate. |  -  |
| **500** | We caught an unexpected error on our side. Please report with providing the Hetras-Tracking-Id from the response headers and we will check the logfiles. |  -  |
| **503** | The server is currently unavailable. Please try later. |  -  |

