# CityNameSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getcitymatch**](CityNameSimilarityKeyApi.md#getcitymatch) | **GET** /getcitymatch | Gets a similarity key for matching purposes for city name data |


<a id="getcitymatch"></a>
# **getcitymatch**
> Getcitymatch200Response getcitymatch(license, city)

Gets a similarity key for matching purposes for city name data

Gets a similarity key for matching purposes for city name data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CityNameSimilarityKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    CityNameSimilarityKeyApi apiInstance = new CityNameSimilarityKeyApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String city = "city_example"; // String | City name from which to generate similarity key
    try {
      Getcitymatch200Response result = apiInstance.getcitymatch(license, city);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CityNameSimilarityKeyApi#getcitymatch");
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
| **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | |
| **city** | **String**| City name from which to generate similarity key | |

### Return type

[**Getcitymatch200Response**](Getcitymatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated similarity key for city name data |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

