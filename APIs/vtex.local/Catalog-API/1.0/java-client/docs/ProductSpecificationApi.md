# ProductSpecificationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtProductProductIdSpecificationPost**](ProductSpecificationApi.md#apiCatalogPvtProductProductIdSpecificationPost) | **POST** /api/catalog/pvt/product/{productId}/specification | Associate Product Specification |
| [**apiCatalogPvtProductProductIdSpecificationvaluePut**](ProductSpecificationApi.md#apiCatalogPvtProductProductIdSpecificationvaluePut) | **PUT** /api/catalog/pvt/product/{productId}/specificationvalue | Associate product specification using specification name and group name |
| [**deleteAllProductSpecifications**](ProductSpecificationApi.md#deleteAllProductSpecifications) | **DELETE** /api/catalog/pvt/product/{productId}/specification | Delete all Product Specifications by Product ID |
| [**deleteaProductSpecification**](ProductSpecificationApi.md#deleteaProductSpecification) | **DELETE** /api/catalog/pvt/product/{productId}/specification/{specificationId} | Delete a specific Product Specification |
| [**getProductSpecification**](ProductSpecificationApi.md#getProductSpecification) | **GET** /api/catalog_system/pvt/products/{productId}/specification | Get Product Specification by Product ID |
| [**getProductSpecificationbyProductID**](ProductSpecificationApi.md#getProductSpecificationbyProductID) | **GET** /api/catalog/pvt/product/{productId}/specification | Get Product Specification and its information by Product ID |
| [**updateProductSpecification**](ProductSpecificationApi.md#updateProductSpecification) | **POST** /api/catalog_system/pvt/products/{productId}/specification | Update Product Specification by Product ID |


<a id="apiCatalogPvtProductProductIdSpecificationPost"></a>
# **apiCatalogPvtProductProductIdSpecificationPost**
> ApiCatalogPvtProductProductIdSpecificationPost200Response apiCatalogPvtProductProductIdSpecificationPost(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationPostRequest)

Associate Product Specification

Associates a previously defined Specification to a Product.    ### Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 41,      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSpecificationApi;

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

    ProductSpecificationApi apiInstance = new ProductSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    ApiCatalogPvtProductProductIdSpecificationPostRequest apiCatalogPvtProductProductIdSpecificationPostRequest = new ApiCatalogPvtProductProductIdSpecificationPostRequest(); // ApiCatalogPvtProductProductIdSpecificationPostRequest | 
    try {
      ApiCatalogPvtProductProductIdSpecificationPost200Response result = apiInstance.apiCatalogPvtProductProductIdSpecificationPost(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSpecificationApi#apiCatalogPvtProductProductIdSpecificationPost");
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
| **productId** | **Integer**| Product’s unique numerical identifier. | |
| **apiCatalogPvtProductProductIdSpecificationPostRequest** | [**ApiCatalogPvtProductProductIdSpecificationPostRequest**](ApiCatalogPvtProductProductIdSpecificationPostRequest.md)|  | [optional] |

### Return type

[**ApiCatalogPvtProductProductIdSpecificationPost200Response**](ApiCatalogPvtProductProductIdSpecificationPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtProductProductIdSpecificationvaluePut"></a>
# **apiCatalogPvtProductProductIdSpecificationvaluePut**
> List&lt;ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner&gt; apiCatalogPvtProductProductIdSpecificationvaluePut(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationvaluePutRequest)

Associate product specification using specification name and group name

Associates a specification to a product using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Material\&quot;,      \&quot;GroupName\&quot;: \&quot;Additional Information\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;Cotton\&quot;,         \&quot;Polyester\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 53,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 60,          \&quot;Text\&quot;: \&quot;Cotton\&quot;      },      {          \&quot;Id\&quot;: 54,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 61,          \&quot;Text\&quot;: \&quot;Polyester\&quot;      }  ]  &#x60;&#x60;&#x60;  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSpecificationApi;

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

    ProductSpecificationApi apiInstance = new ProductSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    ApiCatalogPvtProductProductIdSpecificationvaluePutRequest apiCatalogPvtProductProductIdSpecificationvaluePutRequest = new ApiCatalogPvtProductProductIdSpecificationvaluePutRequest(); // ApiCatalogPvtProductProductIdSpecificationvaluePutRequest | 
    try {
      List<ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner> result = apiInstance.apiCatalogPvtProductProductIdSpecificationvaluePut(contentType, accept, productId, apiCatalogPvtProductProductIdSpecificationvaluePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSpecificationApi#apiCatalogPvtProductProductIdSpecificationvaluePut");
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
| **productId** | **Integer**| Product’s unique numerical identifier. | |
| **apiCatalogPvtProductProductIdSpecificationvaluePutRequest** | [**ApiCatalogPvtProductProductIdSpecificationvaluePutRequest**](ApiCatalogPvtProductProductIdSpecificationvaluePutRequest.md)|  | [optional] |

### Return type

[**List&lt;ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner&gt;**](ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteAllProductSpecifications"></a>
# **deleteAllProductSpecifications**
> deleteAllProductSpecifications(contentType, accept, productId)

Delete all Product Specifications by Product ID

Deletes all Product Specifications given a specific Product ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSpecificationApi;

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

    ProductSpecificationApi apiInstance = new ProductSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    try {
      apiInstance.deleteAllProductSpecifications(contentType, accept, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSpecificationApi#deleteAllProductSpecifications");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |

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

<a id="deleteaProductSpecification"></a>
# **deleteaProductSpecification**
> deleteaProductSpecification(contentType, accept, productId, specificationId)

Delete a specific Product Specification

Deletes a specific Product Specification given a Product ID and a Specification ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSpecificationApi;

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

    ProductSpecificationApi apiInstance = new ProductSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    Integer specificationId = 7; // Integer | Product Specification’s unique numerical identifier.
    try {
      apiInstance.deleteaProductSpecification(contentType, accept, productId, specificationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSpecificationApi#deleteaProductSpecification");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |
| **specificationId** | **Integer**| Product Specification’s unique numerical identifier. | |

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

<a id="getProductSpecification"></a>
# **getProductSpecification**
> List&lt;GetorUpdateProductSpecification&gt; getProductSpecification(contentType, accept, productId)

Get Product Specification by Product ID

Retrieves all specifications of a product by the product&#39;s ID.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSpecificationApi;

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

    ProductSpecificationApi apiInstance = new ProductSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    try {
      List<GetorUpdateProductSpecification> result = apiInstance.getProductSpecification(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSpecificationApi#getProductSpecification");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |

### Return type

[**List&lt;GetorUpdateProductSpecification&gt;**](GetorUpdateProductSpecification.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Cache-Control -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-AspNet-Version -  <br>  * X-Powered-By -  <br>  * false -  <br>  * p3p -  <br>  * powered -  <br>  * x-vtex-operation-id -  <br>  |

<a id="getProductSpecificationbyProductID"></a>
# **getProductSpecificationbyProductID**
> List&lt;GetProductSpecificationbyProductID200ResponseInner&gt; getProductSpecificationbyProductID(contentType, accept, productId)

Get Product Specification and its information by Product ID

Retrieves information of all specifications of a product by the product&#39;s ID.     ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 227,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;FieldValueId\&quot;: 135,          \&quot;Text\&quot;: \&quot;ValueA\&quot;      },      {          \&quot;Id\&quot;: 228,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;FieldValueId\&quot;: 1,          \&quot;Text\&quot;: \&quot;Giant\&quot;      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSpecificationApi;

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

    ProductSpecificationApi apiInstance = new ProductSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    try {
      List<GetProductSpecificationbyProductID200ResponseInner> result = apiInstance.getProductSpecificationbyProductID(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSpecificationApi#getProductSpecificationbyProductID");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |

### Return type

[**List&lt;GetProductSpecificationbyProductID200ResponseInner&gt;**](GetProductSpecificationbyProductID200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateProductSpecification"></a>
# **updateProductSpecification**
> updateProductSpecification(contentType, accept, productId, getorUpdateProductSpecification)

Update Product Specification by Product ID

Updates the value of a product specification by the product&#39;s ID. The ID or name can be used to identify what product specification will be updated. Specification fields must be previously created in your Catalog.    ### Request body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductSpecificationApi;

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

    ProductSpecificationApi apiInstance = new ProductSpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique identifier.
    List<GetorUpdateProductSpecification> getorUpdateProductSpecification = Arrays.asList(); // List<GetorUpdateProductSpecification> | 
    try {
      apiInstance.updateProductSpecification(contentType, accept, productId, getorUpdateProductSpecification);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductSpecificationApi#updateProductSpecification");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique identifier. | |
| **getorUpdateProductSpecification** | [**List&lt;GetorUpdateProductSpecification&gt;**](GetorUpdateProductSpecification.md)|  | |

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

