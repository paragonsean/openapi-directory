# DefaultApi

All URIs are relative to *https://ipgeolocation.abstractapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1Get**](DefaultApi.md#v1Get) | **GET** /v1/ |  |


<a id="v1Get"></a>
# **v1Get**
> InlineResponse200 v1Get(apiKey, ipAddress, fields)



Retrieve the location of an IP address

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
    defaultClient.setBasePath("https://ipgeolocation.abstractapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiKey = "apiKey_example"; // String | 
    String ipAddress = "195.154.25.40"; // String | 
    String fields = "country,city,timezone"; // String | 
    try {
      InlineResponse200 result = apiInstance.v1Get(apiKey, ipAddress, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#v1Get");
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
| **apiKey** | **String**|  | |
| **ipAddress** | **String**|  | [optional] |
| **fields** | **String**|  | [optional] |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Location of geolocated IP |  -  |

