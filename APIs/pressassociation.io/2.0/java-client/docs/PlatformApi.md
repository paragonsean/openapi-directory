# PlatformApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPlatform**](PlatformApi.md#getPlatform) | **GET** /platform/{platformId} | Platform Detail |
| [**listPlatformRegions**](PlatformApi.md#listPlatformRegions) | **GET** /platform/{platformId}/region | Platform Region Collection |
| [**listPlatforms**](PlatformApi.md#listPlatforms) | **GET** /platform | Platform Collection |


<a id="getPlatform"></a>
# **getPlatform**
> Object getPlatform(platformId)

Platform Detail

Return the content of the selected platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    PlatformApi apiInstance = new PlatformApi(defaultClient);
    String platformId = "d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3"; // String | The identifier for the selected platform.
    try {
      Object result = apiInstance.getPlatform(platformId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformApi#getPlatform");
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
| **platformId** | **String**| The identifier for the selected platform. | [default to d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listPlatformRegions"></a>
# **listPlatformRegions**
> Object listPlatformRegions(platformId, aliases)

Platform Region Collection

Return a list of regions for a platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    PlatformApi apiInstance = new PlatformApi(defaultClient);
    String platformId = "d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3"; // String | The identifier for the selected platform.
    Boolean aliases = true; // Boolean | Flag to display Legacy and Provider Ids.
    try {
      Object result = apiInstance.listPlatformRegions(platformId, aliases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformApi#listPlatformRegions");
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
| **platformId** | **String**| The identifier for the selected platform. | [default to d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3] |
| **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listPlatforms"></a>
# **listPlatforms**
> Object listPlatforms(aliases)

Platform Collection

Return a list of available platforms.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlatformApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    PlatformApi apiInstance = new PlatformApi(defaultClient);
    Boolean aliases = true; // Boolean | Flag to display Legacy and Provider Ids.
    try {
      Object result = apiInstance.listPlatforms(aliases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlatformApi#listPlatforms");
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
| **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

