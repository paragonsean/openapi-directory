# WorkflowTriggerHistoriesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workflowTriggerHistoriesGet**](WorkflowTriggerHistoriesApi.md#workflowTriggerHistoriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/histories/{historyName} |  |
| [**workflowTriggerHistoriesList**](WorkflowTriggerHistoriesApi.md#workflowTriggerHistoriesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/triggers/{triggerName}/histories |  |


<a id="workflowTriggerHistoriesGet"></a>
# **workflowTriggerHistoriesGet**
> WorkflowTriggerHistory workflowTriggerHistoriesGet(subscriptionId, resourceGroupName, workflowName, triggerName, historyName, apiVersion)



Gets a workflow trigger history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggerHistoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggerHistoriesApi apiInstance = new WorkflowTriggerHistoriesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String historyName = "historyName_example"; // String | The workflow trigger history name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowTriggerHistory result = apiInstance.workflowTriggerHistoriesGet(subscriptionId, resourceGroupName, workflowName, triggerName, historyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggerHistoriesApi#workflowTriggerHistoriesGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **workflowName** | **String**| The workflow name. | |
| **triggerName** | **String**| The workflow trigger name. | |
| **historyName** | **String**| The workflow trigger history name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowTriggerHistory**](WorkflowTriggerHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowTriggerHistoriesList"></a>
# **workflowTriggerHistoriesList**
> WorkflowTriggerHistoryListResult workflowTriggerHistoriesList(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, $top, $filter)



Gets a list of workflow trigger histories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTriggerHistoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowTriggerHistoriesApi apiInstance = new WorkflowTriggerHistoriesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String triggerName = "triggerName_example"; // String | The workflow trigger name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      WorkflowTriggerHistoryListResult result = apiInstance.workflowTriggerHistoriesList(subscriptionId, resourceGroupName, workflowName, triggerName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTriggerHistoriesApi#workflowTriggerHistoriesList");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **workflowName** | **String**| The workflow name. | |
| **triggerName** | **String**| The workflow trigger name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**WorkflowTriggerHistoryListResult**](WorkflowTriggerHistoryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

