# RegisteredServerResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registeredServersCreate**](RegisteredServerResourceApi.md#registeredServersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId} |  |
| [**registeredServersDelete**](RegisteredServerResourceApi.md#registeredServersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId} |  |
| [**registeredServersGet**](RegisteredServerResourceApi.md#registeredServersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers/{serverId} |  |
| [**registeredServersListByStorageSyncService**](RegisteredServerResourceApi.md#registeredServersListByStorageSyncService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/registeredServers |  |


<a id="registeredServersCreate"></a>
# **registeredServersCreate**
> RegisteredServer registeredServersCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, serverId, parameters)



Add a new registered server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisteredServerResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegisteredServerResourceApi apiInstance = new RegisteredServerResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String serverId = "serverId_example"; // String | GUID identifying the on-premises server.
    RegisteredServerCreateParameters parameters = new RegisteredServerCreateParameters(); // RegisteredServerCreateParameters | Body of Registered Server object.
    try {
      RegisteredServer result = apiInstance.registeredServersCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, serverId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisteredServerResourceApi#registeredServersCreate");
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
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |
| **serverId** | **String**| GUID identifying the on-premises server. | |
| **parameters** | [**RegisteredServerCreateParameters**](RegisteredServerCreateParameters.md)| Body of Registered Server object. | |

### Return type

[**RegisteredServer**](RegisteredServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registered Server resources in Sync Group |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **202** | Asynchronous Operation Status Location |  * Azure-AsyncOperation - Operation Status Location URI <br>  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="registeredServersDelete"></a>
# **registeredServersDelete**
> registeredServersDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, serverId)



Delete the given registered server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisteredServerResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegisteredServerResourceApi apiInstance = new RegisteredServerResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String serverId = "serverId_example"; // String | GUID identifying the on-premises server.
    try {
      apiInstance.registeredServersDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, serverId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisteredServerResourceApi#registeredServersDelete");
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
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |
| **serverId** | **String**| GUID identifying the on-premises server. | |

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
| **200** | Ok |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **202** | Asynchronous Operation Status Location |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **204** | Resource doesn&#39;t exist |  -  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="registeredServersGet"></a>
# **registeredServersGet**
> RegisteredServer registeredServersGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, serverId)



Get a given registered server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisteredServerResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegisteredServerResourceApi apiInstance = new RegisteredServerResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String serverId = "serverId_example"; // String | GUID identifying the on-premises server.
    try {
      RegisteredServer result = apiInstance.registeredServersGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, serverId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisteredServerResourceApi#registeredServersGet");
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
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |
| **serverId** | **String**| GUID identifying the on-premises server. | |

### Return type

[**RegisteredServer**](RegisteredServer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registered Server resources in Sync Group |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="registeredServersListByStorageSyncService"></a>
# **registeredServersListByStorageSyncService**
> RegisteredServerArray registeredServersListByStorageSyncService(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName)



Get a given registered server list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegisteredServerResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RegisteredServerResourceApi apiInstance = new RegisteredServerResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    try {
      RegisteredServerArray result = apiInstance.registeredServersListByStorageSyncService(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegisteredServerResourceApi#registeredServersListByStorageSyncService");
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
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |

### Return type

[**RegisteredServerArray**](RegisteredServerArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of Registered Server resources in Storage Sync Service |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

