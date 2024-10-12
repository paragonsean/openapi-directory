# StorageInsightsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storageInsightsCreateOrUpdate**](StorageInsightsApi.md#storageInsightsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName} |  |
| [**storageInsightsDelete**](StorageInsightsApi.md#storageInsightsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName} |  |
| [**storageInsightsGet**](StorageInsightsApi.md#storageInsightsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName} |  |
| [**storageInsightsListByWorkspace**](StorageInsightsApi.md#storageInsightsListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs |  |


<a id="storageInsightsCreateOrUpdate"></a>
# **storageInsightsCreateOrUpdate**
> StorageInsight storageInsightsCreateOrUpdate(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId, parameters)



Create or update a storage insight.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageInsightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageInsightsApi apiInstance = new StorageInsightsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String storageInsightName = "storageInsightName_example"; // String | Name of the storageInsightsConfigs resource
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    StorageInsight parameters = new StorageInsight(); // StorageInsight | The parameters required to create or update a storage insight.
    try {
      StorageInsight result = apiInstance.storageInsightsCreateOrUpdate(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageInsightsApi#storageInsightsCreateOrUpdate");
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
| **storageInsightName** | **String**| Name of the storageInsightsConfigs resource | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Subscription ID. | |
| **parameters** | [**StorageInsight**](StorageInsight.md)| The parameters required to create or update a storage insight. | |

### Return type

[**StorageInsight**](StorageInsight.md)

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

<a id="storageInsightsDelete"></a>
# **storageInsightsDelete**
> storageInsightsDelete(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId)



Deletes a storageInsightsConfigs resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageInsightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageInsightsApi apiInstance = new StorageInsightsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String storageInsightName = "storageInsightName_example"; // String | Name of the storageInsightsConfigs resource
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    try {
      apiInstance.storageInsightsDelete(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageInsightsApi#storageInsightsDelete");
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
| **storageInsightName** | **String**| Name of the storageInsightsConfigs resource | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Subscription ID. | |

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

<a id="storageInsightsGet"></a>
# **storageInsightsGet**
> StorageInsight storageInsightsGet(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId)



Gets a storage insight instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageInsightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageInsightsApi apiInstance = new StorageInsightsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String storageInsightName = "storageInsightName_example"; // String | Name of the storageInsightsConfigs resource
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    try {
      StorageInsight result = apiInstance.storageInsightsGet(resourceGroupName, workspaceName, storageInsightName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageInsightsApi#storageInsightsGet");
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
| **storageInsightName** | **String**| Name of the storageInsightsConfigs resource | |
| **apiVersion** | **String**| The client API version. | |
| **subscriptionId** | **String**| The Subscription ID. | |

### Return type

[**StorageInsight**](StorageInsight.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="storageInsightsListByWorkspace"></a>
# **storageInsightsListByWorkspace**
> StorageInsightListResult storageInsightsListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Lists the storage insight instances within a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StorageInsightsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    StorageInsightsApi apiInstance = new StorageInsightsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    try {
      StorageInsightListResult result = apiInstance.storageInsightsListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StorageInsightsApi#storageInsightsListByWorkspace");
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

[**StorageInsightListResult**](StorageInsightListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

