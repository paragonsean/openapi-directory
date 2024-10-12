# SavedSearchesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**savedSearchesCreateOrUpdate**](SavedSearchesApi.md#savedSearchesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/savedSearches/{savedSearchId} |  |
| [**savedSearchesDelete**](SavedSearchesApi.md#savedSearchesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/savedSearches/{savedSearchId} |  |
| [**savedSearchesGet**](SavedSearchesApi.md#savedSearchesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/savedSearches/{savedSearchId} |  |
| [**savedSearchesListByWorkspace**](SavedSearchesApi.md#savedSearchesListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/savedSearches |  |


<a id="savedSearchesCreateOrUpdate"></a>
# **savedSearchesCreateOrUpdate**
> SavedSearch savedSearchesCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion, parameters)



Creates or updates a saved search for a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedSearchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SavedSearchesApi apiInstance = new SavedSearchesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String savedSearchId = "savedSearchId_example"; // String | The id of the saved search.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    SavedSearch parameters = new SavedSearch(); // SavedSearch | The parameters required to save a search.
    try {
      SavedSearch result = apiInstance.savedSearchesCreateOrUpdate(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedSearchesApi#savedSearchesCreateOrUpdate");
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
| **savedSearchId** | **String**| The id of the saved search. | |
| **apiVersion** | **String**| The client API version. | |
| **parameters** | [**SavedSearch**](SavedSearch.md)| The parameters required to save a search. | |

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="savedSearchesDelete"></a>
# **savedSearchesDelete**
> savedSearchesDelete(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion)



Deletes the specified saved search in a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedSearchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SavedSearchesApi apiInstance = new SavedSearchesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String savedSearchId = "savedSearchId_example"; // String | The id of the saved search.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      apiInstance.savedSearchesDelete(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedSearchesApi#savedSearchesDelete");
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
| **savedSearchId** | **String**| The id of the saved search. | |
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
| **200** | OK response definition. |  -  |

<a id="savedSearchesGet"></a>
# **savedSearchesGet**
> SavedSearch savedSearchesGet(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion)



Gets the specified saved search for a given workspace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedSearchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SavedSearchesApi apiInstance = new SavedSearchesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String savedSearchId = "savedSearchId_example"; // String | The id of the saved search.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    try {
      SavedSearch result = apiInstance.savedSearchesGet(subscriptionId, resourceGroupName, workspaceName, savedSearchId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedSearchesApi#savedSearchesGet");
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
| **savedSearchId** | **String**| The id of the saved search. | |
| **apiVersion** | **String**| The client API version. | |

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="savedSearchesListByWorkspace"></a>
# **savedSearchesListByWorkspace**
> SavedSearchesListResult savedSearchesListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId)



Gets the saved searches for a given Log Analytics Workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SavedSearchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SavedSearchesApi apiInstance = new SavedSearchesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group name.
    String workspaceName = "workspaceName_example"; // String | The Log Analytics Workspace name.
    String apiVersion = "apiVersion_example"; // String | The client API version.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription ID.
    try {
      SavedSearchesListResult result = apiInstance.savedSearchesListByWorkspace(resourceGroupName, workspaceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SavedSearchesApi#savedSearchesListByWorkspace");
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

[**SavedSearchesListResult**](SavedSearchesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of saved searches for the given Log Analytics Workspace. |  -  |

