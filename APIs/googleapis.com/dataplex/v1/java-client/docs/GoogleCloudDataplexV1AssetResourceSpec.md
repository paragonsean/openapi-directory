

# GoogleCloudDataplexV1AssetResourceSpec

Identifies the cloud resource that is referenced by this asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Immutable. Relative name of the cloud resource that contains the data that is being managed within a lake. For example: projects/{project_number}/buckets/{bucket_id} projects/{project_number}/datasets/{dataset_id} |  [optional] |
|**readAccessMode** | [**ReadAccessModeEnum**](#ReadAccessModeEnum) | Optional. Determines how read permissions are handled for each asset and their associated tables. Only available to storage buckets assets. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Immutable. Type of resource. |  [optional] |



## Enum: ReadAccessModeEnum

| Name | Value |
|---- | -----|
| ACCESS_MODE_UNSPECIFIED | &quot;ACCESS_MODE_UNSPECIFIED&quot; |
| DIRECT | &quot;DIRECT&quot; |
| MANAGED | &quot;MANAGED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| STORAGE_BUCKET | &quot;STORAGE_BUCKET&quot; |
| BIGQUERY_DATASET | &quot;BIGQUERY_DATASET&quot; |



