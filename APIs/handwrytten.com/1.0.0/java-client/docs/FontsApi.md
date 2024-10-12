# FontsApi

All URIs are relative to *https://api.handwrytten.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fontsList**](FontsApi.md#fontsList) | **GET** /fonts/list | Lists Handwryting styles available for use |


<a id="fontsList"></a>
# **fontsList**
> List&lt;Font&gt; fontsList()

Lists Handwryting styles available for use

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FontsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.handwrytten.com/v1");

    FontsApi apiInstance = new FontsApi(defaultClient);
    try {
      List<Font> result = apiInstance.fontsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FontsApi#fontsList");
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

[**List&lt;Font&gt;**](Font.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

