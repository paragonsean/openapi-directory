# WorkflowRunActionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workflowRunActionRepetitionsGet**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName} |  |
| [**workflowRunActionRepetitionsList**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions |  |
| [**workflowRunActionRepetitionsListExpressionTraces**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsListExpressionTraces) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName}/listExpressionTraces |  |
| [**workflowRunActionRepetitionsRequestHistoriesGet**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsRequestHistoriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName}/requestHistories/{requestHistoryName} |  |
| [**workflowRunActionRepetitionsRequestHistoriesList**](WorkflowRunActionsApi.md#workflowRunActionRepetitionsRequestHistoriesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/repetitions/{repetitionName}/requestHistories |  |
| [**workflowRunActionRequestHistoriesGet**](WorkflowRunActionsApi.md#workflowRunActionRequestHistoriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/requestHistories/{requestHistoryName} |  |
| [**workflowRunActionRequestHistoriesList**](WorkflowRunActionsApi.md#workflowRunActionRequestHistoriesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/requestHistories |  |
| [**workflowRunActionScopedRepetitionsGet**](WorkflowRunActionsApi.md#workflowRunActionScopedRepetitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/scopeRepetitions/{repetitionName} |  |
| [**workflowRunActionScopedRepetitionsList**](WorkflowRunActionsApi.md#workflowRunActionScopedRepetitionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/scopeRepetitions |  |
| [**workflowRunActionsGet**](WorkflowRunActionsApi.md#workflowRunActionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName} |  |
| [**workflowRunActionsList**](WorkflowRunActionsApi.md#workflowRunActionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions |  |
| [**workflowRunActionsListExpressionTraces**](WorkflowRunActionsApi.md#workflowRunActionsListExpressionTraces) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/workflows/{workflowName}/runs/{runName}/actions/{actionName}/listExpressionTraces |  |


<a id="workflowRunActionRepetitionsGet"></a>
# **workflowRunActionRepetitionsGet**
> WorkflowRunActionRepetitionDefinition workflowRunActionRepetitionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion)



Get a workflow run action repetition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String repetitionName = "repetitionName_example"; // String | The workflow repetition.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowRunActionRepetitionDefinition result = apiInstance.workflowRunActionRepetitionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionRepetitionsGet");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **repetitionName** | **String**| The workflow repetition. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowRunActionRepetitionDefinition**](WorkflowRunActionRepetitionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowRunActionRepetitionsList"></a>
# **workflowRunActionRepetitionsList**
> WorkflowRunActionRepetitionDefinitionCollection workflowRunActionRepetitionsList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



Get all of a workflow run action repetitions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowRunActionRepetitionDefinitionCollection result = apiInstance.workflowRunActionRepetitionsList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionRepetitionsList");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowRunActionRepetitionDefinitionCollection**](WorkflowRunActionRepetitionDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowRunActionRepetitionsListExpressionTraces"></a>
# **workflowRunActionRepetitionsListExpressionTraces**
> ExpressionTraces workflowRunActionRepetitionsListExpressionTraces(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion)



Lists a workflow run expression trace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String repetitionName = "repetitionName_example"; // String | The workflow repetition.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      ExpressionTraces result = apiInstance.workflowRunActionRepetitionsListExpressionTraces(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionRepetitionsListExpressionTraces");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **repetitionName** | **String**| The workflow repetition. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**ExpressionTraces**](ExpressionTraces.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowRunActionRepetitionsRequestHistoriesGet"></a>
# **workflowRunActionRepetitionsRequestHistoriesGet**
> RequestHistory workflowRunActionRepetitionsRequestHistoriesGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, requestHistoryName, apiVersion)



Gets a workflow run repetition request history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String repetitionName = "repetitionName_example"; // String | The workflow repetition.
    String requestHistoryName = "requestHistoryName_example"; // String | The request history name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      RequestHistory result = apiInstance.workflowRunActionRepetitionsRequestHistoriesGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, requestHistoryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionRepetitionsRequestHistoriesGet");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **repetitionName** | **String**| The workflow repetition. | |
| **requestHistoryName** | **String**| The request history name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**RequestHistory**](RequestHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workflowRunActionRepetitionsRequestHistoriesList"></a>
# **workflowRunActionRepetitionsRequestHistoriesList**
> RequestHistoryListResult workflowRunActionRepetitionsRequestHistoriesList(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion)



List a workflow run repetition request history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String repetitionName = "repetitionName_example"; // String | The workflow repetition.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      RequestHistoryListResult result = apiInstance.workflowRunActionRepetitionsRequestHistoriesList(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionRepetitionsRequestHistoriesList");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **repetitionName** | **String**| The workflow repetition. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**RequestHistoryListResult**](RequestHistoryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workflowRunActionRequestHistoriesGet"></a>
# **workflowRunActionRequestHistoriesGet**
> RequestHistory workflowRunActionRequestHistoriesGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, requestHistoryName, apiVersion)



Gets a workflow run request history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String requestHistoryName = "requestHistoryName_example"; // String | The request history name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      RequestHistory result = apiInstance.workflowRunActionRequestHistoriesGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, requestHistoryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionRequestHistoriesGet");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **requestHistoryName** | **String**| The request history name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**RequestHistory**](RequestHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workflowRunActionRequestHistoriesList"></a>
# **workflowRunActionRequestHistoriesList**
> RequestHistoryListResult workflowRunActionRequestHistoriesList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



List a workflow run request history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      RequestHistoryListResult result = apiInstance.workflowRunActionRequestHistoriesList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionRequestHistoriesList");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**RequestHistoryListResult**](RequestHistoryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="workflowRunActionScopedRepetitionsGet"></a>
# **workflowRunActionScopedRepetitionsGet**
> WorkflowRunActionRepetitionDefinition workflowRunActionScopedRepetitionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion)



Get a workflow run action scoped repetition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String repetitionName = "repetitionName_example"; // String | The workflow repetition.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowRunActionRepetitionDefinition result = apiInstance.workflowRunActionScopedRepetitionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, repetitionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionScopedRepetitionsGet");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **repetitionName** | **String**| The workflow repetition. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowRunActionRepetitionDefinition**](WorkflowRunActionRepetitionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowRunActionScopedRepetitionsList"></a>
# **workflowRunActionScopedRepetitionsList**
> WorkflowRunActionRepetitionDefinitionCollection workflowRunActionScopedRepetitionsList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



List the workflow run action scoped repetitions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowRunActionRepetitionDefinitionCollection result = apiInstance.workflowRunActionScopedRepetitionsList(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionScopedRepetitionsList");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowRunActionRepetitionDefinitionCollection**](WorkflowRunActionRepetitionDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowRunActionsGet"></a>
# **workflowRunActionsGet**
> WorkflowRunAction workflowRunActionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



Gets a workflow run action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      WorkflowRunAction result = apiInstance.workflowRunActionsGet(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionsGet");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**WorkflowRunAction**](WorkflowRunAction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowRunActionsList"></a>
# **workflowRunActionsList**
> WorkflowRunActionListResult workflowRunActionsList(subscriptionId, resourceGroupName, workflowName, runName, apiVersion, $top, $filter)



Gets a list of workflow run actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Options for filters include: Status.
    try {
      WorkflowRunActionListResult result = apiInstance.workflowRunActionsList(subscriptionId, resourceGroupName, workflowName, runName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionsList");
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
| **runName** | **String**| The workflow run name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. Options for filters include: Status. | [optional] |

### Return type

[**WorkflowRunActionListResult**](WorkflowRunActionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="workflowRunActionsListExpressionTraces"></a>
# **workflowRunActionsListExpressionTraces**
> ExpressionTraces workflowRunActionsListExpressionTraces(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion)



Lists a workflow run expression trace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowRunActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkflowRunActionsApi apiInstance = new WorkflowRunActionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String workflowName = "workflowName_example"; // String | The workflow name.
    String runName = "runName_example"; // String | The workflow run name.
    String actionName = "actionName_example"; // String | The workflow action name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      ExpressionTraces result = apiInstance.workflowRunActionsListExpressionTraces(subscriptionId, resourceGroupName, workflowName, runName, actionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowRunActionsApi#workflowRunActionsListExpressionTraces");
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
| **runName** | **String**| The workflow run name. | |
| **actionName** | **String**| The workflow action name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**ExpressionTraces**](ExpressionTraces.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

