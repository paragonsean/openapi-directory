# JobExecutionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobExecutionsCancel**](JobExecutionsApi.md#jobExecutionsCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/cancel |  |
| [**jobExecutionsCreate**](JobExecutionsApi.md#jobExecutionsCreate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/start |  |
| [**jobExecutionsCreateOrUpdate**](JobExecutionsApi.md#jobExecutionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId} |  |
| [**jobExecutionsGet**](JobExecutionsApi.md#jobExecutionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId} |  |
| [**jobExecutionsListByAgent**](JobExecutionsApi.md#jobExecutionsListByAgent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/executions |  |
| [**jobExecutionsListByJob**](JobExecutionsApi.md#jobExecutionsListByJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions |  |


<a id="jobExecutionsCancel"></a>
# **jobExecutionsCancel**
> jobExecutionsCancel(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion)



Requests cancellation of a job execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobExecutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobExecutionsApi apiInstance = new JobExecutionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job.
    UUID jobExecutionId = UUID.randomUUID(); // UUID | The id of the job execution to cancel.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.jobExecutionsCancel(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobExecutionsApi#jobExecutionsCancel");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **jobAgentName** | **String**| The name of the job agent. | |
| **jobName** | **String**| The name of the job. | |
| **jobExecutionId** | **UUID**| The id of the job execution to cancel. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully requested cancellation of the job execution. |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="jobExecutionsCreate"></a>
# **jobExecutionsCreate**
> JobExecution jobExecutionsCreate(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion)



Starts an elastic job execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobExecutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobExecutionsApi apiInstance = new JobExecutionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job to get.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobExecution result = apiInstance.jobExecutionsCreate(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobExecutionsApi#jobExecutionsCreate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **jobAgentName** | **String**| The name of the job agent. | |
| **jobName** | **String**| The name of the job to get. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobExecution**](JobExecution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully started an execution for the job. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="jobExecutionsCreateOrUpdate"></a>
# **jobExecutionsCreateOrUpdate**
> JobExecution jobExecutionsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion)



Creates or updates a job execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobExecutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobExecutionsApi apiInstance = new JobExecutionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job to get.
    UUID jobExecutionId = UUID.randomUUID(); // UUID | The job execution id to create the job execution under.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobExecution result = apiInstance.jobExecutionsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobExecutionsApi#jobExecutionsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **jobAgentName** | **String**| The name of the job agent. | |
| **jobName** | **String**| The name of the job to get. | |
| **jobExecutionId** | **UUID**| The job execution id to create the job execution under. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobExecution**](JobExecution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A job execution for the job with the given id already existed. |  -  |
| **201** | Successfully started an execution for the job. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobExecutionsGet"></a>
# **jobExecutionsGet**
> JobExecution jobExecutionsGet(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion)



Gets a job execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobExecutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobExecutionsApi apiInstance = new JobExecutionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job.
    UUID jobExecutionId = UUID.randomUUID(); // UUID | The id of the job execution
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobExecution result = apiInstance.jobExecutionsGet(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobExecutionsApi#jobExecutionsGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **jobAgentName** | **String**| The name of the job agent. | |
| **jobName** | **String**| The name of the job. | |
| **jobExecutionId** | **UUID**| The id of the job execution | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobExecution**](JobExecution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the job. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobExecutionsListByAgent"></a>
# **jobExecutionsListByAgent**
> JobExecutionListResult jobExecutionsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, createTimeMin, createTimeMax, endTimeMin, endTimeMax, isActive, $skip, $top)



Lists all executions in a job agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobExecutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobExecutionsApi apiInstance = new JobExecutionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    OffsetDateTime createTimeMin = OffsetDateTime.now(); // OffsetDateTime | If specified, only job executions created at or after the specified time are included.
    OffsetDateTime createTimeMax = OffsetDateTime.now(); // OffsetDateTime | If specified, only job executions created before the specified time are included.
    OffsetDateTime endTimeMin = OffsetDateTime.now(); // OffsetDateTime | If specified, only job executions completed at or after the specified time are included.
    OffsetDateTime endTimeMax = OffsetDateTime.now(); // OffsetDateTime | If specified, only job executions completed before the specified time are included.
    Boolean isActive = true; // Boolean | If specified, only active or only completed job executions are included.
    Integer $skip = 56; // Integer | The number of elements in the collection to skip.
    Integer $top = 56; // Integer | The number of elements to return from the collection.
    try {
      JobExecutionListResult result = apiInstance.jobExecutionsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, createTimeMin, createTimeMax, endTimeMin, endTimeMax, isActive, $skip, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobExecutionsApi#jobExecutionsListByAgent");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **jobAgentName** | **String**| The name of the job agent. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **createTimeMin** | **OffsetDateTime**| If specified, only job executions created at or after the specified time are included. | [optional] |
| **createTimeMax** | **OffsetDateTime**| If specified, only job executions created before the specified time are included. | [optional] |
| **endTimeMin** | **OffsetDateTime**| If specified, only job executions completed at or after the specified time are included. | [optional] |
| **endTimeMax** | **OffsetDateTime**| If specified, only job executions completed before the specified time are included. | [optional] |
| **isActive** | **Boolean**| If specified, only active or only completed job executions are included. | [optional] |
| **$skip** | **Integer**| The number of elements in the collection to skip. | [optional] |
| **$top** | **Integer**| The number of elements to return from the collection. | [optional] |

### Return type

[**JobExecutionListResult**](JobExecutionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved job executions. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobExecutionsListByJob"></a>
# **jobExecutionsListByJob**
> JobExecutionListResult jobExecutionsListByJob(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, createTimeMin, createTimeMax, endTimeMin, endTimeMax, isActive, $skip, $top)



Lists a job&#39;s executions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobExecutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobExecutionsApi apiInstance = new JobExecutionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job to get.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    OffsetDateTime createTimeMin = OffsetDateTime.now(); // OffsetDateTime | If specified, only job executions created at or after the specified time are included.
    OffsetDateTime createTimeMax = OffsetDateTime.now(); // OffsetDateTime | If specified, only job executions created before the specified time are included.
    OffsetDateTime endTimeMin = OffsetDateTime.now(); // OffsetDateTime | If specified, only job executions completed at or after the specified time are included.
    OffsetDateTime endTimeMax = OffsetDateTime.now(); // OffsetDateTime | If specified, only job executions completed before the specified time are included.
    Boolean isActive = true; // Boolean | If specified, only active or only completed job executions are included.
    Integer $skip = 56; // Integer | The number of elements in the collection to skip.
    Integer $top = 56; // Integer | The number of elements to return from the collection.
    try {
      JobExecutionListResult result = apiInstance.jobExecutionsListByJob(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion, createTimeMin, createTimeMax, endTimeMin, endTimeMax, isActive, $skip, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobExecutionsApi#jobExecutionsListByJob");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **jobAgentName** | **String**| The name of the job agent. | |
| **jobName** | **String**| The name of the job to get. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **createTimeMin** | **OffsetDateTime**| If specified, only job executions created at or after the specified time are included. | [optional] |
| **createTimeMax** | **OffsetDateTime**| If specified, only job executions created before the specified time are included. | [optional] |
| **endTimeMin** | **OffsetDateTime**| If specified, only job executions completed at or after the specified time are included. | [optional] |
| **endTimeMax** | **OffsetDateTime**| If specified, only job executions completed before the specified time are included. | [optional] |
| **isActive** | **Boolean**| If specified, only active or only completed job executions are included. | [optional] |
| **$skip** | **Integer**| The number of elements in the collection to skip. | [optional] |
| **$top** | **Integer**| The number of elements to return from the collection. | [optional] |

### Return type

[**JobExecutionListResult**](JobExecutionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved job executions. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

