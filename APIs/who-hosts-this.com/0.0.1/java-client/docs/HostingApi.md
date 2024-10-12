# HostingApi

All URIs are relative to *https://www.who-hosts-this.com/APIEndpoint*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**detectGet**](HostingApi.md#detectGet) | **GET** /Detect | Discover the hosting provider for a web site |


<a id="detectGet"></a>
# **detectGet**
> detectGet(url)

Discover the hosting provider for a web site

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.who-hosts-this.com/APIEndpoint");
    
    // Configure API key authorization: QueryKey
    ApiKeyAuth QueryKey = (ApiKeyAuth) defaultClient.getAuthentication("QueryKey");
    QueryKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //QueryKey.setApiKeyPrefix("Token");

    HostingApi apiInstance = new HostingApi(defaultClient);
    String url = "url_example"; // String | The url of the page to check
    try {
      apiInstance.detectGet(url);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostingApi#detectGet");
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
| **url** | **String**| The url of the page to check | |

### Return type

null (empty response body)

### Authorization

[QueryKey](../README.md#QueryKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status of the detection and list of any found hosting providers |  -  |

