# HybridRunbookWorkerGroupApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hybridRunbookWorkerGroupDelete**](HybridRunbookWorkerGroupApi.md#hybridRunbookWorkerGroupDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName} |  |
| [**hybridRunbookWorkerGroupGet**](HybridRunbookWorkerGroupApi.md#hybridRunbookWorkerGroupGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName} |  |
| [**hybridRunbookWorkerGroupListByAutomationAccount**](HybridRunbookWorkerGroupApi.md#hybridRunbookWorkerGroupListByAutomationAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups |  |
| [**hybridRunbookWorkerGroupUpdate**](HybridRunbookWorkerGroupApi.md#hybridRunbookWorkerGroupUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName} |  |


<a id="hybridRunbookWorkerGroupDelete"></a>
# **hybridRunbookWorkerGroupDelete**
> hybridRunbookWorkerGroupDelete(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion)



Delete a hybrid runbook worker group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridRunbookWorkerGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridRunbookWorkerGroupApi apiInstance = new HybridRunbookWorkerGroupApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String hybridRunbookWorkerGroupName = "hybridRunbookWorkerGroupName_example"; // String | The hybrid runbook worker group name
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.hybridRunbookWorkerGroupDelete(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridRunbookWorkerGroupApi#hybridRunbookWorkerGroupDelete");
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
| **hybridRunbookWorkerGroupName** | **String**| The hybrid runbook worker group name | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
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

<a id="hybridRunbookWorkerGroupGet"></a>
# **hybridRunbookWorkerGroupGet**
> HybridRunbookWorkerGroup hybridRunbookWorkerGroupGet(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion)



Retrieve a hybrid runbook worker group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridRunbookWorkerGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridRunbookWorkerGroupApi apiInstance = new HybridRunbookWorkerGroupApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String hybridRunbookWorkerGroupName = "hybridRunbookWorkerGroupName_example"; // String | The hybrid runbook worker group name
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      HybridRunbookWorkerGroup result = apiInstance.hybridRunbookWorkerGroupGet(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridRunbookWorkerGroupApi#hybridRunbookWorkerGroupGet");
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
| **hybridRunbookWorkerGroupName** | **String**| The hybrid runbook worker group name | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**HybridRunbookWorkerGroup**](HybridRunbookWorkerGroup.md)

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

<a id="hybridRunbookWorkerGroupListByAutomationAccount"></a>
# **hybridRunbookWorkerGroupListByAutomationAccount**
> HybridRunbookWorkerGroupsListResult hybridRunbookWorkerGroupListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, $filter)



Retrieve a list of hybrid runbook worker groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridRunbookWorkerGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridRunbookWorkerGroupApi apiInstance = new HybridRunbookWorkerGroupApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      HybridRunbookWorkerGroupsListResult result = apiInstance.hybridRunbookWorkerGroupListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridRunbookWorkerGroupApi#hybridRunbookWorkerGroupListByAutomationAccount");
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

[**HybridRunbookWorkerGroupsListResult**](HybridRunbookWorkerGroupsListResult.md)

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

<a id="hybridRunbookWorkerGroupUpdate"></a>
# **hybridRunbookWorkerGroupUpdate**
> HybridRunbookWorkerGroup hybridRunbookWorkerGroupUpdate(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion, parameters)



Update a hybrid runbook worker group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridRunbookWorkerGroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridRunbookWorkerGroupApi apiInstance = new HybridRunbookWorkerGroupApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
    String automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
    String hybridRunbookWorkerGroupName = "hybridRunbookWorkerGroupName_example"; // String | The hybrid runbook worker group name
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    HybridRunbookWorkerGroupUpdateParameters parameters = new HybridRunbookWorkerGroupUpdateParameters(); // HybridRunbookWorkerGroupUpdateParameters | The hybrid runbook worker group
    try {
      HybridRunbookWorkerGroup result = apiInstance.hybridRunbookWorkerGroupUpdate(resourceGroupName, automationAccountName, hybridRunbookWorkerGroupName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridRunbookWorkerGroupApi#hybridRunbookWorkerGroupUpdate");
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
| **hybridRunbookWorkerGroupName** | **String**| The hybrid runbook worker group name | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**HybridRunbookWorkerGroupUpdateParameters**](HybridRunbookWorkerGroupUpdateParameters.md)| The hybrid runbook worker group | |

### Return type

[**HybridRunbookWorkerGroup**](HybridRunbookWorkerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Automation error response describing why the operation failed. |  -  |

