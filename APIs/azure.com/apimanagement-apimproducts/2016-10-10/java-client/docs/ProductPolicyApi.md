# ProductPolicyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productPolicyCreateOrUpdate**](ProductPolicyApi.md#productPolicyCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/policy |  |
| [**productPolicyDelete**](ProductPolicyApi.md#productPolicyDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/policy |  |
| [**productPolicyGet**](ProductPolicyApi.md#productPolicyGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/products/{productId}/policy |  |


<a id="productPolicyCreateOrUpdate"></a>
# **productPolicyCreateOrUpdate**
> productPolicyCreateOrUpdate(resourceGroupName, serviceName, productId, ifMatch, apiVersion, subscriptionId, parameters)



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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductPolicyApi apiInstance = new ProductPolicyApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the product policy to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Object parameters = null; // Object | The policy contents to apply.
    try {
      apiInstance.productPolicyCreateOrUpdate(resourceGroupName, serviceName, productId, ifMatch, apiVersion, subscriptionId, parameters);
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |
| **ifMatch** | **String**| The entity state (Etag) version of the product policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | **Object**| The policy contents to apply. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/vnd.ms-azure-apim.policy+xml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Product policy configuration was successfully created. |  -  |
| **204** | Product policy configuration of the tenant was successfully updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="productPolicyDelete"></a>
# **productPolicyDelete**
> productPolicyDelete(resourceGroupName, serviceName, productId, ifMatch, apiVersion, subscriptionId)



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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductPolicyApi apiInstance = new ProductPolicyApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    String ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the product policy to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.productPolicyDelete(resourceGroupName, serviceName, productId, ifMatch, apiVersion, subscriptionId);
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |
| **ifMatch** | **String**| The entity state (Etag) version of the product policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

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
> File productPolicyGet(resourceGroupName, serviceName, apiVersion, subscriptionId, productId)



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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductPolicyApi apiInstance = new ProductPolicyApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | Product identifier. Must be unique in the current API Management service instance.
    try {
      File result = apiInstance.productPolicyGet(resourceGroupName, serviceName, apiVersion, subscriptionId, productId);
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| Product identifier. Must be unique in the current API Management service instance. | |

### Return type

[**File**](File.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.ms-azure-apim.policy+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product Policy information. |  * ETag - Current entity state version. Should be treated as opaque and used to make conditional HTTP requests. <br>  |

