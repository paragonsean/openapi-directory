# HybridConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hybridConnectionsCreateOrUpdate**](HybridConnectionsApi.md#hybridConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName} |  |
| [**hybridConnectionsCreateOrUpdateAuthorizationRule**](HybridConnectionsApi.md#hybridConnectionsCreateOrUpdateAuthorizationRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName}/authorizationRules/{authorizationRuleName} |  |
| [**hybridConnectionsDelete**](HybridConnectionsApi.md#hybridConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName} |  |
| [**hybridConnectionsDeleteAuthorizationRule**](HybridConnectionsApi.md#hybridConnectionsDeleteAuthorizationRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName}/authorizationRules/{authorizationRuleName} |  |
| [**hybridConnectionsGet**](HybridConnectionsApi.md#hybridConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName} |  |
| [**hybridConnectionsGetAuthorizationRule**](HybridConnectionsApi.md#hybridConnectionsGetAuthorizationRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName}/authorizationRules/{authorizationRuleName} |  |
| [**hybridConnectionsListAuthorizationRules**](HybridConnectionsApi.md#hybridConnectionsListAuthorizationRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName}/authorizationRules |  |
| [**hybridConnectionsListByNamespace**](HybridConnectionsApi.md#hybridConnectionsListByNamespace) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections |  |
| [**hybridConnectionsListKeys**](HybridConnectionsApi.md#hybridConnectionsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName}/authorizationRules/{authorizationRuleName}/ListKeys |  |
| [**hybridConnectionsListPostAuthorizationRules**](HybridConnectionsApi.md#hybridConnectionsListPostAuthorizationRules) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName}/authorizationRules |  |
| [**hybridConnectionsPostAuthorizationRule**](HybridConnectionsApi.md#hybridConnectionsPostAuthorizationRule) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName}/authorizationRules/{authorizationRuleName} |  |
| [**hybridConnectionsRegenerateKeys**](HybridConnectionsApi.md#hybridConnectionsRegenerateKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Relay/namespaces/{namespaceName}/HybridConnections/{hybridConnectionName}/authorizationRules/{authorizationRuleName}/regenerateKeys |  |


<a id="hybridConnectionsCreateOrUpdate"></a>
# **hybridConnectionsCreateOrUpdate**
> HybridConnection hybridConnectionsCreateOrUpdate(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId, parameters)



Creates or Updates a service HybridConnection. This operation is idempotent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    HybridConnection parameters = new HybridConnection(); // HybridConnection | Parameters supplied to create a HybridConnection.
    try {
      HybridConnection result = apiInstance.hybridConnectionsCreateOrUpdate(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsCreateOrUpdate");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**HybridConnection**](HybridConnection.md)| Parameters supplied to create a HybridConnection. | |

### Return type

[**HybridConnection**](HybridConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to Create Hybrid Connections succeeded |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsCreateOrUpdateAuthorizationRule"></a>
# **hybridConnectionsCreateOrUpdateAuthorizationRule**
> AuthorizationRule hybridConnectionsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Creates or Updates an authorization rule for a HybridConnection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    AuthorizationRule parameters = new AuthorizationRule(); // AuthorizationRule | The authorization rule parameters
    try {
      AuthorizationRule result = apiInstance.hybridConnectionsCreateOrUpdateAuthorizationRule(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsCreateOrUpdateAuthorizationRule");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**AuthorizationRule**](AuthorizationRule.md)| The authorization rule parameters | |

### Return type

[**AuthorizationRule**](AuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HybridConnection Authorization rule created |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsDelete"></a>
# **hybridConnectionsDelete**
> hybridConnectionsDelete(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId)



Deletes a HybridConnection .

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.hybridConnectionsDelete(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsDelete");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **apiVersion** | **String**| Client Api Version. | |
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
| **200** | Request to delete Hybrid Connections succeeded. |  -  |
| **204** | No Content. The request has been accepted but the Hybrid Connections was not found. |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsDeleteAuthorizationRule"></a>
# **hybridConnectionsDeleteAuthorizationRule**
> hybridConnectionsDeleteAuthorizationRule(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId)



Deletes a HybridConnection authorization rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.hybridConnectionsDeleteAuthorizationRule(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsDeleteAuthorizationRule");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
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
| **200** | HybridConnection authorizationRule deleted |  -  |
| **204** | Authorization rule does not exist |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsGet"></a>
# **hybridConnectionsGet**
> HybridConnection hybridConnectionsGet(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId)



Returns the description for the specified HybridConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      HybridConnection result = apiInstance.hybridConnectionsGet(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsGet");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**HybridConnection**](HybridConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved hybridConnection description |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsGetAuthorizationRule"></a>
# **hybridConnectionsGetAuthorizationRule**
> AuthorizationRule hybridConnectionsGetAuthorizationRule(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId)



HybridConnection authorizationRule for a HybridConnection by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRule result = apiInstance.hybridConnectionsGetAuthorizationRule(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsGetAuthorizationRule");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRule**](AuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HybridConnection AuthorizationRule returned successfully |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsListAuthorizationRules"></a>
# **hybridConnectionsListAuthorizationRules**
> AuthorizationRuleListResult hybridConnectionsListAuthorizationRules(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId)



Authorization rules for a HybridConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRuleListResult result = apiInstance.hybridConnectionsListAuthorizationRules(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsListAuthorizationRules");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRuleListResult**](AuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization rules successfully returned. |  -  |

<a id="hybridConnectionsListByNamespace"></a>
# **hybridConnectionsListByNamespace**
> HybridConnectionListResult hybridConnectionsListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId)



Lists the HybridConnection within the namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      HybridConnectionListResult result = apiInstance.hybridConnectionsListByNamespace(resourceGroupName, namespaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsListByNamespace");
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
| **namespaceName** | **String**| The Namespace Name | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**HybridConnectionListResult**](HybridConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to retrieve HybridConnections by NameSpace succeeded |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsListKeys"></a>
# **hybridConnectionsListKeys**
> AuthorizationRuleKeys hybridConnectionsListKeys(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId)



Primary and Secondary ConnectionStrings to the HybridConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRuleKeys result = apiInstance.hybridConnectionsListKeys(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsListKeys");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRuleKeys**](AuthorizationRuleKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to retirve ConnectionStrings to the HybridConnection succeeded |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsListPostAuthorizationRules"></a>
# **hybridConnectionsListPostAuthorizationRules**
> AuthorizationRuleListResult hybridConnectionsListPostAuthorizationRules(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId)



Authorization rules for a HybridConnection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRuleListResult result = apiInstance.hybridConnectionsListPostAuthorizationRules(resourceGroupName, namespaceName, hybridConnectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsListPostAuthorizationRules");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRuleListResult**](AuthorizationRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization rules successfully returned. |  -  |

<a id="hybridConnectionsPostAuthorizationRule"></a>
# **hybridConnectionsPostAuthorizationRule**
> AuthorizationRule hybridConnectionsPostAuthorizationRule(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId)



HybridConnection authorizationRule for a HybridConnection by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AuthorizationRule result = apiInstance.hybridConnectionsPostAuthorizationRule(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsPostAuthorizationRule");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AuthorizationRule**](AuthorizationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | HybridConnection AuthorizationRule returned successfully |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

<a id="hybridConnectionsRegenerateKeys"></a>
# **hybridConnectionsRegenerateKeys**
> AuthorizationRuleKeys hybridConnectionsRegenerateKeys(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId, parameters)



Regenerates the Primary or Secondary ConnectionStrings to the HybridConnection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridConnectionsApi apiInstance = new HybridConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String namespaceName = "namespaceName_example"; // String | The Namespace Name
    String hybridConnectionName = "hybridConnectionName_example"; // String | The hybrid connection name.
    String authorizationRuleName = "authorizationRuleName_example"; // String | The authorizationRule name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    RegenerateKeysParameters parameters = new RegenerateKeysParameters(); // RegenerateKeysParameters | Parameters supplied to regenerate Auth Rule.
    try {
      AuthorizationRuleKeys result = apiInstance.hybridConnectionsRegenerateKeys(resourceGroupName, namespaceName, hybridConnectionName, authorizationRuleName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridConnectionsApi#hybridConnectionsRegenerateKeys");
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
| **namespaceName** | **String**| The Namespace Name | |
| **hybridConnectionName** | **String**| The hybrid connection name. | |
| **authorizationRuleName** | **String**| The authorizationRule name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**RegenerateKeysParameters**](RegenerateKeysParameters.md)| Parameters supplied to regenerate Auth Rule. | |

### Return type

[**AuthorizationRuleKeys**](AuthorizationRuleKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to regenerate ConnectionStrings to HybridConnection succeeded |  -  |
| **0** | Relay error response describing why the operation failed. |  -  |

