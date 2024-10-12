

# GoogleCloudDocumentaiV1beta3Dataset

A singleton resource under a Processor which configures a collection of documents.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentWarehouseConfig** | [**GoogleCloudDocumentaiV1beta3DatasetDocumentWarehouseConfig**](GoogleCloudDocumentaiV1beta3DatasetDocumentWarehouseConfig.md) |  |  [optional] |
|**gcsManagedConfig** | [**GoogleCloudDocumentaiV1beta3DatasetGCSManagedConfig**](GoogleCloudDocumentaiV1beta3DatasetGCSManagedConfig.md) |  |  [optional] |
|**name** | **String** | Dataset resource name. Format: &#x60;projects/{project}/locations/{location}/processors/{processor}/dataset&#x60; |  [optional] |
|**spannerIndexingConfig** | **Object** | Configuration specific to spanner-based indexing. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Required. State of the dataset. Ignored when updating dataset. |  [optional] |
|**unmanagedDatasetConfig** | **Object** | Configuration specific to an unmanaged dataset. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| UNINITIALIZED | &quot;UNINITIALIZED&quot; |
| INITIALIZING | &quot;INITIALIZING&quot; |
| INITIALIZED | &quot;INITIALIZED&quot; |



