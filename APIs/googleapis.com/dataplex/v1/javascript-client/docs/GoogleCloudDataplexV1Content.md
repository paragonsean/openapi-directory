# CloudDataplexApi.GoogleCloudDataplexV1Content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Content creation time. | [optional] [readonly] 
**dataText** | **String** | Required. Content data in string format. | [optional] 
**description** | **String** | Optional. Description of the content. | [optional] 
**labels** | **{String: String}** | Optional. User defined labels for the content. | [optional] 
**name** | **String** | Output only. The relative resource name of the content, of the form: projects/{project_id}/locations/{location_id}/lakes/{lake_id}/content/{content_id} | [optional] [readonly] 
**notebook** | [**GoogleCloudDataplexV1ContentNotebook**](GoogleCloudDataplexV1ContentNotebook.md) |  | [optional] 
**path** | **String** | Required. The path for the Content file, represented as directory structure. Unique within a lake. Limited to alphanumerics, hyphens, underscores, dots and slashes. | [optional] 
**sqlScript** | [**GoogleCloudDataplexV1ContentSqlScript**](GoogleCloudDataplexV1ContentSqlScript.md) |  | [optional] 
**uid** | **String** | Output only. System generated globally unique ID for the content. This ID will be different if the content is deleted and re-created with the same name. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the content was last updated. | [optional] [readonly] 


