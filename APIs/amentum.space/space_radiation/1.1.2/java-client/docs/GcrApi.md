# GcrApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiEndpointsGCRCalculateDlrFlux**](GcrApi.md#appApiEndpointsGCRCalculateDlrFlux) | **GET** /gcr/flux_dlr | Calculate particle flux   |


<a id="appApiEndpointsGCRCalculateDlrFlux"></a>
# **appApiEndpointsGCRCalculateDlrFlux**
> FluxAtEnergy appApiEndpointsGCRCalculateDlrFlux(year, month, day, z, energy)

Calculate particle flux  

for the given energy, atomic number, and date. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GcrApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    GcrApi apiInstance = new GcrApi(defaultClient);
    Integer year = 2017; // Integer | <br>
    Integer month = 1; // Integer | <br>
    Integer day = 1; // Integer | <br>
    BigDecimal z = new BigDecimal("6"); // BigDecimal | <br>Particle atomic number
    BigDecimal energy = new BigDecimal("100"); // BigDecimal | <br>Particle energy in MeV/n<br> Valid range: [0, 10<sup>6</sup>] MeV/n<br>  
    try {
      FluxAtEnergy result = apiInstance.appApiEndpointsGCRCalculateDlrFlux(year, month, day, z, energy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GcrApi#appApiEndpointsGCRCalculateDlrFlux");
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
| **year** | **Integer**| &lt;br&gt; | |
| **month** | **Integer**| &lt;br&gt; | |
| **day** | **Integer**| &lt;br&gt; | |
| **z** | **BigDecimal**| &lt;br&gt;Particle atomic number | |
| **energy** | **BigDecimal**| &lt;br&gt;Particle energy in MeV/n&lt;br&gt; Valid range: [0, 10&lt;sup&gt;6&lt;/sup&gt;] MeV/n&lt;br&gt;   | |

### Return type

[**FluxAtEnergy**](FluxAtEnergy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful flux calculation |  -  |

