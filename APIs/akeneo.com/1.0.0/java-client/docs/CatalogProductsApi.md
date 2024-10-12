# CatalogProductsApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAppCatalogMappedProducts**](CatalogProductsApi.md#getAppCatalogMappedProducts) | **GET** /api/rest/v1/catalogs/{id}/mapped-products | Get the list of mapped products related to a catalog |
| [**getAppCatalogProductUuids**](CatalogProductsApi.md#getAppCatalogProductUuids) | **GET** /api/rest/v1/catalogs/{id}/product-uuids | Get the list of product uuids |
| [**getAppCatalogProducts**](CatalogProductsApi.md#getAppCatalogProducts) | **GET** /api/rest/v1/catalogs/{id}/products | Get the list of products related to a catalog |
| [**getAppCatalogProductsUuid**](CatalogProductsApi.md#getAppCatalogProductsUuid) | **GET** /api/rest/v1/catalogs/{id}/products/{uuid} | Get a product related to a catalog |


<a id="getAppCatalogMappedProducts"></a>
# **getAppCatalogMappedProducts**
> Products getAppCatalogMappedProducts(id, searchAfter, limit, updatedBefore, updatedAfter)

Get the list of mapped products related to a catalog

This endpoint allows you to get the list of products related to a catalog when the mapping is enabled. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogProductsApi apiInstance = new CatalogProductsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    String searchAfter = "cursor to the first page"; // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Integer limit = 100; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    LocalDate updatedBefore = LocalDate.now(); // LocalDate | Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
    LocalDate updatedAfter = LocalDate.now(); // LocalDate | Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
    try {
      Products result = apiInstance.getAppCatalogMappedProducts(id, searchAfter, limit, updatedBefore, updatedAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogProductsApi#getAppCatalogMappedProducts");
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
| **id** | **UUID**| Catalog ID | |
| **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100] |
| **updatedBefore** | **LocalDate**| Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints) | [optional] |
| **updatedAfter** | **LocalDate**| Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints) | [optional] |

### Return type

[**Products**](Products.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the paginated **mapped** products |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Catalog not found |  -  |

<a id="getAppCatalogProductUuids"></a>
# **getAppCatalogProductUuids**
> ProductUuids getAppCatalogProductUuids(id, searchAfter, limit, updatedBefore, updatedAfter)

Get the list of product uuids

This endpoint allows you to get the list of uuids of products contained in a catalog. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogProductsApi apiInstance = new CatalogProductsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Id of the catalog
    String searchAfter = "cursor to the first page"; // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Integer limit = 100; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    LocalDate updatedBefore = LocalDate.now(); // LocalDate | Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
    LocalDate updatedAfter = LocalDate.now(); // LocalDate | Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
    try {
      ProductUuids result = apiInstance.getAppCatalogProductUuids(id, searchAfter, limit, updatedBefore, updatedAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogProductsApi#getAppCatalogProductUuids");
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
| **id** | **UUID**| Id of the catalog | |
| **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100] |
| **updatedBefore** | **LocalDate**| Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints) | [optional] |
| **updatedAfter** | **LocalDate**| Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints) | [optional] |

### Return type

[**ProductUuids**](ProductUuids.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the paginated product uuids |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Catalog not found |  -  |

<a id="getAppCatalogProducts"></a>
# **getAppCatalogProducts**
> Products getAppCatalogProducts(id, searchAfter, limit, updatedBefore, updatedAfter)

Get the list of products related to a catalog

This endpoint allows you to get the list of products related to a catalog. Products are paginated and they can be filtered. In the Enterprise Edition, permissions based on your app settings are applied to the set of products you request. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogProductsApi apiInstance = new CatalogProductsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    String searchAfter = "cursor to the first page"; // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    Integer limit = 100; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    LocalDate updatedBefore = LocalDate.now(); // LocalDate | Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints)
    LocalDate updatedAfter = LocalDate.now(); // LocalDate | Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints)
    try {
      Products result = apiInstance.getAppCatalogProducts(id, searchAfter, limit, updatedBefore, updatedAfter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogProductsApi#getAppCatalogProducts");
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
| **id** | **UUID**| Catalog ID | |
| **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to cursor to the first page] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100] |
| **updatedBefore** | **LocalDate**| Filter products that have been updated BEFORE the provided date (Only available on Catalogs endpoints) | [optional] |
| **updatedAfter** | **LocalDate**| Filter products that have been updated AFTER the provided date (Only available on Catalogs endpoints) | [optional] |

### Return type

[**Products**](Products.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the paginated products |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Catalog not found |  -  |

<a id="getAppCatalogProductsUuid"></a>
# **getAppCatalogProductsUuid**
> getAppCatalogProductsUuid(id, uuid)

Get a product related to a catalog

This endpoint allows you to get a specific product related to a catalog. In the Enterprise Edition, permissions based on your app settings are applied on the product you request. Please, note that a disabled catalog can return an HTTP 200 with a payload containing an error message, for more details see the &lt;a href&#x3D;\&quot;apps/catalogs.html#troubleshooting\&quot;&gt;App Catalog&lt;/a&gt; section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogProductsApi apiInstance = new CatalogProductsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    UUID uuid = UUID.randomUUID(); // UUID | Product UUID
    try {
      apiInstance.getAppCatalogProductsUuid(id, uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogProductsApi#getAppCatalogProductsUuid");
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
| **id** | **UUID**| Catalog ID | |
| **uuid** | **UUID**| Product UUID | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the product |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Catalog not found |  -  |

