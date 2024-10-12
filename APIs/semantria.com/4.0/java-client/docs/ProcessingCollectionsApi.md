# ProcessingCollectionsApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelCollection**](ProcessingCollectionsApi.md#cancelCollection) | **DELETE** /collection/{collection_id}.{content_type} | Cancel collection analysis |
| [**queueCollection**](ProcessingCollectionsApi.md#queueCollection) | **POST** /collection.{content_type} | Queue collection for analysis |
| [**receiveCollectionAnalyticData**](ProcessingCollectionsApi.md#receiveCollectionAnalyticData) | **GET** /collection/{collection_id}.{content_type} | Retrieve collection analysis or its status in queue |
| [**retrieveProcessedCollections**](ProcessingCollectionsApi.md#retrieveProcessedCollections) | **GET** /collection/processed.{content_type} | Retrieve collections analysis |


<a id="cancelCollection"></a>
# **cancelCollection**
> cancelCollection(collectionId, contentType, configId)

Cancel collection analysis

This method cancels collection analysis by unique ID on Semantria side if it is waiting for analysis in queue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingCollectionsApi apiInstance = new ProcessingCollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection ID
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      apiInstance.cancelCollection(collectionId, contentType, configId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingCollectionsApi#cancelCollection");
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
| **collectionId** | **String**| Collection ID | |
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

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
| **200** | Client request accepted. Document canceled from processing on the server. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **404** | No collections with provided ID found on server. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="queueCollection"></a>
# **queueCollection**
> Collection queueCollection(contentType, collection, configId)

Queue collection for analysis

This method queues collection of documents onto the server for analysis. Queued collection of documents analyzes in common context as entire thing. If unique configuration ID provided, Semantria uses settings of that configuration during analysis, in opposite the primary configuration uses. Collection IDs are unique in scope of configuration. If the same ID appears twice, Semantria overrides existing collection with the new Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingCollectionsApi apiInstance = new ProcessingCollectionsApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object collection = null; // Object | Parametrized JSON or XML object.
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      Collection result = apiInstance.queueCollection(contentType, collection, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingCollectionsApi#queueCollection");
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
| **collection** | **Object**| Parametrized JSON or XML object. | |
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

### Return type

[**Collection**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the sentiment-bearing phrases list. |  -  |
| **202** | Client request accepted and queued for processing. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Documents limit per collection is achieved. |  -  |
| **413** | Characters limit for single document exceeded. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="receiveCollectionAnalyticData"></a>
# **receiveCollectionAnalyticData**
> CollectionAnalyticData receiveCollectionAnalyticData(collectionId, contentType, configId)

Retrieve collection analysis or its status in queue

This method retrieves analysis results for documents collection by its unique ID or the collection’s status in queue if it did not analyzed yet. Semantria guarantees delivering of all collections back to the client even if they FAILED on Semantria side due to some reason.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingCollectionsApi apiInstance = new ProcessingCollectionsApi(defaultClient);
    String collectionId = "collectionId_example"; // String | Collection ID
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      CollectionAnalyticData result = apiInstance.receiveCollectionAnalyticData(collectionId, contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingCollectionsApi#receiveCollectionAnalyticData");
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
| **collectionId** | **String**| Collection ID | |
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

### Return type

[**CollectionAnalyticData**](CollectionAnalyticData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted. Server responds with processed document or its status. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **404** | No collections with provided ID found on server. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="retrieveProcessedCollections"></a>
# **retrieveProcessedCollections**
> CollectionAnalyticData retrieveProcessedCollections(contentType, configId)

Retrieve collections analysis

This method retrieves analysis results for processed collections from Semantria. FAILED collections will have FAILED status in response. Semantria responds with limited amount of results per API call. If configuration ID provided, Semantria responds with the collections, which were queued using the same configuration ID, in opposite Primary configuration uses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProcessingCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ProcessingCollectionsApi apiInstance = new ProcessingCollectionsApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration used for analysis.
    try {
      CollectionAnalyticData result = apiInstance.retrieveProcessedCollections(contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProcessingCollectionsApi#retrieveProcessedCollections");
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
| **configId** | **String**| Identifier of configuration used for analysis. | [optional] |

### Return type

[**CollectionAnalyticData**](CollectionAnalyticData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with processed collections. |  -  |
| **202** | Client request accepted, no processed collections found on the server. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

