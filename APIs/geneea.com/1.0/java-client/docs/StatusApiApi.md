# StatusApiApi

All URIs are relative to *https://api.geneea.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**status**](StatusApiApi.md#status) | **GET** /status | Gets status of the Interpretor service |


<a id="status"></a>
# **status**
> String status()

Gets status of the Interpretor service

status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.geneea.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    StatusApiApi apiInstance = new StatusApiApi(defaultClient);
    try {
      String result = apiInstance.status();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApiApi#status");
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

**String**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

