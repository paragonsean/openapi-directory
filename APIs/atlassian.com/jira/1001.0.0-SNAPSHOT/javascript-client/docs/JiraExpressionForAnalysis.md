# TheJiraCloudPlatformRestApi.JiraExpressionForAnalysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contextVariables** | **{String: String}** | Context variables and their types. The type checker assumes that [common context variables](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/#context-variables), such as &#x60;issue&#x60; or &#x60;project&#x60;, are available in context and sets their type. Use this property to override the default types or provide details of new variables. | [optional] 
**expressions** | **[String]** | The list of Jira expressions to analyse. | 


