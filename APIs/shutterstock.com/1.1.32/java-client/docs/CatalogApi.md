# CatalogApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addToCollection**](CatalogApi.md#addToCollection) | **POST** /v2/catalog/collections/{collection_id}/items | Add items to catalog collections |
| [**createCollection**](CatalogApi.md#createCollection) | **POST** /v2/catalog/collections | Create catalog collections |
| [**deleteCollection**](CatalogApi.md#deleteCollection) | **DELETE** /v2/catalog/collections/{collection_id} | Delete catalog collections |
| [**deleteFromCollection**](CatalogApi.md#deleteFromCollection) | **DELETE** /v2/catalog/collections/{collection_id}/items | Remove items from catalog collection |
| [**getCollections**](CatalogApi.md#getCollections) | **GET** /v2/catalog/collections | List catalog collections |
| [**searchCatalog**](CatalogApi.md#searchCatalog) | **GET** /v2/catalog/search | Search catalogs for assets |
| [**updateCollection**](CatalogApi.md#updateCollection) | **PATCH** /v2/catalog/collections/{collection_id} | Update collection metadata |


<a id="addToCollection"></a>
# **addToCollection**
> CatalogCollection addToCollection(collectionId, createCatalogCollectionItems)

Add items to catalog collections

This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user&#39;s account&#39;s catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String collectionId = "126351028"; // String | The ID of the collection to add assets to
    CreateCatalogCollectionItems createCatalogCollectionItems = new CreateCatalogCollectionItems(); // CreateCatalogCollectionItems | Collection item attributes to add to collection
    try {
      CatalogCollection result = apiInstance.addToCollection(collectionId, createCatalogCollectionItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#addToCollection");
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
| **collectionId** | **String**| The ID of the collection to add assets to | |
| **createCatalogCollectionItems** | [**CreateCatalogCollectionItems**](CreateCatalogCollectionItems.md)| Collection item attributes to add to collection | |

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createCollection"></a>
# **createCollection**
> CatalogCollection createCollection(createCatalogCollection)

Create catalog collections

This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later, use &#x60;PATCH /v2/catalog/collections/{collection_id}/items&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    CreateCatalogCollection createCatalogCollection = new CreateCatalogCollection(); // CreateCatalogCollection | Create a catalog collection and, optionally, add items.
    try {
      CatalogCollection result = apiInstance.createCollection(createCatalogCollection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#createCollection");
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
| **createCatalogCollection** | [**CreateCatalogCollection**](CreateCatalogCollection.md)| Create a catalog collection and, optionally, add items. | |

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |

<a id="deleteCollection"></a>
# **deleteCollection**
> deleteCollection(collectionId)

Delete catalog collections

This endpoint deletes a catalog collection. It does not remove the assets from the user&#39;s account&#39;s catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String collectionId = "126351028"; // String | The ID of the collection to delete
    try {
      apiInstance.deleteCollection(collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#deleteCollection");
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
| **collectionId** | **String**| The ID of the collection to delete | |

### Return type

null (empty response body)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **404** | Collection not found |  -  |

<a id="deleteFromCollection"></a>
# **deleteFromCollection**
> CatalogCollection deleteFromCollection(collectionId, removeCatalogCollectionItems)

Remove items from catalog collection

This endpoint removes assets from a catalog collection. It does not remove the assets from the user&#39;s account&#39;s catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String collectionId = "126351028"; // String | The ID of the collection to remove assets from
    RemoveCatalogCollectionItems removeCatalogCollectionItems = new RemoveCatalogCollectionItems(); // RemoveCatalogCollectionItems | Items to remove from the collection
    try {
      CatalogCollection result = apiInstance.deleteFromCollection(collectionId, removeCatalogCollectionItems);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#deleteFromCollection");
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
| **collectionId** | **String**| The ID of the collection to remove assets from | |
| **removeCatalogCollectionItems** | [**RemoveCatalogCollectionItems**](RemoveCatalogCollectionItems.md)| Items to remove from the collection | |

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCollections"></a>
# **getCollections**
> CatalogCollectionDataList getCollections(page, perPage, sort, shared)

List catalog collections

This endpoint returns a list of catalog collections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String sort = "newest"; // String | Sort by
    Boolean shared = false; // Boolean | Set to true to omit collections that you own and return only collections  that are shared with you
    try {
      CatalogCollectionDataList result = apiInstance.getCollections(page, perPage, sort, shared);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#getCollections");
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
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **sort** | **String**| Sort by | [optional] [default to newest] [enum: newest, oldest] |
| **shared** | **Boolean**| Set to true to omit collections that you own and return only collections  that are shared with you | [optional] [default to false] |

### Return type

[**CatalogCollectionDataList**](CatalogCollectionDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid status value |  -  |

<a id="searchCatalog"></a>
# **searchCatalog**
> CatalogCollectionItemDataList searchCatalog(sort, page, perPage, query, collectionId, assetType)

Search catalogs for assets

This endpoint searches for assets in the account&#39;s catalog. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String sort = "newest"; // String | Sort by
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    String query = "dogs on the beach"; // String | One or more search terms separated by spaces
    List<String> collectionId = Arrays.asList(); // List<String> | Filter by collection id
    List<String> assetType = Arrays.asList(); // List<String> | Filter by asset type
    try {
      CatalogCollectionItemDataList result = apiInstance.searchCatalog(sort, page, perPage, query, collectionId, assetType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#searchCatalog");
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
| **sort** | **String**| Sort by | [optional] [default to newest] [enum: newest, oldest] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **query** | **String**| One or more search terms separated by spaces | [optional] |
| **collectionId** | [**List&lt;String&gt;**](String.md)| Filter by collection id | [optional] |
| **assetType** | [**List&lt;String&gt;**](String.md)| Filter by asset type | [optional] [enum: image, video, audio, elements, editorial-image, editorial-video] |

### Return type

[**CatalogCollectionItemDataList**](CatalogCollectionItemDataList.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="updateCollection"></a>
# **updateCollection**
> CatalogCollection updateCollection(collectionId, updateCatalogCollection)

Update collection metadata

This endpoint updates the metadata of a catalog collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
    String collectionId = "126351028"; // String | ID of collection that needs to be modified
    UpdateCatalogCollection updateCatalogCollection = new UpdateCatalogCollection(); // UpdateCatalogCollection | Collections Metadata to update
    try {
      CatalogCollection result = apiInstance.updateCollection(collectionId, updateCatalogCollection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#updateCollection");
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
| **collectionId** | **String**| ID of collection that needs to be modified | |
| **updateCatalogCollection** | [**UpdateCatalogCollection**](UpdateCatalogCollection.md)| Collections Metadata to update | |

### Return type

[**CatalogCollection**](CatalogCollection.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

