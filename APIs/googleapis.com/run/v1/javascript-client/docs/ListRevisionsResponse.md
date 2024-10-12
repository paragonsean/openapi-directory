# CloudRunAdminApi.ListRevisionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersion** | **String** | The API version for this call such as \&quot;serving.knative.dev/v1\&quot;. | [optional] 
**items** | [**[Revision]**](Revision.md) | List of Revisions. | [optional] 
**kind** | **String** | The kind of this resource, in this case \&quot;RevisionList\&quot;. | [optional] 
**metadata** | [**ListMeta**](ListMeta.md) |  | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 


