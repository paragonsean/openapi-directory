# DefaultApi

All URIs are relative to *https://api.ip2location.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rootGet**](DefaultApi.md#rootGet) | **GET** / |  |


<a id="rootGet"></a>
# **rootGet**
> rootGet(key, ip, format, lang)



Geolocate user&#39;s location information via IP address

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
    defaultClient.setBasePath("https://api.ip2location.io");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | API key.
    String ip = "8.8.8.8"; // String | IP address (IPv4 or IPv6) for reverse IP location lookup purposes. If not present, the server IP address will be used for the location lookup.
    String format = "json"; // String | Format of the response message.
    String lang = "ar"; // String | Translation information. The translation only applicable for continent, country, region and city name. This parameter is only available for Plus and Security plan only.
    try {
      apiInstance.rootGet(key, ip, format, lang);
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
| **key** | **String**| API key. | |
| **ip** | **String**| IP address (IPv4 or IPv6) for reverse IP location lookup purposes. If not present, the server IP address will be used for the location lookup. | |
| **format** | **String**| Format of the response message. | [optional] [enum: json, xml] |
| **lang** | **String**| Translation information. The translation only applicable for continent, country, region and city name. This parameter is only available for Plus and Security plan only. | [optional] [enum: ar, cs, da, de, en, es, et, fi, fr, ga, it, ja, ko, ms, nl, pt, ru, sv, tr, vi, zh-cn, zh-tw] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get response from IP lookup |  -  |

