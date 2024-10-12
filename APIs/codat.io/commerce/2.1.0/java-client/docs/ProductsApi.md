# ProductsApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listProductCategories**](ProductsApi.md#listProductCategories) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-productCategories | List product categories |
| [**listProducts**](ProductsApi.md#listProducts) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-products | List products |


<a id="listProductCategories"></a>
# **listProductCategories**
> ProductCategories listProductCategories(page, pageSize, query, orderBy)

List product categories

Product categories are used to classify a group of products together, either by type (eg \&quot;Furniture\&quot;), or sometimes by tax profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Integer page = 1; // Integer | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    Integer pageSize = 100; // Integer | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    String query = "query_example"; // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    String orderBy = "-modifiedDate"; // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    try {
      ProductCategories result = apiInstance.listProductCategories(page, pageSize, query, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#listProductCategories");
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
| **page** | **Integer**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1] |
| **pageSize** | **Integer**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100] |
| **query** | **String**| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] |
| **orderBy** | **String**| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] |

### Return type

[**ProductCategories**](ProductCategories.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listProducts"></a>
# **listProducts**
> Products listProducts(page, pageSize, query, orderBy)

List products

The Products data type provides the company&#39;s product inventory, and includes the price and quantity of all products, and product variants, available for sale.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    Integer page = 1; // Integer | Page number. [Read more](https://docs.codat.io/using-the-api/paging).
    Integer pageSize = 100; // Integer | Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging).
    String query = "query_example"; // String | Codat query string. [Read more](https://docs.codat.io/using-the-api/querying).
    String orderBy = "-modifiedDate"; // String | Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results).
    try {
      Products result = apiInstance.listProducts(page, pageSize, query, orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#listProducts");
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
| **page** | **Integer**| Page number. [Read more](https://docs.codat.io/using-the-api/paging). | [default to 1] |
| **pageSize** | **Integer**| Number of records to return in a page. [Read more](https://docs.codat.io/using-the-api/paging). | [optional] [default to 100] |
| **query** | **String**| Codat query string. [Read more](https://docs.codat.io/using-the-api/querying). | [optional] |
| **orderBy** | **String**| Field to order results by. [Read more](https://docs.codat.io/using-the-api/ordering-results). | [optional] |

### Return type

[**Products**](Products.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

