# ManagedClustersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedClustersCreateOrUpdate**](ManagedClustersApi.md#managedClustersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName} | Creates or updates a managed cluster. |
| [**managedClustersDelete**](ManagedClustersApi.md#managedClustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName} | Deletes a managed cluster. |
| [**managedClustersGet**](ManagedClustersApi.md#managedClustersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName} | Gets a managed cluster. |
| [**managedClustersGetAccessProfile**](ManagedClustersApi.md#managedClustersGetAccessProfile) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/accessProfiles/{roleName}/listCredential | Gets an access profile of a managed cluster. |
| [**managedClustersGetUpgradeProfile**](ManagedClustersApi.md#managedClustersGetUpgradeProfile) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/upgradeProfiles/default | Gets upgrade profile for a managed cluster. |
| [**managedClustersList**](ManagedClustersApi.md#managedClustersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerService/managedClusters | Gets a list of managed clusters in the specified subscription. |
| [**managedClustersListByResourceGroup**](ManagedClustersApi.md#managedClustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters | Lists managed clusters in the specified subscription and resource group. |
| [**managedClustersListClusterAdminCredentials**](ManagedClustersApi.md#managedClustersListClusterAdminCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/listClusterAdminCredential | Gets cluster admin credential of a managed cluster. |
| [**managedClustersListClusterUserCredentials**](ManagedClustersApi.md#managedClustersListClusterUserCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/listClusterUserCredential | Gets cluster user credential of a managed cluster. |
| [**managedClustersResetAADProfile**](ManagedClustersApi.md#managedClustersResetAADProfile) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/resetAADProfile | Reset AAD Profile of a managed cluster. |
| [**managedClustersResetServicePrincipalProfile**](ManagedClustersApi.md#managedClustersResetServicePrincipalProfile) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName}/resetServicePrincipalProfile | Reset Service Principal Profile of a managed cluster. |
| [**managedClustersUpdateTags**](ManagedClustersApi.md#managedClustersUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerService/managedClusters/{resourceName} | Updates tags on a managed cluster. |
| [**operationsList**](ManagedClustersApi.md#operationsList) | **GET** /providers/Microsoft.ContainerService/operations |  |


<a id="managedClustersCreateOrUpdate"></a>
# **managedClustersCreateOrUpdate**
> ManagedCluster managedClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Creates or updates a managed cluster.

Creates or updates a managed cluster with the specified configuration for agents and Kubernetes version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    ManagedCluster parameters = new ManagedCluster(); // ManagedCluster | Parameters supplied to the Create or Update a Managed Cluster operation.
    try {
      ManagedCluster result = apiInstance.managedClustersCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersCreateOrUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |
| **parameters** | [**ManagedCluster**](ManagedCluster.md)| Parameters supplied to the Create or Update a Managed Cluster operation. | |

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="managedClustersDelete"></a>
# **managedClustersDelete**
> managedClustersDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)

Deletes a managed cluster.

Deletes the managed cluster with a specified resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    try {
      apiInstance.managedClustersDelete(apiVersion, subscriptionId, resourceGroupName, resourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersDelete");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |

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
| **204** | NoContent |  -  |

<a id="managedClustersGet"></a>
# **managedClustersGet**
> ManagedCluster managedClustersGet(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets a managed cluster.

Gets the details of the managed cluster with a specified resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    try {
      ManagedCluster result = apiInstance.managedClustersGet(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedClustersGetAccessProfile"></a>
# **managedClustersGetAccessProfile**
> ManagedClusterAccessProfile managedClustersGetAccessProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, roleName)

Gets an access profile of a managed cluster.

Gets the accessProfile for the specified role name of the managed cluster with a specified resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    String roleName = "roleName_example"; // String | The name of the role for managed cluster accessProfile resource.
    try {
      ManagedClusterAccessProfile result = apiInstance.managedClustersGetAccessProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersGetAccessProfile");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |
| **roleName** | **String**| The name of the role for managed cluster accessProfile resource. | |

### Return type

[**ManagedClusterAccessProfile**](ManagedClusterAccessProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedClustersGetUpgradeProfile"></a>
# **managedClustersGetUpgradeProfile**
> ManagedClusterUpgradeProfile managedClustersGetUpgradeProfile(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets upgrade profile for a managed cluster.

Gets the details of the upgrade profile for a managed cluster with a specified resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    try {
      ManagedClusterUpgradeProfile result = apiInstance.managedClustersGetUpgradeProfile(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersGetUpgradeProfile");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |

### Return type

[**ManagedClusterUpgradeProfile**](ManagedClusterUpgradeProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedClustersList"></a>
# **managedClustersList**
> ManagedClusterListResult managedClustersList(apiVersion, subscriptionId)

Gets a list of managed clusters in the specified subscription.

Gets a list of managed clusters in the specified subscription. The operation returns properties of each managed cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ManagedClusterListResult result = apiInstance.managedClustersList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ManagedClusterListResult**](ManagedClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedClustersListByResourceGroup"></a>
# **managedClustersListByResourceGroup**
> ManagedClusterListResult managedClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Lists managed clusters in the specified subscription and resource group.

Lists managed clusters in the specified subscription and resource group. The operation returns properties of each managed cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    try {
      ManagedClusterListResult result = apiInstance.managedClustersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersListByResourceGroup");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |

### Return type

[**ManagedClusterListResult**](ManagedClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedClustersListClusterAdminCredentials"></a>
# **managedClustersListClusterAdminCredentials**
> CredentialResults managedClustersListClusterAdminCredentials(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets cluster admin credential of a managed cluster.

Gets cluster admin credential of the managed cluster with a specified resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    try {
      CredentialResults result = apiInstance.managedClustersListClusterAdminCredentials(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersListClusterAdminCredentials");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |

### Return type

[**CredentialResults**](CredentialResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedClustersListClusterUserCredentials"></a>
# **managedClustersListClusterUserCredentials**
> CredentialResults managedClustersListClusterUserCredentials(apiVersion, subscriptionId, resourceGroupName, resourceName)

Gets cluster user credential of a managed cluster.

Gets cluster user credential of the managed cluster with a specified resource group and name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    try {
      CredentialResults result = apiInstance.managedClustersListClusterUserCredentials(apiVersion, subscriptionId, resourceGroupName, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersListClusterUserCredentials");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |

### Return type

[**CredentialResults**](CredentialResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedClustersResetAADProfile"></a>
# **managedClustersResetAADProfile**
> managedClustersResetAADProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Reset AAD Profile of a managed cluster.

Update the AAD Profile for a managed cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    ManagedClusterAADProfile parameters = new ManagedClusterAADProfile(); // ManagedClusterAADProfile | Parameters supplied to the Reset AAD Profile operation for a Managed Cluster.
    try {
      apiInstance.managedClustersResetAADProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersResetAADProfile");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |
| **parameters** | [**ManagedClusterAADProfile**](ManagedClusterAADProfile.md)| Parameters supplied to the Reset AAD Profile operation for a Managed Cluster. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="managedClustersResetServicePrincipalProfile"></a>
# **managedClustersResetServicePrincipalProfile**
> managedClustersResetServicePrincipalProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Reset Service Principal Profile of a managed cluster.

Update the service principal Profile for a managed cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    ManagedClusterServicePrincipalProfile parameters = new ManagedClusterServicePrincipalProfile(); // ManagedClusterServicePrincipalProfile | Parameters supplied to the Reset Service Principal Profile operation for a Managed Cluster.
    try {
      apiInstance.managedClustersResetServicePrincipalProfile(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersResetServicePrincipalProfile");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |
| **parameters** | [**ManagedClusterServicePrincipalProfile**](ManagedClusterServicePrincipalProfile.md)| Parameters supplied to the Reset Service Principal Profile operation for a Managed Cluster. | |

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
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="managedClustersUpdateTags"></a>
# **managedClustersUpdateTags**
> ManagedCluster managedClustersUpdateTags(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters)

Updates tags on a managed cluster.

Updates a managed cluster with the specified tags.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String resourceName = "resourceName_example"; // String | The name of the managed cluster resource.
    TagsObject parameters = new TagsObject(); // TagsObject | Parameters supplied to the Update Managed Cluster Tags operation.
    try {
      ManagedCluster result = apiInstance.managedClustersUpdateTags(apiVersion, subscriptionId, resourceGroupName, resourceName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#managedClustersUpdateTags");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **resourceName** | **String**| The name of the managed cluster resource. | |
| **parameters** | [**TagsObject**](TagsObject.md)| Parameters supplied to the Update Managed Cluster Tags operation. | |

### Return type

[**ManagedCluster**](ManagedCluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="operationsList"></a>
# **operationsList**
> OperationListResult operationsList(apiVersion)



Gets a list of compute operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedClustersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedClustersApi apiInstance = new ManagedClustersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      OperationListResult result = apiInstance.operationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedClustersApi#operationsList");
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
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**OperationListResult**](OperationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

