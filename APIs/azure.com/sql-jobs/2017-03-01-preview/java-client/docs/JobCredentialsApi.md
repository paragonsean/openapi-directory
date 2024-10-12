# JobCredentialsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobCredentialsCreateOrUpdate**](JobCredentialsApi.md#jobCredentialsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/credentials/{credentialName} |  |
| [**jobCredentialsDelete**](JobCredentialsApi.md#jobCredentialsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/credentials/{credentialName} |  |
| [**jobCredentialsGet**](JobCredentialsApi.md#jobCredentialsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/credentials/{credentialName} |  |
| [**jobCredentialsListByAgent**](JobCredentialsApi.md#jobCredentialsListByAgent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/jobAgents/{jobAgentName}/credentials |  |


<a id="jobCredentialsCreateOrUpdate"></a>
# **jobCredentialsCreateOrUpdate**
> JobCredential jobCredentialsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion, parameters)



Creates or updates a job credential.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobCredentialsApi apiInstance = new JobCredentialsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String credentialName = "credentialName_example"; // String | The name of the credential.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    JobCredential parameters = new JobCredential(); // JobCredential | The requested job credential state.
    try {
      JobCredential result = apiInstance.jobCredentialsCreateOrUpdate(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCredentialsApi#jobCredentialsCreateOrUpdate");
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
| **credentialName** | **String**| The name of the credential. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**JobCredential**](JobCredential.md)| The requested job credential state. | |

### Return type

[**JobCredential**](JobCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the credential. |  -  |
| **201** | Successfully created the credential. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 400 InvalidJobCredentialUsername - Invalid credential username.   * 403 JobCredentialPermissionError - Azure Resource Manager does not have permission to use or manage the credential.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

<a id="jobCredentialsDelete"></a>
# **jobCredentialsDelete**
> jobCredentialsDelete(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion)



Deletes a job credential.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobCredentialsApi apiInstance = new JobCredentialsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String credentialName = "credentialName_example"; // String | The name of the credential.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.jobCredentialsDelete(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCredentialsApi#jobCredentialsDelete");
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
| **credentialName** | **String**| The name of the credential. | |
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
| **200** | Successfully deleted the credential. |  -  |
| **204** | A credential with the specified name does not exist. |  -  |
| **0** | *** Error Responses: ***   * 403 JobCredentialPermissionError - Azure Resource Manager does not have permission to use or manage the credential.   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="jobCredentialsGet"></a>
# **jobCredentialsGet**
> JobCredential jobCredentialsGet(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion)



Gets a jobs credential.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobCredentialsApi apiInstance = new JobCredentialsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String credentialName = "credentialName_example"; // String | The name of the credential.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobCredential result = apiInstance.jobCredentialsGet(resourceGroupName, serverName, jobAgentName, credentialName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCredentialsApi#jobCredentialsGet");
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
| **credentialName** | **String**| The name of the credential. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**JobCredential**](JobCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the job credential. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 ResourceNotFound - The requested resource was not found. |  -  |

<a id="jobCredentialsListByAgent"></a>
# **jobCredentialsListByAgent**
> JobCredentialListResult jobCredentialsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion)



Gets a list of jobs credentials.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    JobCredentialsApi apiInstance = new JobCredentialsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String jobAgentName = "jobAgentName_example"; // String | The name of the job agent.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      JobCredentialListResult result = apiInstance.jobCredentialsListByAgent(resourceGroupName, serverName, jobAgentName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCredentialsApi#jobCredentialsListByAgent");
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

[**JobCredentialListResult**](JobCredentialListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of job credentials. |  -  |
| **0** | *** Error Responses: ***   * 404 JobAgentNotFound - Specified job agent does not exist in the specified logical server.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found |  -  |

