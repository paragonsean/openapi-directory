# CollectionBetaApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETAllCollections**](CollectionBetaApi.md#gETAllCollections) | **GET** /api/catalog_system/pvt/collection/search | Get All Collections |
| [**gETAllInactiveCollections**](CollectionBetaApi.md#gETAllInactiveCollections) | **GET** /api/catalog/pvt/collection/inactive | Get All Inactive Collections |
| [**gETCollectionsbyseachterms**](CollectionBetaApi.md#gETCollectionsbyseachterms) | **GET** /api/catalog_system/pvt/collection/search/{searchTerms} | Get Collections by search terms |
| [**gETImportfileexample**](CollectionBetaApi.md#gETImportfileexample) | **GET** /api/catalog/pvt/collection/stockkeepingunit/importfileexample | Import Collection file example |
| [**gETProductsfromacollection**](CollectionBetaApi.md#gETProductsfromacollection) | **GET** /api/catalog/pvt/collection/{collectionId}/products | Get products from a collection |
| [**pOSTAddproductsbyimportfile**](CollectionBetaApi.md#pOSTAddproductsbyimportfile) | **POST** /api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importinsert | Add products to Collection by imported file |
| [**pOSTCreateCollection**](CollectionBetaApi.md#pOSTCreateCollection) | **POST** /api/catalog/pvt/collection/ | Create Collection |
| [**pOSTRemoveproductsbyimportfile**](CollectionBetaApi.md#pOSTRemoveproductsbyimportfile) | **POST** /api/catalog/pvt/collection/{collectionId}/stockkeepingunit/importexclude | Remove products from Collection by imported file |


<a id="gETAllCollections"></a>
# **gETAllCollections**
> gETAllCollections(contentType, accept, page, pageSize, orderByAsc)

Get All Collections

Retrieves a list of all collections matching a filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionBetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CollectionBetaApi apiInstance = new CollectionBetaApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer page = 2; // Integer | Page number.
    Integer pageSize = 15; // Integer | Number of the items of the page.
    Boolean orderByAsc = true; // Boolean | Defines if the items of the page are in ascending order.
    try {
      apiInstance.gETAllCollections(contentType, accept, page, pageSize, orderByAsc);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionBetaApi#gETAllCollections");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **page** | **Integer**| Page number. | |
| **pageSize** | **Integer**| Number of the items of the page. | |
| **orderByAsc** | **Boolean**| Defines if the items of the page are in ascending order. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="gETAllInactiveCollections"></a>
# **gETAllInactiveCollections**
> gETAllInactiveCollections(contentType, accept)

Get All Inactive Collections

Retrieves a list of Collection IDs of the inactive Collections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionBetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CollectionBetaApi apiInstance = new CollectionBetaApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.gETAllInactiveCollections(contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionBetaApi#gETAllInactiveCollections");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="gETCollectionsbyseachterms"></a>
# **gETCollectionsbyseachterms**
> gETCollectionsbyseachterms(contentType, accept, searchTerms, page, pageSize, orderByAsc)

Get Collections by search terms

Retrieves a list of collections matching a filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionBetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CollectionBetaApi apiInstance = new CollectionBetaApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String searchTerms = "costume"; // String | String that will search for a collection related to it.
    Integer page = 2; // Integer | Page number.
    Integer pageSize = 15; // Integer | Number of the items of the page.
    Boolean orderByAsc = true; // Boolean | Defines if the items of the page are in ascending order.
    try {
      apiInstance.gETCollectionsbyseachterms(contentType, accept, searchTerms, page, pageSize, orderByAsc);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionBetaApi#gETCollectionsbyseachterms");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **searchTerms** | **String**| String that will search for a collection related to it. | |
| **page** | **Integer**| Page number. | [optional] |
| **pageSize** | **Integer**| Number of the items of the page. | [optional] |
| **orderByAsc** | **Boolean**| Defines if the items of the page are in ascending order. | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="gETImportfileexample"></a>
# **gETImportfileexample**
> gETImportfileexample(contentType, accept)

Import Collection file example

Imports a sample of the imported XLS file. You need to save the response file to your device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionBetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CollectionBetaApi apiInstance = new CollectionBetaApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.gETImportfileexample(contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionBetaApi#gETImportfileexample");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="gETProductsfromacollection"></a>
# **gETProductsfromacollection**
> gETProductsfromacollection(contentType, accept, collectionId, page, pageSize, filter, active, visible, categoryId, brandId, supplierId, salesChannelId, releaseFrom, releaseTo, specificationProduct, specificationFieldId)

Get products from a collection

Retrieves information about the products from a collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionBetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CollectionBetaApi apiInstance = new CollectionBetaApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer collectionId = 1; // Integer | Collection's unique identifier.
    Integer page = 2; // Integer | Page number.
    Integer pageSize = 15; // Integer | Number of the items of the page.
    String filter = "Pre launch"; // String | Filter used to refine the Collection's products.
    Boolean active = true; // Boolean | Defines if the status of the product is active or not.
    Boolean visible = true; // Boolean | Defines if the product is visible on the store or not.
    Integer categoryId = 12; // Integer | Product's Category unique identifier.
    Integer brandId = 3; // Integer | Product's Brand unique identifier.
    Integer supplierId = 1; // Integer | Product's Supplier unique identifier.
    Integer salesChannelId = 1; // Integer | Product's Trade Policy unique identifier.
    String releaseFrom = "2069-11-26T15:23:00"; // String | Product past release date.
    String releaseTo = "2069-11-26T15:23:00"; // String | Product future release date.
    String specificationProduct = "M"; // String | Product Specification Field Value. You must also fill in `SpecificationFieldId` to use this parameter.
    Integer specificationFieldId = 40; // Integer | Product Specification Field unique identifier.
    try {
      apiInstance.gETProductsfromacollection(contentType, accept, collectionId, page, pageSize, filter, active, visible, categoryId, brandId, supplierId, salesChannelId, releaseFrom, releaseTo, specificationProduct, specificationFieldId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionBetaApi#gETProductsfromacollection");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **collectionId** | **Integer**| Collection&#39;s unique identifier. | |
| **page** | **Integer**| Page number. | [optional] |
| **pageSize** | **Integer**| Number of the items of the page. | [optional] |
| **filter** | **String**| Filter used to refine the Collection&#39;s products. | [optional] |
| **active** | **Boolean**| Defines if the status of the product is active or not. | [optional] |
| **visible** | **Boolean**| Defines if the product is visible on the store or not. | [optional] |
| **categoryId** | **Integer**| Product&#39;s Category unique identifier. | [optional] |
| **brandId** | **Integer**| Product&#39;s Brand unique identifier. | [optional] |
| **supplierId** | **Integer**| Product&#39;s Supplier unique identifier. | [optional] |
| **salesChannelId** | **Integer**| Product&#39;s Trade Policy unique identifier. | [optional] |
| **releaseFrom** | **String**| Product past release date. | [optional] |
| **releaseTo** | **String**| Product future release date. | [optional] |
| **specificationProduct** | **String**| Product Specification Field Value. You must also fill in &#x60;SpecificationFieldId&#x60; to use this parameter. | [optional] |
| **specificationFieldId** | **Integer**| Product Specification Field unique identifier. | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="pOSTAddproductsbyimportfile"></a>
# **pOSTAddproductsbyimportfile**
> pOSTAddproductsbyimportfile(contentType, accept, collectionId, _file)

Add products to Collection by imported file

Adds products to a collection from the request body file. The file must be an imported template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionBetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CollectionBetaApi apiInstance = new CollectionBetaApi(defaultClient);
    String contentType = "multipart/form-data"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer collectionId = 1; // Integer | Collection's unique identifier.
    Object _file = null; // Object | XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint.
    try {
      apiInstance.pOSTAddproductsbyimportfile(contentType, accept, collectionId, _file);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionBetaApi#pOSTAddproductsbyimportfile");
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
| **contentType** | **String**| Type of the content being sent. | [default to multipart/form-data] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **collectionId** | **Integer**| Collection&#39;s unique identifier. | |
| **_file** | [**Object**](Object.md)| XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint. | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="pOSTCreateCollection"></a>
# **pOSTCreateCollection**
> pOSTCreateCollection(contentType, accept, requestBody)

Create Collection

Creates a new collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionBetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CollectionBetaApi apiInstance = new CollectionBetaApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    RequestBody requestBody = new RequestBody(); // RequestBody | 
    try {
      apiInstance.pOSTCreateCollection(contentType, accept, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionBetaApi#pOSTCreateCollection");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **requestBody** | [**RequestBody**](RequestBody.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="pOSTRemoveproductsbyimportfile"></a>
# **pOSTRemoveproductsbyimportfile**
> pOSTRemoveproductsbyimportfile(contentType, accept, collectionId, _file)

Remove products from Collection by imported file

Removes products from a collection from the request body file. The file must be an imported template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollectionBetaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CollectionBetaApi apiInstance = new CollectionBetaApi(defaultClient);
    String contentType = "multipart/form-data"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer collectionId = 1; // Integer | Collection's unique identifier.
    Object _file = null; // Object | XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint.
    try {
      apiInstance.pOSTRemoveproductsbyimportfile(contentType, accept, collectionId, _file);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollectionBetaApi#pOSTRemoveproductsbyimportfile");
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
| **contentType** | **String**| Type of the content being sent. | [default to multipart/form-data] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **collectionId** | **Integer**| Collection&#39;s unique identifier. | |
| **_file** | [**Object**](Object.md)| XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint. | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

