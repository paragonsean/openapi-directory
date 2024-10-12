# RepairManagementApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelRepairTask**](RepairManagementApi.md#cancelRepairTask) | **POST** /$/CancelRepairTask | Requests the cancellation of the given repair task. |
| [**createRepairTask**](RepairManagementApi.md#createRepairTask) | **POST** /$/CreateRepairTask | Creates a new repair task. |
| [**deleteRepairTask**](RepairManagementApi.md#deleteRepairTask) | **POST** /$/DeleteRepairTask | Deletes a completed repair task. |
| [**forceApproveRepairTask**](RepairManagementApi.md#forceApproveRepairTask) | **POST** /$/ForceApproveRepairTask | Forces the approval of the given repair task. |
| [**getRepairTaskList**](RepairManagementApi.md#getRepairTaskList) | **GET** /$/GetRepairTaskList | Gets a list of repair tasks matching the given filters. |
| [**updateRepairExecutionState**](RepairManagementApi.md#updateRepairExecutionState) | **POST** /$/UpdateRepairExecutionState | Updates the execution state of a repair task. |
| [**updateRepairTaskHealthPolicy**](RepairManagementApi.md#updateRepairTaskHealthPolicy) | **POST** /$/UpdateRepairTaskHealthPolicy | Updates the health policy of the given repair task. |


<a id="cancelRepairTask"></a>
# **cancelRepairTask**
> RepairTaskUpdateInfo cancelRepairTask(apiVersion, repairTaskCancelDescription)

Requests the cancellation of the given repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepairManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    RepairManagementApi apiInstance = new RepairManagementApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    RepairTaskCancelDescription repairTaskCancelDescription = new RepairTaskCancelDescription(); // RepairTaskCancelDescription | Describes the repair task to be cancelled.
    try {
      RepairTaskUpdateInfo result = apiInstance.cancelRepairTask(apiVersion, repairTaskCancelDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepairManagementApi#cancelRepairTask");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **repairTaskCancelDescription** | [**RepairTaskCancelDescription**](RepairTaskCancelDescription.md)| Describes the repair task to be cancelled. | |

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. The response body provides information about the updated repair task. Success indicates that the cancellation request was recorded, but does not guarantee that the repair task will be cancelled. Clients may use the State property of the repair task to determine the current state of the repair task. |  -  |
| **0** | The detailed error response. |  -  |

<a id="createRepairTask"></a>
# **createRepairTask**
> RepairTaskUpdateInfo createRepairTask(apiVersion, repairTask)

Creates a new repair task.

For clusters that have the Repair Manager Service configured, this API provides a way to create repair tasks that run automatically or manually. For repair tasks that run automatically, an appropriate repair executor must be running for each repair action to run automatically. These are currently only available in specially-configured Azure Cloud Services.  To create a manual repair task, provide the set of impacted node names and the expected impact. When the state of the created repair task changes to approved, you can safely perform repair actions on those nodes.  This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepairManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    RepairManagementApi apiInstance = new RepairManagementApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    RepairTask repairTask = new RepairTask(); // RepairTask | Describes the repair task to be created or updated.
    try {
      RepairTaskUpdateInfo result = apiInstance.createRepairTask(apiVersion, repairTask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepairManagementApi#createRepairTask");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **repairTask** | [**RepairTask**](RepairTask.md)| Describes the repair task to be created or updated. | |

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. The response body provides information about the created repair task. |  -  |
| **0** | The detailed error response. |  -  |

<a id="deleteRepairTask"></a>
# **deleteRepairTask**
> deleteRepairTask(apiVersion, repairTaskDeleteDescription)

Deletes a completed repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepairManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    RepairManagementApi apiInstance = new RepairManagementApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    RepairTaskDeleteDescription repairTaskDeleteDescription = new RepairTaskDeleteDescription(); // RepairTaskDeleteDescription | Describes the repair task to be deleted.
    try {
      apiInstance.deleteRepairTask(apiVersion, repairTaskDeleteDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepairManagementApi#deleteRepairTask");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **repairTaskDeleteDescription** | [**RepairTaskDeleteDescription**](RepairTaskDeleteDescription.md)| Describes the repair task to be deleted. | |

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
| **200** | A successful operation will return 200 status code. |  -  |
| **0** | The detailed error response. |  -  |

<a id="forceApproveRepairTask"></a>
# **forceApproveRepairTask**
> RepairTaskUpdateInfo forceApproveRepairTask(apiVersion, repairTaskApproveDescription)

Forces the approval of the given repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepairManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    RepairManagementApi apiInstance = new RepairManagementApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    RepairTaskApproveDescription repairTaskApproveDescription = new RepairTaskApproveDescription(); // RepairTaskApproveDescription | Describes the repair task to be approved.
    try {
      RepairTaskUpdateInfo result = apiInstance.forceApproveRepairTask(apiVersion, repairTaskApproveDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepairManagementApi#forceApproveRepairTask");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **repairTaskApproveDescription** | [**RepairTaskApproveDescription**](RepairTaskApproveDescription.md)| Describes the repair task to be approved. | |

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. The response body provides information about the updated repair task. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getRepairTaskList"></a>
# **getRepairTaskList**
> List&lt;RepairTask&gt; getRepairTaskList(apiVersion, taskIdFilter, stateFilter, executorFilter)

Gets a list of repair tasks matching the given filters.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepairManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    RepairManagementApi apiInstance = new RepairManagementApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    String taskIdFilter = "taskIdFilter_example"; // String | The repair task ID prefix to be matched.
    Integer stateFilter = 56; // Integer | A bitwise-OR of the following values, specifying which task states should be included in the result list.  - 1 - Created - 2 - Claimed - 4 - Preparing - 8 - Approved - 16 - Executing - 32 - Restoring - 64 - Completed
    String executorFilter = "executorFilter_example"; // String | The name of the repair executor whose claimed tasks should be included in the list.
    try {
      List<RepairTask> result = apiInstance.getRepairTaskList(apiVersion, taskIdFilter, stateFilter, executorFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepairManagementApi#getRepairTaskList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **taskIdFilter** | **String**| The repair task ID prefix to be matched. | [optional] |
| **stateFilter** | **Integer**| A bitwise-OR of the following values, specifying which task states should be included in the result list.  - 1 - Created - 2 - Claimed - 4 - Preparing - 8 - Approved - 16 - Executing - 32 - Restoring - 64 - Completed | [optional] |
| **executorFilter** | **String**| The name of the repair executor whose claimed tasks should be included in the list. | [optional] |

### Return type

[**List&lt;RepairTask&gt;**](RepairTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. The response body provides a list of repair tasks matching all of the given filters. |  -  |
| **0** | The detailed error response. |  -  |

<a id="updateRepairExecutionState"></a>
# **updateRepairExecutionState**
> RepairTaskUpdateInfo updateRepairExecutionState(apiVersion, repairTask)

Updates the execution state of a repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepairManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    RepairManagementApi apiInstance = new RepairManagementApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    RepairTask repairTask = new RepairTask(); // RepairTask | Describes the repair task to be created or updated.
    try {
      RepairTaskUpdateInfo result = apiInstance.updateRepairExecutionState(apiVersion, repairTask);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepairManagementApi#updateRepairExecutionState");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **repairTask** | [**RepairTask**](RepairTask.md)| Describes the repair task to be created or updated. | |

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. The response body provides information about the updated repair task. |  -  |
| **0** | The detailed error response. |  -  |

<a id="updateRepairTaskHealthPolicy"></a>
# **updateRepairTaskHealthPolicy**
> RepairTaskUpdateInfo updateRepairTaskHealthPolicy(apiVersion, repairTaskUpdateHealthPolicyDescription)

Updates the health policy of the given repair task.

This API supports the Service Fabric platform; it is not meant to be used directly from your code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepairManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    RepairManagementApi apiInstance = new RepairManagementApi(defaultClient);
    String apiVersion = "6.0"; // String | The version of the API. This parameter is required and its value must be '6.0'.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version.
    RepairTaskUpdateHealthPolicyDescription repairTaskUpdateHealthPolicyDescription = new RepairTaskUpdateHealthPolicyDescription(); // RepairTaskUpdateHealthPolicyDescription | Describes the repair task healthy policy to be updated.
    try {
      RepairTaskUpdateInfo result = apiInstance.updateRepairTaskHealthPolicy(apiVersion, repairTaskUpdateHealthPolicyDescription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepairManagementApi#updateRepairTaskHealthPolicy");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.0&#39;.  Service Fabric REST API version is based on the runtime version in which the API was introduced or was changed. Service Fabric runtime supports more than one version of the API. This is the latest supported version of the API. If a lower API version is passed, the returned response may be different from the one documented in this specification.  Additionally the runtime accept any version that is higher than the latest supported version up to the current version of the runtime. So if the latest API version is 6.0, but if the runtime is 6.1, in order to make it easier to write the clients, the runtime will accept version 6.1 for that API. However the behavior of the API will be as per the documented 6.0 version. | [default to 6.0] [enum: 6.0] |
| **repairTaskUpdateHealthPolicyDescription** | [**RepairTaskUpdateHealthPolicyDescription**](RepairTaskUpdateHealthPolicyDescription.md)| Describes the repair task healthy policy to be updated. | |

### Return type

[**RepairTaskUpdateInfo**](RepairTaskUpdateInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code. The response body provides information about the updated repair task. |  -  |
| **0** | The detailed error response. |  -  |

