# CategoriesApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addCategories**](CategoriesApi.md#addCategories) | **POST** /categories.{content_type} | Add user categories |
| [**deleteCategories**](CategoriesApi.md#deleteCategories) | **DELETE** /categories.{content_type} | Remove user categories |
| [**getCategories**](CategoriesApi.md#getCategories) | **GET** /categories.{content_type} | Retrieve user categories |
| [**updateCategories**](CategoriesApi.md#updateCategories) | **PUT** /categories.{content_type} | Updates user categories |


<a id="addCategories"></a>
# **addCategories**
> List&lt;CategoryResponseVersion&gt; addCategories(contentType, categories, configId)

Add user categories

This method adds user categories on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object categories = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration user categories linked to.
    try {
      List<CategoryResponseVersion> result = apiInstance.addCategories(contentType, categories, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#addCategories");
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
| **contentType** | **String**|  | |
| **categories** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration user categories linked to. | [optional] |

### Return type

[**List&lt;CategoryResponseVersion&gt;**](CategoryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed categories per configuration or samples per category achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="deleteCategories"></a>
# **deleteCategories**
> deleteCategories(contentType, categoryIDs, configId)

Remove user categories

This method removes certain user categories by their IDs on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    List<String> categoryIDs = Arrays.asList(); // List<String> | List of user category identifiers.
    String configId = "configId_example"; // String | Identifier of configuration user categories linked to.
    try {
      apiInstance.deleteCategories(contentType, categoryIDs, configId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#deleteCategories");
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
| **contentType** | **String**|  | |
| **categoryIDs** | [**List&lt;String&gt;**](String.md)| List of user category identifiers. | |
| **configId** | **String**| Identifier of configuration user categories linked to. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **403** | Forbidden. Server responds if client tries to remove primary configuration. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="getCategories"></a>
# **getCategories**
> List&lt;CategoryResponseVersion&gt; getCategories(contentType, configId)

Retrieve user categories

This method retrieves list of user categories available on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration user categories linked to.
    try {
      List<CategoryResponseVersion> result = apiInstance.getCategories(contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#getCategories");
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
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration user categories linked to. | [optional] |

### Return type

[**List&lt;CategoryResponseVersion&gt;**](CategoryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the categories list. |  -  |
| **202** | Client request accepted, no categories found. Server responds with empty body. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="updateCategories"></a>
# **updateCategories**
> List&lt;CategoryResponseVersion&gt; updateCategories(contentType, categories, configId)

Updates user categories

This method updates user categories by unique IDs on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object categories = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration user categories linked to.
    try {
      List<CategoryResponseVersion> result = apiInstance.updateCategories(contentType, categories, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#updateCategories");
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
| **contentType** | **String**|  | |
| **categories** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration user categories linked to. | [optional] |

### Return type

[**List&lt;CategoryResponseVersion&gt;**](CategoryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed categories per configuration or samples per category achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

