# WorkspacesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspacesDeleteGateways**](WorkspacesApi.md#workspacesDeleteGateways) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/gateways/{gatewayId} |  |
| [**workspacesGetPurgeStatus**](WorkspacesApi.md#workspacesGetPurgeStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/operations/{purgeId} |  |
| [**workspacesGetSchema**](WorkspacesApi.md#workspacesGetSchema) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/schema |  |
| [**workspacesListKeys**](WorkspacesApi.md#workspacesListKeys) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/listKeys |  |
| [**workspacesListLinkTargets**](WorkspacesApi.md#workspacesListLinkTargets) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.OperationalInsights/linkTargets |  |
| [**workspacesPurge**](WorkspacesApi.md#workspacesPurge) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/purge |  |
| [**workspacesRegenerateSharedKeys**](WorkspacesApi.md#workspacesRegenerateSharedKeys) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/regenerateSharedKey |  |


<a id="workspacesDeleteGateways"></a>
# **workspacesDeleteGateways**
> workspacesDeleteGateways(subscriptionId, resourceGroupName, workspaceName, gatewayId, apiVersion)



Delete a Log Analytics gateway.

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
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String gatewayId = "gatewayId_example"; // String | The Log Analytics gateway Id.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.workspacesDeleteGateways(subscriptionId, resourceGroupName, workspaceName, gatewayId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesDeleteGateways");
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
| **subscriptionId** | **String**| The Subscription ID. | |
| **resourceGroupName** | **String**| The Resource Group name. | |
| **workspaceName** | **String**| The Log Analytics Workspace name. | |
| **gatewayId** | **String**| The Log Analytics gateway Id. | |
| **apiVersion** | **String**| The client API version. | |

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
| **200** | The specified gateway was deleted successfully. |  -  |

<a id="workspacesGetPurgeStatus"></a>
# **workspacesGetPurgeStatus**
> WorkspacePurgeStatusResponse workspacesGetPurgeStatus(resourceGroupName, apiVersion, subscriptionId, workspaceName, purgeId)



Gets status of an ongoing purge operation.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String purgeId = "purgeId_example"; // String | In a purge status request, this is the Id of the operation the status of which is returned.
    try {
      WorkspacePurgeStatusResponse result = apiInstance.workspacesGetPurgeStatus(resourceGroupName, apiVersion, subscriptionId, workspaceName, purgeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesGetPurgeStatus");
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
| **resourceGroupName** | **String**| The Resource Group name. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Subscription ID. | |
| **workspaceName** | **String**| The Log Analytics Workspace name. | |
| **purgeId** | **String**| In a purge status request, this is the Id of the operation the status of which is returned. | |

### Return type

[**WorkspacePurgeStatusResponse**](WorkspacePurgeStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns status of purge operation in body of response. e.g.:  running, completed. |  -  |

<a id="workspacesGetSchema"></a>
# **workspacesGetSchema**
> SearchGetSchemaResponse workspacesGetSchema(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets the schema for a given workspace.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    try {
      SearchGetSchemaResponse result = apiInstance.workspacesGetSchema(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesGetSchema");
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
| **resourceGroupName** | **String**| The Resource Group name. | |
| **workspaceName** | **String**| The Log Analytics Workspace name. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Subscription ID. | |

### Return type

[**SearchGetSchemaResponse**](SearchGetSchemaResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesListKeys"></a>
# **workspacesListKeys**
> SharedKeys workspacesListKeys(subscriptionId, resourceGroupName, workspaceName, apiVersion)



Gets the shared keys for a Log Analytics Workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace.

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
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      SharedKeys result = apiInstance.workspacesListKeys(subscriptionId, resourceGroupName, workspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListKeys");
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
| **subscriptionId** | **String**| The Subscription ID. | |
| **resourceGroupName** | **String**| The Resource Group name. | |
| **workspaceName** | **String**| The Log Analytics Workspace name. | |
| **apiVersion** | **String**| The client API version. | |

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
| **200** | Returns the shared keys associated with the Log Analytics Workspace. |  -  |

<a id="workspacesListLinkTargets"></a>
# **workspacesListLinkTargets**
> List&lt;LinkTarget&gt; workspacesListLinkTargets(apiVersion, subscriptionId)



Get a list of workspaces which the current user has administrator privileges and are not associated with an Azure Subscription. The subscriptionId parameter in the Url is ignored.

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
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    try {
      List<LinkTarget> result = apiInstance.workspacesListLinkTargets(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesListLinkTargets");
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
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Subscription ID. | |

### Return type

[**List&lt;LinkTarget&gt;**](LinkTarget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="workspacesPurge"></a>
# **workspacesPurge**
> WorkspacePurgeResponse workspacesPurge(resourceGroupName, apiVersion, subscriptionId, workspaceName, body)



Purges data in an Log Analytics workspace by a set of user-defined filters.  In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.

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
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    WorkspacePurgeBody body = new WorkspacePurgeBody(); // WorkspacePurgeBody | Describes the body of a request to purge data in a single table of an Log Analytics Workspace
    try {
      WorkspacePurgeResponse result = apiInstance.workspacesPurge(resourceGroupName, apiVersion, subscriptionId, workspaceName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesPurge");
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
| **resourceGroupName** | **String**| The Resource Group name. | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Subscription ID. | |
| **workspaceName** | **String**| The Log Analytics Workspace name. | |
| **body** | [**WorkspacePurgeBody**](WorkspacePurgeBody.md)| Describes the body of a request to purge data in a single table of an Log Analytics Workspace | |

### Return type

[**WorkspacePurgeResponse**](WorkspacePurgeResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted request for purging an Log Analytics workspace. |  * x-ms-status-location - The location from which to request the operation status. <br>  |

<a id="workspacesRegenerateSharedKeys"></a>
# **workspacesRegenerateSharedKeys**
> SharedKeys workspacesRegenerateSharedKeys(subscriptionId, resourceGroupName, workspaceName, apiVersion)



Regenerates the shared keys for a Log Analytics Workspace. These keys are used to connect Microsoft Operational Insights agents to the workspace.

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
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      SharedKeys result = apiInstance.workspacesRegenerateSharedKeys(subscriptionId, resourceGroupName, workspaceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesRegenerateSharedKeys");
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
| **subscriptionId** | **String**| The Subscription ID. | |
| **resourceGroupName** | **String**| The Resource Group name. | |
| **workspaceName** | **String**| The Log Analytics Workspace name. | |
| **apiVersion** | **String**| The client API version. | |

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
| **200** | Returns the new shared keys associated with the Log Analytics Workspace. |  -  |

