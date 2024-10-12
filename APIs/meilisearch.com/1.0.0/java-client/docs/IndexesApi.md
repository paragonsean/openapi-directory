# IndexesApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIndexWithPrimaryKey**](IndexesApi.md#createIndexWithPrimaryKey) | **POST** /indexes | Create index with primary key |
| [**deleteAnIndex**](IndexesApi.md#deleteAnIndex) | **DELETE** /indexes/books | Delete an index |
| [**getIndexes**](IndexesApi.md#getIndexes) | **GET** /indexes | Get indexes |
| [**showIndex**](IndexesApi.md#showIndex) | **GET** /indexes/books | Show index |
| [**swapIndexes**](IndexesApi.md#swapIndexes) | **POST** /indexes/swap-indexes | Swap indexes |
| [**updateIndex**](IndexesApi.md#updateIndex) | **PATCH** /indexes/books | Update index |


<a id="createIndexWithPrimaryKey"></a>
# **createIndexWithPrimaryKey**
> createIndexWithPrimaryKey(createIndexWithPrimaryKeyRequest)

Create index with primary key

Create index with primary key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    IndexesApi apiInstance = new IndexesApi(defaultClient);
    CreateIndexWithPrimaryKeyRequest createIndexWithPrimaryKeyRequest = new CreateIndexWithPrimaryKeyRequest(); // CreateIndexWithPrimaryKeyRequest | 
    try {
      apiInstance.createIndexWithPrimaryKey(createIndexWithPrimaryKeyRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexesApi#createIndexWithPrimaryKey");
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
| **createIndexWithPrimaryKeyRequest** | [**CreateIndexWithPrimaryKeyRequest**](CreateIndexWithPrimaryKeyRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteAnIndex"></a>
# **deleteAnIndex**
> deleteAnIndex()

Delete an index

Delete an index

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    IndexesApi apiInstance = new IndexesApi(defaultClient);
    try {
      apiInstance.deleteAnIndex();
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexesApi#deleteAnIndex");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getIndexes"></a>
# **getIndexes**
> getIndexes(offset, limit)

Get indexes

Get indexes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    IndexesApi apiInstance = new IndexesApi(defaultClient);
    String offset = "0"; // String | 
    String limit = "2"; // String | 
    try {
      apiInstance.getIndexes(offset, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexesApi#getIndexes");
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
| **offset** | **String**|  | [optional] |
| **limit** | **String**|  | [optional] |

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
| **200** |  |  -  |

<a id="showIndex"></a>
# **showIndex**
> showIndex()

Show index

Show index

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    IndexesApi apiInstance = new IndexesApi(defaultClient);
    try {
      apiInstance.showIndex();
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexesApi#showIndex");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="swapIndexes"></a>
# **swapIndexes**
> swapIndexes(swapIndexesRequestInner)

Swap indexes

Swap indexes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    IndexesApi apiInstance = new IndexesApi(defaultClient);
    List<SwapIndexesRequestInner> swapIndexesRequestInner = Arrays.asList(); // List<SwapIndexesRequestInner> | 
    try {
      apiInstance.swapIndexes(swapIndexesRequestInner);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexesApi#swapIndexes");
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
| **swapIndexesRequestInner** | [**List&lt;SwapIndexesRequestInner&gt;**](SwapIndexesRequestInner.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateIndex"></a>
# **updateIndex**
> updateIndex(updateIndexRequest)

Update index

Can only change the document identifier if it has not already been added before.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    IndexesApi apiInstance = new IndexesApi(defaultClient);
    UpdateIndexRequest updateIndexRequest = new UpdateIndexRequest(); // UpdateIndexRequest | 
    try {
      apiInstance.updateIndex(updateIndexRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexesApi#updateIndex");
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
| **updateIndexRequest** | [**UpdateIndexRequest**](UpdateIndexRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

