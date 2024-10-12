# DdosCustomPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ddosCustomPoliciesCreateOrUpdate**](DdosCustomPoliciesApi.md#ddosCustomPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosCustomPolicies/{ddosCustomPolicyName} |  |
| [**ddosCustomPoliciesDelete**](DdosCustomPoliciesApi.md#ddosCustomPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosCustomPolicies/{ddosCustomPolicyName} |  |
| [**ddosCustomPoliciesGet**](DdosCustomPoliciesApi.md#ddosCustomPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosCustomPolicies/{ddosCustomPolicyName} |  |
| [**ddosCustomPoliciesUpdateTags**](DdosCustomPoliciesApi.md#ddosCustomPoliciesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ddosCustomPolicies/{ddosCustomPolicyName} |  |


<a id="ddosCustomPoliciesCreateOrUpdate"></a>
# **ddosCustomPoliciesCreateOrUpdate**
> DdosCustomPolicy ddosCustomPoliciesCreateOrUpdate(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, parameters)



Creates or updates a DDoS custom policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DdosCustomPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DdosCustomPoliciesApi apiInstance = new DdosCustomPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ddosCustomPolicyName = "ddosCustomPolicyName_example"; // String | The name of the DDoS custom policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DdosCustomPolicy parameters = new DdosCustomPolicy(); // DdosCustomPolicy | Parameters supplied to the create or update operation.
    try {
      DdosCustomPolicy result = apiInstance.ddosCustomPoliciesCreateOrUpdate(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DdosCustomPoliciesApi#ddosCustomPoliciesCreateOrUpdate");
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
| **ddosCustomPolicyName** | **String**| The name of the DDoS custom policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**DdosCustomPolicy**](DdosCustomPolicy.md)| Parameters supplied to the create or update operation. | |

### Return type

[**DdosCustomPolicy**](DdosCustomPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting DDoS custom policy resource. |  -  |
| **201** | Create successful. The operation returns the resulting DDoS custom policy resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ddosCustomPoliciesDelete"></a>
# **ddosCustomPoliciesDelete**
> ddosCustomPoliciesDelete(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId)



Deletes the specified DDoS custom policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DdosCustomPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DdosCustomPoliciesApi apiInstance = new DdosCustomPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ddosCustomPolicyName = "ddosCustomPolicyName_example"; // String | The name of the DDoS custom policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.ddosCustomPoliciesDelete(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DdosCustomPoliciesApi#ddosCustomPoliciesDelete");
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
| **ddosCustomPolicyName** | **String**| The name of the DDoS custom policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Delete successful. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | Request successful. Resource does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ddosCustomPoliciesGet"></a>
# **ddosCustomPoliciesGet**
> DdosCustomPolicy ddosCustomPoliciesGet(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId)



Gets information about the specified DDoS custom policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DdosCustomPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DdosCustomPoliciesApi apiInstance = new DdosCustomPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ddosCustomPolicyName = "ddosCustomPolicyName_example"; // String | The name of the DDoS custom policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DdosCustomPolicy result = apiInstance.ddosCustomPoliciesGet(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DdosCustomPoliciesApi#ddosCustomPoliciesGet");
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
| **ddosCustomPolicyName** | **String**| The name of the DDoS custom policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DdosCustomPolicy**](DdosCustomPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the specified DDoS custom policy resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="ddosCustomPoliciesUpdateTags"></a>
# **ddosCustomPoliciesUpdateTags**
> DdosCustomPolicy ddosCustomPoliciesUpdateTags(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, parameters)



Update a DDoS custom policy tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DdosCustomPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DdosCustomPoliciesApi apiInstance = new DdosCustomPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ddosCustomPolicyName = "ddosCustomPolicyName_example"; // String | The name of the DDoS custom policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DdosCustomPoliciesUpdateTagsRequest parameters = new DdosCustomPoliciesUpdateTagsRequest(); // DdosCustomPoliciesUpdateTagsRequest | Parameters supplied to the update DDoS custom policy resource tags.
    try {
      DdosCustomPolicy result = apiInstance.ddosCustomPoliciesUpdateTags(resourceGroupName, ddosCustomPolicyName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DdosCustomPoliciesApi#ddosCustomPoliciesUpdateTags");
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
| **ddosCustomPolicyName** | **String**| The name of the DDoS custom policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**DdosCustomPoliciesUpdateTagsRequest**](DdosCustomPoliciesUpdateTagsRequest.md)| Parameters supplied to the update DDoS custom policy resource tags. | |

### Return type

[**DdosCustomPolicy**](DdosCustomPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Update successful. The operation returns the resulting DDoS custom policy resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

