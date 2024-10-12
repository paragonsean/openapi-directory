# CurrentGlobalTimeApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getglobaltime**](CurrentGlobalTimeApi.md#getglobaltime) | **GET** /getglobaltime | Gets the current time for a global locale |


<a id="getglobaltime"></a>
# **getglobaltime**
> Getglobaltime200Response getglobaltime(license, locale)

Gets the current time for a global locale

Gets the current time for a global locale (city, state, region, or country such as Chicago, London, Paris, Seoul, Spain, Buenos Aires, Hawaii, Moscow, Tokyo, Hanoi, etc.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CurrentGlobalTimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    CurrentGlobalTimeApi apiInstance = new CurrentGlobalTimeApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String locale = "locale_example"; // String | Geographic locale to get the current time for
    try {
      Getglobaltime200Response result = apiInstance.getglobaltime(license, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CurrentGlobalTimeApi#getglobaltime");
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
| **locale** | **String**| Geographic locale to get the current time for | |

### Return type

[**Getglobaltime200Response**](Getglobaltime200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current global time in many forms and related information |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **404** | locale not found |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

