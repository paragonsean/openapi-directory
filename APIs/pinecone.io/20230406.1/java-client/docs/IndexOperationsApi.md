# IndexOperationsApi

All URIs are relative to *https://controller.us-east1-gcp.pinecone.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureIndex**](IndexOperationsApi.md#configureIndex) | **PATCH** /databases/{indexName} | Configure index |
| [**createCollection**](IndexOperationsApi.md#createCollection) | **POST** /collections | Create collection |
| [**createIndex**](IndexOperationsApi.md#createIndex) | **POST** /databases | Create index |
| [**deleteCollection**](IndexOperationsApi.md#deleteCollection) | **DELETE** /collections/{collectionName} | Delete Collection |
| [**deleteIndex**](IndexOperationsApi.md#deleteIndex) | **DELETE** /databases/{indexName} | Delete Index |
| [**describeCollection**](IndexOperationsApi.md#describeCollection) | **GET** /collections/{collectionName} | Describe collection |
| [**describeIndex**](IndexOperationsApi.md#describeIndex) | **GET** /databases/{indexName} | Describe index |
| [**listCollections**](IndexOperationsApi.md#listCollections) | **GET** /collections | List collections |
| [**listIndexes**](IndexOperationsApi.md#listIndexes) | **GET** /databases | List indexes |


<a id="configureIndex"></a>
# **configureIndex**
> configureIndex(indexName, indexConfiguration)

Configure index

This operation specifies the pod type and number of replicas for an index.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    String indexName = "indexName_example"; // String | 
    IndexConfiguration indexConfiguration = new IndexConfiguration(); // IndexConfiguration | 
    try {
      apiInstance.configureIndex(indexName, indexConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#configureIndex");
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
| **indexName** | **String**|  | |
| **indexConfiguration** | [**IndexConfiguration**](IndexConfiguration.md)|  | |

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The index has been successfully updated. |  -  |
| **400** | Quota exceeded, or invalid parameters. |  -  |
| **404** | Index not found. |  -  |
| **500** | Internal error. Can be caused by invalid parameters. |  -  |

<a id="createCollection"></a>
# **createCollection**
> createCollection(collectionDefinition)

Create collection

This operation creates a Pinecone collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    CollectionDefinition collectionDefinition = new CollectionDefinition(); // CollectionDefinition | 
    try {
      apiInstance.createCollection(collectionDefinition);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#createCollection");
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
| **collectionDefinition** | [**CollectionDefinition**](CollectionDefinition.md)|  | |

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The collection has been successfully created. |  -  |
| **400** | Quota exceeded, or invalid parameters. |  -  |
| **409** | A collection with the name provided already exists. |  -  |
| **500** | Internal error. Can be caused by invalid parameters. |  -  |

<a id="createIndex"></a>
# **createIndex**
> createIndex(indexDefinition)

Create index

This operation creates a Pinecone index. You can use it to specify the measure of similarity, the dimension of vectors to be stored in the index, the numbers of replicas to use, and more.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    IndexDefinition indexDefinition = new IndexDefinition(); // IndexDefinition | 
    try {
      apiInstance.createIndex(indexDefinition);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#createIndex");
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
| **indexDefinition** | [**IndexDefinition**](IndexDefinition.md)|  | |

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The collection has been successfully created. |  -  |
| **400** | Quota exceeded, or invalid parameters. |  -  |
| **409** | Index of given name already exists. |  -  |
| **500** | Internal error. Can be caused by invalid parameters. |  -  |

<a id="deleteCollection"></a>
# **deleteCollection**
> deleteCollection(collectionName)

Delete Collection

This operation deletes an existing collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    String collectionName = "collectionName_example"; // String | 
    try {
      apiInstance.deleteCollection(collectionName);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#deleteCollection");
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
| **collectionName** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The collection has been successfully deleted. |  -  |
| **404** | Collection not found. |  -  |
| **500** | Internal error. Can be caused by invalid parameters. |  -  |

<a id="deleteIndex"></a>
# **deleteIndex**
> deleteIndex(indexName)

Delete Index

This operation deletes an existing index.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    String indexName = "indexName_example"; // String | 
    try {
      apiInstance.deleteIndex(indexName);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#deleteIndex");
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
| **indexName** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The index has been successfully deleted. |  -  |
| **404** | Index not found. |  -  |
| **500** | Internal error. Can be caused by invalid parameters. |  -  |

<a id="describeCollection"></a>
# **describeCollection**
> Collection describeCollection(collectionName)

Describe collection

Get a description of a collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    String collectionName = "collectionName_example"; // String | 
    try {
      Collection result = apiInstance.describeCollection(collectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#describeCollection");
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
| **collectionName** | **String**|  | |

### Return type

[**Collection**](Collection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This operation returns a list of all the collections in your current project. |  -  |
| **404** | Collection not found. |  -  |
| **500** | Internal error. Can be caused by invalid parameters. |  -  |

<a id="describeIndex"></a>
# **describeIndex**
> Index describeIndex(indexName)

Describe index

Get a description of an index.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    String indexName = "indexName_example"; // String | 
    try {
      Index result = apiInstance.describeIndex(indexName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#describeIndex");
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
| **indexName** | **String**|  | |

### Return type

[**Index**](Index.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This operation returns a list of all the collections in your current project. |  -  |
| **404** | Index not found. |  -  |
| **500** | Internal error. Can be caused by invalid parameters. |  -  |

<a id="listCollections"></a>
# **listCollections**
> List&lt;String&gt; listCollections()

List collections

This operation returns a list of your Pinecone collections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    try {
      List<String> result = apiInstance.listCollections();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#listCollections");
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

**List&lt;String&gt;**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This operation returns a list of all the collections in your current project. |  -  |

<a id="listIndexes"></a>
# **listIndexes**
> List&lt;String&gt; listIndexes()

List indexes

This operation returns a list of your Pinecone indexes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://controller.us-east1-gcp.pinecone.io");
    
    // Configure API key authorization: ApiKey
    ApiKeyAuth ApiKey = (ApiKeyAuth) defaultClient.getAuthentication("ApiKey");
    ApiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKey.setApiKeyPrefix("Token");

    IndexOperationsApi apiInstance = new IndexOperationsApi(defaultClient);
    try {
      List<String> result = apiInstance.listIndexes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexOperationsApi#listIndexes");
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

**List&lt;String&gt;**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This operation returns a list of all the indexes that you have previously created, and which are associated with the given API key |  -  |

