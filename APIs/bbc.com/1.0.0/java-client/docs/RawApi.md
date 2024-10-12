# RawApi

All URIs are relative to *https://programmes.api.bbc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRawAncestors**](RawApi.md#getRawAncestors) | **GET** /v1/episodes/{pid}/ancestors/ | Get raw ancestors |
| [**getRawBrand**](RawApi.md#getRawBrand) | **GET** /v1/brands/{pid} | Get raw brand |
| [**getRawBrandFranchises**](RawApi.md#getRawBrandFranchises) | **GET** /v1/brands/{pid}/franchises/ | Get raw brand franchise |
| [**getRawEpisode**](RawApi.md#getRawEpisode) | **GET** /v1/episodes/{pid} | Get raw episode |
| [**getRawFormats**](RawApi.md#getRawFormats) | **GET** /v1/episodes/{pid}/formats/ | Get raw formats |
| [**getRawGenreGroups**](RawApi.md#getRawGenreGroups) | **GET** /v1/episodes/{pid}/genre_groups/ | Get raw genre groups |
| [**getRawImage**](RawApi.md#getRawImage) | **GET** /v1/images/{pid} | Get raw image |
| [**getRawMasterbrand**](RawApi.md#getRawMasterbrand) | **GET** /v1/master_brands/{mbid} | Get raw masterbrand |
| [**getRawPromotion**](RawApi.md#getRawPromotion) | **GET** /v1/promotions/{pid} | Get raw promotion |


<a id="getRawAncestors"></a>
# **getRawAncestors**
> Nitro getRawAncestors(pid)

Get raw ancestors

Get raw ancestors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String pid = "pid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawAncestors(pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawAncestors");
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
| **pid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

<a id="getRawBrand"></a>
# **getRawBrand**
> Nitro getRawBrand(pid)

Get raw brand

Get raw brand

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String pid = "pid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawBrand(pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawBrand");
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
| **pid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

<a id="getRawBrandFranchises"></a>
# **getRawBrandFranchises**
> Nitro getRawBrandFranchises(pid)

Get raw brand franchise

Get raw brand franchises

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String pid = "pid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawBrandFranchises(pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawBrandFranchises");
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
| **pid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

<a id="getRawEpisode"></a>
# **getRawEpisode**
> Nitro getRawEpisode(pid)

Get raw episode

Get raw episode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String pid = "pid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawEpisode(pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawEpisode");
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
| **pid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

<a id="getRawFormats"></a>
# **getRawFormats**
> Nitro getRawFormats(pid)

Get raw formats

Get raw formats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String pid = "pid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawFormats(pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawFormats");
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
| **pid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

<a id="getRawGenreGroups"></a>
# **getRawGenreGroups**
> Nitro getRawGenreGroups(pid)

Get raw genre groups

Get raw genre groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String pid = "pid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawGenreGroups(pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawGenreGroups");
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
| **pid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

<a id="getRawImage"></a>
# **getRawImage**
> Nitro getRawImage(pid)

Get raw image

Get raw image

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String pid = "pid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawImage(pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawImage");
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
| **pid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

<a id="getRawMasterbrand"></a>
# **getRawMasterbrand**
> Nitro getRawMasterbrand(mbid)

Get raw masterbrand

Get raw masterbrand

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String mbid = "mbid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawMasterbrand(mbid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawMasterbrand");
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
| **mbid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

<a id="getRawPromotion"></a>
# **getRawPromotion**
> Nitro getRawPromotion(pid)

Get raw promotion

Get raw promotion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RawApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://programmes.api.bbc.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RawApi apiInstance = new RawApi(defaultClient);
    String pid = "pid_example"; // String | 
    try {
      Nitro result = apiInstance.getRawPromotion(pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RawApi#getRawPromotion");
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
| **pid** | **String**|  | |

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nitro response |  -  |

