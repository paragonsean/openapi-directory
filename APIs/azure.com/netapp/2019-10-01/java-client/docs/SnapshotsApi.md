# SnapshotsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**snapshotsCreate**](SnapshotsApi.md#snapshotsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots/{snapshotName} | Create a snapshot |
| [**snapshotsDelete**](SnapshotsApi.md#snapshotsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots/{snapshotName} | Delete a snapshot |
| [**snapshotsGet**](SnapshotsApi.md#snapshotsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots/{snapshotName} | Describe a snapshot |
| [**snapshotsList**](SnapshotsApi.md#snapshotsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots | Describe all snapshots |
| [**snapshotsUpdate**](SnapshotsApi.md#snapshotsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName}/snapshots/{snapshotName} | Update a snapshot |


<a id="snapshotsCreate"></a>
# **snapshotsCreate**
> Snapshot snapshotsCreate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, body)

Create a snapshot

Create the specified snapshot within the given volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String snapshotName = "snapshotName_example"; // String | The name of the mount target
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    Snapshot body = new Snapshot(); // Snapshot | Snapshot object supplied in the body of the operation.
    try {
      Snapshot result = apiInstance.snapshotsCreate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#snapshotsCreate");
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
| **snapshotName** | **String**| The name of the mount target | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |
| **body** | [**Snapshot**](Snapshot.md)| Snapshot object supplied in the body of the operation. | |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Snapshot created |  -  |
| **202** | Accepted -- Create request accepted; operation will complete asynchronously |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="snapshotsDelete"></a>
# **snapshotsDelete**
> snapshotsDelete(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion)

Delete a snapshot

Delete snapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String snapshotName = "snapshotName_example"; // String | The name of the mount target
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.snapshotsDelete(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#snapshotsDelete");
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
| **snapshotName** | **String**| The name of the mount target | |
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
| **200** | OK |  -  |
| **202** | Accepted -- Create, update or delete request accepted; operation will complete asynchronously |  -  |
| **204** | NoContent -- Resource does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="snapshotsGet"></a>
# **snapshotsGet**
> Snapshot snapshotsGet(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion)

Describe a snapshot

Get details of the specified snapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String snapshotName = "snapshotName_example"; // String | The name of the mount target
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      Snapshot result = apiInstance.snapshotsGet(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#snapshotsGet");
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
| **snapshotName** | **String**| The name of the mount target | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |

### Return type

[**Snapshot**](Snapshot.md)

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

<a id="snapshotsList"></a>
# **snapshotsList**
> SnapshotsList snapshotsList(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)

Describe all snapshots

List all snapshots associated with the volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    try {
      SnapshotsList result = apiInstance.snapshotsList(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#snapshotsList");
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

[**SnapshotsList**](SnapshotsList.md)

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

<a id="snapshotsUpdate"></a>
# **snapshotsUpdate**
> Snapshot snapshotsUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, body)

Update a snapshot

Patch a snapshot

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SnapshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SnapshotsApi apiInstance = new SnapshotsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String snapshotName = "snapshotName_example"; // String | The name of the mount target
    String apiVersion = "2019-10-01"; // String | Version of the API to be used with the client request.
    SnapshotPatch body = new SnapshotPatch(); // SnapshotPatch | Snapshot object supplied in the body of the operation.
    try {
      Snapshot result = apiInstance.snapshotsUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, snapshotName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SnapshotsApi#snapshotsUpdate");
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
| **snapshotName** | **String**| The name of the mount target | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2019-10-01] |
| **body** | [**SnapshotPatch**](SnapshotPatch.md)| Snapshot object supplied in the body of the operation. | |

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted -- Update request accepted; operation will complete asynchronously |  -  |
| **0** | Error response describing why the operation failed. |  -  |

