# AttachedDatabaseConfigurationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attachedDatabaseConfigurationsCreateOrUpdate**](AttachedDatabaseConfigurationsApi.md#attachedDatabaseConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/attachedDatabaseConfigurations/{attachedDatabaseConfigurationName} |  |
| [**attachedDatabaseConfigurationsDelete**](AttachedDatabaseConfigurationsApi.md#attachedDatabaseConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/attachedDatabaseConfigurations/{attachedDatabaseConfigurationName} |  |
| [**attachedDatabaseConfigurationsGet**](AttachedDatabaseConfigurationsApi.md#attachedDatabaseConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/attachedDatabaseConfigurations/{attachedDatabaseConfigurationName} |  |
| [**attachedDatabaseConfigurationsListByCluster**](AttachedDatabaseConfigurationsApi.md#attachedDatabaseConfigurationsListByCluster) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/attachedDatabaseConfigurations |  |


<a id="attachedDatabaseConfigurationsCreateOrUpdate"></a>
# **attachedDatabaseConfigurationsCreateOrUpdate**
> AttachedDatabaseConfiguration attachedDatabaseConfigurationsCreateOrUpdate(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion, parameters)



Creates or updates an attached database configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachedDatabaseConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AttachedDatabaseConfigurationsApi apiInstance = new AttachedDatabaseConfigurationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String attachedDatabaseConfigurationName = "attachedDatabaseConfigurationName_example"; // String | The name of the attached database configuration.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    AttachedDatabaseConfiguration parameters = new AttachedDatabaseConfiguration(); // AttachedDatabaseConfiguration | The database parameters supplied to the CreateOrUpdate operation.
    try {
      AttachedDatabaseConfiguration result = apiInstance.attachedDatabaseConfigurationsCreateOrUpdate(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachedDatabaseConfigurationsApi#attachedDatabaseConfigurationsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **attachedDatabaseConfigurationName** | **String**| The name of the attached database configuration. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |
| **parameters** | [**AttachedDatabaseConfiguration**](AttachedDatabaseConfiguration.md)| The database parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**AttachedDatabaseConfiguration**](AttachedDatabaseConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the database. |  -  |
| **201** | Successfully created the database. |  -  |
| **202** | Accepted the create database request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="attachedDatabaseConfigurationsDelete"></a>
# **attachedDatabaseConfigurationsDelete**
> attachedDatabaseConfigurationsDelete(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion)



Deletes the attached database configuration with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachedDatabaseConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AttachedDatabaseConfigurationsApi apiInstance = new AttachedDatabaseConfigurationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String attachedDatabaseConfigurationName = "attachedDatabaseConfigurationName_example"; // String | The name of the attached database configuration.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      apiInstance.attachedDatabaseConfigurationsDelete(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachedDatabaseConfigurationsApi#attachedDatabaseConfigurationsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **attachedDatabaseConfigurationName** | **String**| The name of the attached database configuration. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the database. |  -  |
| **202** | Accepted. |  -  |
| **204** | The specified database does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="attachedDatabaseConfigurationsGet"></a>
# **attachedDatabaseConfigurationsGet**
> AttachedDatabaseConfiguration attachedDatabaseConfigurationsGet(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion)



Returns an attached database configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachedDatabaseConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AttachedDatabaseConfigurationsApi apiInstance = new AttachedDatabaseConfigurationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String attachedDatabaseConfigurationName = "attachedDatabaseConfigurationName_example"; // String | The name of the attached database configuration.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      AttachedDatabaseConfiguration result = apiInstance.attachedDatabaseConfigurationsGet(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachedDatabaseConfigurationsApi#attachedDatabaseConfigurationsGet");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **attachedDatabaseConfigurationName** | **String**| The name of the attached database configuration. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**AttachedDatabaseConfiguration**](AttachedDatabaseConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified attached database configuration. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="attachedDatabaseConfigurationsListByCluster"></a>
# **attachedDatabaseConfigurationsListByCluster**
> AttachedDatabaseConfigurationListResult attachedDatabaseConfigurationsListByCluster(resourceGroupName, clusterName, subscriptionId, apiVersion)



Returns the list of attached database configurations of the given Kusto cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttachedDatabaseConfigurationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    AttachedDatabaseConfigurationsApi apiInstance = new AttachedDatabaseConfigurationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      AttachedDatabaseConfigurationListResult result = apiInstance.attachedDatabaseConfigurationsListByCluster(resourceGroupName, clusterName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttachedDatabaseConfigurationsApi#attachedDatabaseConfigurationsListByCluster");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**AttachedDatabaseConfigurationListResult**](AttachedDatabaseConfigurationListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of attached database configurations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

