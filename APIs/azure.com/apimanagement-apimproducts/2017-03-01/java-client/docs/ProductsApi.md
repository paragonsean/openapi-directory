# ProductsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productCreateOrUpdate**](ProductsApi.md#productCreateOrUpdate) | **PUT** /products/{productId} |  |
| [**productDelete**](ProductsApi.md#productDelete) | **DELETE** /products/{productId} |  |
| [**productGet**](ProductsApi.md#productGet) | **GET** /products/{productId} |  |
| [**productList**](ProductsApi.md#productList) | **GET** /products |  |
| [**productUpdate**](ProductsApi.md#productUpdate) | **PATCH** /products/{productId} |  |


<a id="productCreateOrUpdate"></a>
# **productCreateOrUpdate**
> ProductContract productCreateOrUpdate(productId, apiVersion, parameters)



Creates or Updates a product.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    ProductContract parameters = new ProductContract(); // ProductContract | Create or update parameters.
    try {
      ProductContract result = apiInstance.productCreateOrUpdate(productId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productCreateOrUpdate");
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
| **parameters** | [**ProductContract**](ProductContract.md)| Create or update parameters. | |

### Return type

[**ProductContract**](ProductContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product was successfully updated. |  -  |
| **201** | Product was successfully created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productDelete"></a>
# **productDelete**
> productDelete(productId, ifMatch, apiVersion, deleteSubscriptions)



Delete product.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    Boolean deleteSubscriptions = true; // Boolean | Delete existing subscriptions to the product or not.
    try {
      apiInstance.productDelete(productId, ifMatch, apiVersion, deleteSubscriptions);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productDelete");
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
| **ifMatch** | **String**| ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **deleteSubscriptions** | **Boolean**| Delete existing subscriptions to the product or not. | [optional] |

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
| **204** | The product was successfully deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productGet"></a>
# **productGet**
> ProductContract productGet(productId, apiVersion)



Gets the details of the product specified by its identifier.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      ProductContract result = apiInstance.productGet(productId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productGet");
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

### Return type

[**ProductContract**](ProductContract.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body contains the specified Product entity. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productList"></a>
# **productList**
> ProductCollection productList(apiVersion, $filter, $top, $skip, expandGroups)



Lists a collection of products in the specified service instance.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | terms       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state       | eq                     |                                             |
    Integer $top = 56; // Integer | Number of records to return.
    Integer $skip = 56; // Integer | Number of records to skip.
    Boolean expandGroups = true; // Boolean | When set to true, the response contains an array of groups that have visibility to the product. The default is false.
    try {
      ProductCollection result = apiInstance.productList(apiVersion, $filter, $top, $skip, expandGroups);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **$filter** | **String**| | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | terms       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state       | eq                     |                                             | | [optional] |
| **$top** | **Integer**| Number of records to return. | [optional] |
| **$skip** | **Integer**| Number of records to skip. | [optional] |
| **expandGroups** | **Boolean**| When set to true, the response contains an array of groups that have visibility to the product. The default is false. | [optional] |

### Return type

[**ProductCollection**](ProductCollection.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Collection of the Product entities for the specified API Management service instance. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productUpdate"></a>
# **productUpdate**
> productUpdate(productId, ifMatch, apiVersion, parameters)



Update product.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    ProductUpdateParameters parameters = new ProductUpdateParameters(); // ProductUpdateParameters | Update parameters.
    try {
      apiInstance.productUpdate(productId, ifMatch, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productUpdate");
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
| **ifMatch** | **String**| ETag of the Product Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**ProductUpdateParameters**](ProductUpdateParameters.md)| Update parameters. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content in case of Update Successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

