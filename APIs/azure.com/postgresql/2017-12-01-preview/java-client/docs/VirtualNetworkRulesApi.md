# VirtualNetworkRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualNetworkRulesCreateOrUpdate**](VirtualNetworkRulesApi.md#virtualNetworkRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/servers/{serverName}/virtualNetworkRules/{virtualNetworkRuleName} |  |
| [**virtualNetworkRulesDelete**](VirtualNetworkRulesApi.md#virtualNetworkRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/servers/{serverName}/virtualNetworkRules/{virtualNetworkRuleName} |  |
| [**virtualNetworkRulesGet**](VirtualNetworkRulesApi.md#virtualNetworkRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/servers/{serverName}/virtualNetworkRules/{virtualNetworkRuleName} |  |
| [**virtualNetworkRulesListByServer**](VirtualNetworkRulesApi.md#virtualNetworkRulesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/servers/{serverName}/virtualNetworkRules |  |


<a id="virtualNetworkRulesCreateOrUpdate"></a>
# **virtualNetworkRulesCreateOrUpdate**
> VirtualNetworkRule virtualNetworkRulesCreateOrUpdate(resourceGroupName, serverName, subscriptionId, apiVersion, virtualNetworkRuleName, parameters)



Creates or updates an existing virtual network rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule.
    VirtualNetworkRule parameters = new VirtualNetworkRule(); // VirtualNetworkRule | The requested virtual Network Rule Resource state.
    try {
      VirtualNetworkRule result = apiInstance.virtualNetworkRulesCreateOrUpdate(resourceGroupName, serverName, subscriptionId, apiVersion, virtualNetworkRuleName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesCreateOrUpdate");
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
| **virtualNetworkRuleName** | **String**| The name of the virtual network rule. | |
| **parameters** | [**VirtualNetworkRule**](VirtualNetworkRule.md)| The requested virtual Network Rule Resource state. | |

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated a virtual network rule. |  -  |
| **201** | Successfully created a virtual network rule. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceId - Invalid resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 NullVirtualNetworkRequest - Virtual Network Request is Null   * 400 NullVirtualNetworkRequestParameters - Virtual Network Request Parameters are Null   * 400 NullVirtualNetworkSubnetId - The Virtual Network Subnet Id is null   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 VirtualNetworkRuleNotEnabled - Azure SQL Server Virtual Network Rule feature is not enabled   * 404 OperationIdNotFound - The operation with Id does not exist.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation. |  -  |

<a id="virtualNetworkRulesDelete"></a>
# **virtualNetworkRulesDelete**
> virtualNetworkRulesDelete(resourceGroupName, serverName, virtualNetworkRuleName, subscriptionId, apiVersion)



Deletes the virtual network rule with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.virtualNetworkRulesDelete(resourceGroupName, serverName, virtualNetworkRuleName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesDelete");
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
| **virtualNetworkRuleName** | **String**| The name of the virtual network rule. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

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
| **200** | Successfully deleted the virtual network rule. |  -  |
| **202** | Accepted |  -  |
| **204** | The specified virtual network rule does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceId - Invalid resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 NullVirtualNetworkRequest - Virtual Network Request is Null   * 400 NullVirtualNetworkRequestParameters - Virtual Network Request Parameters are Null   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 OperationIdNotFound - The operation with Id does not exist.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation. |  -  |

<a id="virtualNetworkRulesGet"></a>
# **virtualNetworkRulesGet**
> VirtualNetworkRule virtualNetworkRulesGet(resourceGroupName, serverName, subscriptionId, apiVersion, virtualNetworkRuleName)



Gets a virtual network rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule.
    try {
      VirtualNetworkRule result = apiInstance.virtualNetworkRulesGet(resourceGroupName, serverName, subscriptionId, apiVersion, virtualNetworkRuleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesGet");
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
| **virtualNetworkRuleName** | **String**| The name of the virtual network rule. | |

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved a specified virtual network rule. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="virtualNetworkRulesListByServer"></a>
# **virtualNetworkRulesListByServer**
> VirtualNetworkRuleListResult virtualNetworkRulesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of virtual network rules in a server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkRulesApi apiInstance = new VirtualNetworkRulesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      VirtualNetworkRuleListResult result = apiInstance.virtualNetworkRulesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkRulesApi#virtualNetworkRulesListByServer");
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

[**VirtualNetworkRuleListResult**](VirtualNetworkRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of virtual network rules. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

