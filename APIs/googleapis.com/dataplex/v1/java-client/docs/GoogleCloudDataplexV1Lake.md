

# GoogleCloudDataplexV1Lake

A lake is a centralized repository for managing enterprise data across the organization distributed across many cloud projects, and stored in a variety of storage services such as Google Cloud Storage and BigQuery. The resources attached to a lake are referred to as managed resources. Data within these managed resources can be structured or unstructured. A lake provides data admins with tools to organize, secure and manage their data at scale, and provides data scientists and data engineers an integrated experience to easily search, discover, analyze and transform data and associated metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetStatus** | [**GoogleCloudDataplexV1AssetStatus**](GoogleCloudDataplexV1AssetStatus.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time when the lake was created. |  [optional] [readonly] |
|**description** | **String** | Optional. Description of the lake. |  [optional] |
|**displayName** | **String** | Optional. User friendly display name. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. User-defined labels for the lake. |  [optional] |
|**metastore** | [**GoogleCloudDataplexV1LakeMetastore**](GoogleCloudDataplexV1LakeMetastore.md) |  |  [optional] |
|**metastoreStatus** | [**GoogleCloudDataplexV1LakeMetastoreStatus**](GoogleCloudDataplexV1LakeMetastoreStatus.md) |  |  [optional] |
|**name** | **String** | Output only. The relative resource name of the lake, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}. |  [optional] [readonly] |
|**serviceAccount** | **String** | Output only. Service account associated with this lake. This service account must be authorized to access or operate on resources managed by the lake. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the lake. |  [optional] [readonly] |
|**uid** | **String** | Output only. System generated globally unique ID for the lake. This ID will be different if the lake is deleted and re-created with the same name. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the lake was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ACTION_REQUIRED | &quot;ACTION_REQUIRED&quot; |



