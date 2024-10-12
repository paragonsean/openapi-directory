# CloudDataplexApi.GoogleCloudDataplexV1Lake

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetStatus** | [**GoogleCloudDataplexV1AssetStatus**](GoogleCloudDataplexV1AssetStatus.md) |  | [optional] 
**createTime** | **String** | Output only. The time when the lake was created. | [optional] [readonly] 
**description** | **String** | Optional. Description of the lake. | [optional] 
**displayName** | **String** | Optional. User friendly display name. | [optional] 
**labels** | **{String: String}** | Optional. User-defined labels for the lake. | [optional] 
**metastore** | [**GoogleCloudDataplexV1LakeMetastore**](GoogleCloudDataplexV1LakeMetastore.md) |  | [optional] 
**metastoreStatus** | [**GoogleCloudDataplexV1LakeMetastoreStatus**](GoogleCloudDataplexV1LakeMetastoreStatus.md) |  | [optional] 
**name** | **String** | Output only. The relative resource name of the lake, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}. | [optional] [readonly] 
**serviceAccount** | **String** | Output only. Service account associated with this lake. This service account must be authorized to access or operate on resources managed by the lake. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the lake. | [optional] [readonly] 
**uid** | **String** | Output only. System generated globally unique ID for the lake. This ID will be different if the lake is deleted and re-created with the same name. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the lake was last updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `ACTION_REQUIRED` (value: `"ACTION_REQUIRED"`)




