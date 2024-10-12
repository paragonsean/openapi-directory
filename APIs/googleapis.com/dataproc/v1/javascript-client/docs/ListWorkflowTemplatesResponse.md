# CloudDataprocApi.ListWorkflowTemplatesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | Output only. This token is included in the response if there are more results to fetch. To fetch additional results, provide this value as the page_token in a subsequent ListWorkflowTemplatesRequest. | [optional] [readonly] 
**templates** | [**[WorkflowTemplate]**](WorkflowTemplate.md) | Output only. WorkflowTemplates list. | [optional] [readonly] 
**unreachable** | **[String]** | Output only. List of workflow templates that could not be included in the response. Attempting to get one of these resources may indicate why it was not included in the list response. | [optional] [readonly] 


