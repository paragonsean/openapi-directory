# AtmCountriesApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**atmsV1CountryGet**](AtmCountriesApi.md#atmsV1CountryGet) | **GET** /atms/v1/country | Returns countries with valid ATM locations. |


<a id="atmsV1CountryGet"></a>
# **atmsV1CountryGet**
> CountriesResponse atmsV1CountryGet()

Returns countries with valid ATM locations.

Returns countries with valid ATM locations. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AtmCountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    AtmCountriesApi apiInstance = new AtmCountriesApi(defaultClient);
    try {
      CountriesResponse result = apiInstance.atmsV1CountryGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AtmCountriesApi#atmsV1CountryGet");
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

[**CountriesResponse**](CountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of all the countries that contain ATMs |  -  |
| **0** | Unexpected error |  -  |

