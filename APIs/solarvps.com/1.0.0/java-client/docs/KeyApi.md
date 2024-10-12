# KeyApi

All URIs are relative to *http://api.ss.solarvps.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**keyGenerateGet**](KeyApi.md#keyGenerateGet) | **GET** /key/generate | Generate API Key |
| [**keyGetGet**](KeyApi.md#keyGetGet) | **GET** /key/get | Get API Key |


<a id="keyGenerateGet"></a>
# **keyGenerateGet**
> keyGenerateGet(username, password)

Generate API Key

API Key is regenerated if it already exists

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String username = "username_example"; // String | Email address used to login to SolarSystem
    String password = "password_example"; // String | Password used to login to SolarSystem
    try {
      apiInstance.keyGenerateGet(username, password);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyGenerateGet");
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
| **username** | **String**| Email address used to login to SolarSystem | |
| **password** | **String**| Password used to login to SolarSystem | |

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

<a id="keyGetGet"></a>
# **keyGetGet**
> keyGetGet(username, password)

Get API Key

Gets the API Key for user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String username = "username_example"; // String | Email address used to login to SolarSystem
    String password = "password_example"; // String | Password used to login to SolarSystem
    try {
      apiInstance.keyGetGet(username, password);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#keyGetGet");
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
| **username** | **String**| Email address used to login to SolarSystem | |
| **password** | **String**| Password used to login to SolarSystem | |

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

