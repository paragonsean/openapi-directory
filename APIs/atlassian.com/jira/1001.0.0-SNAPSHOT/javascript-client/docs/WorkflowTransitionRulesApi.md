# TheJiraCloudPlatformRestApi.WorkflowTransitionRulesApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteWorkflowTransitionRuleConfigurations**](WorkflowTransitionRulesApi.md#deleteWorkflowTransitionRuleConfigurations) | **PUT** /rest/api/3/workflow/rule/config/delete | Delete workflow transition rule configurations
[**getWorkflowTransitionRuleConfigurations**](WorkflowTransitionRulesApi.md#getWorkflowTransitionRuleConfigurations) | **GET** /rest/api/3/workflow/rule/config | Get workflow transition rule configurations
[**updateWorkflowTransitionRuleConfigurations**](WorkflowTransitionRulesApi.md#updateWorkflowTransitionRuleConfigurations) | **PUT** /rest/api/3/workflow/rule/config | Update workflow transition rule configurations



## deleteWorkflowTransitionRuleConfigurations

> WorkflowTransitionRulesUpdateErrors deleteWorkflowTransitionRuleConfigurations(workflowsWithTransitionRulesDetails)

Delete workflow transition rule configurations

Deletes workflow transition rules from one or more workflows. These rule types are supported:   *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)  *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)  *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)  Only rules created by the calling Connect app can be deleted.  **[Permissions](#permissions) required:** Only Connect apps can use this operation.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowTransitionRulesApi();
let workflowsWithTransitionRulesDetails = {"workflows":[{"workflowId":{"draft":false,"name":"Internal support workflow"},"workflowRuleIds":["b4d6cbdc-59f5-11e9-8647-d663bd873d93","d663bd873d93-59f5-11e9-8647-b4d6cbdc","11e9-59f5-b4d6cbdc-8647-d663bd873d93"]}]}; // WorkflowsWithTransitionRulesDetails | 
apiInstance.deleteWorkflowTransitionRuleConfigurations(workflowsWithTransitionRulesDetails, (error, data, response) => {
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
 **workflowsWithTransitionRulesDetails** | [**WorkflowsWithTransitionRulesDetails**](WorkflowsWithTransitionRulesDetails.md)|  | 

### Return type

[**WorkflowTransitionRulesUpdateErrors**](WorkflowTransitionRulesUpdateErrors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getWorkflowTransitionRuleConfigurations

> PageBeanWorkflowTransitionRules getWorkflowTransitionRuleConfigurations(types, opts)

Get workflow transition rule configurations

Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules:   *  of one or more transition rule types, such as [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).  *  matching one or more transition rule keys.  Only workflows containing transition rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app are returned.  Due to server-side optimizations, workflows with an empty list of rules may be returned; these workflows can be ignored.  **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowTransitionRulesApi();
let types = ["null"]; // [String] | The types of the transition rules to return.
let opts = {
  'startAt': 0, // Number | The index of the first item to return in a page of results (page offset).
  'maxResults': 10, // Number | The maximum number of items to return per page.
  'keys': ["null"], // [String] | The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return.
  'workflowNames': ["null"], // [String] | EXPERIMENTAL: The list of workflow names to filter by.
  'withTags': ["null"], // [String] | EXPERIMENTAL: The list of `tags` to filter by.
  'draft': true, // Boolean | EXPERIMENTAL: Whether draft or published workflows are returned. If not provided, both workflow types are returned.
  'expand': "expand_example" // String | Use [expand](#expansion) to include additional information in the response. This parameter accepts `transition`, which, for each rule, returns information about the transition the rule is assigned to.
};
apiInstance.getWorkflowTransitionRuleConfigurations(types, opts, (error, data, response) => {
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
 **types** | [**[String]**](String.md)| The types of the transition rules to return. | 
 **startAt** | **Number**| The index of the first item to return in a page of results (page offset). | [optional] [default to 0]
 **maxResults** | **Number**| The maximum number of items to return per page. | [optional] [default to 10]
 **keys** | [**[String]**](String.md)| The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return. | [optional] 
 **workflowNames** | [**[String]**](String.md)| EXPERIMENTAL: The list of workflow names to filter by. | [optional] 
 **withTags** | [**[String]**](String.md)| EXPERIMENTAL: The list of &#x60;tags&#x60; to filter by. | [optional] 
 **draft** | **Boolean**| EXPERIMENTAL: Whether draft or published workflows are returned. If not provided, both workflow types are returned. | [optional] 
 **expand** | **String**| Use [expand](#expansion) to include additional information in the response. This parameter accepts &#x60;transition&#x60;, which, for each rule, returns information about the transition the rule is assigned to. | [optional] 

### Return type

[**PageBeanWorkflowTransitionRules**](PageBeanWorkflowTransitionRules.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWorkflowTransitionRuleConfigurations

> WorkflowTransitionRulesUpdateErrors updateWorkflowTransitionRuleConfigurations(workflowTransitionRulesUpdate)

Update workflow transition rule configurations

Updates configuration of workflow transition rules. The following rule types are supported:   *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)  *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)  *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)  Only rules created by the calling Connect app can be updated.  To assist with app migration, this operation can be used to:   *  Disable a rule.  *  Add a &#x60;tag&#x60;. Use this to filter rules in the [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).  Rules are enabled if the &#x60;disabled&#x60; parameter is not provided.  **[Permissions](#permissions) required:** Only Connect apps can use this operation.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.WorkflowTransitionRulesApi();
let workflowTransitionRulesUpdate = {"workflows":[{"conditions":[{"configuration":{"disabled":false,"value":"{ \"size\": \"medium\" }"},"id":"d663bd873d93-59f5-11e9-8647-b4d6cbdc"}],"postFunctions":[{"configuration":{"disabled":false,"value":"{ \"color\": \"red\" }"},"id":"b4d6cbdc-59f5-11e9-8647-d663bd873d93"}],"validators":[{"configuration":{"disabled":false,"value":"{ \"shape\": \"square\" }"},"id":"11e9-59f5-b4d6cbdc-8647-d663bd873d93"}],"workflowId":{"draft":false,"name":"My Workflow name"}}]}; // WorkflowTransitionRulesUpdate | 
apiInstance.updateWorkflowTransitionRuleConfigurations(workflowTransitionRulesUpdate, (error, data, response) => {
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
 **workflowTransitionRulesUpdate** | [**WorkflowTransitionRulesUpdate**](WorkflowTransitionRulesUpdate.md)|  | 

### Return type

[**WorkflowTransitionRulesUpdateErrors**](WorkflowTransitionRulesUpdateErrors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

