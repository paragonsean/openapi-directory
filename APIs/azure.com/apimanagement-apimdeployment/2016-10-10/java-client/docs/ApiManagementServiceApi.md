# ApiManagementServiceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiManagementServicesApplyNetworkConfigurationUpdates**](ApiManagementServiceApi.md#apiManagementServicesApplyNetworkConfigurationUpdates) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/applynetworkconfigurationupdates |  |
| [**apiManagementServicesBackup**](ApiManagementServiceApi.md#apiManagementServicesBackup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/backup |  |
| [**apiManagementServicesCheckNameAvailability**](ApiManagementServiceApi.md#apiManagementServicesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.ApiManagement/checkNameAvailability |  |
| [**apiManagementServicesCreateOrUpdate**](ApiManagementServiceApi.md#apiManagementServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName} |  |
| [**apiManagementServicesDelete**](ApiManagementServiceApi.md#apiManagementServicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName} |  |
| [**apiManagementServicesGet**](ApiManagementServiceApi.md#apiManagementServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName} |  |
| [**apiManagementServicesGetSsoToken**](ApiManagementServiceApi.md#apiManagementServicesGetSsoToken) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/getssotoken |  |
| [**apiManagementServicesList**](ApiManagementServiceApi.md#apiManagementServicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ApiManagement/service/ |  |
| [**apiManagementServicesListByResourceGroup**](ApiManagementServiceApi.md#apiManagementServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/ |  |
| [**apiManagementServicesManageDeployments**](ApiManagementServiceApi.md#apiManagementServicesManageDeployments) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/managedeployments |  |
| [**apiManagementServicesRestore**](ApiManagementServiceApi.md#apiManagementServicesRestore) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/restore |  |
| [**apiManagementServicesUpdate**](ApiManagementServiceApi.md#apiManagementServicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName} |  |
| [**apiManagementServicesUpdateHostname**](ApiManagementServiceApi.md#apiManagementServicesUpdateHostname) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/updatehostname |  |
| [**apiManagementServicesUploadCertificate**](ApiManagementServiceApi.md#apiManagementServicesUploadCertificate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/uploadcertificate |  |


<a id="apiManagementServicesApplyNetworkConfigurationUpdates"></a>
# **apiManagementServicesApplyNetworkConfigurationUpdates**
> ApiManagementServiceResource apiManagementServicesApplyNetworkConfigurationUpdates(resourceGroupName, serviceName, apiVersion, subscriptionId)



Updates the Microsoft.ApiManagement resource running in the Virtual network to pick the updated network settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApiManagementServiceResource result = apiInstance.apiManagementServicesApplyNetworkConfigurationUpdates(resourceGroupName, serviceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesApplyNetworkConfigurationUpdates");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApiManagementServiceResource**](ApiManagementServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service was successfully updated with new virtual network configurations. |  -  |
| **202** | Accepted: Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesBackup"></a>
# **apiManagementServicesBackup**
> ApiManagementServiceResource apiManagementServicesBackup(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters)



Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiManagementServiceBackupRestoreParameters parameters = new ApiManagementServiceBackupRestoreParameters(); // ApiManagementServiceBackupRestoreParameters | Parameters supplied to the ApiManagementServices_Backup operation.
    try {
      ApiManagementServiceResource result = apiInstance.apiManagementServicesBackup(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesBackup");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiManagementServiceBackupRestoreParameters**](ApiManagementServiceBackupRestoreParameters.md)| Parameters supplied to the ApiManagementServices_Backup operation. | |

### Return type

[**ApiManagementServiceResource**](ApiManagementServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully backed up the API Management service to the storage account. |  -  |
| **202** | Accepted: Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesCheckNameAvailability"></a>
# **apiManagementServicesCheckNameAvailability**
> ApiManagementServiceNameAvailabilityResult apiManagementServicesCheckNameAvailability(apiVersion, subscriptionId, parameters)



Checks availability and correctness of a name for an API Management service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiManagementServiceCheckNameAvailabilityParameters parameters = new ApiManagementServiceCheckNameAvailabilityParameters(); // ApiManagementServiceCheckNameAvailabilityParameters | Parameters supplied to the CheckNameAvailability operation.
    try {
      ApiManagementServiceNameAvailabilityResult result = apiInstance.apiManagementServicesCheckNameAvailability(apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesCheckNameAvailability");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiManagementServiceCheckNameAvailabilityParameters**](ApiManagementServiceCheckNameAvailabilityParameters.md)| Parameters supplied to the CheckNameAvailability operation. | |

### Return type

[**ApiManagementServiceNameAvailabilityResult**](ApiManagementServiceNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The result of check name availability. |  -  |

<a id="apiManagementServicesCreateOrUpdate"></a>
# **apiManagementServicesCreateOrUpdate**
> ApiManagementServiceResource apiManagementServicesCreateOrUpdate(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters)



Creates or updates an API Management service. This is long running operation and could take several minutes to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiManagementServiceResource parameters = new ApiManagementServiceResource(); // ApiManagementServiceResource | Parameters supplied to the CreateOrUpdate API Management service operation.
    try {
      ApiManagementServiceResource result = apiInstance.apiManagementServicesCreateOrUpdate(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiManagementServiceResource**](ApiManagementServiceResource.md)| Parameters supplied to the CreateOrUpdate API Management service operation. | |

### Return type

[**ApiManagementServiceResource**](ApiManagementServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The service was successfully set up. |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesDelete"></a>
# **apiManagementServicesDelete**
> apiManagementServicesDelete(resourceGroupName, serviceName, apiVersion, subscriptionId)



Deletes an existing API Management service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.apiManagementServicesDelete(resourceGroupName, serviceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | Service was successfully deleted. |  -  |
| **204** | Service is already deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesGet"></a>
# **apiManagementServicesGet**
> ApiManagementServiceResource apiManagementServicesGet(resourceGroupName, serviceName, apiVersion, subscriptionId)



Gets an API Management service resource description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApiManagementServiceResource result = apiInstance.apiManagementServicesGet(resourceGroupName, serviceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApiManagementServiceResource**](ApiManagementServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully got the API Management Service Resource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesGetSsoToken"></a>
# **apiManagementServicesGetSsoToken**
> ApiManagementServiceGetSsoTokenResult apiManagementServicesGetSsoToken(resourceGroupName, serviceName, apiVersion, subscriptionId)



Gets the Single-Sign-On token for the API Management Service which is valid for 5 Minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApiManagementServiceGetSsoTokenResult result = apiInstance.apiManagementServicesGetSsoToken(resourceGroupName, serviceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesGetSsoToken");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApiManagementServiceGetSsoTokenResult**](ApiManagementServiceGetSsoTokenResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK if successful with the SSO Redirect URI. |  -  |

<a id="apiManagementServicesList"></a>
# **apiManagementServicesList**
> ApiManagementServiceListResult apiManagementServicesList(apiVersion, subscriptionId)



Lists all API Management services within an Azure subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApiManagementServiceListResult result = apiInstance.apiManagementServicesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApiManagementServiceListResult**](ApiManagementServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The API Management service list. |  -  |

<a id="apiManagementServicesListByResourceGroup"></a>
# **apiManagementServicesListByResourceGroup**
> ApiManagementServiceListResult apiManagementServicesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



List all API Management services within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ApiManagementServiceListResult result = apiInstance.apiManagementServicesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ApiManagementServiceListResult**](ApiManagementServiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The API Management service list. |  -  |

<a id="apiManagementServicesManageDeployments"></a>
# **apiManagementServicesManageDeployments**
> ApiManagementServiceResource apiManagementServicesManageDeployments(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters)



Manages deployments of an API Management service. This operation can be used to do the following: Change SKU, Change SKU Units, Change Service Tier (Developer/Standard/Premium) and Manage VPN Configuration. This is a long running operation and can take several minutes to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiManagementServiceManageDeploymentsParameters parameters = new ApiManagementServiceManageDeploymentsParameters(); // ApiManagementServiceManageDeploymentsParameters | Parameters supplied to the ManageDeployments operation.
    try {
      ApiManagementServiceResource result = apiInstance.apiManagementServicesManageDeployments(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesManageDeployments");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiManagementServiceManageDeploymentsParameters**](ApiManagementServiceManageDeploymentsParameters.md)| Parameters supplied to the ManageDeployments operation. | |

### Return type

[**ApiManagementServiceResource**](ApiManagementServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully applied the new deployment Configuration on the API Management service. |  -  |
| **202** | Accepted. The location header contains the URL where the status of the long running operation can be checked.The response also includes the unmodified ApiManagementServiceResource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesRestore"></a>
# **apiManagementServicesRestore**
> ApiManagementServiceResource apiManagementServicesRestore(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters)



Restores a backup of an API Management service created using the ApiManagementServices_Backup operation on the current service. This is a long running operation and could take several minutes to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiManagementServiceBackupRestoreParameters parameters = new ApiManagementServiceBackupRestoreParameters(); // ApiManagementServiceBackupRestoreParameters | Parameters supplied to the Restore API Management service from backup operation.
    try {
      ApiManagementServiceResource result = apiInstance.apiManagementServicesRestore(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesRestore");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiManagementServiceBackupRestoreParameters**](ApiManagementServiceBackupRestoreParameters.md)| Parameters supplied to the Restore API Management service from backup operation. | |

### Return type

[**ApiManagementServiceResource**](ApiManagementServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully restored the backup onto the API Management service. |  -  |
| **202** | Accepted: Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesUpdate"></a>
# **apiManagementServicesUpdate**
> ApiManagementServiceResource apiManagementServicesUpdate(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters)



Updates an existing API Management service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiManagementServiceUpdateParameters parameters = new ApiManagementServiceUpdateParameters(); // ApiManagementServiceUpdateParameters | Parameters supplied to the CreateOrUpdate API Management service operation.
    try {
      ApiManagementServiceResource result = apiInstance.apiManagementServicesUpdate(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiManagementServiceUpdateParameters**](ApiManagementServiceUpdateParameters.md)| Parameters supplied to the CreateOrUpdate API Management service operation. | |

### Return type

[**ApiManagementServiceResource**](ApiManagementServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the current API Management service. |  -  |
| **202** | Accepted: Location header contains the URL where the status of the long running operation can be checked. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesUpdateHostname"></a>
# **apiManagementServicesUpdateHostname**
> ApiManagementServiceResource apiManagementServicesUpdateHostname(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters)



Creates, updates, or deletes the custom hostnames for an API Management service. The custom hostname can be applied to the Proxy and Portal endpoint. This is a long running operation and could take several minutes to complete.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiManagementServiceUpdateHostnameParameters parameters = new ApiManagementServiceUpdateHostnameParameters(); // ApiManagementServiceUpdateHostnameParameters | Parameters supplied to the UpdateHostname operation.
    try {
      ApiManagementServiceResource result = apiInstance.apiManagementServicesUpdateHostname(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesUpdateHostname");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiManagementServiceUpdateHostnameParameters**](ApiManagementServiceUpdateHostnameParameters.md)| Parameters supplied to the UpdateHostname operation. | |

### Return type

[**ApiManagementServiceResource**](ApiManagementServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Service was successfully updated with desired hostnames. |  -  |
| **202** | Accepted. The location header contains the URL where the status of the long running operation can be checked. The response also includes the unmodified ApiManagementServiceResource. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="apiManagementServicesUploadCertificate"></a>
# **apiManagementServicesUploadCertificate**
> CertificateInformation apiManagementServicesUploadCertificate(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters)



Upload Custom Domain SSL certificate for an API Management service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiManagementServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApiManagementServiceApi apiInstance = new ApiManagementServiceApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String serviceName = "serviceName_example"; // String | The name of the API Management service.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ApiManagementServiceUploadCertificateParameters parameters = new ApiManagementServiceUploadCertificateParameters(); // ApiManagementServiceUploadCertificateParameters | Parameters supplied to the Upload SSL certificate for an API Management service operation.
    try {
      CertificateInformation result = apiInstance.apiManagementServicesUploadCertificate(resourceGroupName, serviceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiManagementServiceApi#apiManagementServicesUploadCertificate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **serviceName** | **String**| The name of the API Management service. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ApiManagementServiceUploadCertificateParameters**](ApiManagementServiceUploadCertificateParameters.md)| Parameters supplied to the Upload SSL certificate for an API Management service operation. | |

### Return type

[**CertificateInformation**](CertificateInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully uploaded certificate to the API Management Service. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

