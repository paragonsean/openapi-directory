# InfoApi

All URIs are relative to *https://developer.o2.cz/mobility/sandbox/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInfo**](InfoApi.md#getInfo) | **GET** /info | Information about versions of application and data. |


<a id="getInfo"></a>
# **getInfo**
> InfoResult getInfo()

Information about versions of application and data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.o2.cz/mobility/sandbox/api");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      InfoResult result = apiInstance.getInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#getInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InfoResult**](InfoResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response with the requested content. |  -  |

