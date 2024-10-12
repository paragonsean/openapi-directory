# DefaultApi

All URIs are relative to *https://regcheck.local/infiniteloopltd/CarRegistration/1.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**check**](DefaultApi.md#check) | **GET** /Check | Gets details of a UK Vehicle |


<a id="check"></a>
# **check**
> List&lt;Object&gt; check(searchString)

Gets details of a UK Vehicle

Gets details of a UK Vehicle 

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
    defaultClient.setBasePath("https://regcheck.local/infiniteloopltd/CarRegistration/1.0.0");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String searchString = "searchString_example"; // String | A registration number
    try {
      List<Object> result = apiInstance.check(searchString);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#check");
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
| **searchString** | **String**| A registration number | |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | vehicle information |  -  |
| **500** | bad input parameter |  -  |

