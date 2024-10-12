# ServiceEndpointPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serviceEndpointPoliciesCreateOrUpdate**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName} |  |
| [**serviceEndpointPoliciesDelete**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName} |  |
| [**serviceEndpointPoliciesGet**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName} |  |
| [**serviceEndpointPoliciesList**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ServiceEndpointPolicies |  |
| [**serviceEndpointPoliciesListByResourceGroup**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies |  |
| [**serviceEndpointPoliciesUpdate**](ServiceEndpointPoliciesApi.md#serviceEndpointPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/serviceEndpointPolicies/{serviceEndpointPolicyName} |  |


<a id="serviceEndpointPoliciesCreateOrUpdate"></a>
# **serviceEndpointPoliciesCreateOrUpdate**
> ServiceEndpointPolicy serviceEndpointPoliciesCreateOrUpdate(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, parameters)



Creates or updates a service Endpoint Policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPoliciesApi apiInstance = new ServiceEndpointPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ServiceEndpointPolicy parameters = new ServiceEndpointPolicy(); // ServiceEndpointPolicy | Parameters supplied to the create or update service endpoint policy operation.
    try {
      ServiceEndpointPolicy result = apiInstance.serviceEndpointPoliciesCreateOrUpdate(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPoliciesApi#serviceEndpointPoliciesCreateOrUpdate");
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
| **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ServiceEndpointPolicy**](ServiceEndpointPolicy.md)| Parameters supplied to the create or update service endpoint policy operation. | |

### Return type

[**ServiceEndpointPolicy**](ServiceEndpointPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ServiceEndpointPolicy resource. |  -  |
| **201** | Create successful. The operation returns the resulting ServiceEndpointPolicy resource. |  -  |

<a id="serviceEndpointPoliciesDelete"></a>
# **serviceEndpointPoliciesDelete**
> serviceEndpointPoliciesDelete(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId)



Deletes the specified service endpoint policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPoliciesApi apiInstance = new ServiceEndpointPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.serviceEndpointPoliciesDelete(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPoliciesApi#serviceEndpointPoliciesDelete");
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
| **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Request successful. Resource does not exist. |  -  |

<a id="serviceEndpointPoliciesGet"></a>
# **serviceEndpointPoliciesGet**
> ServiceEndpointPolicy serviceEndpointPoliciesGet(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, $expand)



Gets the specified service Endpoint Policies in a specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPoliciesApi apiInstance = new ServiceEndpointPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $expand = "$expand_example"; // String | Expands referenced resources.
    try {
      ServiceEndpointPolicy result = apiInstance.serviceEndpointPoliciesGet(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPoliciesApi#serviceEndpointPoliciesGet");
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
| **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$expand** | **String**| Expands referenced resources. | [optional] |

### Return type

[**ServiceEndpointPolicy**](ServiceEndpointPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting ServiceEndpointPolicy resource. |  -  |

<a id="serviceEndpointPoliciesList"></a>
# **serviceEndpointPoliciesList**
> ServiceEndpointPolicyListResult serviceEndpointPoliciesList(apiVersion, subscriptionId)



Gets all the service endpoint policies in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPoliciesApi apiInstance = new ServiceEndpointPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ServiceEndpointPolicyListResult result = apiInstance.serviceEndpointPoliciesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPoliciesApi#serviceEndpointPoliciesList");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ServiceEndpointPolicyListResult**](ServiceEndpointPolicyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ServiceEndpointPolicy resources. |  -  |

<a id="serviceEndpointPoliciesListByResourceGroup"></a>
# **serviceEndpointPoliciesListByResourceGroup**
> ServiceEndpointPolicyListResult serviceEndpointPoliciesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all service endpoint Policies in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPoliciesApi apiInstance = new ServiceEndpointPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ServiceEndpointPolicyListResult result = apiInstance.serviceEndpointPoliciesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPoliciesApi#serviceEndpointPoliciesListByResourceGroup");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ServiceEndpointPolicyListResult**](ServiceEndpointPolicyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a list of ServiceEndpointPolicy resources. |  -  |

<a id="serviceEndpointPoliciesUpdate"></a>
# **serviceEndpointPoliciesUpdate**
> ServiceEndpointPolicy serviceEndpointPoliciesUpdate(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, parameters)



Updates service Endpoint Policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceEndpointPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceEndpointPoliciesApi apiInstance = new ServiceEndpointPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceEndpointPolicyName = "serviceEndpointPolicyName_example"; // String | The name of the service endpoint policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ServiceEndpointPoliciesUpdateRequest parameters = new ServiceEndpointPoliciesUpdateRequest(); // ServiceEndpointPoliciesUpdateRequest | Parameters supplied to update service endpoint policy tags.
    try {
      ServiceEndpointPolicy result = apiInstance.serviceEndpointPoliciesUpdate(resourceGroupName, serviceEndpointPolicyName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceEndpointPoliciesApi#serviceEndpointPoliciesUpdate");
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
| **serviceEndpointPolicyName** | **String**| The name of the service endpoint policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ServiceEndpointPoliciesUpdateRequest**](ServiceEndpointPoliciesUpdateRequest.md)| Parameters supplied to update service endpoint policy tags. | |

### Return type

[**ServiceEndpointPolicy**](ServiceEndpointPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting ServiceEndpointPolicy resource. |  -  |

