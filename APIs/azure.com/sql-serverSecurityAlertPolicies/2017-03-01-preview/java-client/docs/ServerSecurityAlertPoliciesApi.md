# ServerSecurityAlertPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverSecurityAlertPoliciesCreateOrUpdate**](ServerSecurityAlertPoliciesApi.md#serverSecurityAlertPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/securityAlertPolicies/{securityAlertPolicyName} |  |
| [**serverSecurityAlertPoliciesGet**](ServerSecurityAlertPoliciesApi.md#serverSecurityAlertPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/securityAlertPolicies/{securityAlertPolicyName} |  |
| [**serverSecurityAlertPoliciesListByServer**](ServerSecurityAlertPoliciesApi.md#serverSecurityAlertPoliciesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/securityAlertPolicies |  |


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
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the threat detection policy. |  -  |
| **202** | Created request to set the server threat detection policy. |  -  |
| **0** | *** Error Responses: ***   * 400 SecurityAlertPoliciesInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 SecurityAlertPoliciesInvalidStorageAccountCredentials - The provided storage account access key is not valid.   * 400 InvalidServerSecurityAlertPolicyCreateRequest - The create server Threat Detection security alert policy request does not exist or has no properties object.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 409 ServerSecurityAlertPolicyInProgress - Set server security alert policy is already in progress   * 409 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later |  -  |

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
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the server threat detection policy. |  -  |
| **0** | *** Error Responses: ***   * 400 SecurityAlertPoliciesInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 SecurityAlertPoliciesInvalidStorageAccountCredentials - The provided storage account access key is not valid.   * 400 InvalidServerSecurityAlertPolicyCreateRequest - The create server Threat Detection security alert policy request does not exist or has no properties object.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 409 ServerSecurityAlertPolicyInProgress - Set server security alert policy is already in progress   * 409 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 GetServerSecurityAlertPolicyFailed - Failed to get Threat Detection settings |  -  |

<a id="serverSecurityAlertPoliciesListByServer"></a>
# **serverSecurityAlertPoliciesListByServer**
> LogicalServerSecurityAlertPolicyListResult serverSecurityAlertPoliciesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Get the server&#39;s threat detection policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerSecurityAlertPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerSecurityAlertPoliciesApi apiInstance = new ServerSecurityAlertPoliciesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      LogicalServerSecurityAlertPolicyListResult result = apiInstance.serverSecurityAlertPoliciesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerSecurityAlertPoliciesApi#serverSecurityAlertPoliciesListByServer");
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
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**LogicalServerSecurityAlertPolicyListResult**](LogicalServerSecurityAlertPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the server threat detection policies. |  -  |
| **0** | *** Error Responses: ***   * 400 SecurityAlertPoliciesInvalidStorageAccountName - The provided storage account is not valid or does not exist.   * 400 SecurityAlertPoliciesInvalidStorageAccountCredentials - The provided storage account access key is not valid.   * 400 InvalidServerSecurityAlertPolicyCreateRequest - The create server Threat Detection security alert policy request does not exist or has no properties object.   * 400 DataSecurityInvalidUserSuppliedParameter - An invalid parameter value was provided by the client.   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 400 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 409 ServerSecurityAlertPolicyInProgress - Set server security alert policy is already in progress   * 409 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 DatabaseIsUnavailable - Loading failed. Please try again later.   * 500 UpsertServerSecurityAlertPolicyFailed - An error has occurred while saving Threat detection settings, please try again later   * 500 GetServerSecurityAlertPolicyFailed - Failed to get Threat Detection settings |  -  |

