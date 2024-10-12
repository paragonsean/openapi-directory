# SoftwareUpdateConfigurationRunApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**softwareUpdateConfigurationRunsGetById**](SoftwareUpdateConfigurationRunApi.md#softwareUpdateConfigurationRunsGetById) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationRuns/{softwareUpdateConfigurationRunId} |  |
| [**softwareUpdateConfigurationRunsList**](SoftwareUpdateConfigurationRunApi.md#softwareUpdateConfigurationRunsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationRuns |  |


<a id="softwareUpdateConfigurationRunsGetById"></a>
# **softwareUpdateConfigurationRunsGetById**
> SoftwareUpdateConfigurationRun softwareUpdateConfigurationRunsGetById(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationRunId, apiVersion, clientRequestId)



Get a single software update configuration Run by Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwareUpdateConfigurationRunApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SoftwareUpdateConfigurationRunApi apiInstance = new SoftwareUpdateConfigurationRunApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    UUID softwareUpdateConfigurationRunId = UUID.randomUUID(); // UUID | The Id of the software update configuration run.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String clientRequestId = "clientRequestId_example"; // String | Identifies this specific client request.
    try {
      SoftwareUpdateConfigurationRun result = apiInstance.softwareUpdateConfigurationRunsGetById(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationRunId, apiVersion, clientRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareUpdateConfigurationRunApi#softwareUpdateConfigurationRunsGetById");
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
| **softwareUpdateConfigurationRunId** | **UUID**| The Id of the software update configuration run. | |
| **apiVersion** | **String**| Client Api Version. | |
| **clientRequestId** | **String**| Identifies this specific client request. | [optional] |

### Return type

[**SoftwareUpdateConfigurationRun**](SoftwareUpdateConfigurationRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single software update configuration Run. |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

<a id="softwareUpdateConfigurationRunsList"></a>
# **softwareUpdateConfigurationRunsList**
> SoftwareUpdateConfigurationRunListResult softwareUpdateConfigurationRunsList(subscriptionId, resourceGroupName, automationAccountName, apiVersion, clientRequestId, $filter, $skip, $top)



Return list of software update configuration runs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SoftwareUpdateConfigurationRunApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SoftwareUpdateConfigurationRunApi apiInstance = new SoftwareUpdateConfigurationRunApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String clientRequestId = "clientRequestId_example"; // String | Identifies this specific client request.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. You can use the following filters: 'properties/osType', 'properties/status', 'properties/startTime', and 'properties/softwareUpdateConfiguration/name'
    String $skip = "$skip_example"; // String | Number of entries you skip before returning results
    String $top = "$top_example"; // String | Maximum number of entries returned in the results collection
    try {
      SoftwareUpdateConfigurationRunListResult result = apiInstance.softwareUpdateConfigurationRunsList(subscriptionId, resourceGroupName, automationAccountName, apiVersion, clientRequestId, $filter, $skip, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SoftwareUpdateConfigurationRunApi#softwareUpdateConfigurationRunsList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **clientRequestId** | **String**| Identifies this specific client request. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. You can use the following filters: &#39;properties/osType&#39;, &#39;properties/status&#39;, &#39;properties/startTime&#39;, and &#39;properties/softwareUpdateConfiguration/name&#39; | [optional] |
| **$skip** | **String**| Number of entries you skip before returning results | [optional] |
| **$top** | **String**| Maximum number of entries returned in the results collection | [optional] |

### Return type

[**SoftwareUpdateConfigurationRunListResult**](SoftwareUpdateConfigurationRunListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return list of software update configurations runs. |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

