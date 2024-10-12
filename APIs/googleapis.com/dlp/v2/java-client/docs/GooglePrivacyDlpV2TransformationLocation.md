

# GooglePrivacyDlpV2TransformationLocation

Specifies the location of a transformation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerType** | [**ContainerTypeEnum**](#ContainerTypeEnum) | Information about the functionality of the container where this finding occurred, if available. |  [optional] |
|**findingId** | **String** | For infotype transformations, link to the corresponding findings ID so that location information does not need to be duplicated. Each findings ID correlates to an entry in the findings output table, this table only gets created when users specify to save findings (add the save findings action to the request). |  [optional] |
|**recordTransformation** | [**GooglePrivacyDlpV2RecordTransformation**](GooglePrivacyDlpV2RecordTransformation.md) |  |  [optional] |



## Enum: ContainerTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_CONTAINER | &quot;TRANSFORM_UNKNOWN_CONTAINER&quot; |
| BODY | &quot;TRANSFORM_BODY&quot; |
| METADATA | &quot;TRANSFORM_METADATA&quot; |
| TABLE | &quot;TRANSFORM_TABLE&quot; |



