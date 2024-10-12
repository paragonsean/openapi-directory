# WorkflowTransitionRulesApi

All URIs are relative to *https://your-domain.atlassian.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteWorkflowTransitionRuleConfigurations**](WorkflowTransitionRulesApi.md#deleteWorkflowTransitionRuleConfigurations) | **PUT** /rest/api/3/workflow/rule/config/delete | Delete workflow transition rule configurations |
| [**getWorkflowTransitionRuleConfigurations**](WorkflowTransitionRulesApi.md#getWorkflowTransitionRuleConfigurations) | **GET** /rest/api/3/workflow/rule/config | Get workflow transition rule configurations |
| [**updateWorkflowTransitionRuleConfigurations**](WorkflowTransitionRulesApi.md#updateWorkflowTransitionRuleConfigurations) | **PUT** /rest/api/3/workflow/rule/config | Update workflow transition rule configurations |


<a id="deleteWorkflowTransitionRuleConfigurations"></a>
# **deleteWorkflowTransitionRuleConfigurations**
> WorkflowTransitionRulesUpdateErrors deleteWorkflowTransitionRuleConfigurations(workflowsWithTransitionRulesDetails)

Delete workflow transition rule configurations

Deletes workflow transition rules from one or more workflows. These rule types are supported:   *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)  *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)  *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)  Only rules created by the calling Connect app can be deleted.  **[Permissions](#permissions) required:** Only Connect apps can use this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTransitionRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WorkflowTransitionRulesApi apiInstance = new WorkflowTransitionRulesApi(defaultClient);
    WorkflowsWithTransitionRulesDetails workflowsWithTransitionRulesDetails = new WorkflowsWithTransitionRulesDetails(); // WorkflowsWithTransitionRulesDetails | 
    try {
      WorkflowTransitionRulesUpdateErrors result = apiInstance.deleteWorkflowTransitionRuleConfigurations(workflowsWithTransitionRulesDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTransitionRulesApi#deleteWorkflowTransitionRuleConfigurations");
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
| **workflowsWithTransitionRulesDetails** | [**WorkflowsWithTransitionRulesDetails**](WorkflowsWithTransitionRulesDetails.md)|  | |

### Return type

[**WorkflowTransitionRulesUpdateErrors**](WorkflowTransitionRulesUpdateErrors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the request is successful. |  -  |
| **400** | Returned if the request is invalid. |  -  |
| **403** | Returned if the caller is not a Connect app. |  -  |

<a id="getWorkflowTransitionRuleConfigurations"></a>
# **getWorkflowTransitionRuleConfigurations**
> PageBeanWorkflowTransitionRules getWorkflowTransitionRuleConfigurations(types, startAt, maxResults, keys, workflowNames, withTags, draft, expand)

Get workflow transition rule configurations

Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules:   *  of one or more transition rule types, such as [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).  *  matching one or more transition rule keys.  Only workflows containing transition rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app are returned.  Due to server-side optimizations, workflows with an empty list of rules may be returned; these workflows can be ignored.  **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTransitionRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WorkflowTransitionRulesApi apiInstance = new WorkflowTransitionRulesApi(defaultClient);
    Set<String> types = Arrays.asList(); // Set<String> | The types of the transition rules to return.
    Long startAt = 0L; // Long | The index of the first item to return in a page of results (page offset).
    Integer maxResults = 10; // Integer | The maximum number of items to return per page.
    Set<String> keys = Arrays.asList(); // Set<String> | The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return.
    Set<String> workflowNames = Arrays.asList(); // Set<String> | EXPERIMENTAL: The list of workflow names to filter by.
    Set<String> withTags = Arrays.asList(); // Set<String> | EXPERIMENTAL: The list of `tags` to filter by.
    Boolean draft = true; // Boolean | EXPERIMENTAL: Whether draft or published workflows are returned. If not provided, both workflow types are returned.
    String expand = "expand_example"; // String | Use [expand](#expansion) to include additional information in the response. This parameter accepts `transition`, which, for each rule, returns information about the transition the rule is assigned to.
    try {
      PageBeanWorkflowTransitionRules result = apiInstance.getWorkflowTransitionRuleConfigurations(types, startAt, maxResults, keys, workflowNames, withTags, draft, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTransitionRulesApi#getWorkflowTransitionRuleConfigurations");
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
| **types** | [**Set&lt;String&gt;**](String.md)| The types of the transition rules to return. | [enum: postfunction, condition, validator] |
| **startAt** | **Long**| The index of the first item to return in a page of results (page offset). | [optional] [default to 0] |
| **maxResults** | **Integer**| The maximum number of items to return per page. | [optional] [default to 10] |
| **keys** | [**Set&lt;String&gt;**](String.md)| The transition rule class keys, as defined in the Connect or the Forge app descriptor, of the transition rules to return. | [optional] |
| **workflowNames** | [**Set&lt;String&gt;**](String.md)| EXPERIMENTAL: The list of workflow names to filter by. | [optional] |
| **withTags** | [**Set&lt;String&gt;**](String.md)| EXPERIMENTAL: The list of &#x60;tags&#x60; to filter by. | [optional] |
| **draft** | **Boolean**| EXPERIMENTAL: Whether draft or published workflows are returned. If not provided, both workflow types are returned. | [optional] |
| **expand** | **String**| Use [expand](#expansion) to include additional information in the response. This parameter accepts &#x60;transition&#x60;, which, for each rule, returns information about the transition the rule is assigned to. | [optional] |

### Return type

[**PageBeanWorkflowTransitionRules**](PageBeanWorkflowTransitionRules.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the request is successful. |  -  |
| **400** | Returned if the request is invalid. |  -  |
| **403** | Returned if the caller is not a Connect or a Forge app. |  -  |
| **404** | Returned if any transition rule type is not supported. |  -  |

<a id="updateWorkflowTransitionRuleConfigurations"></a>
# **updateWorkflowTransitionRuleConfigurations**
> WorkflowTransitionRulesUpdateErrors updateWorkflowTransitionRuleConfigurations(workflowTransitionRulesUpdate)

Update workflow transition rule configurations

Updates configuration of workflow transition rules. The following rule types are supported:   *  [post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/)  *  [conditions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-condition/)  *  [validators](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-validator/)  Only rules created by the calling Connect app can be updated.  To assist with app migration, this operation can be used to:   *  Disable a rule.  *  Add a &#x60;tag&#x60;. Use this to filter rules in the [Get workflow transition rule configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-rules/#api-rest-api-3-workflow-rule-config-get).  Rules are enabled if the &#x60;disabled&#x60; parameter is not provided.  **[Permissions](#permissions) required:** Only Connect apps can use this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowTransitionRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    WorkflowTransitionRulesApi apiInstance = new WorkflowTransitionRulesApi(defaultClient);
    WorkflowTransitionRulesUpdate workflowTransitionRulesUpdate = new WorkflowTransitionRulesUpdate(); // WorkflowTransitionRulesUpdate | 
    try {
      WorkflowTransitionRulesUpdateErrors result = apiInstance.updateWorkflowTransitionRuleConfigurations(workflowTransitionRulesUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowTransitionRulesApi#updateWorkflowTransitionRuleConfigurations");
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
| **workflowTransitionRulesUpdate** | [**WorkflowTransitionRulesUpdate**](WorkflowTransitionRulesUpdate.md)|  | |

### Return type

[**WorkflowTransitionRulesUpdateErrors**](WorkflowTransitionRulesUpdateErrors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the request is successful. |  -  |
| **400** | Returned if the request is invalid. |  -  |
| **403** | Returned if the caller is not a Connect app. |  -  |

