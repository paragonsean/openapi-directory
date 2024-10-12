# CloudAssetApi.SavedQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**QueryContent**](QueryContent.md) |  | [optional] 
**createTime** | **String** | Output only. The create time of this saved query. | [optional] [readonly] 
**creator** | **String** | Output only. The account&#39;s email address who has created this saved query. | [optional] [readonly] 
**description** | **String** | The description of this saved query. This value should be fewer than 255 characters. | [optional] 
**labels** | **{String: String}** | Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters. | [optional] 
**lastUpdateTime** | **String** | Output only. The last update time of this saved query. | [optional] [readonly] 
**lastUpdater** | **String** | Output only. The account&#39;s email address who has updated this saved query most recently. | [optional] [readonly] 
**name** | **String** | The resource name of the saved query. The format must be: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id | [optional] 


