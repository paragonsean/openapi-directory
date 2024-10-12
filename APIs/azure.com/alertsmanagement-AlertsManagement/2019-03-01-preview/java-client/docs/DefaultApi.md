# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**alertsChangeState**](DefaultApi.md#alertsChangeState) | **POST** /{scope}/providers/Microsoft.AlertsManagement/alerts/{alertId}/changestate |  |
| [**alertsGetAll**](DefaultApi.md#alertsGetAll) | **GET** /{scope}/providers/Microsoft.AlertsManagement/alerts |  |
| [**alertsGetById**](DefaultApi.md#alertsGetById) | **GET** /{scope}/providers/Microsoft.AlertsManagement/alerts/{alertId} | Get a specific alert. |
| [**alertsGetHistory**](DefaultApi.md#alertsGetHistory) | **GET** /{scope}/providers/Microsoft.AlertsManagement/alerts/{alertId}/history |  |
| [**alertsGetSummary**](DefaultApi.md#alertsGetSummary) | **GET** /{scope}/providers/Microsoft.AlertsManagement/alertsSummary |  |
| [**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.AlertsManagement/operations |  |
| [**smartGroupsChangeState**](DefaultApi.md#smartGroupsChangeState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/changeState |  |
| [**smartGroupsGetAll**](DefaultApi.md#smartGroupsGetAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups | Get all Smart Groups within a specified subscription |
| [**smartGroupsGetById**](DefaultApi.md#smartGroupsGetById) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId} | Get information related to a specific Smart Group. |
| [**smartGroupsGetHistory**](DefaultApi.md#smartGroupsGetHistory) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AlertsManagement/smartGroups/{smartGroupId}/history |  |


<a id="alertsChangeState"></a>
# **alertsChangeState**
> Alert alertsChangeState(scope, alertId, apiVersion, newState)



Change the state of an alert.

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
    String scope = "scope_example"; // String | scope here is resourceId for which alert is created.
    String alertId = "alertId_example"; // String | Unique ID of an alert instance.
    String apiVersion = "2018-05-05"; // String | API version.
    String newState = "New"; // String | New state of the alert.
    try {
      Alert result = apiInstance.alertsChangeState(scope, alertId, apiVersion, newState);
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
| **scope** | **String**| scope here is resourceId for which alert is created. | |
| **alertId** | **String**| Unique ID of an alert instance. | |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |
| **newState** | **String**| New state of the alert. | [enum: New, Acknowledged, Closed] |

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
> AlertsList alertsGetAll(scope, apiVersion, targetResource, targetResourceType, targetResourceGroup, monitorService, monitorCondition, severity, alertState, alertRule, smartGroupId, includeContext, includeEgressConfig, pageCount, sortBy, sortOrder, select, timeRange, customTimeRange)



List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime. 

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
    String scope = "scope_example"; // String | scope here is resourceId for which alert is created.
    String apiVersion = "2018-05-05"; // String | API version.
    String targetResource = "targetResource_example"; // String | Filter by target resource( which is full ARM ID) Default value is select all.
    String targetResourceType = "targetResourceType_example"; // String | Filter by target resource type. Default value is select all.
    String targetResourceGroup = "targetResourceGroup_example"; // String | Filter by target resource group name. Default value is select all.
    String monitorService = "Application Insights"; // String | Filter by monitor service which generates the alert instance. Default value is select all.
    String monitorCondition = "Fired"; // String | Filter by monitor condition which is either 'Fired' or 'Resolved'. Default value is to select all.
    String severity = "Sev0"; // String | Filter by severity.  Default value is select all.
    String alertState = "New"; // String | Filter by state of the alert instance. Default value is to select all.
    String alertRule = "alertRule_example"; // String | Filter by specific alert rule.  Default value is to select all.
    String smartGroupId = "smartGroupId_example"; // String | Filter the alerts list by the Smart Group Id. Default value is none.
    Boolean includeContext = true; // Boolean | Include context which has contextual data specific to the monitor service. Default value is false'
    Boolean includeEgressConfig = true; // Boolean | Include egress config which would be used for displaying the content in portal.  Default value is 'false'.
    Integer pageCount = 56; // Integer | Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \"includeContent\"  filter is selected, maximum value allowed is 25. Default value is 25.
    String sortBy = "name"; // String | Sort the query results by input field,  Default value is 'lastModifiedDateTime'.
    String sortOrder = "asc"; // String | Sort the query results order in either ascending or descending.  Default value is 'desc' for time fields and 'asc' for others.
    String select = "select_example"; // String | This filter allows to selection of the fields(comma separated) which would  be part of the essential section. This would allow to project only the  required fields rather than getting entire content.  Default is to fetch all the fields in the essentials section.
    String timeRange = "1h"; // String | Filter by time range by below listed values. Default value is 1 day.
    String customTimeRange = "customTimeRange_example"; // String | Filter by custom time range in the format <start-time>/<end-time>  where time is in (ISO-8601 format)'. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none.
    try {
      AlertsList result = apiInstance.alertsGetAll(scope, apiVersion, targetResource, targetResourceType, targetResourceGroup, monitorService, monitorCondition, severity, alertState, alertRule, smartGroupId, includeContext, includeEgressConfig, pageCount, sortBy, sortOrder, select, timeRange, customTimeRange);
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
| **scope** | **String**| scope here is resourceId for which alert is created. | |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |
| **targetResource** | **String**| Filter by target resource( which is full ARM ID) Default value is select all. | [optional] |
| **targetResourceType** | **String**| Filter by target resource type. Default value is select all. | [optional] |
| **targetResourceGroup** | **String**| Filter by target resource group name. Default value is select all. | [optional] |
| **monitorService** | **String**| Filter by monitor service which generates the alert instance. Default value is select all. | [optional] [enum: Application Insights, ActivityLog Administrative, ActivityLog Security, ActivityLog Recommendation, ActivityLog Policy, ActivityLog Autoscale, Log Analytics, Nagios, Platform, SCOM, ServiceHealth, SmartDetector, VM Insights, Zabbix] |
| **monitorCondition** | **String**| Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all. | [optional] [enum: Fired, Resolved] |
| **severity** | **String**| Filter by severity.  Default value is select all. | [optional] [enum: Sev0, Sev1, Sev2, Sev3, Sev4] |
| **alertState** | **String**| Filter by state of the alert instance. Default value is to select all. | [optional] [enum: New, Acknowledged, Closed] |
| **alertRule** | **String**| Filter by specific alert rule.  Default value is to select all. | [optional] |
| **smartGroupId** | **String**| Filter the alerts list by the Smart Group Id. Default value is none. | [optional] |
| **includeContext** | **Boolean**| Include context which has contextual data specific to the monitor service. Default value is false&#39; | [optional] |
| **includeEgressConfig** | **Boolean**| Include egress config which would be used for displaying the content in portal.  Default value is &#39;false&#39;. | [optional] |
| **pageCount** | **Integer**| Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \&quot;includeContent\&quot;  filter is selected, maximum value allowed is 25. Default value is 25. | [optional] |
| **sortBy** | **String**| Sort the query results by input field,  Default value is &#39;lastModifiedDateTime&#39;. | [optional] [enum: name, severity, alertState, monitorCondition, targetResource, targetResourceName, targetResourceGroup, targetResourceType, startDateTime, lastModifiedDateTime] |
| **sortOrder** | **String**| Sort the query results order in either ascending or descending.  Default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others. | [optional] [enum: asc, desc] |
| **select** | **String**| This filter allows to selection of the fields(comma separated) which would  be part of the essential section. This would allow to project only the  required fields rather than getting entire content.  Default is to fetch all the fields in the essentials section. | [optional] |
| **timeRange** | **String**| Filter by time range by below listed values. Default value is 1 day. | [optional] [enum: 1h, 1d, 7d, 30d] |
| **customTimeRange** | **String**| Filter by custom time range in the format &lt;start-time&gt;/&lt;end-time&gt;  where time is in (ISO-8601 format)&#39;. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none. | [optional] |

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
> Alert alertsGetById(scope, alertId, apiVersion)

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
    String scope = "scope_example"; // String | scope here is resourceId for which alert is created.
    String alertId = "alertId_example"; // String | Unique ID of an alert instance.
    String apiVersion = "2018-05-05"; // String | API version.
    try {
      Alert result = apiInstance.alertsGetById(scope, alertId, apiVersion);
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
| **scope** | **String**| scope here is resourceId for which alert is created. | |
| **alertId** | **String**| Unique ID of an alert instance. | |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |

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
> AlertModification alertsGetHistory(scope, alertId, apiVersion)



Get the history of an alert, which captures any monitor condition changes (Fired/Resolved) and alert state changes (New/Acknowledged/Closed).

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
    String scope = "scope_example"; // String | scope here is resourceId for which alert is created.
    String alertId = "alertId_example"; // String | Unique ID of an alert instance.
    String apiVersion = "2018-05-05"; // String | API version.
    try {
      AlertModification result = apiInstance.alertsGetHistory(scope, alertId, apiVersion);
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
| **scope** | **String**| scope here is resourceId for which alert is created. | |
| **alertId** | **String**| Unique ID of an alert instance. | |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |

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
| **200** | OK. Returns the history of the specified alert. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="alertsGetSummary"></a>
# **alertsGetSummary**
> AlertsSummary alertsGetSummary(scope, groupby, apiVersion, includeSmartGroupsCount, targetResource, targetResourceType, targetResourceGroup, monitorService, monitorCondition, severity, alertState, alertRule, timeRange, customTimeRange)



Get a summarized count of your alerts grouped by various parameters (e.g. grouping by &#39;Severity&#39; returns the count of alerts for each severity).

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
    String scope = "scope_example"; // String | scope here is resourceId for which alert is created.
    String groupby = "severity"; // String | This parameter allows the result set to be grouped by input fields. For example, groupby=severity,alertstate.
    String apiVersion = "2018-05-05"; // String | API version.
    Boolean includeSmartGroupsCount = true; // Boolean | Include count of the SmartGroups as part of the summary. Default value is 'false'.
    String targetResource = "targetResource_example"; // String | Filter by target resource( which is full ARM ID) Default value is select all.
    String targetResourceType = "targetResourceType_example"; // String | Filter by target resource type. Default value is select all.
    String targetResourceGroup = "targetResourceGroup_example"; // String | Filter by target resource group name. Default value is select all.
    String monitorService = "Application Insights"; // String | Filter by monitor service which generates the alert instance. Default value is select all.
    String monitorCondition = "Fired"; // String | Filter by monitor condition which is either 'Fired' or 'Resolved'. Default value is to select all.
    String severity = "Sev0"; // String | Filter by severity.  Default value is select all.
    String alertState = "New"; // String | Filter by state of the alert instance. Default value is to select all.
    String alertRule = "alertRule_example"; // String | Filter by specific alert rule.  Default value is to select all.
    String timeRange = "1h"; // String | Filter by time range by below listed values. Default value is 1 day.
    String customTimeRange = "customTimeRange_example"; // String | Filter by custom time range in the format <start-time>/<end-time>  where time is in (ISO-8601 format)'. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none.
    try {
      AlertsSummary result = apiInstance.alertsGetSummary(scope, groupby, apiVersion, includeSmartGroupsCount, targetResource, targetResourceType, targetResourceGroup, monitorService, monitorCondition, severity, alertState, alertRule, timeRange, customTimeRange);
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
| **scope** | **String**| scope here is resourceId for which alert is created. | |
| **groupby** | **String**| This parameter allows the result set to be grouped by input fields. For example, groupby&#x3D;severity,alertstate. | [enum: severity, alertState, monitorCondition, monitorService, signalType, alertRule] |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |
| **includeSmartGroupsCount** | **Boolean**| Include count of the SmartGroups as part of the summary. Default value is &#39;false&#39;. | [optional] |
| **targetResource** | **String**| Filter by target resource( which is full ARM ID) Default value is select all. | [optional] |
| **targetResourceType** | **String**| Filter by target resource type. Default value is select all. | [optional] |
| **targetResourceGroup** | **String**| Filter by target resource group name. Default value is select all. | [optional] |
| **monitorService** | **String**| Filter by monitor service which generates the alert instance. Default value is select all. | [optional] [enum: Application Insights, ActivityLog Administrative, ActivityLog Security, ActivityLog Recommendation, ActivityLog Policy, ActivityLog Autoscale, Log Analytics, Nagios, Platform, SCOM, ServiceHealth, SmartDetector, VM Insights, Zabbix] |
| **monitorCondition** | **String**| Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all. | [optional] [enum: Fired, Resolved] |
| **severity** | **String**| Filter by severity.  Default value is select all. | [optional] [enum: Sev0, Sev1, Sev2, Sev3, Sev4] |
| **alertState** | **String**| Filter by state of the alert instance. Default value is to select all. | [optional] [enum: New, Acknowledged, Closed] |
| **alertRule** | **String**| Filter by specific alert rule.  Default value is to select all. | [optional] |
| **timeRange** | **String**| Filter by time range by below listed values. Default value is 1 day. | [optional] [enum: 1h, 1d, 7d, 30d] |
| **customTimeRange** | **String**| Filter by custom time range in the format &lt;start-time&gt;/&lt;end-time&gt;  where time is in (ISO-8601 format)&#39;. Permissible values is within 30 days from  query time. Either timeRange or customTimeRange could be used but not both. Default is none. | [optional] |

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
| **200** | OK. Alert summary returned. |  -  |
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
    String apiVersion = "2018-05-05"; // String | API version.
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
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |

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



Change the state of a Smart Group.

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String smartGroupId = "smartGroupId_example"; // String | Smart group unique id. 
    String apiVersion = "2018-05-05"; // String | API version.
    String newState = "New"; // String | New state of the alert.
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **smartGroupId** | **String**| Smart group unique id.  | |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |
| **newState** | **String**| New state of the alert. | [enum: New, Acknowledged, Closed] |

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
| **200** | OK. Smart Group state updated. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="smartGroupsGetAll"></a>
# **smartGroupsGetAll**
> SmartGroupsList smartGroupsGetAll(subscriptionId, apiVersion, targetResource, targetResourceGroup, targetResourceType, monitorService, monitorCondition, severity, smartGroupState, timeRange, pageCount, sortBy, sortOrder)

Get all Smart Groups within a specified subscription

List all the Smart Groups within a specified subscription. 

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2018-05-05"; // String | API version.
    String targetResource = "targetResource_example"; // String | Filter by target resource( which is full ARM ID) Default value is select all.
    String targetResourceGroup = "targetResourceGroup_example"; // String | Filter by target resource group name. Default value is select all.
    String targetResourceType = "targetResourceType_example"; // String | Filter by target resource type. Default value is select all.
    String monitorService = "Application Insights"; // String | Filter by monitor service which generates the alert instance. Default value is select all.
    String monitorCondition = "Fired"; // String | Filter by monitor condition which is either 'Fired' or 'Resolved'. Default value is to select all.
    String severity = "Sev0"; // String | Filter by severity.  Default value is select all.
    String smartGroupState = "New"; // String | Filter by state of the smart group. Default value is to select all.
    String timeRange = "1h"; // String | Filter by time range by below listed values. Default value is 1 day.
    Integer pageCount = 56; // Integer | Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \"includeContent\"  filter is selected, maximum value allowed is 25. Default value is 25.
    String sortBy = "alertsCount"; // String | Sort the query results by input field. Default value is sort by 'lastModifiedDateTime'.
    String sortOrder = "asc"; // String | Sort the query results order in either ascending or descending.  Default value is 'desc' for time fields and 'asc' for others.
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |
| **targetResource** | **String**| Filter by target resource( which is full ARM ID) Default value is select all. | [optional] |
| **targetResourceGroup** | **String**| Filter by target resource group name. Default value is select all. | [optional] |
| **targetResourceType** | **String**| Filter by target resource type. Default value is select all. | [optional] |
| **monitorService** | **String**| Filter by monitor service which generates the alert instance. Default value is select all. | [optional] [enum: Application Insights, ActivityLog Administrative, ActivityLog Security, ActivityLog Recommendation, ActivityLog Policy, ActivityLog Autoscale, Log Analytics, Nagios, Platform, SCOM, ServiceHealth, SmartDetector, VM Insights, Zabbix] |
| **monitorCondition** | **String**| Filter by monitor condition which is either &#39;Fired&#39; or &#39;Resolved&#39;. Default value is to select all. | [optional] [enum: Fired, Resolved] |
| **severity** | **String**| Filter by severity.  Default value is select all. | [optional] [enum: Sev0, Sev1, Sev2, Sev3, Sev4] |
| **smartGroupState** | **String**| Filter by state of the smart group. Default value is to select all. | [optional] [enum: New, Acknowledged, Closed] |
| **timeRange** | **String**| Filter by time range by below listed values. Default value is 1 day. | [optional] [enum: 1h, 1d, 7d, 30d] |
| **pageCount** | **Integer**| Determines number of alerts returned per page in response. Permissible value is between 1 to 250. When the \&quot;includeContent\&quot;  filter is selected, maximum value allowed is 25. Default value is 25. | [optional] |
| **sortBy** | **String**| Sort the query results by input field. Default value is sort by &#39;lastModifiedDateTime&#39;. | [optional] [enum: alertsCount, state, severity, startDateTime, lastModifiedDateTime] |
| **sortOrder** | **String**| Sort the query results order in either ascending or descending.  Default value is &#39;desc&#39; for time fields and &#39;asc&#39; for others. | [optional] [enum: asc, desc] |

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

Get information related to a specific Smart Group.

Get information related to a specific Smart Group.

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String smartGroupId = "smartGroupId_example"; // String | Smart group unique id. 
    String apiVersion = "2018-05-05"; // String | API version.
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **smartGroupId** | **String**| Smart group unique id.  | |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |

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



Get the history a smart group, which captures any Smart Group state changes (New/Acknowledged/Closed) .

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String smartGroupId = "smartGroupId_example"; // String | Smart group unique id. 
    String apiVersion = "2018-05-05"; // String | API version.
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **smartGroupId** | **String**| Smart group unique id.  | |
| **apiVersion** | **String**| API version. | [enum: 2018-05-05] |

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

