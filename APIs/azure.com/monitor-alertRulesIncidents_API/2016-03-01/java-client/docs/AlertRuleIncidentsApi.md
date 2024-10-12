# AlertRuleIncidentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**alertRuleIncidentsGet**](AlertRuleIncidentsApi.md#alertRuleIncidentsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName}/incidents/{incidentName} |  |
| [**alertRuleIncidentsListByAlertRule**](AlertRuleIncidentsApi.md#alertRuleIncidentsListByAlertRule) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/alertrules/{ruleName}/incidents |  |


<a id="alertRuleIncidentsGet"></a>
# **alertRuleIncidentsGet**
> Incident alertRuleIncidentsGet(resourceGroupName, ruleName, incidentName, apiVersion, subscriptionId)



Gets an incident associated to an alert rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertRuleIncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertRuleIncidentsApi apiInstance = new AlertRuleIncidentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String incidentName = "incidentName_example"; // String | The name of the incident to retrieve.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      Incident result = apiInstance.alertRuleIncidentsGet(resourceGroupName, ruleName, incidentName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertRuleIncidentsApi#alertRuleIncidentsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **ruleName** | **String**| The name of the rule. | |
| **incidentName** | **String**| The name of the incident to retrieve. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

[**Incident**](Incident.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for one alert rule related incident |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertRuleIncidentsListByAlertRule"></a>
# **alertRuleIncidentsListByAlertRule**
> IncidentListResult alertRuleIncidentsListByAlertRule(resourceGroupName, ruleName, apiVersion, subscriptionId)



Gets a list of incidents associated to an alert rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertRuleIncidentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AlertRuleIncidentsApi apiInstance = new AlertRuleIncidentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String ruleName = "ruleName_example"; // String | The name of the rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
    try {
      IncidentListResult result = apiInstance.alertRuleIncidentsListByAlertRule(resourceGroupName, ruleName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertRuleIncidentsApi#alertRuleIncidentsListByAlertRule");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **ruleName** | **String**| The name of the rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| The Azure subscription Id. | |

### Return type

[**IncidentListResult**](IncidentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request for a list of alert rule related incidents |  -  |

