

# GoogleCloudAiplatformV1ExamplesOverride

Overrides for example-based explanations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crowdingCount** | **Integer** | The number of neighbors to return that have the same crowding tag. |  [optional] |
|**dataFormat** | [**DataFormatEnum**](#DataFormatEnum) | The format of the data being provided with each call. |  [optional] |
|**neighborCount** | **Integer** | The number of neighbors to return. |  [optional] |
|**restrictions** | [**List&lt;GoogleCloudAiplatformV1ExamplesRestrictionsNamespace&gt;**](GoogleCloudAiplatformV1ExamplesRestrictionsNamespace.md) | Restrict the resulting nearest neighbors to respect these constraints. |  [optional] |
|**returnEmbeddings** | **Boolean** | If true, return the embeddings instead of neighbors. |  [optional] |



## Enum: DataFormatEnum

| Name | Value |
|---- | -----|
| DATA_FORMAT_UNSPECIFIED | &quot;DATA_FORMAT_UNSPECIFIED&quot; |
| INSTANCES | &quot;INSTANCES&quot; |
| EMBEDDINGS | &quot;EMBEDDINGS&quot; |



