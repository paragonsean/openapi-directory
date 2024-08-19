# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.PolicyInsights/operations |  |
| [**policyStatesListQueryResultsForManagementGroup**](DefaultApi.md#policyStatesListQueryResultsForManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults |  |
| [**policyStatesListQueryResultsForPolicyDefinition**](DefaultApi.md#policyStatesListQueryResultsForPolicyDefinition) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policyDefinitions/{policyDefinitionName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults |  |
| [**policyStatesListQueryResultsForPolicySetDefinition**](DefaultApi.md#policyStatesListQueryResultsForPolicySetDefinition) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policySetDefinitions/{policySetDefinitionName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults |  |
| [**policyStatesListQueryResultsForResource**](DefaultApi.md#policyStatesListQueryResultsForResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults |  |
| [**policyStatesListQueryResultsForResourceGroup**](DefaultApi.md#policyStatesListQueryResultsForResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults |  |
| [**policyStatesListQueryResultsForResourceGroupLevelPolicyAssignment**](DefaultApi.md#policyStatesListQueryResultsForResourceGroupLevelPolicyAssignment) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{authorizationNamespace}/policyAssignments/{policyAssignmentName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults |  |
| [**policyStatesListQueryResultsForSubscription**](DefaultApi.md#policyStatesListQueryResultsForSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults |  |
| [**policyStatesListQueryResultsForSubscriptionLevelPolicyAssignment**](DefaultApi.md#policyStatesListQueryResultsForSubscriptionLevelPolicyAssignment) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policyAssignments/{policyAssignmentName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults |  |
| [**policyStatesSummarizeForManagementGroup**](DefaultApi.md#policyStatesSummarizeForManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesSummaryResource}/summarize |  |
| [**policyStatesSummarizeForPolicyDefinition**](DefaultApi.md#policyStatesSummarizeForPolicyDefinition) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policyDefinitions/{policyDefinitionName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesSummaryResource}/summarize |  |
| [**policyStatesSummarizeForPolicySetDefinition**](DefaultApi.md#policyStatesSummarizeForPolicySetDefinition) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policySetDefinitions/{policySetDefinitionName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesSummaryResource}/summarize |  |
| [**policyStatesSummarizeForResource**](DefaultApi.md#policyStatesSummarizeForResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesSummaryResource}/summarize |  |
| [**policyStatesSummarizeForResourceGroup**](DefaultApi.md#policyStatesSummarizeForResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesSummaryResource}/summarize |  |
| [**policyStatesSummarizeForResourceGroupLevelPolicyAssignment**](DefaultApi.md#policyStatesSummarizeForResourceGroupLevelPolicyAssignment) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{authorizationNamespace}/policyAssignments/{policyAssignmentName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesSummaryResource}/summarize |  |
| [**policyStatesSummarizeForSubscription**](DefaultApi.md#policyStatesSummarizeForSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesSummaryResource}/summarize |  |
| [**policyStatesSummarizeForSubscriptionLevelPolicyAssignment**](DefaultApi.md#policyStatesSummarizeForSubscriptionLevelPolicyAssignment) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policyAssignments/{policyAssignmentName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesSummaryResource}/summarize |  |
| [**policyStatesTriggerResourceGroupEvaluation**](DefaultApi.md#policyStatesTriggerResourceGroupEvaluation) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyStates/latest/triggerEvaluation |  |
| [**policyStatesTriggerSubscriptionEvaluation**](DefaultApi.md#policyStatesTriggerSubscriptionEvaluation) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyStates/latest/triggerEvaluation |  |


<a id="operationsList"></a>
# **operationsList**
> OperationsListResults operationsList(apiVersion)



Lists available operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      OperationsListResults result = apiInstance.operationsList(apiVersion);
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
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**OperationsListResults**](OperationsListResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of available operations. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesListQueryResultsForManagementGroup"></a>
# **policyStatesListQueryResultsForManagementGroup**
> PolicyStatesQueryResults policyStatesListQueryResultsForManagementGroup(policyStatesResource, managementGroupsNamespace, managementGroupName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy states for the resources under the management group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesResource = "default"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
    String managementGroupName = "managementGroupName_example"; // String | Management group name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyStatesQueryResults result = apiInstance.policyStatesListQueryResultsForManagementGroup(policyStatesResource, managementGroupsNamespace, managementGroupName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesListQueryResultsForManagementGroup");
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
| **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | [enum: default, latest] |
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupName** | **String**| Management group name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesListQueryResultsForPolicyDefinition"></a>
# **policyStatesListQueryResultsForPolicyDefinition**
> PolicyStatesQueryResults policyStatesListQueryResultsForPolicyDefinition(policyStatesResource, subscriptionId, authorizationNamespace, policyDefinitionName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy states for the subscription level policy definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesResource = "default"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String authorizationNamespace = "Microsoft.Authorization"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
    String policyDefinitionName = "policyDefinitionName_example"; // String | Policy definition name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyStatesQueryResults result = apiInstance.policyStatesListQueryResultsForPolicyDefinition(policyStatesResource, subscriptionId, authorizationNamespace, policyDefinitionName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesListQueryResultsForPolicyDefinition");
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
| **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | [enum: default, latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | [enum: Microsoft.Authorization] |
| **policyDefinitionName** | **String**| Policy definition name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesListQueryResultsForPolicySetDefinition"></a>
# **policyStatesListQueryResultsForPolicySetDefinition**
> PolicyStatesQueryResults policyStatesListQueryResultsForPolicySetDefinition(policyStatesResource, subscriptionId, authorizationNamespace, policySetDefinitionName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy states for the subscription level policy set definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesResource = "default"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String authorizationNamespace = "Microsoft.Authorization"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | Policy set definition name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyStatesQueryResults result = apiInstance.policyStatesListQueryResultsForPolicySetDefinition(policyStatesResource, subscriptionId, authorizationNamespace, policySetDefinitionName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesListQueryResultsForPolicySetDefinition");
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
| **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | [enum: default, latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | [enum: Microsoft.Authorization] |
| **policySetDefinitionName** | **String**| Policy set definition name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesListQueryResultsForResource"></a>
# **policyStatesListQueryResultsForResource**
> PolicyStatesQueryResults policyStatesListQueryResultsForResource(policyStatesResource, resourceId, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply, $expand)



Queries policy states for the resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesResource = "default"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
    String resourceId = "resourceId_example"; // String | Resource ID.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    String $expand = "$expand_example"; // String | The $expand query parameter. For example, to expand policyEvaluationDetails, use $expand=policyEvaluationDetails
    try {
      PolicyStatesQueryResults result = apiInstance.policyStatesListQueryResultsForResource(policyStatesResource, resourceId, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesListQueryResultsForResource");
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
| **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | [enum: default, latest] |
| **resourceId** | **String**| Resource ID. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |
| **$expand** | **String**| The $expand query parameter. For example, to expand policyEvaluationDetails, use $expand&#x3D;policyEvaluationDetails | [optional] |

### Return type

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesListQueryResultsForResourceGroup"></a>
# **policyStatesListQueryResultsForResourceGroup**
> PolicyStatesQueryResults policyStatesListQueryResultsForResourceGroup(policyStatesResource, subscriptionId, resourceGroupName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy states for the resources under the resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesResource = "default"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyStatesQueryResults result = apiInstance.policyStatesListQueryResultsForResourceGroup(policyStatesResource, subscriptionId, resourceGroupName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesListQueryResultsForResourceGroup");
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
| **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | [enum: default, latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesListQueryResultsForResourceGroupLevelPolicyAssignment"></a>
# **policyStatesListQueryResultsForResourceGroupLevelPolicyAssignment**
> PolicyStatesQueryResults policyStatesListQueryResultsForResourceGroupLevelPolicyAssignment(policyStatesResource, subscriptionId, resourceGroupName, authorizationNamespace, policyAssignmentName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy states for the resource group level policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesResource = "default"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String authorizationNamespace = "Microsoft.Authorization"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
    String policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyStatesQueryResults result = apiInstance.policyStatesListQueryResultsForResourceGroupLevelPolicyAssignment(policyStatesResource, subscriptionId, resourceGroupName, authorizationNamespace, policyAssignmentName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesListQueryResultsForResourceGroupLevelPolicyAssignment");
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
| **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | [enum: default, latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | [enum: Microsoft.Authorization] |
| **policyAssignmentName** | **String**| Policy assignment name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesListQueryResultsForSubscription"></a>
# **policyStatesListQueryResultsForSubscription**
> PolicyStatesQueryResults policyStatesListQueryResultsForSubscription(policyStatesResource, subscriptionId, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy states for the resources under the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesResource = "default"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyStatesQueryResults result = apiInstance.policyStatesListQueryResultsForSubscription(policyStatesResource, subscriptionId, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesListQueryResultsForSubscription");
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
| **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | [enum: default, latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesListQueryResultsForSubscriptionLevelPolicyAssignment"></a>
# **policyStatesListQueryResultsForSubscriptionLevelPolicyAssignment**
> PolicyStatesQueryResults policyStatesListQueryResultsForSubscriptionLevelPolicyAssignment(policyStatesResource, subscriptionId, authorizationNamespace, policyAssignmentName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy states for the subscription level policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesResource = "default"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String authorizationNamespace = "Microsoft.Authorization"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
    String policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyStatesQueryResults result = apiInstance.policyStatesListQueryResultsForSubscriptionLevelPolicyAssignment(policyStatesResource, subscriptionId, authorizationNamespace, policyAssignmentName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesListQueryResultsForSubscriptionLevelPolicyAssignment");
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
| **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | [enum: default, latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | [enum: Microsoft.Authorization] |
| **policyAssignmentName** | **String**| Policy assignment name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesSummarizeForManagementGroup"></a>
# **policyStatesSummarizeForManagementGroup**
> SummarizeResults policyStatesSummarizeForManagementGroup(policyStatesSummaryResource, managementGroupsNamespace, managementGroupName, apiVersion, $top, $from, $to, $filter)



Summarizes policy states for the resources under the management group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesSummaryResource = "latest"; // String | The virtual resource under PolicyStates resource type for summarize action. In a given time range, 'latest' represents the latest policy state(s) and is the only allowed value.
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
    String managementGroupName = "managementGroupName_example"; // String | Management group name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      SummarizeResults result = apiInstance.policyStatesSummarizeForManagementGroup(policyStatesSummaryResource, managementGroupsNamespace, managementGroupName, apiVersion, $top, $from, $to, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesSummarizeForManagementGroup");
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
| **policyStatesSummaryResource** | **String**| The virtual resource under PolicyStates resource type for summarize action. In a given time range, &#39;latest&#39; represents the latest policy state(s) and is the only allowed value. | [enum: latest] |
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupName** | **String**| Management group name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**SummarizeResults**](SummarizeResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summarize results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesSummarizeForPolicyDefinition"></a>
# **policyStatesSummarizeForPolicyDefinition**
> SummarizeResults policyStatesSummarizeForPolicyDefinition(policyStatesSummaryResource, subscriptionId, authorizationNamespace, policyDefinitionName, apiVersion, $top, $from, $to, $filter)



Summarizes policy states for the subscription level policy definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesSummaryResource = "latest"; // String | The virtual resource under PolicyStates resource type for summarize action. In a given time range, 'latest' represents the latest policy state(s) and is the only allowed value.
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String authorizationNamespace = "Microsoft.Authorization"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
    String policyDefinitionName = "policyDefinitionName_example"; // String | Policy definition name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      SummarizeResults result = apiInstance.policyStatesSummarizeForPolicyDefinition(policyStatesSummaryResource, subscriptionId, authorizationNamespace, policyDefinitionName, apiVersion, $top, $from, $to, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesSummarizeForPolicyDefinition");
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
| **policyStatesSummaryResource** | **String**| The virtual resource under PolicyStates resource type for summarize action. In a given time range, &#39;latest&#39; represents the latest policy state(s) and is the only allowed value. | [enum: latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | [enum: Microsoft.Authorization] |
| **policyDefinitionName** | **String**| Policy definition name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**SummarizeResults**](SummarizeResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summarize results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesSummarizeForPolicySetDefinition"></a>
# **policyStatesSummarizeForPolicySetDefinition**
> SummarizeResults policyStatesSummarizeForPolicySetDefinition(policyStatesSummaryResource, subscriptionId, authorizationNamespace, policySetDefinitionName, apiVersion, $top, $from, $to, $filter)



Summarizes policy states for the subscription level policy set definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesSummaryResource = "latest"; // String | The virtual resource under PolicyStates resource type for summarize action. In a given time range, 'latest' represents the latest policy state(s) and is the only allowed value.
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String authorizationNamespace = "Microsoft.Authorization"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
    String policySetDefinitionName = "policySetDefinitionName_example"; // String | Policy set definition name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      SummarizeResults result = apiInstance.policyStatesSummarizeForPolicySetDefinition(policyStatesSummaryResource, subscriptionId, authorizationNamespace, policySetDefinitionName, apiVersion, $top, $from, $to, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesSummarizeForPolicySetDefinition");
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
| **policyStatesSummaryResource** | **String**| The virtual resource under PolicyStates resource type for summarize action. In a given time range, &#39;latest&#39; represents the latest policy state(s) and is the only allowed value. | [enum: latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | [enum: Microsoft.Authorization] |
| **policySetDefinitionName** | **String**| Policy set definition name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**SummarizeResults**](SummarizeResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summarize results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesSummarizeForResource"></a>
# **policyStatesSummarizeForResource**
> SummarizeResults policyStatesSummarizeForResource(policyStatesSummaryResource, resourceId, apiVersion, $top, $from, $to, $filter)



Summarizes policy states for the resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesSummaryResource = "latest"; // String | The virtual resource under PolicyStates resource type for summarize action. In a given time range, 'latest' represents the latest policy state(s) and is the only allowed value.
    String resourceId = "resourceId_example"; // String | Resource ID.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      SummarizeResults result = apiInstance.policyStatesSummarizeForResource(policyStatesSummaryResource, resourceId, apiVersion, $top, $from, $to, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesSummarizeForResource");
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
| **policyStatesSummaryResource** | **String**| The virtual resource under PolicyStates resource type for summarize action. In a given time range, &#39;latest&#39; represents the latest policy state(s) and is the only allowed value. | [enum: latest] |
| **resourceId** | **String**| Resource ID. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**SummarizeResults**](SummarizeResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summarize results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesSummarizeForResourceGroup"></a>
# **policyStatesSummarizeForResourceGroup**
> SummarizeResults policyStatesSummarizeForResourceGroup(policyStatesSummaryResource, subscriptionId, resourceGroupName, apiVersion, $top, $from, $to, $filter)



Summarizes policy states for the resources under the resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesSummaryResource = "latest"; // String | The virtual resource under PolicyStates resource type for summarize action. In a given time range, 'latest' represents the latest policy state(s) and is the only allowed value.
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      SummarizeResults result = apiInstance.policyStatesSummarizeForResourceGroup(policyStatesSummaryResource, subscriptionId, resourceGroupName, apiVersion, $top, $from, $to, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesSummarizeForResourceGroup");
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
| **policyStatesSummaryResource** | **String**| The virtual resource under PolicyStates resource type for summarize action. In a given time range, &#39;latest&#39; represents the latest policy state(s) and is the only allowed value. | [enum: latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**SummarizeResults**](SummarizeResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summarize results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesSummarizeForResourceGroupLevelPolicyAssignment"></a>
# **policyStatesSummarizeForResourceGroupLevelPolicyAssignment**
> SummarizeResults policyStatesSummarizeForResourceGroupLevelPolicyAssignment(policyStatesSummaryResource, subscriptionId, resourceGroupName, authorizationNamespace, policyAssignmentName, apiVersion, $top, $from, $to, $filter)



Summarizes policy states for the resource group level policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesSummaryResource = "latest"; // String | The virtual resource under PolicyStates resource type for summarize action. In a given time range, 'latest' represents the latest policy state(s) and is the only allowed value.
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String authorizationNamespace = "Microsoft.Authorization"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
    String policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      SummarizeResults result = apiInstance.policyStatesSummarizeForResourceGroupLevelPolicyAssignment(policyStatesSummaryResource, subscriptionId, resourceGroupName, authorizationNamespace, policyAssignmentName, apiVersion, $top, $from, $to, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesSummarizeForResourceGroupLevelPolicyAssignment");
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
| **policyStatesSummaryResource** | **String**| The virtual resource under PolicyStates resource type for summarize action. In a given time range, &#39;latest&#39; represents the latest policy state(s) and is the only allowed value. | [enum: latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | [enum: Microsoft.Authorization] |
| **policyAssignmentName** | **String**| Policy assignment name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**SummarizeResults**](SummarizeResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summarize results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesSummarizeForSubscription"></a>
# **policyStatesSummarizeForSubscription**
> SummarizeResults policyStatesSummarizeForSubscription(policyStatesSummaryResource, subscriptionId, apiVersion, $top, $from, $to, $filter)



Summarizes policy states for the resources under the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesSummaryResource = "latest"; // String | The virtual resource under PolicyStates resource type for summarize action. In a given time range, 'latest' represents the latest policy state(s) and is the only allowed value.
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      SummarizeResults result = apiInstance.policyStatesSummarizeForSubscription(policyStatesSummaryResource, subscriptionId, apiVersion, $top, $from, $to, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesSummarizeForSubscription");
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
| **policyStatesSummaryResource** | **String**| The virtual resource under PolicyStates resource type for summarize action. In a given time range, &#39;latest&#39; represents the latest policy state(s) and is the only allowed value. | [enum: latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**SummarizeResults**](SummarizeResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summarize results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesSummarizeForSubscriptionLevelPolicyAssignment"></a>
# **policyStatesSummarizeForSubscriptionLevelPolicyAssignment**
> SummarizeResults policyStatesSummarizeForSubscriptionLevelPolicyAssignment(policyStatesSummaryResource, subscriptionId, authorizationNamespace, policyAssignmentName, apiVersion, $top, $from, $to, $filter)



Summarizes policy states for the subscription level policy assignment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String policyStatesSummaryResource = "latest"; // String | The virtual resource under PolicyStates resource type for summarize action. In a given time range, 'latest' represents the latest policy state(s) and is the only allowed value.
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String authorizationNamespace = "Microsoft.Authorization"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
    String policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Integer $top = 56; // Integer | Maximum number of records to return.
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    try {
      SummarizeResults result = apiInstance.policyStatesSummarizeForSubscriptionLevelPolicyAssignment(policyStatesSummaryResource, subscriptionId, authorizationNamespace, policyAssignmentName, apiVersion, $top, $from, $to, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesSummarizeForSubscriptionLevelPolicyAssignment");
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
| **policyStatesSummaryResource** | **String**| The virtual resource under PolicyStates resource type for summarize action. In a given time range, &#39;latest&#39; represents the latest policy state(s) and is the only allowed value. | [enum: latest] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | [enum: Microsoft.Authorization] |
| **policyAssignmentName** | **String**| Policy assignment name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |

### Return type

[**SummarizeResults**](SummarizeResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summarize results. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesTriggerResourceGroupEvaluation"></a>
# **policyStatesTriggerResourceGroupEvaluation**
> policyStatesTriggerResourceGroupEvaluation(subscriptionId, resourceGroupName, apiVersion)



Triggers a policy evaluation scan for all the resources under the resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.policyStatesTriggerResourceGroupEvaluation(subscriptionId, resourceGroupName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesTriggerResourceGroupEvaluation");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
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
| **200** | The scan is done. |  -  |
| **202** | The scan was successfully triggered. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyStatesTriggerSubscriptionEvaluation"></a>
# **policyStatesTriggerSubscriptionEvaluation**
> policyStatesTriggerSubscriptionEvaluation(subscriptionId, apiVersion)



Triggers a policy evaluation scan for all the resources under the subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.policyStatesTriggerSubscriptionEvaluation(subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyStatesTriggerSubscriptionEvaluation");
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
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
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
| **200** | The scan is done. |  -  |
| **202** | The scan was successfully triggered. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

