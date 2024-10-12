# CloudEndpointResourceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudEndpointsCreate**](CloudEndpointResourceApi.md#cloudEndpointsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName} |  |
| [**cloudEndpointsDelete**](CloudEndpointResourceApi.md#cloudEndpointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName} |  |
| [**cloudEndpointsGet**](CloudEndpointResourceApi.md#cloudEndpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName} |  |
| [**cloudEndpointsListBySyncGroup**](CloudEndpointResourceApi.md#cloudEndpointsListBySyncGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints |  |
| [**cloudEndpointsPostBackup**](CloudEndpointResourceApi.md#cloudEndpointsPostBackup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/postbackup |  |
| [**cloudEndpointsPostRestore**](CloudEndpointResourceApi.md#cloudEndpointsPostRestore) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/postrestore |  |
| [**cloudEndpointsPreBackup**](CloudEndpointResourceApi.md#cloudEndpointsPreBackup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/prebackup |  |
| [**cloudEndpointsPreRestore**](CloudEndpointResourceApi.md#cloudEndpointsPreRestore) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/prerestore |  |
| [**cloudEndpointsRestoreheartbeat**](CloudEndpointResourceApi.md#cloudEndpointsRestoreheartbeat) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/restoreheartbeat |  |


<a id="cloudEndpointsCreate"></a>
# **cloudEndpointsCreate**
> CloudEndpoint cloudEndpointsCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Create a new CloudEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    CloudEndpointCreateParameters parameters = new CloudEndpointCreateParameters(); // CloudEndpointCreateParameters | Body of Cloud Endpoint resource.
    try {
      CloudEndpoint result = apiInstance.cloudEndpointsCreate(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsCreate");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |
| **parameters** | [**CloudEndpointCreateParameters**](CloudEndpointCreateParameters.md)| Body of Cloud Endpoint resource. | |

### Return type

[**CloudEndpoint**](CloudEndpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cloud Endpoint object |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **202** | Asynchronous Operation Status Location |  * Retry-After - Retry After <br>  * Azure-AsyncOperation - Operation Status Location URI <br>  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="cloudEndpointsDelete"></a>
# **cloudEndpointsDelete**
> cloudEndpointsDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName)



Delete a given CloudEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    try {
      apiInstance.cloudEndpointsDelete(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsDelete");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |

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
| **202** | Asynchronous Operation Status Location |  * Retry-After - Retry After <br>  * Azure-AsyncOperation - Operation Status Location URI <br>  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **204** | Resource doesn&#39;t exist |  -  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="cloudEndpointsGet"></a>
# **cloudEndpointsGet**
> CloudEndpoint cloudEndpointsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName)



Get a given CloudEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    try {
      CloudEndpoint result = apiInstance.cloudEndpointsGet(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsGet");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |

### Return type

[**CloudEndpoint**](CloudEndpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Cloud Endpoint object |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="cloudEndpointsListBySyncGroup"></a>
# **cloudEndpointsListBySyncGroup**
> CloudEndpointArray cloudEndpointsListBySyncGroup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName)



Get a CloudEndpoint List.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    try {
      CloudEndpointArray result = apiInstance.cloudEndpointsListBySyncGroup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsListBySyncGroup");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |

### Return type

[**CloudEndpointArray**](CloudEndpointArray.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of Cloud Endpoint resources in Sync Group |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="cloudEndpointsPostBackup"></a>
# **cloudEndpointsPostBackup**
> PostBackupResponse cloudEndpointsPostBackup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Post Backup a given CloudEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    BackupRequest parameters = new BackupRequest(); // BackupRequest | Body of Backup request.
    try {
      PostBackupResponse result = apiInstance.cloudEndpointsPostBackup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsPostBackup");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |
| **parameters** | [**BackupRequest**](BackupRequest.md)| Body of Backup request. | |

### Return type

[**PostBackupResponse**](PostBackupResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **202** | Asynchronous Operation Status Location |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="cloudEndpointsPostRestore"></a>
# **cloudEndpointsPostRestore**
> cloudEndpointsPostRestore(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Post Restore a given CloudEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    PostRestoreRequest parameters = new PostRestoreRequest(); // PostRestoreRequest | Body of Cloud Endpoint object.
    try {
      apiInstance.cloudEndpointsPostRestore(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsPostRestore");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |
| **parameters** | [**PostRestoreRequest**](PostRestoreRequest.md)| Body of Cloud Endpoint object. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **202** | Asynchronous Operation Status Location |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="cloudEndpointsPreBackup"></a>
# **cloudEndpointsPreBackup**
> cloudEndpointsPreBackup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Pre Backup a given CloudEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    BackupRequest parameters = new BackupRequest(); // BackupRequest | Body of Backup request.
    try {
      apiInstance.cloudEndpointsPreBackup(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsPreBackup");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |
| **parameters** | [**BackupRequest**](BackupRequest.md)| Body of Backup request. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **202** | Asynchronous Operation Status Location |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="cloudEndpointsPreRestore"></a>
# **cloudEndpointsPreRestore**
> cloudEndpointsPreRestore(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters)



Pre Restore a given CloudEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    PreRestoreRequest parameters = new PreRestoreRequest(); // PreRestoreRequest | Body of Cloud Endpoint object.
    try {
      apiInstance.cloudEndpointsPreRestore(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsPreRestore");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |
| **parameters** | [**PreRestoreRequest**](PreRestoreRequest.md)| Body of Cloud Endpoint object. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **202** | Asynchronous Operation Status Location |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  * Location - Operation Status Location URI <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

<a id="cloudEndpointsRestoreheartbeat"></a>
# **cloudEndpointsRestoreheartbeat**
> cloudEndpointsRestoreheartbeat(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName)



Restore Heartbeat a given CloudEndpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudEndpointResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudEndpointResourceApi apiInstance = new CloudEndpointResourceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String storageSyncServiceName = "storageSyncServiceName_example"; // String | Name of Storage Sync Service resource.
    String syncGroupName = "syncGroupName_example"; // String | Name of Sync Group resource.
    String cloudEndpointName = "cloudEndpointName_example"; // String | Name of Cloud Endpoint object.
    try {
      apiInstance.cloudEndpointsRestoreheartbeat(subscriptionId, resourceGroupName, apiVersion, storageSyncServiceName, syncGroupName, cloudEndpointName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudEndpointResourceApi#cloudEndpointsRestoreheartbeat");
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
| **syncGroupName** | **String**| Name of Sync Group resource. | |
| **cloudEndpointName** | **String**| Name of Cloud Endpoint object. | |

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
| **200** | Restore Heartbeat Operation has ran successfully. |  * x-ms-request-id - request id. <br>  * x-ms-correlation-request-id - correlation request id. <br>  |
| **0** | Error message indicating why the operation failed. |  -  |

