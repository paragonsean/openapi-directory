# VehicleApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vehicleGet**](VehicleApi.md#vehicleGet) | **GET** /Vehicle/{ids}/Arrivals | Gets the predictions for a given list of vehicle Id&#39;s. |


<a id="vehicleGet"></a>
# **vehicleGet**
> List&lt;TflApiPresentationEntitiesPrediction&gt; vehicleGet(ids)

Gets the predictions for a given list of vehicle Id&#39;s.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehicleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    VehicleApi apiInstance = new VehicleApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of vehicle ids e.g. LX58CFV,LX11AZB,LX58CFE. Max approx. 25 ids.
    try {
      List<TflApiPresentationEntitiesPrediction> result = apiInstance.vehicleGet(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehicleApi#vehicleGet");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of vehicle ids e.g. LX58CFV,LX11AZB,LX58CFE. Max approx. 25 ids. | |

### Return type

[**List&lt;TflApiPresentationEntitiesPrediction&gt;**](TflApiPresentationEntitiesPrediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

