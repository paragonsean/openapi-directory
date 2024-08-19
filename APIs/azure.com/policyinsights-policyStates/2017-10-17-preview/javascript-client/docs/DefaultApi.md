# PolicyStatesClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.PolicyInsights/operations | 
[**policyStatesGetMetadata**](DefaultApi.md#policyStatesGetMetadata) | **GET** /{scope}/providers/Microsoft.PolicyInsights/policyStates/$metadata | 
[**policyStatesListQueryResultsForManagementGroup**](DefaultApi.md#policyStatesListQueryResultsForManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults | 
[**policyStatesListQueryResultsForResource**](DefaultApi.md#policyStatesListQueryResultsForResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults | 
[**policyStatesListQueryResultsForResourceGroup**](DefaultApi.md#policyStatesListQueryResultsForResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults | 
[**policyStatesListQueryResultsForSubscription**](DefaultApi.md#policyStatesListQueryResultsForSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/policyStates/{policyStatesResource}/queryResults | 



## operationsList

> OperationsListResults operationsList(apiVersion)



Lists available operations.

### Example

```javascript
import PolicyStatesClient from 'policy_states_client';
let defaultClient = PolicyStatesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyStatesClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| API version to use with the client requests. | 

### Return type

[**OperationsListResults**](OperationsListResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyStatesGetMetadata

> String policyStatesGetMetadata(scope, apiVersion)



Gets OData metadata XML document.

### Example

```javascript
import PolicyStatesClient from 'policy_states_client';
let defaultClient = PolicyStatesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyStatesClient.DefaultApi();
let scope = "scope_example"; // String | A valid scope, i.e. management group, subscription, resource group, or resource ID. Scope used has no effect on metadata returned.
let apiVersion = "apiVersion_example"; // String | API version to use with the client requests.
apiInstance.policyStatesGetMetadata(scope, apiVersion, (error, data, response) => {
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


## policyStatesListQueryResultsForManagementGroup

> PolicyStatesQueryResults policyStatesListQueryResultsForManagementGroup(policyStatesResource, managementGroupsNamespace, managementGroupName, apiVersion, opts)



Queries policy states for the resources under the management group.

### Example

```javascript
import PolicyStatesClient from 'policy_states_client';
let defaultClient = PolicyStatesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyStatesClient.DefaultApi();
let policyStatesResource = "policyStatesResource_example"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
let managementGroupsNamespace = "managementGroupsNamespace_example"; // String | The namespace for Microsoft Management resource provider; only \"Microsoft.Management\" is allowed.
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
apiInstance.policyStatesListQueryResultsForManagementGroup(policyStatesResource, managementGroupsNamespace, managementGroupName, apiVersion, opts, (error, data, response) => {
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
 **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | 
 **managementGroupsNamespace** | **String**| The namespace for Microsoft Management resource provider; only \&quot;Microsoft.Management\&quot; is allowed. | 
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

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyStatesListQueryResultsForResource

> PolicyStatesQueryResults policyStatesListQueryResultsForResource(policyStatesResource, resourceId, apiVersion, opts)



Queries policy states for the resource.

### Example

```javascript
import PolicyStatesClient from 'policy_states_client';
let defaultClient = PolicyStatesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyStatesClient.DefaultApi();
let policyStatesResource = "policyStatesResource_example"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
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
apiInstance.policyStatesListQueryResultsForResource(policyStatesResource, resourceId, apiVersion, opts, (error, data, response) => {
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
 **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | 
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

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyStatesListQueryResultsForResourceGroup

> PolicyStatesQueryResults policyStatesListQueryResultsForResourceGroup(policyStatesResource, subscriptionId, resourceGroupName, apiVersion, opts)



Queries policy states for the resources under the resource group.

### Example

```javascript
import PolicyStatesClient from 'policy_states_client';
let defaultClient = PolicyStatesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyStatesClient.DefaultApi();
let policyStatesResource = "policyStatesResource_example"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
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
apiInstance.policyStatesListQueryResultsForResourceGroup(policyStatesResource, subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | 
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

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyStatesListQueryResultsForSubscription

> PolicyStatesQueryResults policyStatesListQueryResultsForSubscription(policyStatesResource, subscriptionId, apiVersion, opts)



Queries policy states for the resources under the subscription.

### Example

```javascript
import PolicyStatesClient from 'policy_states_client';
let defaultClient = PolicyStatesClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyStatesClient.DefaultApi();
let policyStatesResource = "policyStatesResource_example"; // String | The virtual resource under PolicyStates resource type. In a given time range, 'latest' represents the latest policy state(s), whereas 'default' represents all policy state(s).
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
apiInstance.policyStatesListQueryResultsForSubscription(policyStatesResource, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **policyStatesResource** | **String**| The virtual resource under PolicyStates resource type. In a given time range, &#39;latest&#39; represents the latest policy state(s), whereas &#39;default&#39; represents all policy state(s). | 
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

[**PolicyStatesQueryResults**](PolicyStatesQueryResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

