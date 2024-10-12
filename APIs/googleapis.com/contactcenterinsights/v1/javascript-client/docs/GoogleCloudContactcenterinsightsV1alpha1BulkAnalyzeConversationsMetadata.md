# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completedAnalysesCount** | **Number** | The number of requested analyses that have completed successfully so far. | [optional] 
**createTime** | **String** | The time the operation was created. | [optional] 
**endTime** | **String** | The time the operation finished running. | [optional] 
**failedAnalysesCount** | **Number** | The number of requested analyses that have failed so far. | [optional] 
**partialErrors** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | Output only. Partial errors during bulk analyze operation that might cause the operation output to be incomplete. | [optional] [readonly] 
**request** | [**GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsRequest**](GoogleCloudContactcenterinsightsV1alpha1BulkAnalyzeConversationsRequest.md) |  | [optional] 
**totalRequestedAnalysesCount** | **Number** | Total number of analyses requested. Computed by the number of conversations returned by &#x60;filter&#x60; multiplied by &#x60;analysis_percentage&#x60; in the request. | [optional] 


