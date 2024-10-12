# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1BulkDeleteConversationsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | Filter used to select the subset of conversations to delete. | [optional] 
**force** | **Boolean** | If set to true, all of this conversation&#39;s analyses will also be deleted. Otherwise, the request will only succeed if the conversation has no analyses. | [optional] 
**maxDeleteCount** | **Number** | Maximum number of conversations to delete. | [optional] 
**parent** | **String** | Required. The parent resource to delete conversations from. Format: projects/{project}/locations/{location} | [optional] 


