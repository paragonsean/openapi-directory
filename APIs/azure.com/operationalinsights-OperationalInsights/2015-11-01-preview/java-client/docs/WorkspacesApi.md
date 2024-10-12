# WorkspacesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspacesCreateOrUpdate**](WorkspacesApi.md#workspacesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName} |  |
| [**workspacesDelete**](WorkspacesApi.md#workspacesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName} |  |
| [**workspacesDisableIntelligencePack**](WorkspacesApi.md#workspacesDisableIntelligencePack) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/intelligencePacks/{intelligencePackName}/Disable |  |
| [**workspacesEnableIntelligencePack**](WorkspacesApi.md#workspacesEnableIntelligencePack) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/intelligencePacks/{intelligencePackName}/Enable |  |
| [**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName} |  |
| [**workspacesGetSharedKeys**](WorkspacesApi.md#workspacesGetSharedKeys) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/sharedKeys |  |
| [**workspacesList**](WorkspacesApi.md#workspacesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.OperationalInsights/workspaces |  |
| [**workspacesListByResourceGroup**](WorkspacesApi.md#workspacesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces |  |
| [**workspacesListIntelligencePacks**](WorkspacesApi.md#workspacesListIntelligencePacks) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/intelligencePacks |  |
| [**workspacesListManagementGroups**](WorkspacesApi.md#workspacesListManagementGroups) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/managementGroups |  |
| [**workspacesListUsages**](WorkspacesApi.md#workspacesListUsages) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/usages |  |
| [**workspacesUpdate**](WorkspacesApi.md#workspacesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName} |  |


<a id="workspacesCreateOrUpdate"></a>
# **workspacesCreateOrUpdate**
> Workspace workspacesCreateOrUpdate(resourceGroupName, workspaceName, apiVersion, subscriptionId, parameters)



Create or update a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the workspace.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Workspace parameters = new Workspace(); // Workspace | The parameters required to create or update a workspace.
    try {
      Workspace result = apiInstance.workspacesCreateOrUpdate(resourceGroupName, workspaceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The resource group name of the workspace. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**Workspace**](Workspace.md)| The parameters required to create or update a workspace. | |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **201** | Created response definition. |  -  |

<a id="workspacesDelete"></a>
# **workspacesDelete**
> workspacesDelete(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Deletes a workspace instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the workspace.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.workspacesDelete(resourceGroupName, workspaceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesDelete");
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
| **resourceGroupName** | **String**| The resource group name of the workspace. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK response definition. |  -  |
| **204** | NoContent response definition. |  -  |

<a id="workspacesDisableIntelligencePack"></a>
# **workspacesDisableIntelligencePack**
> workspacesDisableIntelligencePack(resourceGroupName, workspaceName, intelligencePackName, apiVersion, subscriptionId)



Disables an intelligence pack for a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
    String intelligencePackName = "intelligencePackName_example"; // String | The name of the intelligence pack to be disabled.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.workspacesDisableIntelligencePack(resourceGroupName, workspaceName, intelligencePackName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesDisableIntelligencePack");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace. | |
| **intelligencePackName** | **String**| The name of the intelligence pack to be disabled. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK response definition. |  -  |

<a id="workspacesEnableIntelligencePack"></a>
# **workspacesEnableIntelligencePack**
> workspacesEnableIntelligencePack(resourceGroupName, workspaceName, intelligencePackName, apiVersion, subscriptionId)



Enables an intelligence pack for a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
    String intelligencePackName = "intelligencePackName_example"; // String | The name of the intelligence pack to be enabled.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.workspacesEnableIntelligencePack(resourceGroupName, workspaceName, intelligencePackName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesEnableIntelligencePack");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace. | |
| **intelligencePackName** | **String**| The name of the intelligence pack to be enabled. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

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
| **200** | OK response definition. |  -  |

<a id="workspacesGet"></a>
# **workspacesGet**
> Workspace workspacesGet(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets a workspace instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the workspace.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      Workspace result = apiInstance.workspacesGet(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesGet");
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
| **resourceGroupName** | **String**| The resource group name of the workspace. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesGetSharedKeys"></a>
# **workspacesGetSharedKeys**
> SharedKeys workspacesGetSharedKeys(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets the shared keys for a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      SharedKeys result = apiInstance.workspacesGetSharedKeys(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesGetSharedKeys");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**SharedKeys**](SharedKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesList"></a>
# **workspacesList**
> WorkspaceListResult workspacesList(apiVersion, subscriptionId)



Gets the workspaces in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      WorkspaceListResult result = apiInstance.workspacesList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesList");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesListByResourceGroup"></a>
# **workspacesListByResourceGroup**
> WorkspaceListResult workspacesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets workspaces in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      WorkspaceListResult result = apiInstance.workspacesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**WorkspaceListResult**](WorkspaceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesListIntelligencePacks"></a>
# **workspacesListIntelligencePacks**
> List&lt;IntelligencePack&gt; workspacesListIntelligencePacks(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Lists all the intelligence packs possible and whether they are enabled or disabled for a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      List<IntelligencePack> result = apiInstance.workspacesListIntelligencePacks(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListIntelligencePacks");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**List&lt;IntelligencePack&gt;**](IntelligencePack.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesListManagementGroups"></a>
# **workspacesListManagementGroups**
> WorkspaceListManagementGroupsResult workspacesListManagementGroups(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets a list of management groups connected to a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      WorkspaceListManagementGroupsResult result = apiInstance.workspacesListManagementGroups(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListManagementGroups");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**WorkspaceListManagementGroupsResult**](WorkspaceListManagementGroupsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesListUsages"></a>
# **workspacesListUsages**
> WorkspaceListUsagesResult workspacesListUsages(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets a list of usage metrics for a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      WorkspaceListUsagesResult result = apiInstance.workspacesListUsages(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListUsages");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**WorkspaceListUsagesResult**](WorkspaceListUsagesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesUpdate"></a>
# **workspacesUpdate**
> Workspace workspacesUpdate(resourceGroupName, workspaceName, apiVersion, subscriptionId, parameters)



Updates a workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name of the workspace.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Workspace parameters = new Workspace(); // Workspace | The parameters required to patch a workspace.
    try {
      Workspace result = apiInstance.workspacesUpdate(resourceGroupName, workspaceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesUpdate");
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
| **resourceGroupName** | **String**| The resource group name of the workspace. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**Workspace**](Workspace.md)| The parameters required to patch a workspace. | |

### Return type

[**Workspace**](Workspace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The existing workspace was successfully updated. Check provisioningStatus to see detailed status. |  -  |

