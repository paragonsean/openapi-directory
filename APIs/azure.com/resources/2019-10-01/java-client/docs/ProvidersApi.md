# ProvidersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**providersGet**](ProvidersApi.md#providersGet) | **GET** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace} |  |
| [**providersGetAtTenantScope**](ProvidersApi.md#providersGetAtTenantScope) | **GET** /providers/{resourceProviderNamespace} |  |
| [**providersList**](ProvidersApi.md#providersList) | **GET** /subscriptions/{subscriptionId}/providers |  |
| [**providersListAtTenantScope**](ProvidersApi.md#providersListAtTenantScope) | **GET** /providers |  |
| [**providersRegister**](ProvidersApi.md#providersRegister) | **POST** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/register |  |
| [**providersUnregister**](ProvidersApi.md#providersUnregister) | **POST** /subscriptions/{subscriptionId}/providers/{resourceProviderNamespace}/unregister |  |


<a id="providersGet"></a>
# **providersGet**
> Provider providersGet(resourceProviderNamespace, apiVersion, subscriptionId, $expand)



Gets the specified resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String $expand = "$expand_example"; // String | The $expand query parameter. For example, to include property aliases in response, use $expand=resourceTypes/aliases.
    try {
      Provider result = apiInstance.providersGet(resourceProviderNamespace, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#providersGet");
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
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$expand** | **String**| The $expand query parameter. For example, to include property aliases in response, use $expand&#x3D;resourceTypes/aliases. | [optional] |

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource provider. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="providersGetAtTenantScope"></a>
# **providersGetAtTenantScope**
> Provider providersGetAtTenantScope(resourceProviderNamespace, apiVersion, $expand)



Gets the specified resource provider at the tenant level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String $expand = "$expand_example"; // String | The $expand query parameter. For example, to include property aliases in response, use $expand=resourceTypes/aliases.
    try {
      Provider result = apiInstance.providersGetAtTenantScope(resourceProviderNamespace, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#providersGetAtTenantScope");
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
| **resourceProviderNamespace** | **String**| The namespace of the resource provider. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$expand** | **String**| The $expand query parameter. For example, to include property aliases in response, use $expand&#x3D;resourceTypes/aliases. | [optional] |

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource provider. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="providersList"></a>
# **providersList**
> ProviderListResult providersList(apiVersion, subscriptionId, $top, $expand)



Gets all resource providers for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | The number of results to return. If null is passed returns all deployments.
    String $expand = "$expand_example"; // String | The properties to include in the results. For example, use &$expand=metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand=resourceTypes/aliases.
    try {
      ProviderListResult result = apiInstance.providersList(apiVersion, subscriptionId, $top, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#providersList");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$top** | **Integer**| The number of results to return. If null is passed returns all deployments. | [optional] |
| **$expand** | **String**| The properties to include in the results. For example, use &amp;$expand&#x3D;metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand&#x3D;resourceTypes/aliases. | [optional] |

### Return type

[**ProviderListResult**](ProviderListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of resource providers. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="providersListAtTenantScope"></a>
# **providersListAtTenantScope**
> ProviderListResult providersListAtTenantScope(apiVersion, $top, $expand)



Gets all resource providers for the tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    Integer $top = 56; // Integer | The number of results to return. If null is passed returns all providers.
    String $expand = "$expand_example"; // String | The properties to include in the results. For example, use &$expand=metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand=resourceTypes/aliases.
    try {
      ProviderListResult result = apiInstance.providersListAtTenantScope(apiVersion, $top, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#providersListAtTenantScope");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **$top** | **Integer**| The number of results to return. If null is passed returns all providers. | [optional] |
| **$expand** | **String**| The properties to include in the results. For example, use &amp;$expand&#x3D;metadata in the query string to retrieve resource provider metadata. To include property aliases in response, use $expand&#x3D;resourceTypes/aliases. | [optional] |

### Return type

[**ProviderListResult**](ProviderListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns an array of resource providers. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="providersRegister"></a>
# **providersRegister**
> Provider providersRegister(resourceProviderNamespace, apiVersion, subscriptionId)



Registers a subscription with a resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider to register.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      Provider result = apiInstance.providersRegister(resourceProviderNamespace, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#providersRegister");
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
| **resourceProviderNamespace** | **String**| The namespace of the resource provider to register. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource provider. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="providersUnregister"></a>
# **providersUnregister**
> Provider providersUnregister(resourceProviderNamespace, apiVersion, subscriptionId)



Unregisters a subscription from a resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProvidersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProvidersApi apiInstance = new ProvidersApi(defaultClient);
    String resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider to unregister.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      Provider result = apiInstance.providersUnregister(resourceProviderNamespace, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProvidersApi#providersUnregister");
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
| **resourceProviderNamespace** | **String**| The namespace of the resource provider to unregister. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**Provider**](Provider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Returns information about the resource provider. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

