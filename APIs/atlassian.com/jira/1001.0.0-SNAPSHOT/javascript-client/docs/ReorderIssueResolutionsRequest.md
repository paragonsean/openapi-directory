# TheJiraCloudPlatformRestApi.ReorderIssueResolutionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **String** | The ID of the resolution. Required if &#x60;position&#x60; isn&#39;t provided. | [optional] 
**ids** | **[String]** | The list of resolution IDs to be reordered. Cannot contain duplicates nor after ID. | 
**position** | **String** | The position for issue resolutions to be moved to. Required if &#x60;after&#x60; isn&#39;t provided. | [optional] 


