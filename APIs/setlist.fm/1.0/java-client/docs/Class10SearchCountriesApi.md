# Class10SearchCountriesApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10SearchCountriesGetCountriesGET**](Class10SearchCountriesApi.md#resource10SearchCountriesGetCountriesGET) | **GET** /1.0/search/countries | Get a complete list of all supported countries. |


<a id="resource10SearchCountriesGetCountriesGET"></a>
# **resource10SearchCountriesGetCountriesGET**
> JsonCountries resource10SearchCountriesGetCountriesGET()

Get a complete list of all supported countries.

Get a complete list of all supported countries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10SearchCountriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10SearchCountriesApi apiInstance = new Class10SearchCountriesApi(defaultClient);
    try {
      JsonCountries result = apiInstance.resource10SearchCountriesGetCountriesGET();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10SearchCountriesApi#resource10SearchCountriesGetCountriesGET");
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

[**JsonCountries**](JsonCountries.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

