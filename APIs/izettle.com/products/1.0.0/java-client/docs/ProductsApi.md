# ProductsApi

All URIs are relative to *https://products.izettle.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countAllProducts**](ProductsApi.md#countAllProducts) | **GET** /organizations/{organizationUuid}/products/v2/count | Retrieve the count of existing products |
| [**createProduct**](ProductsApi.md#createProduct) | **POST** /organizations/{organizationUuid}/products | Create a new product |
| [**deleteProduct**](ProductsApi.md#deleteProduct) | **DELETE** /organizations/{organizationUuid}/products/{productUuid} | Delete a single product |
| [**deleteProducts**](ProductsApi.md#deleteProducts) | **DELETE** /organizations/{organizationUuid}/products | Delete a list of products |
| [**getAllOptions**](ProductsApi.md#getAllOptions) | **GET** /organizations/{organizationUuid}/products/options | Retrieve an aggregate of active Options in the library |
| [**getAllProductsInPos**](ProductsApi.md#getAllProductsInPos) | **GET** /organizations/{organizationUuid}/products | Retrieve all products visible in POS |
| [**getAllProductsV2**](ProductsApi.md#getAllProductsV2) | **GET** /organizations/{organizationUuid}/products/v2 | Retrieve all products visible in POS – v2 |
| [**getProduct**](ProductsApi.md#getProduct) | **GET** /organizations/{organizationUuid}/products/{productUuid} | Retrieve a single product |
| [**updateProduct**](ProductsApi.md#updateProduct) | **PUT** /organizations/{organizationUuid}/products/v2/{productUuid} | Update a single product |


<a id="countAllProducts"></a>
# **countAllProducts**
> List&lt;ProductCountResponse&gt; countAllProducts(organizationUuid)

Retrieve the count of existing products

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    try {
      List<ProductCountResponse> result = apiInstance.countAllProducts(organizationUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#countAllProducts");
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
| **organizationUuid** | **UUID**|  | |

### Return type

[**List&lt;ProductCountResponse&gt;**](ProductCountResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Count of existing products |  -  |

<a id="createProduct"></a>
# **createProduct**
> ProductResponse createProduct(organizationUuid, productCreateRequest, returnEntity)

Create a new product

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    ProductCreateRequest productCreateRequest = new ProductCreateRequest(); // ProductCreateRequest | 
    Boolean returnEntity = false; // Boolean | 
    try {
      ProductResponse result = apiInstance.createProduct(organizationUuid, productCreateRequest, returnEntity);
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
| **organizationUuid** | **UUID**|  | |
| **productCreateRequest** | [**ProductCreateRequest**](ProductCreateRequest.md)|  | |
| **returnEntity** | **Boolean**|  | [optional] [default to false] |

### Return type

[**ProductResponse**](ProductResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Product created. It will include the Product in the response only if &#39;returnEntity&#39; is true |  * ETag - ETag value <br>  * Location - Location of updated product <br>  |

<a id="deleteProduct"></a>
# **deleteProduct**
> deleteProduct(organizationUuid, productUuid)

Delete a single product

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID productUuid = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.deleteProduct(organizationUuid, productUuid);
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
| **organizationUuid** | **UUID**|  | |
| **productUuid** | **UUID**|  | |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Product deleted |  -  |
| **404** | Organization or Product not found |  -  |

<a id="deleteProducts"></a>
# **deleteProducts**
> deleteProducts(organizationUuid, uuid)

Delete a list of products

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    List<UUID> uuid = Arrays.asList(); // List<UUID> | List of product UUIDs to be deleted
    try {
      apiInstance.deleteProducts(organizationUuid, uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#deleteProducts");
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
| **organizationUuid** | **UUID**|  | |
| **uuid** | [**List&lt;UUID&gt;**](UUID.md)| List of product UUIDs to be deleted | |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Products deleted |  -  |

<a id="getAllOptions"></a>
# **getAllOptions**
> List&lt;VariantOptionsResponse&gt; getAllOptions(organizationUuid)

Retrieve an aggregate of active Options in the library

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    try {
      List<VariantOptionsResponse> result = apiInstance.getAllOptions(organizationUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getAllOptions");
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
| **organizationUuid** | **UUID**|  | |

### Return type

[**List&lt;VariantOptionsResponse&gt;**](VariantOptionsResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Options |  -  |

<a id="getAllProductsInPos"></a>
# **getAllProductsInPos**
> List&lt;ProductResponse&gt; getAllProductsInPos(organizationUuid)

Retrieve all products visible in POS

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    try {
      List<ProductResponse> result = apiInstance.getAllProductsInPos(organizationUuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getAllProductsInPos");
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
| **organizationUuid** | **UUID**|  | |

### Return type

[**List&lt;ProductResponse&gt;**](ProductResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of products |  -  |

<a id="getAllProductsV2"></a>
# **getAllProductsV2**
> List&lt;ProductResponse&gt; getAllProductsV2(organizationUuid, sort)

Retrieve all products visible in POS – v2

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    Boolean sort = true; // Boolean | If true, sorts response by created date
    try {
      List<ProductResponse> result = apiInstance.getAllProductsV2(organizationUuid, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#getAllProductsV2");
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
| **organizationUuid** | **UUID**|  | |
| **sort** | **Boolean**| If true, sorts response by created date | [optional] |

### Return type

[**List&lt;ProductResponse&gt;**](ProductResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of products |  -  |

<a id="getProduct"></a>
# **getProduct**
> ProductResponse getProduct(organizationUuid, productUuid, ifNoneMatch)

Retrieve a single product

Get the full product with the provided UUID. The method supports conditional GET through providing a HttpHeaders.IF_NONE_MATCH header. If the conditional prerequisite is fullfilled, the full product is returned, otherwise a 304 not modified will be returned with an empty body.

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID productUuid = UUID.randomUUID(); // UUID | 
    String ifNoneMatch = "ifNoneMatch_example"; // String | 
    try {
      ProductResponse result = apiInstance.getProduct(organizationUuid, productUuid, ifNoneMatch);
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
| **organizationUuid** | **UUID**|  | |
| **productUuid** | **UUID**|  | |
| **ifNoneMatch** | **String**|  | [optional] |

### Return type

[**ProductResponse**](ProductResponse.md)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product |  * ETag - ETag value <br>  |
| **304** | Not modified |  -  |
| **400** | Malformed ETag |  -  |
| **404** | Organization or Product not found |  -  |

<a id="updateProduct"></a>
# **updateProduct**
> updateProduct(organizationUuid, productUuid, fullProductUpdateRequest, ifMatch)

Update a single product

Updates a product entity using JSON merge patch (https://tools.ietf.org/html/rfc7386). This means that only included fields will be changed: null values removes the field on the target entity, and other values updates the field. Conditional updates are supported through the HttpHeaders.IF_MATCH header. If the conditional prerequisite is fullfilled, the product is updated: otherwise a 412 (precondition failed) will be returned with an empty body.

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
    defaultClient.setBasePath("https://products.izettle.com");
    
    // Configure OAuth2 access token for authorization: ZettleOauth
    OAuth ZettleOauth = (OAuth) defaultClient.getAuthentication("ZettleOauth");
    ZettleOauth.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    UUID organizationUuid = UUID.randomUUID(); // UUID | 
    UUID productUuid = UUID.randomUUID(); // UUID | 
    FullProductUpdateRequest fullProductUpdateRequest = new FullProductUpdateRequest(); // FullProductUpdateRequest | 
    String ifMatch = "ifMatch_example"; // String | 
    try {
      apiInstance.updateProduct(organizationUuid, productUuid, fullProductUpdateRequest, ifMatch);
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
| **organizationUuid** | **UUID**|  | |
| **productUuid** | **UUID**|  | |
| **fullProductUpdateRequest** | [**FullProductUpdateRequest**](FullProductUpdateRequest.md)|  | |
| **ifMatch** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[ZettleOauth](../README.md#ZettleOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Product updated |  * ETag - ETag value <br>  * Location - Location of updated product <br>  |
| **400** | Invalid request body |  -  |
| **412** | Precondition failed: ETag did not match the expected value |  -  |

