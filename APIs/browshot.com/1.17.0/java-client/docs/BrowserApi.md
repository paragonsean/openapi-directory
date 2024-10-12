# BrowserApi

All URIs are relative to *https://api.browshot.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBrowserInfo**](BrowserApi.md#getBrowserInfo) | **GET** /browser/info | Get information about a browser |
| [**getBrowsersInfo**](BrowserApi.md#getBrowsersInfo) | **GET** /browser/list | Get all browsers |


<a id="getBrowserInfo"></a>
# **getBrowserInfo**
> Browser getBrowserInfo(id)

Get information about a browser

Get information about a browser.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    Integer id = 56; // Integer | browser ID
    try {
      Browser result = apiInstance.getBrowserInfo(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getBrowserInfo");
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
| **id** | **Integer**| browser ID | |

### Return type

[**Browser**](Browser.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Browser information |  -  |
| **0** | Browser not found |  -  |

<a id="getBrowsersInfo"></a>
# **getBrowsersInfo**
> BrowserList getBrowsersInfo()

Get all browsers

Get all browsers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrowserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.browshot.com/api/v1");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    BrowserApi apiInstance = new BrowserApi(defaultClient);
    try {
      BrowserList result = apiInstance.getBrowsersInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrowserApi#getBrowsersInfo");
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

[**BrowserList**](BrowserList.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instance information |  -  |
| **0** | Account not found |  -  |

