# SyncGroupResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**syncGroupsCreate**](SyncGroupResourceApi.md#syncGroupsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName} |  |
| [**syncGroupsDelete**](SyncGroupResourceApi.md#syncGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName} |  |
| [**syncGroupsGet**](SyncGroupResourceApi.md#syncGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName} |  |
| [**syncGroupsListByStorageSyncService**](SyncGroupResourceApi.md#syncGroupsListByStorageSyncService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups |  |


<a id="syncGroupsCreate"></a>
# **syncGroupsCreate**
> SyncGroup syncGroupsCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, parameters)



Create a new SyncGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SyncGroupResourceApi apiInstance = new SyncGroupResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    SyncGroup parameters = new SyncGroup(); // SyncGroup | Sync Group Body
    try {
      SyncGroup result = apiInstance.syncGroupsCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupResourceApi#syncGroupsCreate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **apiVersion** | **String**| Client Api Version. | |
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **parameters** | [**SyncGroup**](SyncGroup.md)| Sync Group Body | |

### Return type

[**SyncGroup**](SyncGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sync Group object |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="syncGroupsDelete"></a>
# **syncGroupsDelete**
> syncGroupsDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName)



Delete a given SyncGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SyncGroupResourceApi apiInstance = new SyncGroupResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    try {
      apiInstance.syncGroupsDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupResourceApi#syncGroupsDelete");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **apiVersion** | **String**| Client Api Version. | |
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |
| **syncGroupName** | **String**| Name of Sync Group resource. | |

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
| **200** | Sync Group object was deleted |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **204** | Resource doesn&#39;t exist |  -  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="syncGroupsGet"></a>
# **syncGroupsGet**
> SyncGroup syncGroupsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName)



Get a given SyncGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SyncGroupResourceApi apiInstance = new SyncGroupResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    try {
      SyncGroup result = apiInstance.syncGroupsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupResourceApi#syncGroupsGet");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **apiVersion** | **String**| Client Api Version. | |
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |
| **syncGroupName** | **String**| Name of Sync Group resource. | |

### Return type

[**SyncGroup**](SyncGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sync Group object |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="syncGroupsListByStorageSyncService"></a>
# **syncGroupsListByStorageSyncService**
> SyncGroupArray syncGroupsListByStorageSyncService(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName)



Get a SyncGroup List.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyncGroupResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SyncGroupResourceApi apiInstance = new SyncGroupResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    try {
      SyncGroupArray result = apiInstance.syncGroupsListByStorageSyncService(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyncGroupResourceApi#syncGroupsListByStorageSyncService");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **apiVersion** | **String**| Client Api Version. | |
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |

### Return type

[**SyncGroupArray**](SyncGroupArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of Sync Group resources in Storage Sync Service |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

