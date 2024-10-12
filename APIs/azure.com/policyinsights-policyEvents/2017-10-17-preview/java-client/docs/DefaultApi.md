# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policyEventsGetMetadata**](DefaultApi.md#policyEventsGetMetadata) | **GET** /{scope}/providers/Microsoft.PolicyInsights/policyEvents/$metadata |  |
| [**policyEventsListQueryResultsForManagementGroup**](DefaultApi.md#policyEventsListQueryResultsForManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults |  |
| [**policyEventsListQueryResultsForResource**](DefaultApi.md#policyEventsListQueryResultsForResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults |  |
| [**policyEventsListQueryResultsForResourceGroup**](DefaultApi.md#policyEventsListQueryResultsForResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults |  |
| [**policyEventsListQueryResultsForSubscription**](DefaultApi.md#policyEventsListQueryResultsForSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults |  |


<a id="policyEventsGetMetadata"></a>
# **policyEventsGetMetadata**
> String policyEventsGetMetadata(scope, apiVersion)



Gets OData metadata XML document.

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
    String scope = "scope_example"; // String | A valid scope, i.e. management group, subscription, resource group, or resource ID. Scope used has no effect on metadata returned.
    String apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
    try {
      String result = apiInstance.policyEventsGetMetadata(scope, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyEventsGetMetadata");
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
| **scope** | **String**| A valid scope, i.e. management group, subscription, resource group, or resource ID. Scope used has no effect on metadata returned. | |
| **apiVersion** | **String**| API version to use with the client requests. | |

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OData metadata XML document. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="policyEventsListQueryResultsForManagementGroup"></a>
# **policyEventsListQueryResultsForManagementGroup**
> PolicyEventsQueryResults policyEventsListQueryResultsForManagementGroup(policyEventsResource, managementGroupsNamespace, managementGroupName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy events for the resources under the management group.

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
    String policyEventsResource = "default"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
    String managementGroupsNamespace = "Microsoft.Management"; // String | The namespace for Microsoft Management resource provider; only \"Microsoft.Management\" is allowed.
    String managementGroupName = "managementGroupName_example"; // String | Management group name.
    String apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyEventsQueryResults result = apiInstance.policyEventsListQueryResultsForManagementGroup(policyEventsResource, managementGroupsNamespace, managementGroupName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyEventsListQueryResultsForManagementGroup");
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
| **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | [enum: default] |
| **managementGroupsNamespace** | **String**| The namespace for Microsoft Management resource provider; only \&quot;Microsoft.Management\&quot; is allowed. | [enum: Microsoft.Management] |
| **managementGroupName** | **String**| Management group name. | |
| **apiVersion** | **String**| API version to use with the client requests. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

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

<a id="policyEventsListQueryResultsForResource"></a>
# **policyEventsListQueryResultsForResource**
> PolicyEventsQueryResults policyEventsListQueryResultsForResource(policyEventsResource, resourceId, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy events for the resource.

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
    String policyEventsResource = "default"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
    String resourceId = "resourceId_example"; // String | Resource ID.
    String apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyEventsQueryResults result = apiInstance.policyEventsListQueryResultsForResource(policyEventsResource, resourceId, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyEventsListQueryResultsForResource");
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
| **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | [enum: default] |
| **resourceId** | **String**| Resource ID. | |
| **apiVersion** | **String**| API version to use with the client requests. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

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

<a id="policyEventsListQueryResultsForResourceGroup"></a>
# **policyEventsListQueryResultsForResourceGroup**
> PolicyEventsQueryResults policyEventsListQueryResultsForResourceGroup(policyEventsResource, subscriptionId, resourceGroupName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy events for the resources under the resource group.

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
    String policyEventsResource = "default"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
    String apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyEventsQueryResults result = apiInstance.policyEventsListQueryResultsForResourceGroup(policyEventsResource, subscriptionId, resourceGroupName, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyEventsListQueryResultsForResourceGroup");
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
| **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | [enum: default] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group name. | |
| **apiVersion** | **String**| API version to use with the client requests. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

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

<a id="policyEventsListQueryResultsForSubscription"></a>
# **policyEventsListQueryResultsForSubscription**
> PolicyEventsQueryResults policyEventsListQueryResultsForSubscription(policyEventsResource, subscriptionId, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply)



Queries policy events for the resources under the subscription.

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
    String policyEventsResource = "default"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
    String subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
    Integer $top = 56; // Integer | Maximum number of records to return.
    String $orderby = "$orderby_example"; // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
    String $select = "$select_example"; // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
    OffsetDateTime $from = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
    OffsetDateTime $to = OffsetDateTime.now(); // OffsetDateTime | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
    String $filter = "$filter_example"; // String | OData filter expression.
    String $apply = "$apply_example"; // String | OData apply expression for aggregations.
    try {
      PolicyEventsQueryResults result = apiInstance.policyEventsListQueryResultsForSubscription(policyEventsResource, subscriptionId, apiVersion, $top, $orderby, $select, $from, $to, $filter, $apply);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#policyEventsListQueryResultsForSubscription");
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
| **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | [enum: default] |
| **subscriptionId** | **String**| Microsoft Azure subscription ID. | |
| **apiVersion** | **String**| API version to use with the client requests. | |
| **$top** | **Integer**| Maximum number of records to return. | [optional] |
| **$orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] |
| **$select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] |
| **$from** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] |
| **$to** | **OffsetDateTime**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] |
| **$filter** | **String**| OData filter expression. | [optional] |
| **$apply** | **String**| OData apply expression for aggregations. | [optional] |

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

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

