# PrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateEndpointConnectionsDelete**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsGet**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName} |  |
| [**privateEndpointConnectionsPut**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}/privateEndpointConnections/{privateEndpointConnectionName} |  |


<a id="privateEndpointConnectionsDelete"></a>
# **privateEndpointConnectionsDelete**
> PrivateEndpointConnection privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion)



Deletes the specified private endpoint connection associated with the key vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateEndpointConnectionsApi apiInstance = new PrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group that contains the key vault.
    String vaultName = "vaultName_example"; // String | The name of the key vault.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Name of the private endpoint connection associated with the key vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion);
      System.out.println(result);
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group that contains the key vault. | |
| **vaultName** | **String**| The name of the key vault. | |
| **privateEndpointConnectionName** | **String**| Name of the private endpoint connection associated with the key vault. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The private endpoint connection was successfully deleted. |  -  |
| **202** | The private endpoint connection is being deleted. |  * Retry-After - The recommended number of seconds to wait before calling the URI specified in the location header. <br>  * Location - The URI to poll for completion status. <br>  |
| **204** | The private endpoint connection does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateEndpointConnectionsGet"></a>
# **privateEndpointConnectionsGet**
> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion)



Gets the specified private endpoint connection associated with the key vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateEndpointConnectionsApi apiInstance = new PrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group that contains the key vault.
    String vaultName = "vaultName_example"; // String | The name of the key vault.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Name of the private endpoint connection associated with the key vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion);
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group that contains the key vault. | |
| **vaultName** | **String**| The name of the key vault. | |
| **privateEndpointConnectionName** | **String**| Name of the private endpoint connection associated with the key vault. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Private endpoint connection successfully returned. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="privateEndpointConnectionsPut"></a>
# **privateEndpointConnectionsPut**
> PrivateEndpointConnection privateEndpointConnectionsPut(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion, properties)



Updates the specified private endpoint connection associated with the key vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateEndpointConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateEndpointConnectionsApi apiInstance = new PrivateEndpointConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group that contains the key vault.
    String vaultName = "vaultName_example"; // String | The name of the key vault.
    String privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Name of the private endpoint connection associated with the key vault.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    PrivateEndpointConnection properties = new PrivateEndpointConnection(); // PrivateEndpointConnection | The intended state of private endpoint connection.
    try {
      PrivateEndpointConnection result = apiInstance.privateEndpointConnectionsPut(subscriptionId, resourceGroupName, vaultName, privateEndpointConnectionName, apiVersion, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateEndpointConnectionsApi#privateEndpointConnectionsPut");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of the resource group that contains the key vault. | |
| **vaultName** | **String**| The name of the key vault. | |
| **privateEndpointConnectionName** | **String**| Name of the private endpoint connection associated with the key vault. | |
| **apiVersion** | **String**| Client Api Version. | |
| **properties** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)| The intended state of private endpoint connection. | |

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The state of private endpoint connection was updated successfully. |  * Retry-After - The recommended number of seconds to wait before calling the URI specified in the location header. <br>  * Azure-AsyncOperation - (specified only if operation does not finish synchronously) The URI to poll for completion status. The response of this URI may be synchronous or asynchronous. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

