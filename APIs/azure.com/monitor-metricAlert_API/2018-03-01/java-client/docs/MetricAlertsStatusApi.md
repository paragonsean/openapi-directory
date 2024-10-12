# MetricAlertsStatusApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricAlertsStatusList**](MetricAlertsStatusApi.md#metricAlertsStatusList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName}/status |  |
| [**metricAlertsStatusListByName**](MetricAlertsStatusApi.md#metricAlertsStatusListByName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/metricAlerts/{ruleName}/status/{statusName} |  |


<a id="metricAlertsStatusList"></a>
# **metricAlertsStatusList**
> MetricAlertStatusCollection metricAlertsStatusList(subscriptionId, resourceGroupName, ruleName, apiVersion)



Retrieve an alert rule status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricAlertsStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricAlertsStatusApi apiInstance = new MetricAlertsStatusApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      MetricAlertStatusCollection result = apiInstance.metricAlertsStatusList(subscriptionId, resourceGroupName, ruleName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricAlertsStatusApi#metricAlertsStatusList");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**MetricAlertStatusCollection**](MetricAlertStatusCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of metric alerts |  -  |
| **0** | BadRequest |  -  |

<a id="metricAlertsStatusListByName"></a>
# **metricAlertsStatusListByName**
> MetricAlertStatusCollection metricAlertsStatusListByName(subscriptionId, resourceGroupName, ruleName, statusName, apiVersion)



Retrieve an alert rule status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricAlertsStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricAlertsStatusApi apiInstance = new MetricAlertsStatusApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String statusName = "statusName_example"; // String | The name of the status.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      MetricAlertStatusCollection result = apiInstance.metricAlertsStatusListByName(subscriptionId, resourceGroupName, ruleName, statusName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricAlertsStatusApi#metricAlertsStatusListByName");
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
| **subscriptionId** | **String**| The Azure subscription Id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **ruleName** | **String**| The name of the rule. | |
| **statusName** | **String**| The name of the status. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**MetricAlertStatusCollection**](MetricAlertStatusCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of metric alerts |  -  |
| **0** | BadRequest |  -  |

