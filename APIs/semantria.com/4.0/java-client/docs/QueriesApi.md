# QueriesApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addQueries**](QueriesApi.md#addQueries) | **POST** /queries.{content_type} | Add or update queries |
| [**deleteQueries**](QueriesApi.md#deleteQueries) | **DELETE** /queries.{content_type} | Remove queries |
| [**getQueries**](QueriesApi.md#getQueries) | **GET** /queries.{content_type} | Retrieve queries |
| [**updateQueries**](QueriesApi.md#updateQueries) | **PUT** /queries.{content_type} | Update queries |


<a id="addQueries"></a>
# **addQueries**
> List&lt;QueryResponseVersion&gt; addQueries(contentType, queries, configId)

Add or update queries

This method adds queries on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object queries = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration queries linked to.
    try {
      List<QueryResponseVersion> result = apiInstance.addQueries(contentType, queries, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#addQueries");
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
| **queries** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration queries linked to. | [optional] |

### Return type

[**List&lt;QueryResponseVersion&gt;**](QueryResponseVersion.md)

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
| **406** | Number of allowed queries per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="deleteQueries"></a>
# **deleteQueries**
> deleteQueries(contentType, queryIDs, configId)

Remove queries

This method removes certain queries by their IDs on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    List<String> queryIDs = Arrays.asList(); // List<String> | List of query identifiers.
    String configId = "configId_example"; // String | Identifier of configuration queries linked to.
    try {
      apiInstance.deleteQueries(contentType, queryIDs, configId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#deleteQueries");
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
| **queryIDs** | [**List&lt;String&gt;**](String.md)| List of query identifiers. | |
| **configId** | **String**| Identifier of configuration queries linked to. | [optional] |

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

<a id="getQueries"></a>
# **getQueries**
> List&lt;QueryResponseVersion&gt; getQueries(contentType, configId)

Retrieve queries

This method retrieves list of queries available on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration queries linked to.
    try {
      List<QueryResponseVersion> result = apiInstance.getQueries(contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#getQueries");
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
| **configId** | **String**| Identifier of configuration queries linked to. | [optional] |

### Return type

[**List&lt;QueryResponseVersion&gt;**](QueryResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the queries list. |  -  |
| **202** | Client request accepted and no queries found. Server responds with empty body. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="updateQueries"></a>
# **updateQueries**
> List&lt;QueryResponseVersion&gt; updateQueries(contentType, queries, configId)

Update queries

This method updates queries by unique IDs on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    QueriesApi apiInstance = new QueriesApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object queries = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration queries linked to.
    try {
      List<QueryResponseVersion> result = apiInstance.updateQueries(contentType, queries, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueriesApi#updateQueries");
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
| **queries** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration queries linked to. | [optional] |

### Return type

[**List&lt;QueryResponseVersion&gt;**](QueryResponseVersion.md)

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
| **406** | Number of allowed queries per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

