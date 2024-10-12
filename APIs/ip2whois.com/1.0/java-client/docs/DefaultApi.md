# DefaultApi

All URIs are relative to *https://api.ip2whois.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rootGet**](DefaultApi.md#rootGet) | **GET** / |  |


<a id="rootGet"></a>
# **rootGet**
> String rootGet(domain, key, format)



Lookup WHOIS information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ip2whois.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String domain = "domain_example"; // String | Domain name for lookup purpose.
    String key = "key_example"; // String | API key.
    String format = "format_example"; // String | Returns the API response in json (default) or xml format.
    try {
      String result = apiInstance.rootGet(domain, key, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rootGet");
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
| **domain** | **String**| Domain name for lookup purpose. | |
| **key** | **String**| API key. | |
| **format** | **String**| Returns the API response in json (default) or xml format. | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get response from IP2WHOIS |  -  |

