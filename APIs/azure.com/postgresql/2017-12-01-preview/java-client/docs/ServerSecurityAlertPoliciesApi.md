# ServerSecurityAlertPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverSecurityAlertPoliciesCreateOrUpdate**](ServerSecurityAlertPoliciesApi.md#serverSecurityAlertPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/servers/{serverName}/securityAlertPolicies/{securityAlertPolicyName} |  |
| [**serverSecurityAlertPoliciesGet**](ServerSecurityAlertPoliciesApi.md#serverSecurityAlertPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/servers/{serverName}/securityAlertPolicies/{securityAlertPolicyName} |  |


<a id="serverSecurityAlertPoliciesCreateOrUpdate"></a>
# **serverSecurityAlertPoliciesCreateOrUpdate**
> ServerSecurityAlertPolicy serverSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a threat detection policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerSecurityAlertPoliciesApi apiInstance = new ServerSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String securityAlertPolicyName = "Default"; // String | The name of the threat detection policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    ServerSecurityAlertPolicy parameters = new ServerSecurityAlertPolicy(); // ServerSecurityAlertPolicy | The server security alert policy.
    try {
      ServerSecurityAlertPolicy result = apiInstance.serverSecurityAlertPoliciesCreateOrUpdate(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerSecurityAlertPoliciesApi#serverSecurityAlertPoliciesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **securityAlertPolicyName** | **String**| The name of the threat detection policy. | [enum: Default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**ServerSecurityAlertPolicy**](ServerSecurityAlertPolicy.md)| The server security alert policy. | |

### Return type

[**ServerSecurityAlertPolicy**](ServerSecurityAlertPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the threat detection policy. |  -  |
| **202** | Created request to set the server threat detection policy. |  -  |
| **0** | Error response describing why the operation of setting security alert policies failed. |  -  |

<a id="serverSecurityAlertPoliciesGet"></a>
# **serverSecurityAlertPoliciesGet**
> ServerSecurityAlertPolicy serverSecurityAlertPoliciesGet(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion)



Get a server&#39;s security alert policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServerSecurityAlertPoliciesApi apiInstance = new ServerSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String securityAlertPolicyName = "Default"; // String | The name of the security alert policy.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      ServerSecurityAlertPolicy result = apiInstance.serverSecurityAlertPoliciesGet(resourceGroupName, serverName, securityAlertPolicyName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerSecurityAlertPoliciesApi#serverSecurityAlertPoliciesGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **securityAlertPolicyName** | **String**| The name of the security alert policy. | [enum: Default] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**ServerSecurityAlertPolicy**](ServerSecurityAlertPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the server threat detection policy. |  -  |
| **0** | Error response describing why the operation of getting security alert policies failed. |  -  |

