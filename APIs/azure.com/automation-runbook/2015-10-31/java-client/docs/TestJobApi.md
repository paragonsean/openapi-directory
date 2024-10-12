# TestJobApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**testJobCreate**](TestJobApi.md#testJobCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob |  |
| [**testJobGet**](TestJobApi.md#testJobGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob |  |
| [**testJobResume**](TestJobApi.md#testJobResume) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob/resume |  |
| [**testJobStop**](TestJobApi.md#testJobStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob/stop |  |
| [**testJobSuspend**](TestJobApi.md#testJobSuspend) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob/suspend |  |


<a id="testJobCreate"></a>
# **testJobCreate**
> TestJob testJobCreate(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, parameters)



Create a test job of the runbook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestJobApi apiInstance = new TestJobApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String runbookName = "runbookName_example"; // String | The parameters supplied to the create test job operation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    TestJobCreateParameters parameters = new TestJobCreateParameters(); // TestJobCreateParameters | The parameters supplied to the create test job operation.
    try {
      TestJob result = apiInstance.testJobCreate(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestJobApi#testJobCreate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **runbookName** | **String**| The parameters supplied to the create test job operation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**TestJobCreateParameters**](TestJobCreateParameters.md)| The parameters supplied to the create test job operation. | |

### Return type

[**TestJob**](TestJob.md)

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

<a id="testJobGet"></a>
# **testJobGet**
> TestJob testJobGet(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion)



Retrieve the test job for the specified runbook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestJobApi apiInstance = new TestJobApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String runbookName = "runbookName_example"; // String | The runbook name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      TestJob result = apiInstance.testJobGet(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestJobApi#testJobGet");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **runbookName** | **String**| The runbook name. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**TestJob**](TestJob.md)

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

<a id="testJobResume"></a>
# **testJobResume**
> testJobResume(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion)



Resume the test job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestJobApi apiInstance = new TestJobApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String runbookName = "runbookName_example"; // String | The runbook name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.testJobResume(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestJobApi#testJobResume");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **runbookName** | **String**| The runbook name. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

null (empty response body)

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

<a id="testJobStop"></a>
# **testJobStop**
> testJobStop(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion)



Stop the test job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestJobApi apiInstance = new TestJobApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String runbookName = "runbookName_example"; // String | The runbook name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.testJobStop(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestJobApi#testJobStop");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **runbookName** | **String**| The runbook name. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

null (empty response body)

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

<a id="testJobSuspend"></a>
# **testJobSuspend**
> testJobSuspend(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion)



Suspend the test job.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestJobApi apiInstance = new TestJobApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String runbookName = "runbookName_example"; // String | The runbook name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.testJobSuspend(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestJobApi#testJobSuspend");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Name of an Azure Resource group. | |
| **automationAccountName** | **String**| The name of the automation account. | |
| **runbookName** | **String**| The runbook name. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

null (empty response body)

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

