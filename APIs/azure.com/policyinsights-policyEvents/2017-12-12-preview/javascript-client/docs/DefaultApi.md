# PolicyEventsClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyEventsGetMetadata**](DefaultApi.md#policyEventsGetMetadata) | **GET** /{scope}/providers/Microsoft.PolicyInsights/policyEvents/$metadata | 
[**policyEventsListQueryResultsForManagementGroup**](DefaultApi.md#policyEventsListQueryResultsForManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults | 
[**policyEventsListQueryResultsForPolicyDefinition**](DefaultApi.md#policyEventsListQueryResultsForPolicyDefinition) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policyDefinitions/{policyDefinitionName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults | 
[**policyEventsListQueryResultsForPolicySetDefinition**](DefaultApi.md#policyEventsListQueryResultsForPolicySetDefinition) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policySetDefinitions/{policySetDefinitionName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults | 
[**policyEventsListQueryResultsForResource**](DefaultApi.md#policyEventsListQueryResultsForResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults | 
[**policyEventsListQueryResultsForResourceGroup**](DefaultApi.md#policyEventsListQueryResultsForResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults | 
[**policyEventsListQueryResultsForResourceGroupLevelPolicyAssignment**](DefaultApi.md#policyEventsListQueryResultsForResourceGroupLevelPolicyAssignment) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{authorizationNamespace}/policyAssignments/{policyAssignmentName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults | 
[**policyEventsListQueryResultsForSubscription**](DefaultApi.md#policyEventsListQueryResultsForSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults | 
[**policyEventsListQueryResultsForSubscriptionLevelPolicyAssignment**](DefaultApi.md#policyEventsListQueryResultsForSubscriptionLevelPolicyAssignment) | **POST** /subscriptions/{subscriptionId}/providers/{authorizationNamespace}/policyAssignments/{policyAssignmentName}/providers/Microsoft.PolicyInsights/policyEvents/{policyEventsResource}/queryResults | 



## policyEventsGetMetadata

> String policyEventsGetMetadata(scope, apiVersion)



Gets OData metadata XML document.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let scope = "scope_example"; // String | A valid scope, i.e. management group, subscription, resource group, or resource ID. Scope used has no effect on metadata returned.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
apiInstance.policyEventsGetMetadata(scope, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **String**| A valid scope, i.e. management group, subscription, resource group, or resource ID. Scope used has no effect on metadata returned. | 
 **apiVersion** | **String**| API version to use with the client requests. | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml


## policyEventsListQueryResultsForManagementGroup

> PolicyEventsQueryResults policyEventsListQueryResultsForManagementGroup(policyEventsResource, managementGroupsNamespace, managementGroupName, apiVersion, opts)



Queries policy events for the resources under the management group.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let policyEventsResource = "policyEventsResource_example"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
let managementGroupsNamespace = "managementGroupsNamespace_example"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
let managementGroupName = "managementGroupName_example"; // String | Management group name.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'orderby': "orderby_example", // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
  'select': "select_example", // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
  'filter': "filter_example", // String | OData filter expression.
  'apply': "apply_example" // String | OData apply expression for aggregations.
};
apiInstance.policyEventsListQueryResultsForManagementGroup(policyEventsResource, managementGroupsNamespace, managementGroupName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | 
 **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | 
 **managementGroupName** | **String**| Management group name. | 
 **apiVersion** | **String**| API version to use with the client requests. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] 
 **select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] 
 **from** | **Date**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] 
 **to** | **Date**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 
 **apply** | **String**| OData apply expression for aggregations. | [optional] 

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyEventsListQueryResultsForPolicyDefinition

> PolicyEventsQueryResults policyEventsListQueryResultsForPolicyDefinition(policyEventsResource, subscriptionId, authorizationNamespace, policyDefinitionName, apiVersion, opts)



Queries policy events for the subscription level policy definition.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let policyEventsResource = "policyEventsResource_example"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let authorizationNamespace = "authorizationNamespace_example"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
let policyDefinitionName = "policyDefinitionName_example"; // String | Policy definition name.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'orderby': "orderby_example", // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
  'select': "select_example", // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
  'filter': "filter_example", // String | OData filter expression.
  'apply': "apply_example" // String | OData apply expression for aggregations.
};
apiInstance.policyEventsListQueryResultsForPolicyDefinition(policyEventsResource, subscriptionId, authorizationNamespace, policyDefinitionName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | 
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | 
 **policyDefinitionName** | **String**| Policy definition name. | 
 **apiVersion** | **String**| API version to use with the client requests. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] 
 **select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] 
 **from** | **Date**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] 
 **to** | **Date**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 
 **apply** | **String**| OData apply expression for aggregations. | [optional] 

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyEventsListQueryResultsForPolicySetDefinition

> PolicyEventsQueryResults policyEventsListQueryResultsForPolicySetDefinition(policyEventsResource, subscriptionId, authorizationNamespace, policySetDefinitionName, apiVersion, opts)



Queries policy events for the subscription level policy set definition.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let policyEventsResource = "policyEventsResource_example"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let authorizationNamespace = "authorizationNamespace_example"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
let policySetDefinitionName = "policySetDefinitionName_example"; // String | Policy set definition name.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'orderby': "orderby_example", // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
  'select': "select_example", // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
  'filter': "filter_example", // String | OData filter expression.
  'apply': "apply_example" // String | OData apply expression for aggregations.
};
apiInstance.policyEventsListQueryResultsForPolicySetDefinition(policyEventsResource, subscriptionId, authorizationNamespace, policySetDefinitionName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | 
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | 
 **policySetDefinitionName** | **String**| Policy set definition name. | 
 **apiVersion** | **String**| API version to use with the client requests. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] 
 **select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] 
 **from** | **Date**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] 
 **to** | **Date**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 
 **apply** | **String**| OData apply expression for aggregations. | [optional] 

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyEventsListQueryResultsForResource

> PolicyEventsQueryResults policyEventsListQueryResultsForResource(policyEventsResource, resourceId, apiVersion, opts)



Queries policy events for the resource.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let policyEventsResource = "policyEventsResource_example"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
let resourceId = "resourceId_example"; // String | Resource ID.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'orderby': "orderby_example", // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
  'select': "select_example", // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
  'filter': "filter_example", // String | OData filter expression.
  'apply': "apply_example" // String | OData apply expression for aggregations.
};
apiInstance.policyEventsListQueryResultsForResource(policyEventsResource, resourceId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | 
 **resourceId** | **String**| Resource ID. | 
 **apiVersion** | **String**| API version to use with the client requests. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] 
 **select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] 
 **from** | **Date**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] 
 **to** | **Date**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 
 **apply** | **String**| OData apply expression for aggregations. | [optional] 

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyEventsListQueryResultsForResourceGroup

> PolicyEventsQueryResults policyEventsListQueryResultsForResourceGroup(policyEventsResource, subscriptionId, resourceGroupName, apiVersion, opts)



Queries policy events for the resources under the resource group.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let policyEventsResource = "policyEventsResource_example"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'orderby': "orderby_example", // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
  'select': "select_example", // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
  'filter': "filter_example", // String | OData filter expression.
  'apply': "apply_example" // String | OData apply expression for aggregations.
};
apiInstance.policyEventsListQueryResultsForResourceGroup(policyEventsResource, subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | 
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **apiVersion** | **String**| API version to use with the client requests. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] 
 **select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] 
 **from** | **Date**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] 
 **to** | **Date**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 
 **apply** | **String**| OData apply expression for aggregations. | [optional] 

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyEventsListQueryResultsForResourceGroupLevelPolicyAssignment

> PolicyEventsQueryResults policyEventsListQueryResultsForResourceGroupLevelPolicyAssignment(policyEventsResource, subscriptionId, resourceGroupName, authorizationNamespace, policyAssignmentName, apiVersion, opts)



Queries policy events for the resource group level policy assignment.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let policyEventsResource = "policyEventsResource_example"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let authorizationNamespace = "authorizationNamespace_example"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
let policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'orderby': "orderby_example", // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
  'select': "select_example", // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
  'filter': "filter_example", // String | OData filter expression.
  'apply': "apply_example" // String | OData apply expression for aggregations.
};
apiInstance.policyEventsListQueryResultsForResourceGroupLevelPolicyAssignment(policyEventsResource, subscriptionId, resourceGroupName, authorizationNamespace, policyAssignmentName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | 
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | 
 **policyAssignmentName** | **String**| Policy assignment name. | 
 **apiVersion** | **String**| API version to use with the client requests. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] 
 **select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] 
 **from** | **Date**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] 
 **to** | **Date**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 
 **apply** | **String**| OData apply expression for aggregations. | [optional] 

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyEventsListQueryResultsForSubscription

> PolicyEventsQueryResults policyEventsListQueryResultsForSubscription(policyEventsResource, subscriptionId, apiVersion, opts)



Queries policy events for the resources under the subscription.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let policyEventsResource = "policyEventsResource_example"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'orderby': "orderby_example", // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
  'select': "select_example", // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
  'filter': "filter_example", // String | OData filter expression.
  'apply': "apply_example" // String | OData apply expression for aggregations.
};
apiInstance.policyEventsListQueryResultsForSubscription(policyEventsResource, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | 
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **apiVersion** | **String**| API version to use with the client requests. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] 
 **select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] 
 **from** | **Date**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] 
 **to** | **Date**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 
 **apply** | **String**| OData apply expression for aggregations. | [optional] 

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyEventsListQueryResultsForSubscriptionLevelPolicyAssignment

> PolicyEventsQueryResults policyEventsListQueryResultsForSubscriptionLevelPolicyAssignment(policyEventsResource, subscriptionId, authorizationNamespace, policyAssignmentName, apiVersion, opts)



Queries policy events for the subscription level policy assignment.

### Example

```javascript
import PolicyEventsClient from 'policy_events_client';
let defaultClient = PolicyEventsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyEventsClient.DefaultApi();
let policyEventsResource = "policyEventsResource_example"; // String | The name of the virtual resource under PolicyEvents resource type; only \"default\" is allowed.
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let authorizationNamespace = "authorizationNamespace_example"; // String | The namespace for Microsoft Authorization resource provider; only \"Microsoft.Authorization\" is allowed.
let policyAssignmentName = "policyAssignmentName_example"; // String | Policy assignment name.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'orderby': "orderby_example", // String | Ordering expression using OData notation. One or more comma-separated column names with an optional \"desc\" (the default) or \"asc\", e.g. \"$orderby=PolicyAssignmentId, ResourceId asc\".
  'select': "select_example", // String | Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \"$select=PolicyAssignmentId, ResourceId\".
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time.
  'filter': "filter_example", // String | OData filter expression.
  'apply': "apply_example" // String | OData apply expression for aggregations.
};
apiInstance.policyEventsListQueryResultsForSubscriptionLevelPolicyAssignment(policyEventsResource, subscriptionId, authorizationNamespace, policyAssignmentName, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyEventsResource** | **String**| The name of the virtual resource under PolicyEvents resource type; only \&quot;default\&quot; is allowed. | 
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **authorizationNamespace** | **String**| The namespace for Microsoft Authorization resource provider; only \&quot;Microsoft.Authorization\&quot; is allowed. | 
 **policyAssignmentName** | **String**| Policy assignment name. | 
 **apiVersion** | **String**| API version to use with the client requests. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **orderby** | **String**| Ordering expression using OData notation. One or more comma-separated column names with an optional \&quot;desc\&quot; (the default) or \&quot;asc\&quot;, e.g. \&quot;$orderby&#x3D;PolicyAssignmentId, ResourceId asc\&quot;. | [optional] 
 **select** | **String**| Select expression using OData notation. Limits the columns on each record to just those requested, e.g. \&quot;$select&#x3D;PolicyAssignmentId, ResourceId\&quot;. | [optional] 
 **from** | **Date**| ISO 8601 formatted timestamp specifying the start time of the interval to query. When not specified, the service uses ($to - 1-day). | [optional] 
 **to** | **Date**| ISO 8601 formatted timestamp specifying the end time of the interval to query. When not specified, the service uses request time. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 
 **apply** | **String**| OData apply expression for aggregations. | [optional] 

### Return type

[**PolicyEventsQueryResults**](PolicyEventsQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

