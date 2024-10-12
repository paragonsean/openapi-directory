# ProductsApi

All URIs are relative to *https://api.configcat.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProduct**](ProductsApi.md#createProduct) | **POST** /v1/organizations/{organizationId}/products | Create Product |
| [**deleteProduct**](ProductsApi.md#deleteProduct) | **DELETE** /v1/products/{productId} | Delete Product |
| [**getProduct**](ProductsApi.md#getProduct) | **GET** /v1/products/{productId} | Get Product |
| [**getProducts**](ProductsApi.md#getProducts) | **GET** /v1/products | List Products |
| [**updateProduct**](ProductsApi.md#updateProduct) | **PUT** /v1/products/{productId} | Update Product |


<a id="createProduct"></a>
# **createProduct**
> ProductModelHaljson createProduct(organizationId, createProductRequest)

Create Product

This endpoint creates a new Product in a specified Organization  identified by the &#x60;organizationId&#x60; parameter, which can be obtained from the [List Organizations](#operation/get-organizations) endpoint.

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
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationId = UUID.randomUUID(); // UUID | The identifier of the Organization.
    CreateProductRequest createProductRequest = new CreateProductRequest(); // CreateProductRequest | 
    try {
      ProductModelHaljson result = apiInstance.createProduct(organizationId, createProductRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#createProduct");
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
| **organizationId** | **UUID**| The identifier of the Organization. | |
| **createProductRequest** | [**CreateProductRequest**](CreateProductRequest.md)|  | |

### Return type

[**ProductModelHaljson**](ProductModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | When the creation was successful. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="deleteProduct"></a>
# **deleteProduct**
> deleteProduct(productId)

Delete Product

This endpoint removes a Product identified by the &#x60;productId&#x60; parameter.

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
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | The identifier of the Product.
    try {
      apiInstance.deleteProduct(productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#deleteProduct");
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
| **productId** | **UUID**| The identifier of the Product. | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | When the delete was successful. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="getProduct"></a>
# **getProduct**
> ProductModelHaljson getProduct(productId)

Get Product

This endpoint returns the metadata of a Product  identified by the &#x60;productId&#x60;.

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
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | The identifier of the Product.
    try {
      ProductModelHaljson result = apiInstance.getProduct(productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProduct");
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
| **productId** | **UUID**| The identifier of the Product. | |

### Return type

[**ProductModelHaljson**](ProductModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | When everything is ok, the product data returned. |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="getProducts"></a>
# **getProducts**
> List&lt;ProductModelHaljson&gt; getProducts()

List Products

This endpoint returns the list of the Products that belongs to the user.

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
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    try {
      List<ProductModelHaljson> result = apiInstance.getProducts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getProducts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;ProductModelHaljson&gt;**](ProductModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

<a id="updateProduct"></a>
# **updateProduct**
> ProductModelHaljson updateProduct(productId, updateProductRequest)

Update Product

This endpoint updates a Product identified by the &#x60;productId&#x60; parameter.

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
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID productId = UUID.randomUUID(); // UUID | The identifier of the Product.
    UpdateProductRequest updateProductRequest = new UpdateProductRequest(); // UpdateProductRequest | 
    try {
      ProductModelHaljson result = apiInstance.updateProduct(productId, updateProductRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#updateProduct");
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
| **productId** | **UUID**| The identifier of the Product. | |
| **updateProductRequest** | [**UpdateProductRequest**](UpdateProductRequest.md)|  | |

### Return type

[**ProductModelHaljson**](ProductModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, text/json
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request. |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **404** | Not found. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

