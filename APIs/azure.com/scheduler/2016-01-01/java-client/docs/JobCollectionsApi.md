# JobCollectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobCollectionsCreateOrUpdate**](JobCollectionsApi.md#jobCollectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName} |  |
| [**jobCollectionsDelete**](JobCollectionsApi.md#jobCollectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName} |  |
| [**jobCollectionsDisable**](JobCollectionsApi.md#jobCollectionsDisable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/disable |  |
| [**jobCollectionsEnable**](JobCollectionsApi.md#jobCollectionsEnable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName}/enable |  |
| [**jobCollectionsGet**](JobCollectionsApi.md#jobCollectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName} |  |
| [**jobCollectionsListByResourceGroup**](JobCollectionsApi.md#jobCollectionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections |  |
| [**jobCollectionsListBySubscription**](JobCollectionsApi.md#jobCollectionsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Scheduler/jobCollections |  |
| [**jobCollectionsPatch**](JobCollectionsApi.md#jobCollectionsPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Scheduler/jobCollections/{jobCollectionName} |  |


<a id="jobCollectionsCreateOrUpdate"></a>
# **jobCollectionsCreateOrUpdate**
> JobCollectionDefinition jobCollectionsCreateOrUpdate(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, jobCollection)



Provisions a new job collection or updates an existing job collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCollectionsApi apiInstance = new JobCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    JobCollectionDefinition jobCollection = new JobCollectionDefinition(); // JobCollectionDefinition | The job collection definition.
    try {
      JobCollectionDefinition result = apiInstance.jobCollectionsCreateOrUpdate(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, jobCollection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCollectionsApi#jobCollectionsCreateOrUpdate");
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
| **jobCollection** | [**JobCollectionDefinition**](JobCollectionDefinition.md)| The job collection definition. | |

### Return type

[**JobCollectionDefinition**](JobCollectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job collection has been successfully updated. |  -  |
| **201** | The job collection has been successfully created. |  -  |

<a id="jobCollectionsDelete"></a>
# **jobCollectionsDelete**
> jobCollectionsDelete(subscriptionId, resourceGroupName, jobCollectionName, apiVersion)



Deletes a job collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCollectionsApi apiInstance = new JobCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.jobCollectionsDelete(subscriptionId, resourceGroupName, jobCollectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCollectionsApi#jobCollectionsDelete");
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
| **200** | The job collection has been successfully deleted. |  -  |

<a id="jobCollectionsDisable"></a>
# **jobCollectionsDisable**
> jobCollectionsDisable(subscriptionId, resourceGroupName, jobCollectionName, apiVersion)



Disables all of the jobs in the job collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCollectionsApi apiInstance = new JobCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.jobCollectionsDisable(subscriptionId, resourceGroupName, jobCollectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCollectionsApi#jobCollectionsDisable");
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
| **200** | All of the jobs in the job collection have been successfully disabled. |  -  |

<a id="jobCollectionsEnable"></a>
# **jobCollectionsEnable**
> jobCollectionsEnable(subscriptionId, resourceGroupName, jobCollectionName, apiVersion)



Enables all of the jobs in the job collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCollectionsApi apiInstance = new JobCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.jobCollectionsEnable(subscriptionId, resourceGroupName, jobCollectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCollectionsApi#jobCollectionsEnable");
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
| **200** | All of the jobs in the job collection have been successfully enabled. |  -  |

<a id="jobCollectionsGet"></a>
# **jobCollectionsGet**
> JobCollectionDefinition jobCollectionsGet(subscriptionId, resourceGroupName, jobCollectionName, apiVersion)



Gets a job collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCollectionsApi apiInstance = new JobCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      JobCollectionDefinition result = apiInstance.jobCollectionsGet(subscriptionId, resourceGroupName, jobCollectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCollectionsApi#jobCollectionsGet");
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

### Return type

[**JobCollectionDefinition**](JobCollectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job collection has been successfully returned. |  -  |

<a id="jobCollectionsListByResourceGroup"></a>
# **jobCollectionsListByResourceGroup**
> JobCollectionListResult jobCollectionsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Gets all job collections under specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCollectionsApi apiInstance = new JobCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      JobCollectionListResult result = apiInstance.jobCollectionsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCollectionsApi#jobCollectionsListByResourceGroup");
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
| **apiVersion** | **String**| The API version. | |

### Return type

[**JobCollectionListResult**](JobCollectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job collections have been successfully returned. |  -  |

<a id="jobCollectionsListBySubscription"></a>
# **jobCollectionsListBySubscription**
> JobCollectionListResult jobCollectionsListBySubscription(subscriptionId, apiVersion)



Gets all job collections under specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCollectionsApi apiInstance = new JobCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      JobCollectionListResult result = apiInstance.jobCollectionsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCollectionsApi#jobCollectionsListBySubscription");
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
| **apiVersion** | **String**| The API version. | |

### Return type

[**JobCollectionListResult**](JobCollectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job collections have been successfully returned. |  -  |

<a id="jobCollectionsPatch"></a>
# **jobCollectionsPatch**
> JobCollectionDefinition jobCollectionsPatch(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, jobCollection)



Patches an existing job collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JobCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    JobCollectionsApi apiInstance = new JobCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String jobCollectionName = "jobCollectionName_example"; // String | The job collection name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    JobCollectionDefinition jobCollection = new JobCollectionDefinition(); // JobCollectionDefinition | The job collection definition.
    try {
      JobCollectionDefinition result = apiInstance.jobCollectionsPatch(subscriptionId, resourceGroupName, jobCollectionName, apiVersion, jobCollection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JobCollectionsApi#jobCollectionsPatch");
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
| **jobCollection** | [**JobCollectionDefinition**](JobCollectionDefinition.md)| The job collection definition. | |

### Return type

[**JobCollectionDefinition**](JobCollectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The job collection has been successfully patched. |  -  |

