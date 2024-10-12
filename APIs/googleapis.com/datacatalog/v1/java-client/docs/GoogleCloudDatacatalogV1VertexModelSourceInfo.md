

# GoogleCloudDatacatalogV1VertexModelSourceInfo

Detail description of the source information of a Vertex model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copy** | **Boolean** | If this Model is copy of another Model. If true then source_type pertains to the original. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Type of the model source. |  [optional] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| MODEL_SOURCE_TYPE_UNSPECIFIED | &quot;MODEL_SOURCE_TYPE_UNSPECIFIED&quot; |
| AUTOML | &quot;AUTOML&quot; |
| CUSTOM | &quot;CUSTOM&quot; |
| BQML | &quot;BQML&quot; |
| MODEL_GARDEN | &quot;MODEL_GARDEN&quot; |



