# PrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateEndpointConnectionsCreateOrUpdate**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsDelete**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsGet**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsListByPrivateLinkScope**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsListByPrivateLinkScope) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateEndpointConnections |  |


<a id="privateEndpointConnectionsCreateOrUpdate"></a>
# **privateEndpointConnectionsCreateOrUpdate**
> PrivateEndpointConnection privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName, parameters)



Approve or reject a private endpoint connection with a given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateEndpointConnectionsApi apiInstance = new PrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
    PrivateEndpointConnection parameters = new PrivateEndpointConnection(); // PrivateEndpointConnection | 
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateEndpointConnectionsApi#privateEndpointConnectionsCreateOrUpdate");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |
| **privateEndpointConnectionName** | **String**| The name of the private endpoint connection. | |
| **parameters** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)|  | |

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully approved or rejected private endpoint connection. |  -  |
| **202** | Accepted |  -  |

<a id="privateEndpointConnectionsDelete"></a>
# **privateEndpointConnectionsDelete**
> privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName)



Deletes a private endpoint connection with a given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateEndpointConnectionsApi apiInstance = new PrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
    try {
      apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateEndpointConnectionsApi#privateEndpointConnectionsDelete");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |
| **privateEndpointConnectionName** | **String**| The name of the private endpoint connection. | |

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
| **200** | Successfully deleted private endpoint connection. |  -  |
| **202** | Accepted |  -  |
| **204** | Private endpoint connection does not exist. |  -  |

<a id="privateEndpointConnectionsGet"></a>
# **privateEndpointConnectionsGet**
> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName)



Gets a private endpoint connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateEndpointConnectionsApi apiInstance = new PrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateEndpointConnectionsApi#privateEndpointConnectionsGet");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |
| **privateEndpointConnectionName** | **String**| The name of the private endpoint connection. | |

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved a specified private endpoint connection. |  -  |

<a id="privateEndpointConnectionsListByPrivateLinkScope"></a>
# **privateEndpointConnectionsListByPrivateLinkScope**
> PrivateEndpointConnectionListResult privateEndpointConnectionsListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName)



Gets all private endpoint connections on a private link scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrivateEndpointConnectionsApi apiInstance = new PrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
    try {
      PrivateEndpointConnectionListResult result = apiInstance.privateEndpointConnectionsListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateEndpointConnectionsApi#privateEndpointConnectionsListByPrivateLinkScope");
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
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | |

### Return type

[**PrivateEndpointConnectionListResult**](PrivateEndpointConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved private endpoint connections. |  -  |

