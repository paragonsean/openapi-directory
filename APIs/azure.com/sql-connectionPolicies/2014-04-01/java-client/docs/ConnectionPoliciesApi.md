# ConnectionPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverConnectionPoliciesCreateOrUpdate**](ConnectionPoliciesApi.md#serverConnectionPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/connectionPolicies/{connectionPolicyName} |  |
| [**serverConnectionPoliciesGet**](ConnectionPoliciesApi.md#serverConnectionPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/connectionPolicies/{connectionPolicyName} |  |


<a id="serverConnectionPoliciesCreateOrUpdate"></a>
# **serverConnectionPoliciesCreateOrUpdate**
> ServerConnectionPolicy serverConnectionPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, connectionPolicyName, parameters)



Creates or updates the server&#39;s connection policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ConnectionPoliciesApi apiInstance = new ConnectionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String connectionPolicyName = "default"; // String | The name of the connection policy.
    ServerConnectionPolicy parameters = new ServerConnectionPolicy(); // ServerConnectionPolicy | The required parameters for updating a secure connection policy.
    try {
      ServerConnectionPolicy result = apiInstance.serverConnectionPoliciesCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, connectionPolicyName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionPoliciesApi#serverConnectionPoliciesCreateOrUpdate");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **connectionPolicyName** | **String**| The name of the connection policy. | [enum: default] |
| **parameters** | [**ServerConnectionPolicy**](ServerConnectionPolicy.md)| The required parameters for updating a secure connection policy. | |

### Return type

[**ServerConnectionPolicy**](ServerConnectionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="serverConnectionPoliciesGet"></a>
# **serverConnectionPoliciesGet**
> ServerConnectionPolicy serverConnectionPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, connectionPolicyName)



Gets the server&#39;s secure connection policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ConnectionPoliciesApi apiInstance = new ConnectionPoliciesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String connectionPolicyName = "default"; // String | The name of the connection policy.
    try {
      ServerConnectionPolicy result = apiInstance.serverConnectionPoliciesGet(apiVersion, subscriptionId, resourceGroupName, serverName, connectionPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionPoliciesApi#serverConnectionPoliciesGet");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **connectionPolicyName** | **String**| The name of the connection policy. | [enum: default] |

### Return type

[**ServerConnectionPolicy**](ServerConnectionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

