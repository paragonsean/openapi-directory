# DefaultApi

All URIs are relative to *https://api.geodatasource.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cityGet**](DefaultApi.md#cityGet) | **GET** /city |  |


<a id="cityGet"></a>
# **cityGet**
> String cityGet(key, lng, lat, format)



Get City name by using latitude and longitude

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
    defaultClient.setBasePath("https://api.geodatasource.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | 
    BigDecimal lng = new BigDecimal(78); // BigDecimal | 
    BigDecimal lat = new BigDecimal(78); // BigDecimal | 
    String format = "json"; // String | 
    try {
      String result = apiInstance.cityGet(key, lng, lat, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#cityGet");
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
| **key** | **String**|  | |
| **lng** | **BigDecimal**|  | |
| **lat** | **BigDecimal**|  | |
| **format** | **String**|  | [optional] [enum: json, xml] |

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
| **200** | Get response from longitude latitude lookup |  -  |

