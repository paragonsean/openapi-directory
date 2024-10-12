# JobAgentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobAgentsCreateOrUpdate**](JobAgentsApi.md#jobAgentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName} |  |
| [**jobAgentsDelete**](JobAgentsApi.md#jobAgentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName} |  |
| [**jobAgentsGet**](JobAgentsApi.md#jobAgentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName} |  |
| [**jobAgentsListByServer**](JobAgentsApi.md#jobAgentsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents |  |
| [**jobAgentsUpdate**](JobAgentsApi.md#jobAgentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName} |  |


<a id="jobAgentsCreateOrUpdate"></a>
# **jobAgentsCreateOrUpdate**
> JobAgent jobAgentsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, parameters)



Creates or updates a job agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobAgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobAgentsApi apiInstance = new JobAgentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent to be created or updated.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    JobAgent parameters = new JobAgent(); // JobAgent | The requested job agent resource state.
    try {
      JobAgent result = apiInstance.jobAgentsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobAgentsApi#jobAgentsCreateOrUpdate");
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
| **jobAgentName** | **String**| The name of the job agent to be created or updated. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**JobAgent**](JobAgent.md)| The requested job agent resource state. | |

### Return type

[**JobAgent**](JobAgent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the job agent. |  -  |
| **201** | Successfully created the job agent. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 MissingSkuName - Sku name is required.   * 400 InvalidDatabaseResourceId - Invalid database resource identifier.   * 400 MismatchingSubscriptionWithUrl - The provided subscription did not match the subscription in the Url.   * 400 MismatchingResourceGroupNameWithUrl - The provided resource group name did not match the name in the Url.   * 400 MismatchingServerNameWithUrl - The provided server name did not match the name in the Url.   * 400 DatabaseDoesNotExist - The requested database was not found   * 400 JobAgentExceededQuota - Could not create job agent because it would exceed the quota.   * 400 JobAgentAlreadyExists - The job agent already exists on the server.   * 400 JobAgentDatabaseEditionUnsupported - The specified database&#39;s service level objective is not supported for use as a job agent database.   * 400 JobAgentDatabaseSecondary - A job agent cannot be linked to a geo-secondary database.   * 400 JobAgentDatabaseAlreadyLinked - The specified database is already linked to another job agent.   * 400 CannotUseReservedDatabaseName - Cannot use reserved database name in this operation.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 SubscriptionNotFound - The requested subscription was not found.   * 404 PropertyChangeUnsupported - Property cannot be modified. |  -  |

<a id="jobAgentsDelete"></a>
# **jobAgentsDelete**
> jobAgentsDelete(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion)



Deletes a job agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobAgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobAgentsApi apiInstance = new JobAgentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent to be deleted.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.jobAgentsDelete(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobAgentsApi#jobAgentsDelete");
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
| **jobAgentName** | **String**| The name of the job agent to be deleted. | |
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
| **200** | Successfully deleted the job agent. |  -  |
| **202** | Accepted |  -  |
| **204** | The specified job agent does not exist. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server. |  -  |

<a id="jobAgentsGet"></a>
# **jobAgentsGet**
> JobAgent jobAgentsGet(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion)



Gets a job agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobAgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobAgentsApi apiInstance = new JobAgentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent to be retrieved.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobAgent result = apiInstance.jobAgentsGet(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobAgentsApi#jobAgentsGet");
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
| **jobAgentName** | **String**| The name of the job agent to be retrieved. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobAgent**](JobAgent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified job agent. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server. |  -  |

<a id="jobAgentsListByServer"></a>
# **jobAgentsListByServer**
> JobAgentListResult jobAgentsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of job agents in a server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobAgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobAgentsApi apiInstance = new JobAgentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobAgentListResult result = apiInstance.jobAgentsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobAgentsApi#jobAgentsListByServer");
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
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobAgentListResult**](JobAgentListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of job agents. |  -  |
| **0** | *** Error Responses: ***   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobAgentsUpdate"></a>
# **jobAgentsUpdate**
> JobAgent jobAgentsUpdate(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, parameters)



Updates a job agent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobAgentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobAgentsApi apiInstance = new JobAgentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent to be updated.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    JobAgentUpdate parameters = new JobAgentUpdate(); // JobAgentUpdate | The update to the job agent.
    try {
      JobAgent result = apiInstance.jobAgentsUpdate(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobAgentsApi#jobAgentsUpdate");
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
| **jobAgentName** | **String**| The name of the job agent to be updated. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**JobAgentUpdate**](JobAgentUpdate.md)| The update to the job agent. | |

### Return type

[**JobAgent**](JobAgent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the job agent. |  -  |
| **202** | Accepted |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 PropertyChangeUnsupported - Property cannot be modified. |  -  |

