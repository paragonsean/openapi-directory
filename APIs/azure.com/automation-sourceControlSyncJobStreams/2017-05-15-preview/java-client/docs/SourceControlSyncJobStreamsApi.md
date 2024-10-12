# SourceControlSyncJobStreamsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sourceControlSyncJobStreamsGet**](SourceControlSyncJobStreamsApi.md#sourceControlSyncJobStreamsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}/streams/{streamId} |  |
| [**sourceControlSyncJobStreamsListBySyncJob**](SourceControlSyncJobStreamsApi.md#sourceControlSyncJobStreamsListBySyncJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}/streams |  |


<a id="sourceControlSyncJobStreamsGet"></a>
# **sourceControlSyncJobStreamsGet**
> SourceControlSyncJobStreamById sourceControlSyncJobStreamsGet(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, streamId, subscriptionId, apiVersion)



Retrieve a sync job stream identified by stream id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceControlSyncJobStreamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SourceControlSyncJobStreamsApi apiInstance = new SourceControlSyncJobStreamsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String sourceControlName = "sourceControlName_example"; // String | The source control name.
    UUID sourceControlSyncJobId = UUID.randomUUID(); // UUID | The source control sync job id.
    String streamId = "streamId_example"; // String | The id of the sync job stream.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      SourceControlSyncJobStreamById result = apiInstance.sourceControlSyncJobStreamsGet(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, streamId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceControlSyncJobStreamsApi#sourceControlSyncJobStreamsGet");
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
| **sourceControlName** | **String**| The source control name. | |
| **sourceControlSyncJobId** | **UUID**| The source control sync job id. | |
| **streamId** | **String**| The id of the sync job stream. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**SourceControlSyncJobStreamById**](SourceControlSyncJobStreamById.md)

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

<a id="sourceControlSyncJobStreamsListBySyncJob"></a>
# **sourceControlSyncJobStreamsListBySyncJob**
> SourceControlSyncJobStreamsListBySyncJob sourceControlSyncJobStreamsListBySyncJob(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, subscriptionId, apiVersion, $filter)



Retrieve a list of sync job streams identified by sync job id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SourceControlSyncJobStreamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SourceControlSyncJobStreamsApi apiInstance = new SourceControlSyncJobStreamsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String sourceControlName = "sourceControlName_example"; // String | The source control name.
    UUID sourceControlSyncJobId = UUID.randomUUID(); // UUID | The source control sync job id.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      SourceControlSyncJobStreamsListBySyncJob result = apiInstance.sourceControlSyncJobStreamsListBySyncJob(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SourceControlSyncJobStreamsApi#sourceControlSyncJobStreamsListBySyncJob");
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
| **sourceControlName** | **String**| The source control name. | |
| **sourceControlSyncJobId** | **UUID**| The source control sync job id. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**SourceControlSyncJobStreamsListBySyncJob**](SourceControlSyncJobStreamsListBySyncJob.md)

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

