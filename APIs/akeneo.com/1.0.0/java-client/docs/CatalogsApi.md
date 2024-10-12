# CatalogsApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAppCatalog**](CatalogsApi.md#deleteAppCatalog) | **DELETE** /api/rest/v1/catalogs/{id} | Delete a catalog |
| [**getAppCatalog**](CatalogsApi.md#getAppCatalog) | **GET** /api/rest/v1/catalogs/{id} | Get a catalog |
| [**getAppCatalogs**](CatalogsApi.md#getAppCatalogs) | **GET** /api/rest/v1/catalogs | Get the list of owned catalogs |
| [**patchAppCatalog**](CatalogsApi.md#patchAppCatalog) | **PATCH** /api/rest/v1/catalogs/{id} | Update a catalog |
| [**postAppCatalog**](CatalogsApi.md#postAppCatalog) | **POST** /api/rest/v1/catalogs | Create a new catalog |


<a id="deleteAppCatalog"></a>
# **deleteAppCatalog**
> deleteAppCatalog(id)

Delete a catalog

This endpoint allows you to delete a catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogsApi apiInstance = new CatalogsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    try {
      apiInstance.deleteAppCatalog(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsApi#deleteAppCatalog");
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
| **204** | Deleted |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Catalog not found |  -  |

<a id="getAppCatalog"></a>
# **getAppCatalog**
> PostAppCatalog201Response getAppCatalog(id)

Get a catalog

This endpoint allows you to get the information about a catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogsApi apiInstance = new CatalogsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    try {
      PostAppCatalog201Response result = apiInstance.getAppCatalog(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsApi#getAppCatalog");
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

### Return type

[**PostAppCatalog201Response**](PostAppCatalog201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the catalog |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Catalog not found |  -  |

<a id="getAppCatalogs"></a>
# **getAppCatalogs**
> Catalogs getAppCatalogs(page, limit)

Get the list of owned catalogs

This endpoint allows you to get the list of catalogs you owned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogsApi apiInstance = new CatalogsApi(defaultClient);
    Integer page = 1; // Integer | Number of the page to retrieve when using the `page` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html#pagination\">Pagination</a> section
    Integer limit = 100; // Integer | Number of results by page, see <a href=\"/documentation/pagination.html\">Pagination</a> section
    try {
      Catalogs result = apiInstance.getAppCatalogs(page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsApi#getAppCatalogs");
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
| **page** | **Integer**| Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 1] |
| **limit** | **Integer**| Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to 100] |

### Return type

[**Catalogs**](Catalogs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the paginated catalogs owned by the user making the request |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |

<a id="patchAppCatalog"></a>
# **patchAppCatalog**
> PostAppCatalog201Response patchAppCatalog(id, body)

Update a catalog

This endpoint allows you to update a catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogsApi apiInstance = new CatalogsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    PostAppCatalogRequest body = new PostAppCatalogRequest(); // PostAppCatalogRequest | 
    try {
      PostAppCatalog201Response result = apiInstance.patchAppCatalog(id, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsApi#patchAppCatalog");
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
| **body** | [**PostAppCatalogRequest**](PostAppCatalogRequest.md)|  | [optional] |

### Return type

[**PostAppCatalog201Response**](PostAppCatalog201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Catalog not found |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

<a id="postAppCatalog"></a>
# **postAppCatalog**
> PostAppCatalog201Response postAppCatalog(body)

Create a new catalog

This endpoint allows you to create a new catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    CatalogsApi apiInstance = new CatalogsApi(defaultClient);
    PostAppCatalogRequest body = new PostAppCatalogRequest(); // PostAppCatalogRequest | 
    try {
      PostAppCatalog201Response result = apiInstance.postAppCatalog(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsApi#postAppCatalog");
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
| **body** | [**PostAppCatalogRequest**](PostAppCatalogRequest.md)|  | [optional] |

### Return type

[**PostAppCatalog201Response**](PostAppCatalog201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

