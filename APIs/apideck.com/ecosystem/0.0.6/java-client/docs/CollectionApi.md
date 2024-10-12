# CollectionApi

All URIs are relative to *https://api.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**collectionListingsAll**](CollectionApi.md#collectionListingsAll) | **GET** /ecosystems/{ecosystem_id}/collections/{id}/listings | List collection listings |
| [**collectionsAll**](CollectionApi.md#collectionsAll) | **GET** /ecosystems/{ecosystem_id}/collections | List collections |
| [**collectionsOne**](CollectionApi.md#collectionsOne) | **GET** /ecosystems/{ecosystem_id}/collections/{id} | Get collection |


<a id="collectionListingsAll"></a>
# **collectionListingsAll**
> GetListingsResponse collectionListingsAll(ecosystemId, id, cursor, limit)

List collection listings

List collection listings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String id = "id_example"; // String | ID of the record you are acting upon.
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 50; // Integer | Number of records to return
    try {
      GetListingsResponse result = apiInstance.collectionListingsAll(ecosystemId, id, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#collectionListingsAll");
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
| **ecosystemId** | **String**|  | |
| **id** | **String**| ID of the record you are acting upon. | |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of records to return | [optional] [default to 50] |

### Return type

[**GetListingsResponse**](GetListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listings |  -  |

<a id="collectionsAll"></a>
# **collectionsAll**
> GetCollectionsResponse collectionsAll(ecosystemId, cursor, limit)

List collections

List collections

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 50; // Integer | Number of records to return
    try {
      GetCollectionsResponse result = apiInstance.collectionsAll(ecosystemId, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#collectionsAll");
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
| **ecosystemId** | **String**|  | |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of records to return | [optional] [default to 50] |

### Return type

[**GetCollectionsResponse**](GetCollectionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collections |  -  |

<a id="collectionsOne"></a>
# **collectionsOne**
> GetCollectionResponse collectionsOne(ecosystemId, id)

Get collection

Get collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String id = "id_example"; // String | ID of the record you are acting upon.
    try {
      GetCollectionResponse result = apiInstance.collectionsOne(ecosystemId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#collectionsOne");
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
| **ecosystemId** | **String**|  | |
| **id** | **String**| ID of the record you are acting upon. | |

### Return type

[**GetCollectionResponse**](GetCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collection |  -  |

