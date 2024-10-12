

# GoogleCloudDatacatalogV1VertexDatasetSpec

Specification for vertex dataset resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataItemCount** | **String** | The number of DataItems in this Dataset. Only apply for non-structured Dataset. |  [optional] |
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | Type of the dataset. |  [optional] |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| DATA_TYPE_UNSPECIFIED | &quot;DATA_TYPE_UNSPECIFIED&quot; |
| TABLE | &quot;TABLE&quot; |
| IMAGE | &quot;IMAGE&quot; |
| TEXT | &quot;TEXT&quot; |
| VIDEO | &quot;VIDEO&quot; |
| CONVERSATION | &quot;CONVERSATION&quot; |
| TIME_SERIES | &quot;TIME_SERIES&quot; |
| DOCUMENT | &quot;DOCUMENT&quot; |
| TEXT_TO_SPEECH | &quot;TEXT_TO_SPEECH&quot; |
| TRANSLATION | &quot;TRANSLATION&quot; |
| STORE_VISION | &quot;STORE_VISION&quot; |
| ENTERPRISE_KNOWLEDGE_GRAPH | &quot;ENTERPRISE_KNOWLEDGE_GRAPH&quot; |
| TEXT_PROMPT | &quot;TEXT_PROMPT&quot; |



