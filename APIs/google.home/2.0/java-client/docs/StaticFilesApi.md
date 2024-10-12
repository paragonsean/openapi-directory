# StaticFilesApi

All URIs are relative to *http://example.com/setup*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chromecastIcon**](StaticFilesApi.md#chromecastIcon) | **GET** /icon.png | Chromecast Icon |
| [**legalNotice**](StaticFilesApi.md#legalNotice) | **GET** /NOTICE.html.gz | Legal Notice |


<a id="chromecastIcon"></a>
# **chromecastIcon**
> chromecastIcon()

Chromecast Icon

**Update:** This no longer exists. It&#39;s not useful, anyway.  A redirect to &#x60;http://www.gstatic.com/eureka/images/eureka_device.png&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    StaticFilesApi apiInstance = new StaticFilesApi(defaultClient);
    try {
      apiInstance.chromecastIcon();
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticFilesApi#chromecastIcon");
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

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="legalNotice"></a>
# **legalNotice**
> String legalNotice()

Legal Notice

All licenses of programs used by Home.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com/setup");
    
    // Configure API key authorization: cast-local-authorization-token
    ApiKeyAuth cast-local-authorization-token = (ApiKeyAuth) defaultClient.getAuthentication("cast-local-authorization-token");
    cast-local-authorization-token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cast-local-authorization-token.setApiKeyPrefix("Token");

    StaticFilesApi apiInstance = new StaticFilesApi(defaultClient);
    try {
      String result = apiInstance.legalNotice();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticFilesApi#legalNotice");
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

[cast-local-authorization-token](../README.md#cast-local-authorization-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

