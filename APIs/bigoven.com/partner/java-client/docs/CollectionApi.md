# CollectionApi

All URIs are relative to *https://api2.bigoven.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**collectionCollections**](CollectionApi.md#collectionCollections) | **GET** /collections | Get the list of current, seasonal recipe collections. From here, you can use the /collection/{id} endpoint to retrieve the recipes in those collections. |
| [**collectionGetCollection**](CollectionApi.md#collectionGetCollection) | **GET** /collection/{id} | Gets a recipe collection. A recipe collection is a curated set of recipes. |
| [**collectionGetCollectionMeta**](CollectionApi.md#collectionGetCollectionMeta) | **GET** /collection/{id}/meta | Gets a recipe collection metadata. A recipe collection is a curated set of recipes. |


<a id="collectionCollections"></a>
# **collectionCollections**
> List&lt;BigOvenModelAPI2CollectionInfo&gt; collectionCollections(test)

Get the list of current, seasonal recipe collections. From here, you can use the /collection/{id} endpoint to retrieve the recipes in those collections.

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    String test = "test_example"; // String | 
    try {
      List<BigOvenModelAPI2CollectionInfo> result = apiInstance.collectionCollections(test);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#collectionCollections");
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
| **test** | **String**|  | [optional] |

### Return type

[**List&lt;BigOvenModelAPI2CollectionInfo&gt;**](BigOvenModelAPI2CollectionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionGetCollection"></a>
# **collectionGetCollection**
> BigOvenModelAPI2RecipeSearchResult collectionGetCollection(id, rpp, pg, test, sessionForLogging)

Gets a recipe collection. A recipe collection is a curated set of recipes.

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    Integer id = 56; // Integer | the collection identifier
    Integer rpp = 56; // Integer | results per page
    Integer pg = 56; // Integer | page number (starting with 1)
    Boolean test = true; // Boolean | 
    String sessionForLogging = "sessionForLogging_example"; // String | 
    try {
      BigOvenModelAPI2RecipeSearchResult result = apiInstance.collectionGetCollection(id, rpp, pg, test, sessionForLogging);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#collectionGetCollection");
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
| **id** | **Integer**| the collection identifier | |
| **rpp** | **Integer**| results per page | [optional] |
| **pg** | **Integer**| page number (starting with 1) | [optional] |
| **test** | **Boolean**|  | [optional] |
| **sessionForLogging** | **String**|  | [optional] |

### Return type

[**BigOvenModelAPI2RecipeSearchResult**](BigOvenModelAPI2RecipeSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="collectionGetCollectionMeta"></a>
# **collectionGetCollectionMeta**
> BigOvenModelAPI2CollectionInfo collectionGetCollectionMeta(id)

Gets a recipe collection metadata. A recipe collection is a curated set of recipes.

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
    defaultClient.setBasePath("https://api2.bigoven.com");

    CollectionApi apiInstance = new CollectionApi(defaultClient);
    Integer id = 56; // Integer | the collection identifier
    try {
      BigOvenModelAPI2CollectionInfo result = apiInstance.collectionGetCollectionMeta(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionApi#collectionGetCollectionMeta");
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
| **id** | **Integer**| the collection identifier | |

### Return type

[**BigOvenModelAPI2CollectionInfo**](BigOvenModelAPI2CollectionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

