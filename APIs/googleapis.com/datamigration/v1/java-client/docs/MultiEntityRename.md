

# MultiEntityRename

Options to configure rule type MultiEntityRename. The rule is used to rename multiple entities. The rule filter field can refer to one or more entities. The rule scope can be one of: Database, Schema, Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**newNamePattern** | **String** | Optional. The pattern used to generate the new entity&#39;s name. This pattern must include the characters &#39;{name}&#39;, which will be replaced with the name of the original entity. For example, the pattern &#39;t_{name}&#39; for an entity name jobs would be converted to &#39;t_jobs&#39;. If unspecified, the default value for this field is &#39;{name}&#39; |  [optional] |
|**sourceNameTransformation** | [**SourceNameTransformationEnum**](#SourceNameTransformationEnum) | Optional. Additional transformation that can be done on the source entity name before it is being used by the new_name_pattern, for example lower case. If no transformation is desired, use NO_TRANSFORMATION |  [optional] |



## Enum: SourceNameTransformationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ENTITY_NAME_TRANSFORMATION_UNSPECIFIED&quot; |
| NO_TRANSFORMATION | &quot;ENTITY_NAME_TRANSFORMATION_NO_TRANSFORMATION&quot; |
| LOWER_CASE | &quot;ENTITY_NAME_TRANSFORMATION_LOWER_CASE&quot; |
| UPPER_CASE | &quot;ENTITY_NAME_TRANSFORMATION_UPPER_CASE&quot; |
| CAPITALIZED_CASE | &quot;ENTITY_NAME_TRANSFORMATION_CAPITALIZED_CASE&quot; |



