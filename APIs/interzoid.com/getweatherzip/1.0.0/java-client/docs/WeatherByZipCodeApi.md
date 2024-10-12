# WeatherByZipCodeApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getweatherzipcode**](WeatherByZipCodeApi.md#getweatherzipcode) | **GET** /getweatherzipcode | Gets current weather information for a US zip code |


<a id="getweatherzipcode"></a>
# **getweatherzipcode**
> Getweatherzipcode200Response getweatherzipcode(license, zip)

Gets current weather information for a US zip code

Use a US zip code to retrieve current weather information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WeatherByZipCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    WeatherByZipCodeApi apiInstance = new WeatherByZipCodeApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String zip = "zip_example"; // String | Zip code for weather information
    try {
      Getweatherzipcode200Response result = apiInstance.getweatherzipcode(license, zip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WeatherByZipCodeApi#getweatherzipcode");
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
| **zip** | **String**| Zip code for weather information | |

### Return type

[**Getweatherzipcode200Response**](Getweatherzipcode200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current weather information for zip code |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | zip code not found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

