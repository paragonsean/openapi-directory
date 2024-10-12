# CountriesApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countriesListGet**](CountriesApi.md#countriesListGet) | **GET** /countries/list |  |


<a id="countriesListGet"></a>
# **countriesListGet**
> List&lt;Country&gt; countriesListGet()



Lists the countries to which Handwritten can mail, their associated country ID and any costs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    try {
      List<Country> result = apiInstance.countriesListGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#countriesListGet");
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

[**List&lt;Country&gt;**](Country.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

