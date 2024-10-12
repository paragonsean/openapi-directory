# WeatherByCityAndStateApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getweather**](WeatherByCityAndStateApi.md#getweather) | **GET** /getweather | Gets current weather information for a US city and state |


<a id="getweather"></a>
# **getweather**
> Getweather200Response getweather(license, city, state)

Gets current weather information for a US city and state

Use city and state to retrieve current US weather information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WeatherByCityAndStateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    WeatherByCityAndStateApi apiInstance = new WeatherByCityAndStateApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String city = "city_example"; // String | City for weather information
    String state = "state_example"; // String | State for weather information
    try {
      Getweather200Response result = apiInstance.getweather(license, city, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WeatherByCityAndStateApi#getweather");
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
| **city** | **String**| City for weather information | |
| **state** | **String**| State for weather information | |

### Return type

[**Getweather200Response**](Getweather200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current weather information for a US city |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | city/state not found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

