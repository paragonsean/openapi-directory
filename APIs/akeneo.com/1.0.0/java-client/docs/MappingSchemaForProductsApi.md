# MappingSchemaForProductsApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAppCatalogsMappingSchemaProduct**](MappingSchemaForProductsApi.md#deleteAppCatalogsMappingSchemaProduct) | **DELETE** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Delete the product mapping schema related to a catalog |
| [**getAppCatalogsMappingSchemaProduct**](MappingSchemaForProductsApi.md#getAppCatalogsMappingSchemaProduct) | **GET** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Get the product mapping schema related to a catalog |
| [**putAppCatalogsMappingSchemaProduct**](MappingSchemaForProductsApi.md#putAppCatalogsMappingSchemaProduct) | **PUT** /api/rest/v1/catalogs/{id}/mapping-schemas/product | Create or update the product mapping schema related to a catalog |


<a id="deleteAppCatalogsMappingSchemaProduct"></a>
# **deleteAppCatalogsMappingSchemaProduct**
> deleteAppCatalogsMappingSchemaProduct(id)

Delete the product mapping schema related to a catalog

This endpoint allows you to delete the product mapping schema related to a catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingSchemaForProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    MappingSchemaForProductsApi apiInstance = new MappingSchemaForProductsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    try {
      apiInstance.deleteAppCatalogsMappingSchemaProduct(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingSchemaForProductsApi#deleteAppCatalogsMappingSchemaProduct");
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

<a id="getAppCatalogsMappingSchemaProduct"></a>
# **getAppCatalogsMappingSchemaProduct**
> GetAppCatalogsMappingSchemaProduct200Response getAppCatalogsMappingSchemaProduct(id)

Get the product mapping schema related to a catalog

This endpoint allows you to retrieve the product mapping schema related to a catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingSchemaForProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    MappingSchemaForProductsApi apiInstance = new MappingSchemaForProductsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    try {
      GetAppCatalogsMappingSchemaProduct200Response result = apiInstance.getAppCatalogsMappingSchemaProduct(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingSchemaForProductsApi#getAppCatalogsMappingSchemaProduct");
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

[**GetAppCatalogsMappingSchemaProduct200Response**](GetAppCatalogsMappingSchemaProduct200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return product mapping schema related to a catalog |  -  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **404** | Catalog not found |  -  |

<a id="putAppCatalogsMappingSchemaProduct"></a>
# **putAppCatalogsMappingSchemaProduct**
> putAppCatalogsMappingSchemaProduct(id, body)

Create or update the product mapping schema related to a catalog

This endpoint allows you to create or update the product mapping schema related to a catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MappingSchemaForProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    MappingSchemaForProductsApi apiInstance = new MappingSchemaForProductsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | Catalog ID
    GetAppCatalogsMappingSchemaProduct200Response body = new GetAppCatalogsMappingSchemaProduct200Response(); // GetAppCatalogsMappingSchemaProduct200Response | 
    try {
      apiInstance.putAppCatalogsMappingSchemaProduct(id, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MappingSchemaForProductsApi#putAppCatalogsMappingSchemaProduct");
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
| **body** | [**GetAppCatalogsMappingSchemaProduct200Response**](GetAppCatalogsMappingSchemaProduct200Response.md)|  | [optional] |

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
| **201** | Created |  * Location - URI of the created resource <br>  |
| **401** | Authentication required |  -  |
| **403** | Access forbidden |  -  |
| **415** | Unsupported Media type |  -  |
| **422** | Unprocessable entity |  -  |

