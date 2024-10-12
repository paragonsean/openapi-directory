# DisasterRecoveryConfigurationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**disasterRecoveryConfigurationsCreateOrUpdate**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName} |  |
| [**disasterRecoveryConfigurationsDelete**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName} |  |
| [**disasterRecoveryConfigurationsFailover**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsFailover) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName}/failover |  |
| [**disasterRecoveryConfigurationsFailoverAllowDataLoss**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsFailoverAllowDataLoss) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName}/forceFailoverAllowDataLoss |  |
| [**disasterRecoveryConfigurationsGet**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName} |  |
| [**disasterRecoveryConfigurationsList**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration |  |


<a id="disasterRecoveryConfigurationsCreateOrUpdate"></a>
# **disasterRecoveryConfigurationsCreateOrUpdate**
> DisasterRecoveryConfiguration disasterRecoveryConfigurationsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Creates or updates a disaster recovery configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DisasterRecoveryConfigurationsApi apiInstance = new DisasterRecoveryConfigurationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration to be created/updated.
    try {
      DisasterRecoveryConfiguration result = apiInstance.disasterRecoveryConfigurationsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigurationsApi#disasterRecoveryConfigurationsCreateOrUpdate");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration to be created/updated. | |

### Return type

[**DisasterRecoveryConfiguration**](DisasterRecoveryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted |  -  |

<a id="disasterRecoveryConfigurationsDelete"></a>
# **disasterRecoveryConfigurationsDelete**
> disasterRecoveryConfigurationsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Deletes a disaster recovery configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DisasterRecoveryConfigurationsApi apiInstance = new DisasterRecoveryConfigurationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration to be deleted.
    try {
      apiInstance.disasterRecoveryConfigurationsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigurationsApi#disasterRecoveryConfigurationsDelete");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration to be deleted. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |

<a id="disasterRecoveryConfigurationsFailover"></a>
# **disasterRecoveryConfigurationsFailover**
> disasterRecoveryConfigurationsFailover(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Fails over from the current primary server to this server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DisasterRecoveryConfigurationsApi apiInstance = new DisasterRecoveryConfigurationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration to failover.
    try {
      apiInstance.disasterRecoveryConfigurationsFailover(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigurationsApi#disasterRecoveryConfigurationsFailover");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration to failover. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | No Content |  -  |

<a id="disasterRecoveryConfigurationsFailoverAllowDataLoss"></a>
# **disasterRecoveryConfigurationsFailoverAllowDataLoss**
> disasterRecoveryConfigurationsFailoverAllowDataLoss(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Fails over from the current primary server to this server. This operation might result in data loss.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DisasterRecoveryConfigurationsApi apiInstance = new DisasterRecoveryConfigurationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration to failover forcefully.
    try {
      apiInstance.disasterRecoveryConfigurationsFailoverAllowDataLoss(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigurationsApi#disasterRecoveryConfigurationsFailoverAllowDataLoss");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration to failover forcefully. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | No Content |  -  |

<a id="disasterRecoveryConfigurationsGet"></a>
# **disasterRecoveryConfigurationsGet**
> DisasterRecoveryConfiguration disasterRecoveryConfigurationsGet(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Gets a disaster recovery configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DisasterRecoveryConfigurationsApi apiInstance = new DisasterRecoveryConfigurationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration.
    try {
      DisasterRecoveryConfiguration result = apiInstance.disasterRecoveryConfigurationsGet(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigurationsApi#disasterRecoveryConfigurationsGet");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration. | |

### Return type

[**DisasterRecoveryConfiguration**](DisasterRecoveryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="disasterRecoveryConfigurationsList"></a>
# **disasterRecoveryConfigurationsList**
> DisasterRecoveryConfigurationListResult disasterRecoveryConfigurationsList(apiVersion, subscriptionId, resourceGroupName, serverName)



Lists a server&#39;s disaster recovery configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DisasterRecoveryConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DisasterRecoveryConfigurationsApi apiInstance = new DisasterRecoveryConfigurationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    try {
      DisasterRecoveryConfigurationListResult result = apiInstance.disasterRecoveryConfigurationsList(apiVersion, subscriptionId, resourceGroupName, serverName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DisasterRecoveryConfigurationsApi#disasterRecoveryConfigurationsList");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |

### Return type

[**DisasterRecoveryConfigurationListResult**](DisasterRecoveryConfigurationListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

