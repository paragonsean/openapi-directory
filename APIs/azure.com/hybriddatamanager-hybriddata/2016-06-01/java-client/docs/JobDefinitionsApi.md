# JobDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobDefinitionsCreateOrUpdate**](JobDefinitionsApi.md#jobDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName} |  |
| [**jobDefinitionsDelete**](JobDefinitionsApi.md#jobDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName} |  |
| [**jobDefinitionsGet**](JobDefinitionsApi.md#jobDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName} |  |
| [**jobDefinitionsListByDataManager**](JobDefinitionsApi.md#jobDefinitionsListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/jobDefinitions |  |
| [**jobDefinitionsListByDataService**](JobDefinitionsApi.md#jobDefinitionsListByDataService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions |  |
| [**jobDefinitionsRun**](JobDefinitionsApi.md#jobDefinitionsRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName}/jobDefinitions/{jobDefinitionName}/run |  |


<a id="jobDefinitionsCreateOrUpdate"></a>
# **jobDefinitionsCreateOrUpdate**
> JobDefinition jobDefinitionsCreateOrUpdate(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, jobDefinition)



Creates or updates a job definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobDefinitionsApi apiInstance = new JobDefinitionsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The data service type of the job definition.
    String jobDefinitionName = "jobDefinitionName_example"; // String | The job definition name to be created or updated.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    JobDefinition jobDefinition = new JobDefinition(); // JobDefinition | Job Definition object to be created or updated.
    try {
      JobDefinition result = apiInstance.jobDefinitionsCreateOrUpdate(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, jobDefinition);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobDefinitionsApi#jobDefinitionsCreateOrUpdate");
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
| **dataServiceName** | **String**| The data service type of the job definition. | |
| **jobDefinitionName** | **String**| The job definition name to be created or updated. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **jobDefinition** | [**JobDefinition**](JobDefinition.md)| Job Definition object to be created or updated. | |

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JobDefinition object. |  -  |
| **202** | Accepted request for create/update. |  -  |

<a id="jobDefinitionsDelete"></a>
# **jobDefinitionsDelete**
> jobDefinitionsDelete(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method deletes the given job definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobDefinitionsApi apiInstance = new JobDefinitionsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The data service type of the job definition.
    String jobDefinitionName = "jobDefinitionName_example"; // String | The job definition name to be deleted.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      apiInstance.jobDefinitionsDelete(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobDefinitionsApi#jobDefinitionsDelete");
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
| **dataServiceName** | **String**| The data service type of the job definition. | |
| **jobDefinitionName** | **String**| The job definition name to be deleted. | |
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
| **202** | Accepted request for JobDefinition deletion. |  -  |
| **204** | JobDefinition deleted. |  -  |

<a id="jobDefinitionsGet"></a>
# **jobDefinitionsGet**
> JobDefinition jobDefinitionsGet(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method gets job definition object by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobDefinitionsApi apiInstance = new JobDefinitionsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The data service name of the job definition
    String jobDefinitionName = "jobDefinitionName_example"; // String | The job definition name that is being queried.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    try {
      JobDefinition result = apiInstance.jobDefinitionsGet(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobDefinitionsApi#jobDefinitionsGet");
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
| **dataServiceName** | **String**| The data service name of the job definition | |
| **jobDefinitionName** | **String**| The job definition name that is being queried. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |

### Return type

[**JobDefinition**](JobDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job definition that matches the criteria. |  -  |

<a id="jobDefinitionsListByDataManager"></a>
# **jobDefinitionsListByDataManager**
> JobDefinitionList jobDefinitionsListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter)



This method gets all the job definitions of the given data manager resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobDefinitionsApi apiInstance = new JobDefinitionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      JobDefinitionList result = apiInstance.jobDefinitionsListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobDefinitionsApi#jobDefinitionsListByDataManager");
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

[**JobDefinitionList**](JobDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of job definitions in that resource.OK |  -  |

<a id="jobDefinitionsListByDataService"></a>
# **jobDefinitionsListByDataService**
> JobDefinitionList jobDefinitionsListByDataService(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter)



This method gets all the job definitions of the given data service name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobDefinitionsApi apiInstance = new JobDefinitionsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The data service type of interest.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    String $filter = "$filter_example"; // String | OData Filter options
    try {
      JobDefinitionList result = apiInstance.jobDefinitionsListByDataService(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobDefinitionsApi#jobDefinitionsListByDataService");
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
| **dataServiceName** | **String**| The data service type of interest. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **$filter** | **String**| OData Filter options | [optional] |

### Return type

[**JobDefinitionList**](JobDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of job definitions of the given data service type. |  -  |

<a id="jobDefinitionsRun"></a>
# **jobDefinitionsRun**
> jobDefinitionsRun(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, runParameters)



This method runs a job instance of the given job definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobDefinitionsApi apiInstance = new JobDefinitionsApi(defaultClient);
    String dataServiceName = "dataServiceName_example"; // String | The data service type of the job definition.
    String jobDefinitionName = "jobDefinitionName_example"; // String | Name of the job definition.
    String subscriptionId = "subscriptionId_example"; // String | The Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
    String dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
    String apiVersion = "apiVersion_example"; // String | The API Version
    RunParameters runParameters = new RunParameters(); // RunParameters | Run time parameters for the job definition.
    try {
      apiInstance.jobDefinitionsRun(dataServiceName, jobDefinitionName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, runParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobDefinitionsApi#jobDefinitionsRun");
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
| **dataServiceName** | **String**| The data service type of the job definition. | |
| **jobDefinitionName** | **String**| Name of the job definition. | |
| **subscriptionId** | **String**| The Subscription Id | |
| **resourceGroupName** | **String**| The Resource Group Name | |
| **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | |
| **apiVersion** | **String**| The API Version | |
| **runParameters** | [**RunParameters**](RunParameters.md)| Run time parameters for the job definition. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Job run accepted. |  -  |
| **204** | Job run started. |  -  |

