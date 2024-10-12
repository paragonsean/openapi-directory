# StatsApi

All URIs are relative to *https://api.isbndb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statsGet**](StatsApi.md#statsGet) | **GET** /stats | Gets status on the ISBNDB Database |


<a id="statsGet"></a>
# **statsGet**
> statsGet()

Gets status on the ISBNDB Database

Returns a status object about the ISBNDB database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    StatsApi apiInstance = new StatsApi(defaultClient);
    try {
      apiInstance.statsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#statsGet");
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

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stats on the ISBNDB sucessfully retrieved |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |

