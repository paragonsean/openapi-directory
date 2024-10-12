# EmojisApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**emojisGet**](EmojisApi.md#emojisGet) | **GET** /emojis | Get emojis |


<a id="emojisGet"></a>
# **emojisGet**
> Map&lt;String, String&gt; emojisGet()

Get emojis

Lists all the emojis available to use on GitHub Enterprise Server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmojisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    EmojisApi apiInstance = new EmojisApi(defaultClient);
    try {
      Map<String, String> result = apiInstance.emojisGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmojisApi#emojisGet");
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

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |

