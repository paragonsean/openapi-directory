

# ConversionWorkspace

The main conversion workspace resource entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The timestamp when the workspace resource was created. |  [optional] [readonly] |
|**destination** | [**DatabaseEngineInfo**](DatabaseEngineInfo.md) |  |  [optional] |
|**displayName** | **String** | Optional. The display name for the workspace. |  [optional] |
|**globalSettings** | **Map&lt;String, String&gt;** | Optional. A generic list of settings for the workspace. The settings are database pair dependant and can indicate default behavior for the mapping rules engine or turn on or off specific features. Such examples can be: convert_foreign_key_to_interleave&#x3D;true, skip_triggers&#x3D;false, ignore_non_table_synonyms&#x3D;true |  [optional] |
|**hasUncommittedChanges** | **Boolean** | Output only. Whether the workspace has uncommitted changes (changes which were made after the workspace was committed). |  [optional] [readonly] |
|**latestCommitId** | **String** | Output only. The latest commit ID. |  [optional] [readonly] |
|**latestCommitTime** | **String** | Output only. The timestamp when the workspace was committed. |  [optional] [readonly] |
|**name** | **String** | Full name of the workspace resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. |  [optional] |
|**source** | [**DatabaseEngineInfo**](DatabaseEngineInfo.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The timestamp when the workspace resource was last updated. |  [optional] [readonly] |



