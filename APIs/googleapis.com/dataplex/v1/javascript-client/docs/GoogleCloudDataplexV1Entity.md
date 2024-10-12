# CloudDataplexApi.GoogleCloudDataplexV1Entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**GoogleCloudDataplexV1StorageAccess**](GoogleCloudDataplexV1StorageAccess.md) |  | [optional] 
**asset** | **String** | Required. Immutable. The ID of the asset associated with the storage location containing the entity data. The entity must be with in the same zone with the asset. | [optional] 
**catalogEntry** | **String** | Output only. The name of the associated Data Catalog entry. | [optional] [readonly] 
**compatibility** | [**GoogleCloudDataplexV1EntityCompatibilityStatus**](GoogleCloudDataplexV1EntityCompatibilityStatus.md) |  | [optional] 
**createTime** | **String** | Output only. The time when the entity was created. | [optional] [readonly] 
**dataPath** | **String** | Required. Immutable. The storage path of the entity data. For Cloud Storage data, this is the fully-qualified path to the entity, such as gs://bucket/path/to/data. For BigQuery data, this is the name of the table resource, such as projects/project_id/datasets/dataset_id/tables/table_id. | [optional] 
**dataPathPattern** | **String** | Optional. The set of items within the data path constituting the data in the entity, represented as a glob path. Example: gs://bucket/path/to/data/_**_/_*.csv. | [optional] 
**description** | **String** | Optional. User friendly longer description text. Must be shorter than or equal to 1024 characters. | [optional] 
**displayName** | **String** | Optional. Display name must be shorter than or equal to 256 characters. | [optional] 
**etag** | **String** | Optional. The etag associated with the entity, which can be retrieved with a GetEntity request. Required for update and delete requests. | [optional] 
**format** | [**GoogleCloudDataplexV1StorageFormat**](GoogleCloudDataplexV1StorageFormat.md) |  | [optional] 
**id** | **String** | Required. A user-provided entity ID. It is mutable, and will be used as the published table name. Specifying a new ID in an update entity request will override the existing value. The ID must contain only letters (a-z, A-Z), numbers (0-9), and underscores, and consist of 256 or fewer characters. | [optional] 
**name** | **String** | Output only. The resource name of the entity, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{id}. | [optional] [readonly] 
**schema** | [**GoogleCloudDataplexV1Schema**](GoogleCloudDataplexV1Schema.md) |  | [optional] 
**system** | **String** | Required. Immutable. Identifies the storage system of the entity data. | [optional] 
**type** | **String** | Required. Immutable. The type of entity. | [optional] 
**uid** | **String** | Output only. System generated unique ID for the Entity. This ID will be different if the Entity is deleted and re-created with the same name. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time when the entity was last updated. | [optional] [readonly] 



## Enum: SystemEnum


* `STORAGE_SYSTEM_UNSPECIFIED` (value: `"STORAGE_SYSTEM_UNSPECIFIED"`)

* `CLOUD_STORAGE` (value: `"CLOUD_STORAGE"`)

* `BIGQUERY` (value: `"BIGQUERY"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `TABLE` (value: `"TABLE"`)

* `FILESET` (value: `"FILESET"`)




