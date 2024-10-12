# WebApplicationFirewallPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policiesCreateOrUpdate**](WebApplicationFirewallPoliciesApi.md#policiesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} |  |
| [**policiesDelete**](WebApplicationFirewallPoliciesApi.md#policiesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} |  |
| [**policiesGet**](WebApplicationFirewallPoliciesApi.md#policiesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} |  |
| [**policiesList**](WebApplicationFirewallPoliciesApi.md#policiesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies |  |


<a id="policiesCreateOrUpdate"></a>
# **policiesCreateOrUpdate**
> WebApplicationFirewallPolicy policiesCreateOrUpdate(resourceGroupName, policyName, subscriptionId, apiVersion, parameters)



Create or update policy with specified rule set name within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApplicationFirewallPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WebApplicationFirewallPoliciesApi apiInstance = new WebApplicationFirewallPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String policyName = "policyName_example"; // String | The name of the Web Application Firewall Policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    WebApplicationFirewallPolicy parameters = new WebApplicationFirewallPolicy(); // WebApplicationFirewallPolicy | Policy to be created.
    try {
      WebApplicationFirewallPolicy result = apiInstance.policiesCreateOrUpdate(resourceGroupName, policyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApplicationFirewallPoliciesApi#policiesCreateOrUpdate");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **policyName** | **String**| The name of the Web Application Firewall Policy. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**WebApplicationFirewallPolicy**](WebApplicationFirewallPolicy.md)| Policy to be created. | |

### Return type

[**WebApplicationFirewallPolicy**](WebApplicationFirewallPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new protection policy has been created. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policiesDelete"></a>
# **policiesDelete**
> policiesDelete(resourceGroupName, policyName, subscriptionId, apiVersion)



Deletes Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApplicationFirewallPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WebApplicationFirewallPoliciesApi apiInstance = new WebApplicationFirewallPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String policyName = "policyName_example"; // String | The name of the Web Application Firewall Policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.policiesDelete(resourceGroupName, policyName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApplicationFirewallPoliciesApi#policiesDelete");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **policyName** | **String**| The name of the Web Application Firewall Policy. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |

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
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **204** | No Content. The request has been accepted but the policy was not found. |  -  |

<a id="policiesGet"></a>
# **policiesGet**
> WebApplicationFirewallPolicy policiesGet(resourceGroupName, policyName, subscriptionId, apiVersion)



Retrieve protection policy with specified name within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApplicationFirewallPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WebApplicationFirewallPoliciesApi apiInstance = new WebApplicationFirewallPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String policyName = "policyName_example"; // String | The name of the Web Application Firewall Policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      WebApplicationFirewallPolicy result = apiInstance.policiesGet(resourceGroupName, policyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApplicationFirewallPoliciesApi#policiesGet");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **policyName** | **String**| The name of the Web Application Firewall Policy. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**WebApplicationFirewallPolicy**](WebApplicationFirewallPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policiesList"></a>
# **policiesList**
> WebApplicationFirewallPolicyList policiesList(resourceGroupName, subscriptionId, apiVersion)



Lists all of the protection policies within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApplicationFirewallPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WebApplicationFirewallPoliciesApi apiInstance = new WebApplicationFirewallPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      WebApplicationFirewallPolicyList result = apiInstance.policiesList(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApplicationFirewallPoliciesApi#policiesList");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**WebApplicationFirewallPolicyList**](WebApplicationFirewallPolicyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

