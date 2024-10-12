# DefaultApi

All URIs are relative to *https://api.ip2proxy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rootGet**](DefaultApi.md#rootGet) | **GET** / |  |


<a id="rootGet"></a>
# **rootGet**
> String rootGet(ip, key, _package, format)



Check if an IP address is proxy

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
    defaultClient.setBasePath("https://api.ip2proxy.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ip = "ip_example"; // String | IP address (IPv4) for lookup purpose. If not present, the server IP address will be used for the lookup.
    String key = "key_example"; // String | API key. Please sign up free trial license key at ip2location.com
    String _package = "_package_example"; // String | Package name from PX1 to PX11. If not present, the web service will assume the PX1 package query.
    String format = "json"; // String | If not present, json format will be returned as the search result.
    try {
      String result = apiInstance.rootGet(ip, key, _package, format);
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
| **ip** | **String**| IP address (IPv4) for lookup purpose. If not present, the server IP address will be used for the lookup. | |
| **key** | **String**| API key. Please sign up free trial license key at ip2location.com | |
| **_package** | **String**| Package name from PX1 to PX11. If not present, the web service will assume the PX1 package query. | [optional] |
| **format** | **String**| If not present, json format will be returned as the search result. | [optional] [enum: json, xml] |

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
| **200** | Get response from IP2Proxy |  -  |

