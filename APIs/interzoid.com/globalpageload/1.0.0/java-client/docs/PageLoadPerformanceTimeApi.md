# PageLoadPerformanceTimeApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**globalpageload**](PageLoadPerformanceTimeApi.md#globalpageload) | **GET** /globalpageload | Gets page load (or an API call) performance from a specified global geography such as Paris, Tokyo, Virginia, Mumbai, Frankfurt, London, Seoul, California, Sao Paolo, and many more. |


<a id="globalpageload"></a>
# **globalpageload**
> Globalpageload200Response globalpageload(license, origin, url)

Gets page load (or an API call) performance from a specified global geography such as Paris, Tokyo, Virginia, Mumbai, Frankfurt, London, Seoul, California, Sao Paolo, and many more.

Gets page load performance from a specified geography 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PageLoadPerformanceTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    PageLoadPerformanceTimeApi apiInstance = new PageLoadPerformanceTimeApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String origin = "origin_example"; // String | Geographic location to perform the measurement from (Paris, Hong Kong, Seoul, Mumbai, Sao Paolo, London, etc. see API home page for full list)
    String url = "url_example"; // String | specific URL to perform load test time
    try {
      Globalpageload200Response result = apiInstance.globalpageload(license, origin, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PageLoadPerformanceTimeApi#globalpageload");
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
| **origin** | **String**| Geographic location to perform the measurement from (Paris, Hong Kong, Seoul, Mumbai, Sao Paolo, London, etc. see API home page for full list) | |
| **url** | **String**| specific URL to perform load test time | |

### Return type

[**Globalpageload200Response**](Globalpageload200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Page load performance measurement response |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | origin or url note found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

