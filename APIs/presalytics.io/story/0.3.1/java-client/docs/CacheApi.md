# CacheApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cacheNonceGet**](CacheApi.md#cacheNonceGet) | **GET** /cache/{nonce} | Cache: Get Subdocument |
| [**cachePost**](CacheApi.md#cachePost) | **POST** /cache | Cache: Store Subdocument |


<a id="cacheNonceGet"></a>
# **cacheNonceGet**
> String cacheNonceGet(nonce)

Cache: Get Subdocument

An endpoint for broswer retreive html documents that were cached durin the rendering process via a nonce (token)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CacheApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    CacheApi apiInstance = new CacheApi(defaultClient);
    UUID nonce = UUID.randomUUID(); // UUID | A one-time use token for retieving items in the users cache
    try {
      String result = apiInstance.cacheNonceGet(nonce);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CacheApi#cacheNonceGet");
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
| **nonce** | **UUID**| A one-time use token for retieving items in the users cache | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A cached html subdocument (typically loaded via iframe) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="cachePost"></a>
# **cachePost**
> cachePost(cachePostRequest)

Cache: Store Subdocument

An endpoint for Presalytics Renderers to cache html subdocuments for subsequent retrieval by the browser.  Documents Are retrieved via token expire after 1 minute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CacheApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    CacheApi apiInstance = new CacheApi(defaultClient);
    CachePostRequest cachePostRequest = new CachePostRequest(); // CachePostRequest | parameters to identify an update a collaborator across multiple stories
    try {
      apiInstance.cachePost(cachePostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CacheApi#cachePost");
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
| **cachePostRequest** | [**CachePostRequest**](CachePostRequest.md)| parameters to identify an update a collaborator across multiple stories | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

