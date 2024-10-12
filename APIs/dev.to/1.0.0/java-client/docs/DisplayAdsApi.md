# DisplayAdsApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiDisplayAdsGet**](DisplayAdsApi.md#apiDisplayAdsGet) | **GET** /api/display_ads | display ads |
| [**apiDisplayAdsIdGet**](DisplayAdsApi.md#apiDisplayAdsIdGet) | **GET** /api/display_ads/{id} | display ad |
| [**apiDisplayAdsIdPut**](DisplayAdsApi.md#apiDisplayAdsIdPut) | **PUT** /api/display_ads/{id} | display ads |
| [**apiDisplayAdsIdUnpublishPut**](DisplayAdsApi.md#apiDisplayAdsIdUnpublishPut) | **PUT** /api/display_ads/{id}/unpublish | unpublish |
| [**apiDisplayAdsPost**](DisplayAdsApi.md#apiDisplayAdsPost) | **POST** /api/display_ads | display ads |


<a id="apiDisplayAdsGet"></a>
# **apiDisplayAdsGet**
> List&lt;DisplayAd&gt; apiDisplayAdsGet()

display ads

This endpoint allows the client to retrieve a list of all display ads.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisplayAdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DisplayAdsApi apiInstance = new DisplayAdsApi(defaultClient);
    try {
      List<DisplayAd> result = apiInstance.apiDisplayAdsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisplayAdsApi#apiDisplayAdsGet");
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

[**List&lt;DisplayAd&gt;**](DisplayAd.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |

<a id="apiDisplayAdsIdGet"></a>
# **apiDisplayAdsIdGet**
> apiDisplayAdsIdGet(id)

display ad

This endpoint allows the client to retrieve a single display ad, via its id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisplayAdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DisplayAdsApi apiInstance = new DisplayAdsApi(defaultClient);
    Integer id = 123; // Integer | The ID of the display ad.
    try {
      apiInstance.apiDisplayAdsIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisplayAdsApi#apiDisplayAdsIdGet");
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
| **id** | **Integer**| The ID of the display ad. | |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **404** | Unknown DisplayAd ID |  -  |

<a id="apiDisplayAdsIdPut"></a>
# **apiDisplayAdsIdPut**
> List&lt;DisplayAd&gt; apiDisplayAdsIdPut(id, displayAd)

display ads

This endpoint allows the client to update the attributes of a single display ad, via its id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisplayAdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DisplayAdsApi apiInstance = new DisplayAdsApi(defaultClient);
    Integer id = 123; // Integer | The ID of the display ad.
    List<DisplayAd> displayAd = Arrays.asList(); // List<DisplayAd> | 
    try {
      List<DisplayAd> result = apiInstance.apiDisplayAdsIdPut(id, displayAd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisplayAdsApi#apiDisplayAdsIdPut");
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
| **id** | **Integer**| The ID of the display ad. | |
| **displayAd** | [**List&lt;DisplayAd&gt;**](DisplayAd.md)|  | [optional] |

### Return type

[**List&lt;DisplayAd&gt;**](DisplayAd.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **404** | not found |  -  |

<a id="apiDisplayAdsIdUnpublishPut"></a>
# **apiDisplayAdsIdUnpublishPut**
> apiDisplayAdsIdUnpublishPut(id)

unpublish

This endpoint allows the client to remove a display ad from rotation by un-publishing it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisplayAdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DisplayAdsApi apiInstance = new DisplayAdsApi(defaultClient);
    Integer id = 123; // Integer | The ID of the display ad to unpublish.
    try {
      apiInstance.apiDisplayAdsIdUnpublishPut(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisplayAdsApi#apiDisplayAdsIdUnpublishPut");
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
| **id** | **Integer**| The ID of the display ad to unpublish. | |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | no content |  -  |
| **401** | unauthorized |  -  |
| **404** | not found |  -  |

<a id="apiDisplayAdsPost"></a>
# **apiDisplayAdsPost**
> List&lt;DisplayAd&gt; apiDisplayAdsPost(displayAd)

display ads

This endpoint allows the client to create a new display ad.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisplayAdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    DisplayAdsApi apiInstance = new DisplayAdsApi(defaultClient);
    List<DisplayAd> displayAd = Arrays.asList(); // List<DisplayAd> | 
    try {
      List<DisplayAd> result = apiInstance.apiDisplayAdsPost(displayAd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisplayAdsApi#apiDisplayAdsPost");
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
| **displayAd** | [**List&lt;DisplayAd&gt;**](DisplayAd.md)|  | [optional] |

### Return type

[**List&lt;DisplayAd&gt;**](DisplayAd.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | unauthorized |  -  |
| **422** | unprocessable |  -  |

