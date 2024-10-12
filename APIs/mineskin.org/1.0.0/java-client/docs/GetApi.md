# GetApi

All URIs are relative to *https://api.mineskin.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDelayGet**](GetApi.md#getDelayGet) | **GET** /get/delay |  |
| [**getIdIdGet**](GetApi.md#getIdIdGet) | **GET** /get/id/{id} |  |
| [**getListPageGet**](GetApi.md#getListPageGet) | **GET** /get/list/{page} |  |
| [**getUuidUuidGet**](GetApi.md#getUuidUuidGet) | **GET** /get/uuid/{uuid} |  |


<a id="getDelayGet"></a>
# **getDelayGet**
> GetDelayGet200Response getDelayGet(userAgent)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    GetApi apiInstance = new GetApi(defaultClient);
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    try {
      GetDelayGet200Response result = apiInstance.getDelayGet(userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#getDelayGet");
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
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |

### Return type

[**GetDelayGet200Response**](GetDelayGet200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delay info for the requesting client |  -  |

<a id="getIdIdGet"></a>
# **getIdIdGet**
> SkinInfo getIdIdGet(id, userAgent)



Deprecated. Use /get/uuid instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");

    GetApi apiInstance = new GetApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | 
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    try {
      SkinInfo result = apiInstance.getIdIdGet(id, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#getIdIdGet");
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
| **id** | **BigDecimal**|  | |
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |

### Return type

[**SkinInfo**](SkinInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skin Info |  -  |

<a id="getListPageGet"></a>
# **getListPageGet**
> GetListPageGet200Response getListPageGet(page, userAgent)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");

    GetApi apiInstance = new GetApi(defaultClient);
    BigDecimal page = new BigDecimal(78); // BigDecimal | For reference pagination, the uuid of the last skin in the previous page. For numeric pagination (deprecated), the page number or 'start'.
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    try {
      GetListPageGet200Response result = apiInstance.getListPageGet(page, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#getListPageGet");
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
| **page** | **BigDecimal**| For reference pagination, the uuid of the last skin in the previous page. For numeric pagination (deprecated), the page number or &#39;start&#39;. | |
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |

### Return type

[**GetListPageGet200Response**](GetListPageGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skin Info List |  -  |

<a id="getUuidUuidGet"></a>
# **getUuidUuidGet**
> SkinInfo getUuidUuidGet(uuid, userAgent)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mineskin.org");

    GetApi apiInstance = new GetApi(defaultClient);
    UUID uuid = UUID.randomUUID(); // UUID | 
    String userAgent = "ExampleApp/v1.0"; // String | Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    try {
      SkinInfo result = apiInstance.getUuidUuidGet(uuid, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetApi#getUuidUuidGet");
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
| **uuid** | **UUID**|  | |
| **userAgent** | **String**| Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples | |

### Return type

[**SkinInfo**](SkinInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skin Info |  -  |

