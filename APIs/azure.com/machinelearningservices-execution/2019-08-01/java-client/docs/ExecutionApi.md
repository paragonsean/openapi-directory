# ExecutionApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**executionCancelRunWithUri**](ExecutionApi.md#executionCancelRunWithUri) | **POST** /execution/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentName}/runId/{runId}/cancel | Cancel a run. |
| [**executionStartLocalRun**](ExecutionApi.md#executionStartLocalRun) | **POST** /execution/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentName}/startlocalrun | Start a run on a local machine. |
| [**executionStartRun**](ExecutionApi.md#executionStartRun) | **POST** /execution/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentName}/startrun | Start a run on a remote compute target. |
| [**executionStartSnapshotRun**](ExecutionApi.md#executionStartSnapshotRun) | **POST** /execution/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/experiments/{experimentName}/snapshotrun | Start a run from a snapshot on a remote compute target. |


<a id="executionCancelRunWithUri"></a>
# **executionCancelRunWithUri**
> StartRunResult executionCancelRunWithUri(subscriptionId, resourceGroupName, workspaceName, experimentName, runId)

Cancel a run.

Cancels a run within an experiment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExecutionApi apiInstance = new ExecutionApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String experimentName = "experimentName_example"; // String | The experiment name.
    String runId = "runId_example"; // String | The id of the run to cancel.
    try {
      StartRunResult result = apiInstance.executionCancelRunWithUri(subscriptionId, resourceGroupName, workspaceName, experimentName, runId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecutionApi#executionCancelRunWithUri");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **experimentName** | **String**| The experiment name. | |
| **runId** | **String**| The id of the run to cancel. | |

### Return type

[**StartRunResult**](StartRunResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The run was successfully cancelled. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="executionStartLocalRun"></a>
# **executionStartLocalRun**
> File executionStartLocalRun(subscriptionId, resourceGroupName, workspaceName, experimentName, definition, runId)

Start a run on a local machine.

Starts an experiment run using the provided definition.json file to define the run.              The source code and configuration is defined in a zip archive in project.zip.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExecutionApi apiInstance = new ExecutionApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String experimentName = "experimentName_example"; // String | The experiment name.
    RunDefinition definition = new RunDefinition(); // RunDefinition | A JSON run definition structure.
    String runId = "runId_example"; // String | A run id. If not supplied a run id will be created automatically.
    try {
      File result = apiInstance.executionStartLocalRun(subscriptionId, resourceGroupName, workspaceName, experimentName, definition, runId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecutionApi#executionStartLocalRun");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **experimentName** | **String**| The experiment name. | |
| **definition** | [**RunDefinition**](RunDefinition.md)| A JSON run definition structure. | |
| **runId** | **String**| A run id. If not supplied a run id will be created automatically. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File Response |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="executionStartRun"></a>
# **executionStartRun**
> StartRunResult executionStartRun(subscriptionId, resourceGroupName, workspaceName, experimentName, runDefinitionFile, projectZipFile, runId)

Start a run on a remote compute target.

Starts an experiment run using the provided definition.json file to define the run.              The source code and configuration is defined in a zip archive in project.zip.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExecutionApi apiInstance = new ExecutionApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String experimentName = "experimentName_example"; // String | The experiment name.
    File runDefinitionFile = new File("/path/to/file"); // File | The JSON file containing the RunDefinition
    File projectZipFile = new File("/path/to/file"); // File | The zip archive of the project folder containing the source code to use for the run.
    String runId = "runId_example"; // String | A run id. If not supplied a run id will be created automatically.
    try {
      StartRunResult result = apiInstance.executionStartRun(subscriptionId, resourceGroupName, workspaceName, experimentName, runDefinitionFile, projectZipFile, runId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecutionApi#executionStartRun");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **experimentName** | **String**| The experiment name. | |
| **runDefinitionFile** | **File**| The JSON file containing the RunDefinition | |
| **projectZipFile** | **File**| The zip archive of the project folder containing the source code to use for the run. | |
| **runId** | **String**| A run id. If not supplied a run id will be created automatically. | [optional] |

### Return type

[**StartRunResult**](StartRunResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A run was successfully started. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="executionStartSnapshotRun"></a>
# **executionStartSnapshotRun**
> StartRunResult executionStartSnapshotRun(subscriptionId, resourceGroupName, workspaceName, experimentName, definition, runId)

Start a run from a snapshot on a remote compute target.

Starts an experiment run on the remote compute target using the provided definition.json file to define the run.              The code for the run is retrieved using the snapshotId in definition.json.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecutionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExecutionApi apiInstance = new ExecutionApi(defaultClient);
    UUID subscriptionId = UUID.randomUUID(); // UUID | The Azure Subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The Name of the resource group in which the workspace is located.
    String workspaceName = "workspaceName_example"; // String | The name of the workspace.
    String experimentName = "experimentName_example"; // String | The experiment name.
    RunDefinition definition = new RunDefinition(); // RunDefinition | A JSON run definition structure.
    String runId = "runId_example"; // String | A run id. If not supplied a run id will be created automatically.
    try {
      StartRunResult result = apiInstance.executionStartSnapshotRun(subscriptionId, resourceGroupName, workspaceName, experimentName, definition, runId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecutionApi#executionStartSnapshotRun");
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
| **subscriptionId** | **UUID**| The Azure Subscription ID. | |
| **resourceGroupName** | **String**| The Name of the resource group in which the workspace is located. | |
| **workspaceName** | **String**| The name of the workspace. | |
| **experimentName** | **String**| The experiment name. | |
| **definition** | [**RunDefinition**](RunDefinition.md)| A JSON run definition structure. | |
| **runId** | **String**| A run id. If not supplied a run id will be created automatically. | [optional] |

### Return type

[**StartRunResult**](StartRunResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A snapshot run was successfully started. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

