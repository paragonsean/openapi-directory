# DefaultApi

All URIs are relative to *https://api-vs.herokuapp.com/vs/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesGet**](DefaultApi.md#resourcesGet) | **GET** /resources | Fetch all meanings that contain a specific English string |


<a id="resourcesGet"></a>
# **resourcesGet**
> resourcesGet(description)

Fetch all meanings that contain a specific English string

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
    defaultClient.setBasePath("https://api-vs.herokuapp.com/vs/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String description = "description_example"; // String | The string you are looking for in the word meaning, for example, chariot. Wildcards are allowed, for example, char\\*.
    try {
      apiInstance.resourcesGet(description);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#resourcesGet");
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
| **description** | **String**| The string you are looking for in the word meaning, for example, chariot. Wildcards are allowed, for example, char\\*. | |

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
| **200** | Entries fetched. |  -  |
| **404** | No such string exists in this API. |  -  |

