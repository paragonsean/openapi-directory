# JobTargetGroupsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobTargetGroupsCreateOrUpdate**](JobTargetGroupsApi.md#jobTargetGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/targetGroups/{targetGroupName} |  |
| [**jobTargetGroupsDelete**](JobTargetGroupsApi.md#jobTargetGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/targetGroups/{targetGroupName} |  |
| [**jobTargetGroupsGet**](JobTargetGroupsApi.md#jobTargetGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/targetGroups/{targetGroupName} |  |
| [**jobTargetGroupsListByAgent**](JobTargetGroupsApi.md#jobTargetGroupsListByAgent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/targetGroups |  |


<a id="jobTargetGroupsCreateOrUpdate"></a>
# **jobTargetGroupsCreateOrUpdate**
> JobTargetGroup jobTargetGroupsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion, parameters)



Creates or updates a target group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobTargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobTargetGroupsApi apiInstance = new JobTargetGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String targetGroupName = "targetGroupName_example"; // String | The name of the target group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    JobTargetGroup parameters = new JobTargetGroup(); // JobTargetGroup | The requested state of the target group.
    try {
      JobTargetGroup result = apiInstance.jobTargetGroupsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobTargetGroupsApi#jobTargetGroupsCreateOrUpdate");
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
| **targetGroupName** | **String**| The name of the target group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**JobTargetGroup**](JobTargetGroup.md)| The requested state of the target group. | |

### Return type

[**JobTargetGroup**](JobTargetGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the target group. |  -  |
| **201** | Successfully created the target group. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 InvalidResourceId - Invalid resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 MismatchingJobAccountNameWithUrl - The provided job account name did not match the name in the Url.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobTargetGroupsDelete"></a>
# **jobTargetGroupsDelete**
> jobTargetGroupsDelete(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion)



Deletes a target group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobTargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobTargetGroupsApi apiInstance = new JobTargetGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String targetGroupName = "targetGroupName_example"; // String | The name of the target group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.jobTargetGroupsDelete(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobTargetGroupsApi#jobTargetGroupsDelete");
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
| **targetGroupName** | **String**| The name of the target group. | |
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
| **200** | Successfully deleted the target group. |  -  |
| **204** | A target group with the specified name does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 400 ElasticJobsOperationFailed - Elastic jobs management operation failed.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="jobTargetGroupsGet"></a>
# **jobTargetGroupsGet**
> JobTargetGroup jobTargetGroupsGet(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion)



Gets a target group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobTargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobTargetGroupsApi apiInstance = new JobTargetGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String targetGroupName = "targetGroupName_example"; // String | The name of the target group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobTargetGroup result = apiInstance.jobTargetGroupsGet(resourceGroupName, serverName, jobAgentName, targetGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobTargetGroupsApi#jobTargetGroupsGet");
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
| **targetGroupName** | **String**| The name of the target group. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobTargetGroup**](JobTargetGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the target group. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="jobTargetGroupsListByAgent"></a>
# **jobTargetGroupsListByAgent**
> JobTargetGroupListResult jobTargetGroupsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion)



Gets all target groups in an agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobTargetGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobTargetGroupsApi apiInstance = new JobTargetGroupsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobTargetGroupListResult result = apiInstance.jobTargetGroupsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobTargetGroupsApi#jobTargetGroupsListByAgent");
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

### Return type

[**JobTargetGroupListResult**](JobTargetGroupListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of target groups. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

