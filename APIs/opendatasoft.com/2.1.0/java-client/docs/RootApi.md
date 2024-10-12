# RootApi

All URIs are relative to *https://public.opendatasoft.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRoot**](RootApi.md#getRoot) | **GET** / |  |


<a id="getRoot"></a>
# **getRoot**
> GetRoot200Response getRoot()



API entry point  Provides links for: * catalog, your domain&#39;s list of datasets * opendatasoft, all datasets on the Opendatasoft network 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RootApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://public.opendatasoft.com/api/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    RootApi apiInstance = new RootApi(defaultClient);
    try {
      GetRoot200Response result = apiInstance.getRoot();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RootApi#getRoot");
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

[**GetRoot200Response**](GetRoot200Response.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Provide a set of links to the most basic entry points in the API (sources) |  -  |

