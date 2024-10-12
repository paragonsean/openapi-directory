# JobsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobsCancel**](JobsApi.md#jobsCancel) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/jobs/{jobId}/cancel |  |
| [**jobsGet**](JobsApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/jobs/{jobId} |  |
| [**jobsListByDataManager**](JobsApi.md#jobsListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/jobs |  |
| [**jobsListByDataService**](JobsApi.md#jobsListByDataService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobs |  |
| [**jobsListByJobDefinition**](JobsApi.md#jobsListByJobDefinition) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/jobs |  |
| [**jobsResume**](JobsApi.md#jobsResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/jobs/{jobId}/resume |  |


<a id="jobsCancel"></a>
# **jobsCancel**
> jobsCancel(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Cancels the given job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The name of the data service of the job definition.
    String jobDefinitionName = "jobDefinitionName_example"; // String | The name of the job definition of the job.
    String jobId = "jobId_example"; // String | The job id of the job queried.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      apiInstance.jobsCancel(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsCancel");
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
| **dataServiceName** | **String**| The name of the data service of the job definition. | |
| **jobDefinitionName** | **String**| The name of the job definition of the job. | |
| **jobId** | **String**| The job id of the job queried. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted job cancellation request. |  -  |
| **204** | Job cancelled. |  -  |

<a id="jobsGet"></a>
# **jobsGet**
> Job jobsGet(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion, $expand)



This method gets a data manager job given the jobId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The name of the data service of the job definition.
    String jobDefinitionName = "jobDefinitionName_example"; // String | The name of the job definition of the job.
    String jobId = "jobId_example"; // String | The job id of the job queried.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    String $expand = "$expand_example"; // String | $expand is supported on details parameter for job, which provides details on the job stages.
    try {
      Job result = apiInstance.jobsGet(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsGet");
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
| **dataServiceName** | **String**| The name of the data service of the job definition. | |
| **jobDefinitionName** | **String**| The name of the job definition of the job. | |
| **jobId** | **String**| The job id of the job queried. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **$expand** | **String**| $expand is supported on details parameter for job, which provides details on the job stages. | [optional] |

### Return type

[**Job**](Job.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job that matches the given criteria. |  -  |

<a id="jobsListByDataManager"></a>
# **jobsListByDataManager**
> JobList jobsListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter)



This method gets all the jobs at the data manager resource level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      JobList result = apiInstance.jobsListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsListByDataManager");
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
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **$filter** | **String**| OData Filter options | [optional] |

### Return type

[**JobList**](JobList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of jobs in the resource specified. |  -  |

<a id="jobsListByDataService"></a>
# **jobsListByDataService**
> JobList jobsListByDataService(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter)



This method gets all the jobs of a data service type in a given resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The name of the data service of interest.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      JobList result = apiInstance.jobsListByDataService(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsListByDataService");
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
| **dataServiceName** | **String**| The name of the data service of interest. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **$filter** | **String**| OData Filter options | [optional] |

### Return type

[**JobList**](JobList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of jobs that match the service and resource. |  -  |

<a id="jobsListByJobDefinition"></a>
# **jobsListByJobDefinition**
> JobList jobsListByJobDefinition(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter)



This method gets all the jobs of a given job definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The name of the data service of the job definition.
    String jobDefinitionName = "jobDefinitionName_example"; // String | The name of the job definition for which jobs are needed.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      JobList result = apiInstance.jobsListByJobDefinition(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsListByJobDefinition");
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
| **dataServiceName** | **String**| The name of the data service of the job definition. | |
| **jobDefinitionName** | **String**| The name of the job definition for which jobs are needed. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **$filter** | **String**| OData Filter options | [optional] |

### Return type

[**JobList**](JobList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of jobs. |  -  |

<a id="jobsResume"></a>
# **jobsResume**
> jobsResume(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Resumes the given job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobsApi apiInstance = new JobsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The name of the data service of the job definition.
    String jobDefinitionName = "jobDefinitionName_example"; // String | The name of the job definition of the job.
    String jobId = "jobId_example"; // String | The job id of the job queried.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      apiInstance.jobsResume(dataServiceName, jobDefinitionName, jobId, subscriptionId, resourceGroupName, dataManagerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsResume");
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
| **dataServiceName** | **String**| The name of the data service of the job definition. | |
| **jobDefinitionName** | **String**| The name of the job definition of the job. | |
| **jobId** | **String**| The job id of the job queried. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted job resume request. |  -  |
| **204** | Job resumed. |  -  |

