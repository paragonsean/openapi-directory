# StorageSyncServicesResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageSyncServicesCreate**](StorageSyncServicesResourceApi.md#storageSyncServicesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName} |  |
| [**storageSyncServicesDelete**](StorageSyncServicesResourceApi.md#storageSyncServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName} |  |
| [**storageSyncServicesGet**](StorageSyncServicesResourceApi.md#storageSyncServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName} |  |
| [**storageSyncServicesListByResourceGroup**](StorageSyncServicesResourceApi.md#storageSyncServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices |  |
| [**storageSyncServicesListBySubscription**](StorageSyncServicesResourceApi.md#storageSyncServicesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.StorageSync/storageSyncServices |  |
| [**storageSyncServicesUpdate**](StorageSyncServicesResourceApi.md#storageSyncServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName} |  |


<a id="storageSyncServicesCreate"></a>
# **storageSyncServicesCreate**
> StorageSyncService storageSyncServicesCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, parameters)



Create a new StorageSyncService.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageSyncServicesResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageSyncServicesResourceApi apiInstance = new StorageSyncServicesResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    StorageSyncService parameters = new StorageSyncService(); // StorageSyncService | Storage Sync Service resource name.
    try {
      StorageSyncService result = apiInstance.storageSyncServicesCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageSyncServicesResourceApi#storageSyncServicesCreate");
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
| **parameters** | [**StorageSyncService**](StorageSyncService.md)| Storage Sync Service resource name. | |

### Return type

[**StorageSyncService**](StorageSyncService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Storage Sync Service object created/updated |  -  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="storageSyncServicesDelete"></a>
# **storageSyncServicesDelete**
> storageSyncServicesDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName)



Delete a given StorageSyncService.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageSyncServicesResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageSyncServicesResourceApi apiInstance = new StorageSyncServicesResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    try {
      apiInstance.storageSyncServicesDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageSyncServicesResourceApi#storageSyncServicesDelete");
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

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Storage Sync Service object was deleted. |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **204** | Storage Sync Service Resource doesn&#39;t exist |  -  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="storageSyncServicesGet"></a>
# **storageSyncServicesGet**
> StorageSyncService storageSyncServicesGet(subscriptionId, resourceGroupName, storageSyncServiceName, apiVersion)



Get a given StorageSyncService.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageSyncServicesResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageSyncServicesResourceApi apiInstance = new StorageSyncServicesResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      StorageSyncService result = apiInstance.storageSyncServicesGet(subscriptionId, resourceGroupName, storageSyncServiceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageSyncServicesResourceApi#storageSyncServicesGet");
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
| **storageSyncServiceName** | **String**| Name of Storage Sync Service resource. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**StorageSyncService**](StorageSyncService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Storage Sync Service object |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="storageSyncServicesListByResourceGroup"></a>
# **storageSyncServicesListByResourceGroup**
> StorageSyncServiceArray storageSyncServicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Get a StorageSyncService list by Resource group name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageSyncServicesResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageSyncServicesResourceApi apiInstance = new StorageSyncServicesResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      StorageSyncServiceArray result = apiInstance.storageSyncServicesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageSyncServicesResourceApi#storageSyncServicesListByResourceGroup");
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

### Return type

[**StorageSyncServiceArray**](StorageSyncServiceArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of registered Storage Sync Service resources in the Resource Group |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="storageSyncServicesListBySubscription"></a>
# **storageSyncServicesListBySubscription**
> StorageSyncServiceArray storageSyncServicesListBySubscription(subscriptionId, apiVersion)



Get a StorageSyncService list by subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageSyncServicesResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageSyncServicesResourceApi apiInstance = new StorageSyncServicesResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      StorageSyncServiceArray result = apiInstance.storageSyncServicesListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageSyncServicesResourceApi#storageSyncServicesListBySubscription");
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
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**StorageSyncServiceArray**](StorageSyncServiceArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of registered Storage Sync Service resources in the subscription. |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="storageSyncServicesUpdate"></a>
# **storageSyncServicesUpdate**
> StorageSyncService storageSyncServicesUpdate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, parameters)



Patch a given StorageSyncService.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageSyncServicesResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageSyncServicesResourceApi apiInstance = new StorageSyncServicesResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    StorageSyncService parameters = new StorageSyncService(); // StorageSyncService | Storage Sync Service resource.
    try {
      StorageSyncService result = apiInstance.storageSyncServicesUpdate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageSyncServicesResourceApi#storageSyncServicesUpdate");
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
| **parameters** | [**StorageSyncService**](StorageSyncService.md)| Storage Sync Service resource. | [optional] |

### Return type

[**StorageSyncService**](StorageSyncService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Storage Sync Service object created/updated |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

