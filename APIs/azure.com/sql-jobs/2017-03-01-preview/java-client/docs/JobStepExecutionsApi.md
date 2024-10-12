# JobStepExecutionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobStepExecutionsGet**](JobStepExecutionsApi.md#jobStepExecutionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps/{stepName} |  |
| [**jobStepExecutionsListByJobExecution**](JobStepExecutionsApi.md#jobStepExecutionsListByJobExecution) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/executions/{jobExecutionId}/steps |  |


<a id="jobStepExecutionsGet"></a>
# **jobStepExecutionsGet**
> JobExecution jobStepExecutionsGet(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, stepName, subscriptionId, apiVersion)



Gets a step execution of a job execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobStepExecutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobStepExecutionsApi apiInstance = new JobStepExecutionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job to get.
    UUID jobExecutionId = UUID.randomUUID(); // UUID | The unique id of the job execution
    String stepName = "stepName_example"; // String | The name of the step.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobExecution result = apiInstance.jobStepExecutionsGet(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, stepName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobStepExecutionsApi#jobStepExecutionsGet");
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
| **jobExecutionId** | **UUID**| The unique id of the job execution | |
| **stepName** | **String**| The name of the step. | |
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
| **200** | Successfully retrieved the step execution. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="jobStepExecutionsListByJobExecution"></a>
# **jobStepExecutionsListByJobExecution**
> JobExecutionListResult jobStepExecutionsListByJobExecution(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion, createTimeMin, createTimeMax, endTimeMin, endTimeMax, isActive, $skip, $top)



Lists the step executions of a job execution.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobStepExecutionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobStepExecutionsApi apiInstance = new JobStepExecutionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job to get.
    UUID jobExecutionId = UUID.randomUUID(); // UUID | The id of the job execution
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
      JobExecutionListResult result = apiInstance.jobStepExecutionsListByJobExecution(resourceGroupName, serverName, jobAgentName, jobName, jobExecutionId, subscriptionId, apiVersion, createTimeMin, createTimeMax, endTimeMin, endTimeMax, isActive, $skip, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobStepExecutionsApi#jobStepExecutionsListByJobExecution");
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
| **jobExecutionId** | **UUID**| The id of the job execution | |
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
| **200** | Successfully retrieved the step executions. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

