# DispatchGreenEnergyDistributionApiApi

All URIs are relative to *https://api.corrently.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gsiDispatch_0**](DispatchGreenEnergyDistributionApiApi.md#gsiDispatch_0) | **GET** /gsi/dispatch | Dispatch (Green Energy Distribution Schedule) |


<a id="gsiDispatch_0"></a>
# **gsiDispatch_0**
> GsiDispatch200Response gsiDispatch_0(zip, key)

Dispatch (Green Energy Distribution Schedule)

Dispatch of green energy has two aspects to consider:   - Availability of gerneration facility (depends on weather and installed capacity)   - Demand of energy Using the green power index (GrünstromIndex) we have received a tool to automate distribution of energy in order to prevent redispatch situations. Doing this alows to opimize resource usage (tactical) and leverage data for investment planning (strategic). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DispatchGreenEnergyDistributionApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.corrently.io/v2.0");

    DispatchGreenEnergyDistributionApiApi apiInstance = new DispatchGreenEnergyDistributionApiApi(defaultClient);
    String zip = "zip_example"; // String | Zipcode (Postleitzahl) of a city in Germany.
    String key = "key_example"; // String | Any valid Stromkonto account (address).
    try {
      GsiDispatch200Response result = apiInstance.gsiDispatch_0(zip, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DispatchGreenEnergyDistributionApiApi#gsiDispatch_0");
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
| **zip** | **String**| Zipcode (Postleitzahl) of a city in Germany. | [optional] |
| **key** | **String**| Any valid Stromkonto account (address). | [optional] |

### Return type

[**GsiDispatch200Response**](GsiDispatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

