# DefaultApi

All URIs are relative to *https://api.ip2location.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rootGet**](DefaultApi.md#rootGet) | **GET** / |  |


<a id="rootGet"></a>
# **rootGet**
> String rootGet(ip, key, _package, addon, format, lang)



Get geolocation information via IP address

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
    defaultClient.setBasePath("https://api.ip2location.com/v2");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ip = "8.8.8.8"; // String | IP address (IPv4 or IPv6) for reverse IP location lookup purpose. If not present, the server IP address will be used for the location lookup.
    String key = "key_example"; // String | API Key. Please sign up free trial license key at ip2location.com
    String _package = "WS1"; // String | Web service package of different granularity of return information.
    List<String> addon = Arrays.asList(); // List<String> | Extra information in addition to the above selected package.
    String format = "json"; // String | Format of the response message.
    String lang = "ar"; // String | Translation information. The translation only applicable for continent, country, region and city name for the addon package.
    try {
      String result = apiInstance.rootGet(ip, key, _package, addon, format, lang);
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
| **ip** | **String**| IP address (IPv4 or IPv6) for reverse IP location lookup purpose. If not present, the server IP address will be used for the location lookup. | |
| **key** | **String**| API Key. Please sign up free trial license key at ip2location.com | |
| **_package** | **String**| Web service package of different granularity of return information. | [optional] [enum: WS1, WS2, WS3, WS4, WS5, WS6, WS7, WS8, WS9, WS10, WS11, WS12, WS13, WS14, WS15, WS16, WS17, WS18, WS19, WS20, WS21, WS22, WS23, WS24, WS25] |
| **addon** | [**List&lt;String&gt;**](String.md)| Extra information in addition to the above selected package. | [optional] [enum: continent, country, region, city, geotargeting, country_groupings, time_zone_info] |
| **format** | **String**| Format of the response message. | [optional] [enum: json, xml] |
| **lang** | **String**| Translation information. The translation only applicable for continent, country, region and city name for the addon package. | [optional] [enum: ar, cs, da, de, en, es, et, fi, fr, ga, it, ja, ko, ms, nl, pt, ru, sv, tr, vi, zh-cn, zh-tw] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get response from IP lookup |  -  |

