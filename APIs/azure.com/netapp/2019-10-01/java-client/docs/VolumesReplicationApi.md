# VolumesReplicationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**volumesAuthorizeReplication**](VolumesReplicationApi.md#volumesAuthorizeReplication) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/authorizeReplication | Authorize source volume replication |
| [**volumesBreakReplication**](VolumesReplicationApi.md#volumesBreakReplication) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/breakReplication | Break volume replication |
| [**volumesDeleteReplication**](VolumesReplicationApi.md#volumesDeleteReplication) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/deleteReplication | Delete volume replication |
| [**volumesReplicationStatus**](VolumesReplicationApi.md#volumesReplicationStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/replicationStatus | Get volume replication status |
| [**volumesResyncReplication**](VolumesReplicationApi.md#volumesResyncReplication) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/resyncReplication | Resync volume replication |


<a id="volumesAuthorizeReplication"></a>
# **volumesAuthorizeReplication**
> volumesAuthorizeReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body)

Authorize source volume replication

Authorize the replication connection on the source volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesReplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesReplicationApi apiInstance = new VolumesReplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    AuthorizeRequest body = new AuthorizeRequest(); // AuthorizeRequest | authorize request object supplied in the body of the operation.
    try {
      apiInstance.volumesAuthorizeReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesReplicationApi#volumesAuthorizeReplication");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **volumeName** | **String**| The name of the volume | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |
| **body** | [**AuthorizeRequest**](AuthorizeRequest.md)| authorize request object supplied in the body of the operation. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="volumesBreakReplication"></a>
# **volumesBreakReplication**
> volumesBreakReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Break volume replication

Break the replication connection on the destination volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesReplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesReplicationApi apiInstance = new VolumesReplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.volumesBreakReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesReplicationApi#volumesBreakReplication");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **volumeName** | **String**| The name of the volume | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |

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
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="volumesDeleteReplication"></a>
# **volumesDeleteReplication**
> volumesDeleteReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Delete volume replication

Delete the replication connection on the destination volume, and send release to the source replication

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesReplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesReplicationApi apiInstance = new VolumesReplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.volumesDeleteReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesReplicationApi#volumesDeleteReplication");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **volumeName** | **String**| The name of the volume | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |

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
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="volumesReplicationStatus"></a>
# **volumesReplicationStatus**
> ReplicationStatus volumesReplicationStatus(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Get volume replication status

Get the status of the replication

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesReplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesReplicationApi apiInstance = new VolumesReplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      ReplicationStatus result = apiInstance.volumesReplicationStatus(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesReplicationApi#volumesReplicationStatus");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **volumeName** | **String**| The name of the volume | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |

### Return type

[**ReplicationStatus**](ReplicationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="volumesResyncReplication"></a>
# **volumesResyncReplication**
> volumesResyncReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Resync volume replication

Resync the connection on the destination volume. If the operation is ran on the source volume it will reverse-resync the connection and sync from source to destination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesReplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesReplicationApi apiInstance = new VolumesReplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.volumesResyncReplication(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesReplicationApi#volumesResyncReplication");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **accountName** | **String**| The name of the NetApp account | |
| **poolName** | **String**| The name of the capacity pool | |
| **volumeName** | **String**| The name of the volume | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |

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
| **202** | Accepted |  -  |
| **0** | Error response describing why the operation failed. |  -  |

