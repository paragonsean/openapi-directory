# InfoApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groovInfo**](InfoApi.md#groovInfo) | **GET** /info |  |


<a id="groovInfo"></a>
# **groovInfo**
> GroovInfo groovInfo()



Get information about groov View. No authorization required.

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
    defaultClient.setBasePath("/api");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      GroovInfo result = apiInstance.groovInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#groovInfo");
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

[**GroovInfo**](GroovInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

