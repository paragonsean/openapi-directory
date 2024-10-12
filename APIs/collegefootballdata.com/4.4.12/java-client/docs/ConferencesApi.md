# ConferencesApi

All URIs are relative to *https://api.collegefootballdata.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConferences**](ConferencesApi.md#getConferences) | **GET** /conferences | Conferences |


<a id="getConferences"></a>
# **getConferences**
> List&lt;Conference&gt; getConferences()

Conferences

Get conference list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConferencesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.collegefootballdata.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ConferencesApi apiInstance = new ConferencesApi(defaultClient);
    try {
      List<Conference> result = apiInstance.getConferences();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConferencesApi#getConferences");
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

[**List&lt;Conference&gt;**](Conference.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | error |  -  |

