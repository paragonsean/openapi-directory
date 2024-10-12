# EntitiesApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addEntities**](EntitiesApi.md#addEntities) | **POST** /entities.{content_type} | Add user entities |
| [**deleteEntities**](EntitiesApi.md#deleteEntities) | **DELETE** /entities.{content_type} | Remove user entities |
| [**getEntities**](EntitiesApi.md#getEntities) | **GET** /entities.{content_type} | Retrieve user entities |
| [**updateEntities**](EntitiesApi.md#updateEntities) | **PUT** /entities.{content_type} | Update user entities |


<a id="addEntities"></a>
# **addEntities**
> List&lt;EntityResponseVersion&gt; addEntities(contentType, userEntities, configId)

Add user entities

This method adds user entities on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object userEntities = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration user entities linked to.
    try {
      List<EntityResponseVersion> result = apiInstance.addEntities(contentType, userEntities, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#addEntities");
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
| **userEntities** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration user entities linked to. | [optional] |

### Return type

[**List&lt;EntityResponseVersion&gt;**](EntityResponseVersion.md)

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
| **406** | Number of allowed entities per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="deleteEntities"></a>
# **deleteEntities**
> deleteEntities(contentType)

Remove user entities

This method removes certain user entities by their names on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    try {
      apiInstance.deleteEntities(contentType);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#deleteEntities");
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

<a id="getEntities"></a>
# **getEntities**
> List&lt;EntityResponseVersion&gt; getEntities(contentType, configId)

Retrieve user entities

This method retrieves list of user entities available on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration user entities linked to.
    try {
      List<EntityResponseVersion> result = apiInstance.getEntities(contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#getEntities");
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
| **configId** | **String**| Identifier of configuration user entities linked to. | [optional] |

### Return type

[**List&lt;EntityResponseVersion&gt;**](EntityResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the entities list. |  -  |
| **202** | Client request accepted and no entities found. Server responds with empty body. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="updateEntities"></a>
# **updateEntities**
> List&lt;EntityResponseVersion&gt; updateEntities(contentType, userEntities, configId)

Update user entities

This method updates user entities by unique IDs on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object userEntities = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration user entities linked to.
    try {
      List<EntityResponseVersion> result = apiInstance.updateEntities(contentType, userEntities, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#updateEntities");
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
| **userEntities** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration user entities linked to. | [optional] |

### Return type

[**List&lt;EntityResponseVersion&gt;**](EntityResponseVersion.md)

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
| **406** | Number of allowed entities per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

