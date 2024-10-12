# JobsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobsCreateOrUpdate**](JobsApi.md#jobsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName} |  |
| [**jobsDelete**](JobsApi.md#jobsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName} |  |
| [**jobsGet**](JobsApi.md#jobsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName} |  |
| [**jobsList**](JobsApi.md#jobsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs |  |
| [**jobsListJobHistory**](JobsApi.md#jobsListJobHistory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName}/history |  |
| [**jobsPatch**](JobsApi.md#jobsPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName} |  |
| [**jobsRun**](JobsApi.md#jobsRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/jobs/{jobName}/run |  |


<a id="jobsCreateOrUpdate"></a>
# **jobsCreateOrUpdate**
> JobDefinition jobsCreateOrUpdate(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, job)



Provisions a new job or updates an existing job.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String jobName = "jobName_example"; // String | The job name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    JobDefinition job = new JobDefinition(); // JobDefinition | The job definition.
    try {
      JobDefinition result = apiInstance.jobsCreateOrUpdate(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsCreateOrUpdate");
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
| **jobCollectionName** | **String**| The job collection name. | |
| **jobName** | **String**| The job name. | |
| **apiVersion** | **String**| The API version. | |
| **job** | [**JobDefinition**](JobDefinition.md)| The job definition. | |

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job has been successfully updated. |  -  |
| **201** | The job has been successfully created. |  -  |

<a id="jobsDelete"></a>
# **jobsDelete**
> jobsDelete(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion)



Deletes a job.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String jobName = "jobName_example"; // String | The job name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.jobsDelete(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsDelete");
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
| **jobCollectionName** | **String**| The job collection name. | |
| **jobName** | **String**| The job name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | The job has been successfully deleted. |  -  |

<a id="jobsGet"></a>
# **jobsGet**
> JobDefinition jobsGet(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion)



Gets a job.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String jobName = "jobName_example"; // String | The job name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      JobDefinition result = apiInstance.jobsGet(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion);
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **jobCollectionName** | **String**| The job collection name. | |
| **jobName** | **String**| The job name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job has been successfully returned. |  -  |

<a id="jobsList"></a>
# **jobsList**
> JobListResult jobsList(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, $top, $skip, $filter)



Lists all jobs under the specified job collection.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of jobs to request, in the of range [1..100].
    Integer $skip = 56; // Integer | The (0-based) index of the job history list from which to begin requesting entries.
    String $filter = "$filter_example"; // String | The filter to apply on the job state.
    try {
      JobListResult result = apiInstance.jobsList(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, $top, $skip, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsList");
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
| **jobCollectionName** | **String**| The job collection name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of jobs to request, in the of range [1..100]. | [optional] |
| **$skip** | **Integer**| The (0-based) index of the job history list from which to begin requesting entries. | [optional] |
| **$filter** | **String**| The filter to apply on the job state. | [optional] |

### Return type

[**JobListResult**](JobListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job has been successfully returned. |  -  |

<a id="jobsListJobHistory"></a>
# **jobsListJobHistory**
> JobHistoryListResult jobsListJobHistory(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, $top, $skip, $filter)



Lists job history.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String jobName = "jobName_example"; // String | The job name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | the number of job history to request, in the of range [1..100].
    Integer $skip = 56; // Integer | The (0-based) index of the job history list from which to begin requesting entries.
    String $filter = "$filter_example"; // String | The filter to apply on the job state.
    try {
      JobHistoryListResult result = apiInstance.jobsListJobHistory(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, $top, $skip, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsListJobHistory");
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
| **jobCollectionName** | **String**| The job collection name. | |
| **jobName** | **String**| The job name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| the number of job history to request, in the of range [1..100]. | [optional] |
| **$skip** | **Integer**| The (0-based) index of the job history list from which to begin requesting entries. | [optional] |
| **$filter** | **String**| The filter to apply on the job state. | [optional] |

### Return type

[**JobHistoryListResult**](JobHistoryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job histories have been successfully returned. |  -  |

<a id="jobsPatch"></a>
# **jobsPatch**
> JobDefinition jobsPatch(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, job)



Patches an existing job.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String jobName = "jobName_example"; // String | The job name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    JobDefinition job = new JobDefinition(); // JobDefinition | The job definition.
    try {
      JobDefinition result = apiInstance.jobsPatch(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion, job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsPatch");
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
| **jobCollectionName** | **String**| The job collection name. | |
| **jobName** | **String**| The job name. | |
| **apiVersion** | **String**| The API version. | |
| **job** | [**JobDefinition**](JobDefinition.md)| The job definition. | |

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job has been successfully patched. |  -  |

<a id="jobsRun"></a>
# **jobsRun**
> jobsRun(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion)



Runs a job.

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
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String jobName = "jobName_example"; // String | The job name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.jobsRun(subscriptionId, resourceGroupName, jobCollectionName, jobName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobsApi#jobsRun");
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
| **jobCollectionName** | **String**| The job collection name. | |
| **jobName** | **String**| The job name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | The job has been successfully run. |  -  |

