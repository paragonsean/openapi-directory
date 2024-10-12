# CloudDataplexApi.GoogleCloudDataplexV1AssetResourceSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Immutable. Relative name of the cloud resource that contains the data that is being managed within a lake. For example: projects/{project_number}/buckets/{bucket_id} projects/{project_number}/datasets/{dataset_id} | [optional] 
**readAccessMode** | **String** | Optional. Determines how read permissions are handled for each asset and their associated tables. Only available to storage buckets assets. | [optional] 
**type** | **String** | Required. Immutable. Type of resource. | [optional] 



## Enum: ReadAccessModeEnum


* `ACCESS_MODE_UNSPECIFIED` (value: `"ACCESS_MODE_UNSPECIFIED"`)

* `DIRECT` (value: `"DIRECT"`)

* `MANAGED` (value: `"MANAGED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `STORAGE_BUCKET` (value: `"STORAGE_BUCKET"`)

* `BIGQUERY_DATASET` (value: `"BIGQUERY_DATASET"`)




