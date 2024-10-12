# JobStepsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobStepsCreateOrUpdate**](JobStepsApi.md#jobStepsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/steps/{stepName} |  |
| [**jobStepsDelete**](JobStepsApi.md#jobStepsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/steps/{stepName} |  |
| [**jobStepsGet**](JobStepsApi.md#jobStepsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/steps/{stepName} |  |
| [**jobStepsGetByVersion**](JobStepsApi.md#jobStepsGetByVersion) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/versions/{jobVersion}/steps/{stepName} |  |
| [**jobStepsListByJob**](JobStepsApi.md#jobStepsListByJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/steps |  |
| [**jobStepsListByVersion**](JobStepsApi.md#jobStepsListByVersion) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/jobs/{jobName}/versions/{jobVersion}/steps |  |


<a id="jobStepsCreateOrUpdate"></a>
# **jobStepsCreateOrUpdate**
> JobStep jobStepsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, jobName, stepName, subscriptionId, apiVersion, parameters)



Creates or updates a job step. This will implicitly create a new job version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobStepsApi apiInstance = new JobStepsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job.
    String stepName = "stepName_example"; // String | The name of the job step.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    JobStep parameters = new JobStep(); // JobStep | The requested state of the job step.
    try {
      JobStep result = apiInstance.jobStepsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, jobName, stepName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobStepsApi#jobStepsCreateOrUpdate");
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
| **stepName** | **String**| The name of the job step. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**JobStep**](JobStep.md)| The requested state of the job step. | |

### Return type

[**JobStep**](JobStep.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the job step. |  -  |
| **201** | Successfully added the job step. |  -  |
| **0** | *** Error Responses: ***   * 400 JobStepIdMismatch - Step Id in the specified Job Step URI does not match step id in provided Job Step Resource.   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 InvalidResourceId - Invalid resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 MismatchingJobAccountNameWithUrl - The provided job account name did not match the name in the Url.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobStepsDelete"></a>
# **jobStepsDelete**
> jobStepsDelete(resourceGroupName, serverName, jobAgentName, jobName, stepName, subscriptionId, apiVersion)



Deletes a job step. This will implicitly create a new job version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobStepsApi apiInstance = new JobStepsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job.
    String stepName = "stepName_example"; // String | The name of the job step to delete.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.jobStepsDelete(resourceGroupName, serverName, jobAgentName, jobName, stepName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobStepsApi#jobStepsDelete");
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
| **stepName** | **String**| The name of the job step to delete. | |
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
| **200** | Successfully deleted the job step. |  -  |
| **204** | The specified job step does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="jobStepsGet"></a>
# **jobStepsGet**
> JobStep jobStepsGet(resourceGroupName, serverName, jobAgentName, jobName, stepName, subscriptionId, apiVersion)



Gets a job step in a job&#39;s current version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobStepsApi apiInstance = new JobStepsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job.
    String stepName = "stepName_example"; // String | The name of the job step.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobStep result = apiInstance.jobStepsGet(resourceGroupName, serverName, jobAgentName, jobName, stepName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobStepsApi#jobStepsGet");
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
| **stepName** | **String**| The name of the job step. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobStep**](JobStep.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the job step. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobStepsGetByVersion"></a>
# **jobStepsGetByVersion**
> JobStep jobStepsGetByVersion(resourceGroupName, serverName, jobAgentName, jobName, jobVersion, stepName, subscriptionId, apiVersion)



Gets the specified version of a job step.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobStepsApi apiInstance = new JobStepsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job.
    Integer jobVersion = 56; // Integer | The version of the job to get.
    String stepName = "stepName_example"; // String | The name of the job step.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobStep result = apiInstance.jobStepsGetByVersion(resourceGroupName, serverName, jobAgentName, jobName, jobVersion, stepName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobStepsApi#jobStepsGetByVersion");
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
| **jobVersion** | **Integer**| The version of the job to get. | |
| **stepName** | **String**| The name of the job step. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobStep**](JobStep.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the job step. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobStepsListByJob"></a>
# **jobStepsListByJob**
> JobStepListResult jobStepsListByJob(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion)



Gets all job steps for a job&#39;s current version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobStepsApi apiInstance = new JobStepsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job to get.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobStepListResult result = apiInstance.jobStepsListByJob(resourceGroupName, serverName, jobAgentName, jobName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobStepsApi#jobStepsListByJob");
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

[**JobStepListResult**](JobStepListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of job steps. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobStepsListByVersion"></a>
# **jobStepsListByVersion**
> JobStepListResult jobStepsListByVersion(resourceGroupName, serverName, jobAgentName, jobName, jobVersion, subscriptionId, apiVersion)



Gets all job steps in the specified job version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobStepsApi apiInstance = new JobStepsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String jobName = "jobName_example"; // String | The name of the job to get.
    Integer jobVersion = 56; // Integer | The version of the job to get.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobStepListResult result = apiInstance.jobStepsListByVersion(resourceGroupName, serverName, jobAgentName, jobName, jobVersion, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobStepsApi#jobStepsListByVersion");
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
| **jobVersion** | **Integer**| The version of the job to get. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobStepListResult**](JobStepListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of job steps. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 ResourceNotFound - The requested resource was not found.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

