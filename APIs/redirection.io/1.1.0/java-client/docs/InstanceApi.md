# InstanceApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getInstanceCollection**](InstanceApi.md#getInstanceCollection) | **GET** /instances | Retrieves the collection of Instance resources. |
| [**getInstanceItem**](InstanceApi.md#getInstanceItem) | **GET** /instances/{id} | Retrieves a Instance resource. |
| [**liveInstanceItem**](InstanceApi.md#liveInstanceItem) | **PUT** /instances/{id}/live | Replaces the Instance resource. |
| [**loggingInstanceItem**](InstanceApi.md#loggingInstanceItem) | **PUT** /instances/{id} | Replaces the Instance resource. |
| [**postInstanceCollection**](InstanceApi.md#postInstanceCollection) | **POST** /agent-instance-updates | Creates a Instance resource. |
| [**putInstanceItem**](InstanceApi.md#putInstanceItem) | **PUT** /agent-instance-updates/{id} | Replaces the Instance resource. |


<a id="getInstanceCollection"></a>
# **getInstanceCollection**
> List&lt;InstanceRead&gt; getInstanceCollection(projectId)

Retrieves the collection of Instance resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InstanceApi apiInstance = new InstanceApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    try {
      List<InstanceRead> result = apiInstance.getInstanceCollection(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceApi#getInstanceCollection");
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
| **projectId** | **String**|  | |

### Return type

[**List&lt;InstanceRead&gt;**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instance collection response |  -  |

<a id="getInstanceItem"></a>
# **getInstanceItem**
> InstanceRead getInstanceItem(id)

Retrieves a Instance resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InstanceApi apiInstance = new InstanceApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      InstanceRead result = apiInstance.getInstanceItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceApi#getInstanceItem");
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
| **id** | **String**|  | |

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instance resource response |  -  |
| **404** | Resource not found |  -  |

<a id="liveInstanceItem"></a>
# **liveInstanceItem**
> InstanceRead liveInstanceItem(id, instance)

Replaces the Instance resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InstanceApi apiInstance = new InstanceApi(defaultClient);
    String id = "id_example"; // String | 
    InstanceWrite instance = new InstanceWrite(); // InstanceWrite | The updated Instance resource
    try {
      InstanceRead result = apiInstance.liveInstanceItem(id, instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceApi#liveInstanceItem");
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
| **id** | **String**|  | |
| **instance** | [**InstanceWrite**](InstanceWrite.md)| The updated Instance resource | [optional] |

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instance resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="loggingInstanceItem"></a>
# **loggingInstanceItem**
> InstanceRead loggingInstanceItem(id, instance)

Replaces the Instance resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InstanceApi apiInstance = new InstanceApi(defaultClient);
    String id = "id_example"; // String | 
    InstanceWrite instance = new InstanceWrite(); // InstanceWrite | The updated Instance resource
    try {
      InstanceRead result = apiInstance.loggingInstanceItem(id, instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceApi#loggingInstanceItem");
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
| **id** | **String**|  | |
| **instance** | [**InstanceWrite**](InstanceWrite.md)| The updated Instance resource | [optional] |

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instance resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="postInstanceCollection"></a>
# **postInstanceCollection**
> InstanceRead postInstanceCollection(instance)

Creates a Instance resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InstanceApi apiInstance = new InstanceApi(defaultClient);
    InstanceWrite instance = new InstanceWrite(); // InstanceWrite | The new Instance resource
    try {
      InstanceRead result = apiInstance.postInstanceCollection(instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceApi#postInstanceCollection");
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
| **instance** | [**InstanceWrite**](InstanceWrite.md)| The new Instance resource | [optional] |

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Instance resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="putInstanceItem"></a>
# **putInstanceItem**
> InstanceRead putInstanceItem(id, instance)

Replaces the Instance resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InstanceApi apiInstance = new InstanceApi(defaultClient);
    String id = "id_example"; // String | 
    InstanceWrite instance = new InstanceWrite(); // InstanceWrite | The updated Instance resource
    try {
      InstanceRead result = apiInstance.putInstanceItem(id, instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceApi#putInstanceItem");
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
| **id** | **String**|  | |
| **instance** | [**InstanceWrite**](InstanceWrite.md)| The updated Instance resource | [optional] |

### Return type

[**InstanceRead**](InstanceRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Instance resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

