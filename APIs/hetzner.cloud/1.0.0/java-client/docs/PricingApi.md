# PricingApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pricingGet**](PricingApi.md#pricingGet) | **GET** /pricing | Get all prices |


<a id="pricingGet"></a>
# **pricingGet**
> PricingGet200Response pricingGet()

Get all prices

Returns prices for all resources available on the platform. VAT and currency of the Project owner are used for calculations.  Both net and gross prices are included in the response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PricingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PricingApi apiInstance = new PricingApi(defaultClient);
    try {
      PricingGet200Response result = apiInstance.pricingGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PricingApi#pricingGet");
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

[**PricingGet200Response**](PricingGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;pricing&#x60; key in the reply contains an pricing object with this structure |  -  |

