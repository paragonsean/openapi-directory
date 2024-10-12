# CountriesApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countriesGet**](CountriesApi.md#countriesGet) | **GET** /countries | Retrieve a list of country codes with corresponding subregions |


<a id="countriesGet"></a>
# **countriesGet**
> countriesGet()

Retrieve a list of country codes with corresponding subregions

Retrieve a list of country codes with corresponding subregions

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    CountriesApi apiInstance = new CountriesApi(defaultClient);
    try {
      apiInstance.countriesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling CountriesApi#countriesGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

