# PrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateEndpointConnectionsCreateOrUpdate**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsDelete**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsGet**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsListByConfigurationStore**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsListByConfigurationStore) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections |  |


<a id="privateEndpointConnectionsCreateOrUpdate"></a>
# **privateEndpointConnectionsCreateOrUpdate**
> PrivateEndpointConnection privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName, privateEndpointConnection)



Update the state of the specified private endpoint connection associated with the configuration store.

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
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Private endpoint connection name
    PrivateEndpointConnection privateEndpointConnection = new PrivateEndpointConnection(); // PrivateEndpointConnection | The private endpoint connection properties.
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName, privateEndpointConnection);
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **privateEndpointConnectionName** | **String**| Private endpoint connection name | |
| **privateEndpointConnection** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)| The private endpoint connection properties. | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **201** | The request was successfully accepted; the operation will complete asynchronously. The provisioning state of the resource should indicate the current state of the resource. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="privateEndpointConnectionsDelete"></a>
# **privateEndpointConnectionsDelete**
> privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName)



Deletes a private endpoint connection.

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
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Private endpoint connection name
    try {
      apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName);
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **privateEndpointConnectionName** | **String**| Private endpoint connection name | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **202** | The request was successful; the operation will complete asynchronously. |  -  |
| **204** | No Content - the specified resource was not found. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="privateEndpointConnectionsGet"></a>
# **privateEndpointConnectionsGet**
> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName)



Gets the specified private endpoint connection associated with the configuration store.

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
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Private endpoint connection name
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName);
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |
| **privateEndpointConnectionName** | **String**| Private endpoint connection name | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="privateEndpointConnectionsListByConfigurationStore"></a>
# **privateEndpointConnectionsListByConfigurationStore**
> PrivateEndpointConnectionListResult privateEndpointConnectionsListByConfigurationStore(subscriptionId, resourceGroupName, configStoreName, apiVersion)



Lists all private endpoint connections for a configuration store.

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
    String subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
    String configStoreName = "configStoreName_example"; // String | The name of the configuration store.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      PrivateEndpointConnectionListResult result = apiInstance.privateEndpointConnectionsListByConfigurationStore(subscriptionId, resourceGroupName, configStoreName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateEndpointConnectionsApi#privateEndpointConnectionsListByConfigurationStore");
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
| **subscriptionId** | **String**| The Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | |
| **configStoreName** | **String**| The name of the configuration store. | |
| **apiVersion** | **String**| The client API version. | |

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
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed |  -  |

