# VolumesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**volumesCreateOrUpdate**](VolumesApi.md#volumesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName} |  |
| [**volumesDelete**](VolumesApi.md#volumesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName} |  |
| [**volumesGet**](VolumesApi.md#volumesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName} |  |
| [**volumesList**](VolumesApi.md#volumesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes |  |
| [**volumesUpdate**](VolumesApi.md#volumesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetApp/netAppAccounts/{accountName}/capacityPools/{poolName}/volumes/{volumeName} |  |


<a id="volumesCreateOrUpdate"></a>
# **volumesCreateOrUpdate**
> Volume volumesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body)



Create or update a volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    Volume body = new Volume(); // Volume | Volume object supplied in the body of the operation.
    try {
      Volume result = apiInstance.volumesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesCreateOrUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |
| **body** | [**Volume**](Volume.md)| Volume object supplied in the body of the operation. | |

### Return type

[**Volume**](Volume.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok - volume updated |  -  |
| **201** | Volume created |  -  |
| **202** | Accepted -- Create request accepted; operation will complete asynchronously |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="volumesDelete"></a>
# **volumesDelete**
> volumesDelete(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)



Delete a volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    try {
      apiInstance.volumesDelete(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesDelete");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |

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
| **202** | Accepted -- Create or update request accepted; operation will complete asynchronously |  -  |
| **204** | NoContent -- Resource does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="volumesGet"></a>
# **volumesGet**
> Volume volumesGet(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion)



Get a volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    try {
      Volume result = apiInstance.volumesGet(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |

### Return type

[**Volume**](Volume.md)

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

<a id="volumesList"></a>
# **volumesList**
> VolumeList volumesList(subscriptionId, resourceGroupName, accountName, poolName, apiVersion)



List volumes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    try {
      VolumeList result = apiInstance.volumesList(subscriptionId, resourceGroupName, accountName, poolName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |

### Return type

[**VolumeList**](VolumeList.md)

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

<a id="volumesUpdate"></a>
# **volumesUpdate**
> Volume volumesUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body)



Patch a volume

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String accountName = "accountName_example"; // String | The name of the NetApp account
    String poolName = "poolName_example"; // String | The name of the capacity pool
    String volumeName = "volumeName_example"; // String | The name of the volume
    String apiVersion = "2017-08-15"; // String | Version of the API to be used with the client request.
    VolumePatch body = new VolumePatch(); // VolumePatch | Volume object supplied in the body of the operation.
    try {
      Volume result = apiInstance.volumesUpdate(subscriptionId, resourceGroupName, accountName, poolName, volumeName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#volumesUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | [default to 2017-08-15] |
| **body** | [**VolumePatch**](VolumePatch.md)| Volume object supplied in the body of the operation. | |

### Return type

[**Volume**](Volume.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

