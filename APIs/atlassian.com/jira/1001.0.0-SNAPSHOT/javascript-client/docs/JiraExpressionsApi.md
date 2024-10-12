# TheJiraCloudPlatformRestApi.JiraExpressionsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyseExpression**](JiraExpressionsApi.md#analyseExpression) | **POST** /rest/api/3/expression/analyse | Analyse Jira expression
[**evaluateJiraExpression**](JiraExpressionsApi.md#evaluateJiraExpression) | **POST** /rest/api/3/expression/eval | Evaluate Jira expression



## analyseExpression

> JiraExpressionsAnalysis analyseExpression(jiraExpressionForAnalysis, opts)

Analyse Jira expression

Analyses and validates Jira expressions.  As an experimental feature, this operation can also attempt to type-check the expressions.  Learn more about Jira expressions in the [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).  **[Permissions](#permissions) required**: None.

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

let apiInstance = new TheJiraCloudPlatformRestApi.JiraExpressionsApi();
let jiraExpressionForAnalysis = {"contextVariables":{"listOfStrings":"List<String>","record":"{ a: Number, b: String }","value":"User"},"expressions":["issues.map(issue => issue.properties['property_key'])"]}; // JiraExpressionForAnalysis | The Jira expressions to analyse.
let opts = {
  'check': "'syntax'" // String | The check to perform:   *  `syntax` Each expression's syntax is checked to ensure the expression can be parsed. Also, syntactic limits are validated. For example, the expression's length.  *  `type` EXPERIMENTAL. Each expression is type checked and the final type of the expression inferred. Any type errors that would result in the expression failure at runtime are reported. For example, accessing properties that don't exist or passing the wrong number of arguments to functions. Also performs the syntax check.  *  `complexity` EXPERIMENTAL. Determines the formulae for how many [expensive operations](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#expensive-operations) each expression may execute.
};
apiInstance.analyseExpression(jiraExpressionForAnalysis, opts, (error, data, response) => {
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
 **jiraExpressionForAnalysis** | [**JiraExpressionForAnalysis**](JiraExpressionForAnalysis.md)| The Jira expressions to analyse. | 
 **check** | **String**| The check to perform:   *  &#x60;syntax&#x60; Each expression&#39;s syntax is checked to ensure the expression can be parsed. Also, syntactic limits are validated. For example, the expression&#39;s length.  *  &#x60;type&#x60; EXPERIMENTAL. Each expression is type checked and the final type of the expression inferred. Any type errors that would result in the expression failure at runtime are reported. For example, accessing properties that don&#39;t exist or passing the wrong number of arguments to functions. Also performs the syntax check.  *  &#x60;complexity&#x60; EXPERIMENTAL. Determines the formulae for how many [expensive operations](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#expensive-operations) each expression may execute. | [optional] [default to &#39;syntax&#39;]

### Return type

[**JiraExpressionsAnalysis**](JiraExpressionsAnalysis.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## evaluateJiraExpression

> JiraExpressionResult evaluateJiraExpression(jiraExpressionEvalRequestBean, opts)

Evaluate Jira expression

Evaluates a Jira expression and returns its value.  This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data in a flexible way. Consult the [Jira expressions documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more details.  #### Context variables ####  The following context variables are available to Jira expressions evaluated by this resource. Their presence depends on various factors; usually you need to manually request them in the context object sent in the payload, but some of them are added automatically under certain conditions.   *  &#x60;user&#x60; ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user)): The current user. Always available and equal to &#x60;null&#x60; if the request is anonymous.  *  &#x60;app&#x60; ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#app)): The [Connect app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request. Available only for authenticated requests made by Connect Apps (read more here: [Authentication for Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).  *  &#x60;issue&#x60; ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): The current issue. Available only when the issue is provided in the request context object.  *  &#x60;issues&#x60; ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is provided in the request context object.  *  &#x60;project&#x60; ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#project)): The current project. Available only when the project is provided in the request context object.  *  &#x60;sprint&#x60; ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#sprint)): The current sprint. Available only when the sprint is provided in the request context object.  *  &#x60;board&#x60; ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#board)): The current board. Available only when the board is provided in the request context object.  *  &#x60;serviceDesk&#x60; ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#servicedesk)): The current service desk. Available only when the service desk is provided in the request context object.  *  &#x60;customerRequest&#x60; ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#customerrequest)): The current customer request. Available only when the customer request is provided in the request context object.  Also, custom context variables can be passed in the request with their types. Those variables can be accessed by key in the Jira expression. These variable types are available for use in a custom context:   *  &#x60;user&#x60;: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user) specified as an Atlassian account ID.  *  &#x60;issue&#x60;: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira expression.  *  &#x60;json&#x60;: A JSON object containing custom content.  *  &#x60;list&#x60;: A JSON list of &#x60;user&#x60;, &#x60;issue&#x60;, or &#x60;json&#x60; variable types.  This operation can be accessed anonymously.  **[Permissions](#permissions) required**: None. However, an expression may return different results for different users depending on their permissions. For example, different users may see different comments on the same issue.   Permission to access Jira Software is required to access Jira Software context variables (&#x60;board&#x60; and &#x60;sprint&#x60;) or fields (for example, &#x60;issue.sprint&#x60;).

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

let apiInstance = new TheJiraCloudPlatformRestApi.JiraExpressionsApi();
let jiraExpressionEvalRequestBean = {"context":{"board":10100,"custom":{"config":{"type":"json","value":{"userId":"10002"}},"issuesList":[{"key":"ACJIRA-1471","type":"issue"},{"id":100001,"type":"issue"}],"myUser":{"accountId":"100001","type":"user"},"nullField":{"type":"json"}},"customerRequest":1450,"issue":{"key":"ACJIRA-1470"},"issues":{"jql":{"maxResults":100,"query":"project = HSP","startAt":0,"validation":"strict"}},"project":{"key":"ACJIRA"},"serviceDesk":10023,"sprint":10001},"expression":"{ key: issue.key, type: issue.issueType.name, links: issue.links.map(link => link.linkedIssue.id), listCustomVariable: issuesList.includes(issue), customVariables: myUser.accountId == config.userId}"}; // JiraExpressionEvalRequestBean | The Jira expression and the evaluation context.
let opts = {
  'expand': "expand_example" // String | Use [expand](#expansion) to include additional information in the response. This parameter accepts `meta.complexity` that returns information about the expression complexity. For example, the number of expensive operations used by the expression and how close the expression is to reaching the [complexity limit](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions). Useful when designing and debugging your expressions.
};
apiInstance.evaluateJiraExpression(jiraExpressionEvalRequestBean, opts, (error, data, response) => {
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
 **jiraExpressionEvalRequestBean** | [**JiraExpressionEvalRequestBean**](JiraExpressionEvalRequestBean.md)| The Jira expression and the evaluation context. | 
 **expand** | **String**| Use [expand](#expansion) to include additional information in the response. This parameter accepts &#x60;meta.complexity&#x60; that returns information about the expression complexity. For example, the number of expensive operations used by the expression and how close the expression is to reaching the [complexity limit](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#restrictions). Useful when designing and debugging your expressions. | [optional] 

### Return type

[**JiraExpressionResult**](JiraExpressionResult.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

