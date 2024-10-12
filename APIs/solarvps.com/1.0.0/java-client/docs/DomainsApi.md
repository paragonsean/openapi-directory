# DomainsApi

All URIs are relative to *http://api.ss.solarvps.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainsAddPost**](DomainsApi.md#domainsAddPost) | **POST** /domains/add | Add domain to be managed by SolarVPS Distributed DNS |
| [**domainsDeletePost**](DomainsApi.md#domainsDeletePost) | **POST** /domains/delete | Delete domain from SolarVPS Distributed DNS |
| [**domainsGet**](DomainsApi.md#domainsGet) | **GET** /domains | View all your domains managed by SolarVPS Distributed DNS |


<a id="domainsAddPost"></a>
# **domainsAddPost**
> domainsAddPost(domain)

Add domain to be managed by SolarVPS Distributed DNS

Adds domain to SolarVPS Distributed DNS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domain = "domain_example"; // String | Domain to add to SolarVPS Distributed DNS
    try {
      apiInstance.domainsAddPost(domain);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsAddPost");
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
| **domain** | **String**| Domain to add to SolarVPS Distributed DNS | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="domainsDeletePost"></a>
# **domainsDeletePost**
> domainsDeletePost(domain)

Delete domain from SolarVPS Distributed DNS

Deletes domain from SolarVPS Distributed DNS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domain = "domain_example"; // String | Domain to delete from SolarVPS Distributed DNS
    try {
      apiInstance.domainsDeletePost(domain);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsDeletePost");
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
| **domain** | **String**| Domain to delete from SolarVPS Distributed DNS | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="domainsGet"></a>
# **domainsGet**
> domainsGet()

View all your domains managed by SolarVPS Distributed DNS

Shows all your domains

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    try {
      apiInstance.domainsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsGet");
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

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

