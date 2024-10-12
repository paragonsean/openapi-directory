# ProductApisApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productApiCreateOrUpdate**](ProductApisApi.md#productApiCreateOrUpdate) | **PUT** /products/{productId}/apis/{apiId} |  |
| [**productApiDelete**](ProductApisApi.md#productApiDelete) | **DELETE** /products/{productId}/apis/{apiId} |  |
| [**productApiListByProduct**](ProductApisApi.md#productApiListByProduct) | **GET** /products/{productId}/apis |  |


<a id="productApiCreateOrUpdate"></a>
# **productApiCreateOrUpdate**
> ProductApiCreateOrUpdate200Response productApiCreateOrUpdate(productId, apiId, apiVersion)



Adds an API to the specified product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductApisApi apiInstance = new ProductApisApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      ProductApiCreateOrUpdate200Response result = apiInstance.productApiCreateOrUpdate(productId, apiId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApisApi#productApiCreateOrUpdate");
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
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**ProductApiCreateOrUpdate200Response**](ProductApiCreateOrUpdate200Response.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified API is already added to the product. |  -  |
| **201** | The API was successfully added to the product. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productApiDelete"></a>
# **productApiDelete**
> productApiDelete(productId, apiId, apiVersion)



Deletes the specified API from the specified product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductApisApi apiInstance = new ProductApisApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String apiId = "apiId_example"; // String | API identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.productApiDelete(productId, apiId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApisApi#productApiDelete");
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
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |
| **apiId** | **String**| API identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The API was successfully removed from the product. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productApiListByProduct"></a>
# **productApiListByProduct**
> ProductApiListByProduct200Response productApiListByProduct(productId, apiVersion, $filter, $top, $skip)



Lists a collection of the APIs associated with a product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductApisApi apiInstance = new ProductApisApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | serviceUrl  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | path        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | 
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    try {
      ProductApiListByProduct200Response result = apiInstance.productApiListByProduct(productId, apiVersion, $filter, $top, $skip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductApisApi#productApiListByProduct");
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
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | serviceUrl  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | path        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |  | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |

### Return type

[**ProductApiListByProduct200Response**](ProductApiListByProduct200Response.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains a collection of Api entities in the product. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

