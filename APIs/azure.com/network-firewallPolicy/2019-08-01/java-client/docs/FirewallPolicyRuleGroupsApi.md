# FirewallPolicyRuleGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**firewallPolicyRuleGroupsCreateOrUpdate**](FirewallPolicyRuleGroupsApi.md#firewallPolicyRuleGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleGroups/{ruleGroupName} |  |
| [**firewallPolicyRuleGroupsDelete**](FirewallPolicyRuleGroupsApi.md#firewallPolicyRuleGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleGroups/{ruleGroupName} |  |
| [**firewallPolicyRuleGroupsGet**](FirewallPolicyRuleGroupsApi.md#firewallPolicyRuleGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleGroups/{ruleGroupName} |  |
| [**firewallPolicyRuleGroupsList**](FirewallPolicyRuleGroupsApi.md#firewallPolicyRuleGroupsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/firewallPolicies/{firewallPolicyName}/ruleGroups |  |


<a id="firewallPolicyRuleGroupsCreateOrUpdate"></a>
# **firewallPolicyRuleGroupsCreateOrUpdate**
> FirewallPolicyRuleGroup firewallPolicyRuleGroupsCreateOrUpdate(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId, parameters)



Creates or updates the specified FirewallPolicyRuleGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallPolicyRuleGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FirewallPolicyRuleGroupsApi apiInstance = new FirewallPolicyRuleGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
    String ruleGroupName = "ruleGroupName_example"; // String | The name of the FirewallPolicyRuleGroup.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    FirewallPolicyRuleGroup parameters = new FirewallPolicyRuleGroup(); // FirewallPolicyRuleGroup | Parameters supplied to the create or update FirewallPolicyRuleGroup operation.
    try {
      FirewallPolicyRuleGroup result = apiInstance.firewallPolicyRuleGroupsCreateOrUpdate(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallPolicyRuleGroupsApi#firewallPolicyRuleGroupsCreateOrUpdate");
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
| **firewallPolicyName** | **String**| The name of the Firewall Policy. | |
| **ruleGroupName** | **String**| The name of the FirewallPolicyRuleGroup. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**FirewallPolicyRuleGroup**](FirewallPolicyRuleGroup.md)| Parameters supplied to the create or update FirewallPolicyRuleGroup operation. | |

### Return type

[**FirewallPolicyRuleGroup**](FirewallPolicyRuleGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns the resulting FirewallPolicyRuleGroup resource. |  -  |
| **201** | Request received successfully. The operation returns the resulting FirewallPolicyRuleGroup resource. |  -  |

<a id="firewallPolicyRuleGroupsDelete"></a>
# **firewallPolicyRuleGroupsDelete**
> firewallPolicyRuleGroupsDelete(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId)



Deletes the specified FirewallPolicyRuleGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallPolicyRuleGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FirewallPolicyRuleGroupsApi apiInstance = new FirewallPolicyRuleGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
    String ruleGroupName = "ruleGroupName_example"; // String | The name of the FirewallPolicyRuleGroup.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.firewallPolicyRuleGroupsDelete(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallPolicyRuleGroupsApi#firewallPolicyRuleGroupsDelete");
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
| **firewallPolicyName** | **String**| The name of the Firewall Policy. | |
| **ruleGroupName** | **String**| The name of the FirewallPolicyRuleGroup. | |
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
| **204** | Request successful. Resource with the specified name does not exist. |  -  |

<a id="firewallPolicyRuleGroupsGet"></a>
# **firewallPolicyRuleGroupsGet**
> FirewallPolicyRuleGroup firewallPolicyRuleGroupsGet(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId)



Gets the specified FirewallPolicyRuleGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallPolicyRuleGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FirewallPolicyRuleGroupsApi apiInstance = new FirewallPolicyRuleGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
    String ruleGroupName = "ruleGroupName_example"; // String | The name of the FirewallPolicyRuleGroup.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      FirewallPolicyRuleGroup result = apiInstance.firewallPolicyRuleGroupsGet(resourceGroupName, firewallPolicyName, ruleGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallPolicyRuleGroupsApi#firewallPolicyRuleGroupsGet");
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
| **firewallPolicyName** | **String**| The name of the Firewall Policy. | |
| **ruleGroupName** | **String**| The name of the FirewallPolicyRuleGroup. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**FirewallPolicyRuleGroup**](FirewallPolicyRuleGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request successful. The operation returns a FirewallPolicyRuleGroup resource. |  -  |

<a id="firewallPolicyRuleGroupsList"></a>
# **firewallPolicyRuleGroupsList**
> FirewallPolicyRuleGroupListResult firewallPolicyRuleGroupsList(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId)



Lists all FirewallPolicyRuleGroups in a FirewallPolicy resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirewallPolicyRuleGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    FirewallPolicyRuleGroupsApi apiInstance = new FirewallPolicyRuleGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String firewallPolicyName = "firewallPolicyName_example"; // String | The name of the Firewall Policy.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      FirewallPolicyRuleGroupListResult result = apiInstance.firewallPolicyRuleGroupsList(resourceGroupName, firewallPolicyName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirewallPolicyRuleGroupsApi#firewallPolicyRuleGroupsList");
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
| **firewallPolicyName** | **String**| The name of the Firewall Policy. | |
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**FirewallPolicyRuleGroupListResult**](FirewallPolicyRuleGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of FirewallPolicyRuleGroup resources. |  -  |

