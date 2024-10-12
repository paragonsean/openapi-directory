# StoreApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storeGet**](StoreApi.md#storeGet) | **GET** /store | Get Fortnite Store |


<a id="storeGet"></a>
# **storeGet**
> Object storeGet()

Get Fortnite Store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://skynewz-api-fortnite.herokuapp.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    StoreApi apiInstance = new StoreApi(defaultClient);
    try {
      Object result = apiInstance.storeGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoreApi#storeGet");
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

**Object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current store object |  -  |
| **0** | Unexpected error |  -  |

