# CityDataStandardizationApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getcitystandard**](CityDataStandardizationApi.md#getcitystandard) | **GET** /getcitystandard | Gets a city name standard for US and international cities |


<a id="getcitystandard"></a>
# **getcitystandard**
> Getcitystandard200Response getcitystandard(license, city)

Gets a city name standard for US and international cities

Gets a pre-selected city name standard for US and international cities for various permutations of a given city name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CityDataStandardizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    CityDataStandardizationApi apiInstance = new CityDataStandardizationApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String city = "city_example"; // String | City name from which to retrieve the standardized version
    try {
      Getcitystandard200Response result = apiInstance.getcitystandard(license, city);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CityDataStandardizationApi#getcitystandard");
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
| **city** | **String**| City name from which to retrieve the standardized version | |

### Return type

[**Getcitystandard200Response**](Getcitystandard200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standardized city name data |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

