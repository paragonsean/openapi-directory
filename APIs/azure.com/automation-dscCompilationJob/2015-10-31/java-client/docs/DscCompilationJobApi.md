# DscCompilationJobApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dscCompilationJobCreate**](DscCompilationJobApi.md#dscCompilationJobCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs/{compilationJobId} |  |
| [**dscCompilationJobGet**](DscCompilationJobApi.md#dscCompilationJobGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs/{compilationJobId} |  |
| [**dscCompilationJobGetStream**](DscCompilationJobApi.md#dscCompilationJobGetStream) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs/{jobId}/streams/{jobStreamId} |  |
| [**dscCompilationJobListByAutomationAccount**](DscCompilationJobApi.md#dscCompilationJobListByAutomationAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs |  |
| [**dscCompilationJobStreamListByJob**](DscCompilationJobApi.md#dscCompilationJobStreamListByJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs/{jobId}/streams/ |  |


<a id="dscCompilationJobCreate"></a>
# **dscCompilationJobCreate**
> DscCompilationJob dscCompilationJobCreate(resourceGroupName, automationAccountName, compilationJobId, subscriptionId, apiVersion, parameters)



Creates the Dsc compilation job of the configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DscCompilationJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DscCompilationJobApi apiInstance = new DscCompilationJobApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    UUID compilationJobId = UUID.randomUUID(); // UUID | The DSC configuration Id.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    DscCompilationJobCreateParameters parameters = new DscCompilationJobCreateParameters(); // DscCompilationJobCreateParameters | The parameters supplied to the create compilation job operation.
    try {
      DscCompilationJob result = apiInstance.dscCompilationJobCreate(resourceGroupName, automationAccountName, compilationJobId, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DscCompilationJobApi#dscCompilationJobCreate");
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
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **compilationJobId** | **UUID**| The DSC configuration Id. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**DscCompilationJobCreateParameters**](DscCompilationJobCreateParameters.md)| The parameters supplied to the create compilation job operation. | |

### Return type

[**DscCompilationJob**](DscCompilationJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

<a id="dscCompilationJobGet"></a>
# **dscCompilationJobGet**
> DscCompilationJob dscCompilationJobGet(resourceGroupName, automationAccountName, compilationJobId, subscriptionId, apiVersion)



Retrieve the Dsc configuration compilation job identified by job id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DscCompilationJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DscCompilationJobApi apiInstance = new DscCompilationJobApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    UUID compilationJobId = UUID.randomUUID(); // UUID | The Dsc configuration compilation job id.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      DscCompilationJob result = apiInstance.dscCompilationJobGet(resourceGroupName, automationAccountName, compilationJobId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DscCompilationJobApi#dscCompilationJobGet");
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
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **compilationJobId** | **UUID**| The Dsc configuration compilation job id. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**DscCompilationJob**](DscCompilationJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

<a id="dscCompilationJobGetStream"></a>
# **dscCompilationJobGetStream**
> DscCompilationJobStreamListByJob200ResponseValueInner dscCompilationJobGetStream(resourceGroupName, automationAccountName, jobId, jobStreamId, subscriptionId, apiVersion)



Retrieve the job stream identified by job stream id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DscCompilationJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DscCompilationJobApi apiInstance = new DscCompilationJobApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    UUID jobId = UUID.randomUUID(); // UUID | The job id.
    String jobStreamId = "jobStreamId_example"; // String | The job stream id.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      DscCompilationJobStreamListByJob200ResponseValueInner result = apiInstance.dscCompilationJobGetStream(resourceGroupName, automationAccountName, jobId, jobStreamId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DscCompilationJobApi#dscCompilationJobGetStream");
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
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **jobId** | **UUID**| The job id. | |
| **jobStreamId** | **String**| The job stream id. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**DscCompilationJobStreamListByJob200ResponseValueInner**](DscCompilationJobStreamListByJob200ResponseValueInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

<a id="dscCompilationJobListByAutomationAccount"></a>
# **dscCompilationJobListByAutomationAccount**
> DscCompilationJobListResult dscCompilationJobListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, $filter)



Retrieve a list of dsc compilation jobs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DscCompilationJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DscCompilationJobApi apiInstance = new DscCompilationJobApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      DscCompilationJobListResult result = apiInstance.dscCompilationJobListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DscCompilationJobApi#dscCompilationJobListByAutomationAccount");
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
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**DscCompilationJobListResult**](DscCompilationJobListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

<a id="dscCompilationJobStreamListByJob"></a>
# **dscCompilationJobStreamListByJob**
> DscCompilationJobStreamListByJob200Response dscCompilationJobStreamListByJob(resourceGroupName, automationAccountName, jobId, subscriptionId, apiVersion)



Retrieve all the job streams for the compilation Job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DscCompilationJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DscCompilationJobApi apiInstance = new DscCompilationJobApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    UUID jobId = UUID.randomUUID(); // UUID | The job id.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      DscCompilationJobStreamListByJob200Response result = apiInstance.dscCompilationJobStreamListByJob(resourceGroupName, automationAccountName, jobId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DscCompilationJobApi#dscCompilationJobStreamListByJob");
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
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **jobId** | **UUID**| The job id. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**DscCompilationJobStreamListByJob200Response**](DscCompilationJobStreamListByJob200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

