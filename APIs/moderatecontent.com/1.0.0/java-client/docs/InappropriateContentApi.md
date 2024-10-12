# InappropriateContentApi

All URIs are relative to *https://api.moderatecontent.com/moderate*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rootGet**](InappropriateContentApi.md#rootGet) | **GET** / | Blocks images with nudity |


<a id="rootGet"></a>
# **rootGet**
> rootGet(url)

Blocks images with nudity

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InappropriateContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.moderatecontent.com/moderate");

    InappropriateContentApi apiInstance = new InappropriateContentApi(defaultClient);
    String url = "url_example"; // String | 
    try {
      apiInstance.rootGet(url);
    } catch (ApiException e) {
      System.err.println("Exception when calling InappropriateContentApi#rootGet");
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
| **url** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

