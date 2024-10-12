# ProductPolicyApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productPolicyCreateOrUpdate**](ProductPolicyApi.md#productPolicyCreateOrUpdate) | **PUT** /products/{productId}/policies/{policyId} |  |
| [**productPolicyDelete**](ProductPolicyApi.md#productPolicyDelete) | **DELETE** /products/{productId}/policies/{policyId} |  |
| [**productPolicyGet**](ProductPolicyApi.md#productPolicyGet) | **GET** /products/{productId}/policies/{policyId} |  |
| [**productPolicyListByProduct**](ProductPolicyApi.md#productPolicyListByProduct) | **GET** /products/{productId}/policies |  |


<a id="productPolicyCreateOrUpdate"></a>
# **productPolicyCreateOrUpdate**
> ProductPolicyListByProduct200ResponseValueInner productPolicyCreateOrUpdate(productId, policyId, apiVersion, parameters)



Creates or updates policy configuration for the Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductPolicyApi apiInstance = new ProductPolicyApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String policyId = "policy"; // String | The identifier of the Policy.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    ProductPolicyListByProduct200ResponseValueInner parameters = new ProductPolicyListByProduct200ResponseValueInner(); // ProductPolicyListByProduct200ResponseValueInner | The policy contents to apply.
    try {
      ProductPolicyListByProduct200ResponseValueInner result = apiInstance.productPolicyCreateOrUpdate(productId, policyId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductPolicyApi#productPolicyCreateOrUpdate");
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
| **policyId** | **String**| The identifier of the Policy. | [enum: policy] |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **parameters** | [**ProductPolicyListByProduct200ResponseValueInner**](ProductPolicyListByProduct200ResponseValueInner.md)| The policy contents to apply. | |

### Return type

[**ProductPolicyListByProduct200ResponseValueInner**](ProductPolicyListByProduct200ResponseValueInner.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.ms-azure-apim.policy+xml, application/vnd.ms-azure-apim.policy.raw+xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product policy configuration of the tenant was successfully updated. |  -  |
| **201** | Product policy configuration was successfully created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productPolicyDelete"></a>
# **productPolicyDelete**
> productPolicyDelete(productId, policyId, ifMatch, apiVersion)



Deletes the policy configuration at the Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductPolicyApi apiInstance = new ProductPolicyApi(defaultClient);
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String policyId = "policy"; // String | The identifier of the Policy.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the product policy to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.productPolicyDelete(productId, policyId, ifMatch, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductPolicyApi#productPolicyDelete");
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
| **policyId** | **String**| The identifier of the Policy. | [enum: policy] |
| **ifMatch** | **String**| The entity state (Etag) version of the product policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
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
| **204** | Successfully deleted the policy configuration at the Product level. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productPolicyGet"></a>
# **productPolicyGet**
> ProductPolicyListByProduct200ResponseValueInner productPolicyGet(apiVersion, productId, policyId)



Get the policy configuration at the Product level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductPolicyApi apiInstance = new ProductPolicyApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String policyId = "policy"; // String | The identifier of the Policy.
    try {
      ProductPolicyListByProduct200ResponseValueInner result = apiInstance.productPolicyGet(apiVersion, productId, policyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductPolicyApi#productPolicyGet");
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
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |
| **policyId** | **String**| The identifier of the Policy. | [enum: policy] |

### Return type

[**ProductPolicyListByProduct200ResponseValueInner**](ProductPolicyListByProduct200ResponseValueInner.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.ms-azure-apim.policy+xml, application/vnd.ms-azure-apim.policy.raw+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product Policy information. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productPolicyListByProduct"></a>
# **productPolicyListByProduct**
> ProductPolicyListByProduct200Response productPolicyListByProduct(apiVersion, productId)



Get the policy configuration at the Product level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ProductPolicyApi apiInstance = new ProductPolicyApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    try {
      ProductPolicyListByProduct200Response result = apiInstance.productPolicyListByProduct(apiVersion, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductPolicyApi#productPolicyListByProduct");
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
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |

### Return type

[**ProductPolicyListByProduct200Response**](ProductPolicyListByProduct200Response.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product Policy information. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

