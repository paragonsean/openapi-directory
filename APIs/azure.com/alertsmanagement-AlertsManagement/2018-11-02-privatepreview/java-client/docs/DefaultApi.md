# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actionRulesCreateUpdate**](DefaultApi.md#actionRulesCreateUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules/{actionRuleName} | Create/update an action rule |
| [**actionRulesDelete**](DefaultApi.md#actionRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules/{actionRuleName} | Delete action rule |
| [**actionRulesGetAllResourceGroup**](DefaultApi.md#actionRulesGetAllResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules | Get all action rules created in a resource group |
| [**actionRulesGetAllSubscription**](DefaultApi.md#actionRulesGetAllSubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/actionRules | Get all action rule in a given subscription |
| [**actionRulesGetByName**](DefaultApi.md#actionRulesGetByName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules/{actionRuleName} | Get action rule by name |
| [**actionRulesPatch**](DefaultApi.md#actionRulesPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AlertsManagement/actionRules/{actionRuleName} | Patch action rule |
| [**alertsChangeState**](DefaultApi.md#alertsChangeState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId}/changestate |  |
| [**alertsGetAll**](DefaultApi.md#alertsGetAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts |  |
| [**alertsGetById**](DefaultApi.md#alertsGetById) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId} | Get a specific alert. |
| [**alertsGetHistory**](DefaultApi.md#alertsGetHistory) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alerts/{alertId}/history |  |
| [**alertsGetSummary**](DefaultApi.md#alertsGetSummary) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/alertsSummary |  |
| [**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.AlertsManagement/operations |  |
| [**smartGroupsChangeState**](DefaultApi.md#smartGroupsChangeState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/changeState |  |
| [**smartGroupsGetAll**](DefaultApi.md#smartGroupsGetAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups | Get all smartGroups within the subscription |
| [**smartGroupsGetById**](DefaultApi.md#smartGroupsGetById) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId} | Get information of smart alerts group. |
| [**smartGroupsGetHistory**](DefaultApi.md#smartGroupsGetHistory) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/history |  |


<a id="actionRulesCreateUpdate"></a>
# **actionRulesCreateUpdate**
> ActionRule actionRulesCreateUpdate(subscriptionId, resourceGroup, actionRuleName, actionRule)

Create/update an action rule

Creates/Updates a specific action rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
    String actionRuleName = "actionRuleName_example"; // String | The name of action rule that needs to be created/updated
    ActionRule actionRule = new ActionRule(); // ActionRule | action rule to be created/updated
    try {
      ActionRule result = apiInstance.actionRulesCreateUpdate(subscriptionId, resourceGroup, actionRuleName, actionRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionRulesCreateUpdate");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Resource group name where the resource is created. | |
| **actionRuleName** | **String**| The name of action rule that needs to be created/updated | |
| **actionRule** | [**ActionRule**](ActionRule.md)| action rule to be created/updated | |

### Return type

[**ActionRule**](ActionRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the created/updated action rule |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="actionRulesDelete"></a>
# **actionRulesDelete**
> actionRulesDelete(subscriptionId, resourceGroup, actionRuleName)

Delete action rule

Deletes a given action rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
    String actionRuleName = "actionRuleName_example"; // String | The name that needs to be deleted
    try {
      apiInstance.actionRulesDelete(subscriptionId, resourceGroup, actionRuleName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionRulesDelete");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Resource group name where the resource is created. | |
| **actionRuleName** | **String**| The name that needs to be deleted | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns true if deleted successfully |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="actionRulesGetAllResourceGroup"></a>
# **actionRulesGetAllResourceGroup**
> ActionRulesList actionRulesGetAllResourceGroup(subscriptionId, resourceGroup, targetResourceGroup, targetResourceType, targetResource, severity, monitorService)

Get all action rules created in a resource group

List all action rules of the subscription, created in given resource group and given input filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
    String targetResourceGroup = "targetResourceGroup_example"; // String | filter by target resource group name
    String targetResourceType = "targetResourceType_example"; // String | filter by target resource type
    String targetResource = "targetResource_example"; // String | filter by target resource
    String severity = "Sev0"; // String | filter by severity
    String monitorService = "Platform"; // String | filter by monitor service which is the source of the alert object.
    try {
      ActionRulesList result = apiInstance.actionRulesGetAllResourceGroup(subscriptionId, resourceGroup, targetResourceGroup, targetResourceType, targetResource, severity, monitorService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionRulesGetAllResourceGroup");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Resource group name where the resource is created. | |
| **targetResourceGroup** | **String**| filter by target resource group name | [optional] |
| **targetResourceType** | **String**| filter by target resource type | [optional] |
| **targetResource** | **String**| filter by target resource | [optional] |
| **severity** | **String**| filter by severity | [optional] [enum: Sev0, Sev1, Sev2, Sev3, Sev4] |
| **monitorService** | **String**| filter by monitor service which is the source of the alert object. | [optional] [enum: Platform, Application Insights, Log Analytics, Zabbix, SCOM, Nagios, Infrastructure Insights, ActivityLog Administrative, ActivityLog Security, ActivityLog Recommendation, ActivityLog Policy, ActivityLog Autoscale, ServiceHealth, SmartDetector] |

### Return type

[**ActionRulesList**](ActionRulesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Return the list of action rules |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="actionRulesGetAllSubscription"></a>
# **actionRulesGetAllSubscription**
> ActionRulesList actionRulesGetAllSubscription(subscriptionId, targetResourceGroup, targetResourceType, targetResource, severity, monitorService)

Get all action rule in a given subscription

List all action rules of the subscription and given input filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String targetResourceGroup = "targetResourceGroup_example"; // String | filter by target resource group name
    String targetResourceType = "targetResourceType_example"; // String | filter by target resource type
    String targetResource = "targetResource_example"; // String | filter by target resource
    String severity = "Sev0"; // String | filter by severity
    String monitorService = "Platform"; // String | filter by monitor service which is the source of the alert object.
    try {
      ActionRulesList result = apiInstance.actionRulesGetAllSubscription(subscriptionId, targetResourceGroup, targetResourceType, targetResource, severity, monitorService);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionRulesGetAllSubscription");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **targetResourceGroup** | **String**| filter by target resource group name | [optional] |
| **targetResourceType** | **String**| filter by target resource type | [optional] |
| **targetResource** | **String**| filter by target resource | [optional] |
| **severity** | **String**| filter by severity | [optional] [enum: Sev0, Sev1, Sev2, Sev3, Sev4] |
| **monitorService** | **String**| filter by monitor service which is the source of the alert object. | [optional] [enum: Platform, Application Insights, Log Analytics, Zabbix, SCOM, Nagios, Infrastructure Insights, ActivityLog Administrative, ActivityLog Security, ActivityLog Recommendation, ActivityLog Policy, ActivityLog Autoscale, ServiceHealth, SmartDetector] |

### Return type

[**ActionRulesList**](ActionRulesList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Return the list of action rules |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="actionRulesGetByName"></a>
# **actionRulesGetByName**
> ActionRule actionRulesGetByName(subscriptionId, resourceGroup, actionRuleName)

Get action rule by name

Get a specific action rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
    String actionRuleName = "actionRuleName_example"; // String | The name of action rule that needs to be fetched
    try {
      ActionRule result = apiInstance.actionRulesGetByName(subscriptionId, resourceGroup, actionRuleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionRulesGetByName");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Resource group name where the resource is created. | |
| **actionRuleName** | **String**| The name of action rule that needs to be fetched | |

### Return type

[**ActionRule**](ActionRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the specific action rule |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="actionRulesPatch"></a>
# **actionRulesPatch**
> actionRulesPatch(subscriptionId, resourceGroup, actionRuleName, actionRulePatch)

Patch action rule

Update enabled flag and/or tags for the given action rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Resource group name where the resource is created.
    String actionRuleName = "actionRuleName_example"; // String | The name that needs to be updated
    PatchObject actionRulePatch = new PatchObject(); // PatchObject | Parameters supplied to the operation.
    try {
      apiInstance.actionRulesPatch(subscriptionId, resourceGroup, actionRuleName, actionRulePatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#actionRulesPatch");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Resource group name where the resource is created. | |
| **actionRuleName** | **String**| The name that needs to be updated | |
| **actionRulePatch** | [**PatchObject**](PatchObject.md)| Parameters supplied to the operation. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the created/updated action rule |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsChangeState"></a>
# **alertsChangeState**
> Alert alertsChangeState(subscriptionId, alertId, apiVersion, newState)



Change the state of the alert.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String alertId = "alertId_example"; // String | Unique ID of an alert object.
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    String newState = "New"; // String | filter by state
    try {
      Alert result = apiInstance.alertsChangeState(subscriptionId, alertId, apiVersion, newState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#alertsChangeState");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **alertId** | **String**| Unique ID of an alert object. | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |
| **newState** | **String**| filter by state | [enum: New, Acknowledged, Closed] |

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Alert state updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsGetAll"></a>
# **alertsGetAll**
> AlertsList alertsGetAll(subscriptionId, apiVersion, targetResource, targetResourceGroup, targetResourceType, monitorService, monitorCondition, severity, alertState, smartGroupId, includePayload, pageCount, sortBy, sortOrder, timeRange)



List all the existing alerts, where the results can be selective by passing multiple filter parameters including time range and sorted on specific fields. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    String targetResource = "targetResource_example"; // String | filter by target resource
    String targetResourceGroup = "targetResourceGroup_example"; // String | filter by target resource group name
    String targetResourceType = "targetResourceType_example"; // String | filter by target resource type
    String monitorService = "Platform"; // String | filter by monitor service which is the source of the alert object.
    String monitorCondition = "Fired"; // String | filter by monitor condition which is the state of the alert at monitor service
    String severity = "Sev0"; // String | filter by severity
    String alertState = "New"; // String | filter by state
    String smartGroupId = "smartGroupId_example"; // String | filter by smart Group Id
    Boolean includePayload = true; // Boolean | include payload field content, default value is 'false'.
    Integer pageCount = 56; // Integer | number of items per page, default value is '25'.
    String sortBy = "name"; // String | sort the query results by input field, default value is 'lastModifiedDateTime'.
    String sortOrder = "asc"; // String | sort the query results order in either ascending or descending, default value is 'desc' for time fields and 'asc' for others.
    String timeRange = "1h"; // String | filter by time range, default value is 1 day
    try {
      AlertsList result = apiInstance.alertsGetAll(subscriptionId, apiVersion, targetResource, targetResourceGroup, targetResourceType, monitorService, monitorCondition, severity, alertState, smartGroupId, includePayload, pageCount, sortBy, sortOrder, timeRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#alertsGetAll");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |
| **targetResource** | **String**| filter by target resource | [optional] |
| **targetResourceGroup** | **String**| filter by target resource group name | [optional] |
| **targetResourceType** | **String**| filter by target resource type | [optional] |
| **monitorService** | **String**| filter by monitor service which is the source of the alert object. | [optional] [enum: Platform, Application Insights, Log Analytics, Zabbix, SCOM, Nagios, Infrastructure Insights, ActivityLog Administrative, ActivityLog Security, ActivityLog Recommendation, ActivityLog Policy, ActivityLog Autoscale, ServiceHealth, SmartDetector] |
| **monitorCondition** | **String**| filter by monitor condition which is the state of the alert at monitor service | [optional] [enum: Fired, Resolved] |
| **severity** | **String**| filter by severity | [optional] [enum: Sev0, Sev1, Sev2, Sev3, Sev4] |
| **alertState** | **String**| filter by state | [optional] [enum: New, Acknowledged, Closed] |
| **smartGroupId** | **String**| filter by smart Group Id | [optional] |
| **includePayload** | **Boolean**| include payload field content, default value is &#39;false&#39;. | [optional] |
| **pageCount** | **Integer**| number of items per page, default value is &#39;25&#39;. | [optional] |
| **sortBy** | **String**| sort the query results by input field, default value is &#39;lastModifiedDateTime&#39;. | [optional] [enum: name, severity, alertState, monitorCondition, targetResource, targetResourceName, targetResourceGroup, targetResourceType, startDateTime, lastModifiedDateTime] |
| **sortOrder** | **String**| sort the query results order in either ascending or descending, default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others. | [optional] [enum: asc, desc] |
| **timeRange** | **String**| filter by time range, default value is 1 day | [optional] [enum: 1h, 1d, 7d, 30d] |

### Return type

[**AlertsList**](AlertsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully listed alert objects. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsGetById"></a>
# **alertsGetById**
> Alert alertsGetById(subscriptionId, alertId, apiVersion)

Get a specific alert.

Get information related to a specific alert

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String alertId = "alertId_example"; // String | Unique ID of an alert object.
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    try {
      Alert result = apiInstance.alertsGetById(subscriptionId, alertId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#alertsGetById");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **alertId** | **String**| Unique ID of an alert object. | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |

### Return type

[**Alert**](Alert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the alert with the specified ID. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsGetHistory"></a>
# **alertsGetHistory**
> AlertModification alertsGetHistory(subscriptionId, alertId, apiVersion)



Get the history of the changes of an alert.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String alertId = "alertId_example"; // String | Unique ID of an alert object.
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    try {
      AlertModification result = apiInstance.alertsGetHistory(subscriptionId, alertId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#alertsGetHistory");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **alertId** | **String**| Unique ID of an alert object. | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |

### Return type

[**AlertModification**](AlertModification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the list of changes of alert. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsGetSummary"></a>
# **alertsGetSummary**
> AlertsSummary alertsGetSummary(subscriptionId, apiVersion, targetResourceGroup, timeRange)



Summary of alerts with the count each severity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    String targetResourceGroup = "targetResourceGroup_example"; // String | filter by target resource group name
    String timeRange = "1h"; // String | filter by time range, default value is 1 day
    try {
      AlertsSummary result = apiInstance.alertsGetSummary(subscriptionId, apiVersion, targetResourceGroup, timeRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#alertsGetSummary");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |
| **targetResourceGroup** | **String**| filter by target resource group name | [optional] |
| **timeRange** | **String**| filter by time range, default value is 1 day | [optional] [enum: 1h, 1d, 7d, 30d] |

### Return type

[**AlertsSummary**](AlertsSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Alert state updated. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="operationsList"></a>
# **operationsList**
> OperationsList operationsList(apiVersion)



List all operations available through Azure Alerts Management Resource Provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    try {
      OperationsList result = apiInstance.operationsList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationsList");
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
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |

### Return type

[**OperationsList**](OperationsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Successfully retrieved operations list. |  -  |

<a id="smartGroupsChangeState"></a>
# **smartGroupsChangeState**
> SmartGroup smartGroupsChangeState(subscriptionId, smartGroupId, apiVersion, newState)



Change the state from unresolved to resolved and all the alerts within the smart group will also be resolved.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String smartGroupId = "smartGroupId_example"; // String | Smart Group Id
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    String newState = "New"; // String | filter by state
    try {
      SmartGroup result = apiInstance.smartGroupsChangeState(subscriptionId, smartGroupId, apiVersion, newState);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#smartGroupsChangeState");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **smartGroupId** | **String**| Smart Group Id | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |
| **newState** | **String**| filter by state | [enum: New, Acknowledged, Closed] |

### Return type

[**SmartGroup**](SmartGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Alert state updated. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="smartGroupsGetAll"></a>
# **smartGroupsGetAll**
> SmartGroupsList smartGroupsGetAll(subscriptionId, apiVersion, targetResource, targetResourceGroup, targetResourceType, monitorService, monitorCondition, severity, smartGroupState, timeRange, pageCount, sortBy, sortOrder)

Get all smartGroups within the subscription

List all the smartGroups within the specified subscription. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    String targetResource = "targetResource_example"; // String | filter by target resource
    String targetResourceGroup = "targetResourceGroup_example"; // String | filter by target resource group name
    String targetResourceType = "targetResourceType_example"; // String | filter by target resource type
    String monitorService = "Platform"; // String | filter by monitor service which is the source of the alert object.
    String monitorCondition = "Fired"; // String | filter by monitor condition which is the state of the alert at monitor service
    String severity = "Sev0"; // String | filter by severity
    String smartGroupState = "New"; // String | filter by state
    String timeRange = "1h"; // String | filter by time range, default value is 1 day
    Integer pageCount = 56; // Integer | number of items per page, default value is '25'.
    String sortBy = "alertsCount"; // String | sort the query results by input field, default value is 'lastModifiedDateTime'.
    String sortOrder = "asc"; // String | sort the query results order in either ascending or descending, default value is 'desc' for time fields and 'asc' for others.
    try {
      SmartGroupsList result = apiInstance.smartGroupsGetAll(subscriptionId, apiVersion, targetResource, targetResourceGroup, targetResourceType, monitorService, monitorCondition, severity, smartGroupState, timeRange, pageCount, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#smartGroupsGetAll");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |
| **targetResource** | **String**| filter by target resource | [optional] |
| **targetResourceGroup** | **String**| filter by target resource group name | [optional] |
| **targetResourceType** | **String**| filter by target resource type | [optional] |
| **monitorService** | **String**| filter by monitor service which is the source of the alert object. | [optional] [enum: Platform, Application Insights, Log Analytics, Zabbix, SCOM, Nagios, Infrastructure Insights, ActivityLog Administrative, ActivityLog Security, ActivityLog Recommendation, ActivityLog Policy, ActivityLog Autoscale, ServiceHealth, SmartDetector] |
| **monitorCondition** | **String**| filter by monitor condition which is the state of the alert at monitor service | [optional] [enum: Fired, Resolved] |
| **severity** | **String**| filter by severity | [optional] [enum: Sev0, Sev1, Sev2, Sev3, Sev4] |
| **smartGroupState** | **String**| filter by state | [optional] [enum: New, Acknowledged, Closed] |
| **timeRange** | **String**| filter by time range, default value is 1 day | [optional] [enum: 1h, 1d, 7d, 30d] |
| **pageCount** | **Integer**| number of items per page, default value is &#39;25&#39;. | [optional] |
| **sortBy** | **String**| sort the query results by input field, default value is &#39;lastModifiedDateTime&#39;. | [optional] [enum: alertsCount, state, severity, startDateTime, lastModifiedDateTime] |
| **sortOrder** | **String**| sort the query results order in either ascending or descending, default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others. | [optional] [enum: asc, desc] |

### Return type

[**SmartGroupsList**](SmartGroupsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of all smartGroups. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="smartGroupsGetById"></a>
# **smartGroupsGetById**
> SmartGroup smartGroupsGetById(subscriptionId, smartGroupId, apiVersion)

Get information of smart alerts group.

Get details of smart group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String smartGroupId = "smartGroupId_example"; // String | Smart Group Id
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    try {
      SmartGroup result = apiInstance.smartGroupsGetById(subscriptionId, smartGroupId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#smartGroupsGetById");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **smartGroupId** | **String**| Smart Group Id | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |

### Return type

[**SmartGroup**](SmartGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the group with the specified smart group Id. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="smartGroupsGetHistory"></a>
# **smartGroupsGetHistory**
> SmartGroupModification smartGroupsGetHistory(subscriptionId, smartGroupId, apiVersion)



Get the history of the changes of smart group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String smartGroupId = "smartGroupId_example"; // String | Smart Group Id
    String apiVersion = "2018-11-02-privatepreview"; // String | client API version
    try {
      SmartGroupModification result = apiInstance.smartGroupsGetHistory(subscriptionId, smartGroupId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#smartGroupsGetHistory");
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
| **subscriptionId** | **String**| subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **smartGroupId** | **String**| Smart Group Id | |
| **apiVersion** | **String**| client API version | [enum: 2018-11-02-privatepreview, 2018-05-05] |

### Return type

[**SmartGroupModification**](SmartGroupModification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the list of changes of smart group. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

