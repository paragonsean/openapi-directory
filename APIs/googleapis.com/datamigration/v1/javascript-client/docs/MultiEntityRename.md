# DatabaseMigrationApi.MultiEntityRename

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**newNamePattern** | **String** | Optional. The pattern used to generate the new entity&#39;s name. This pattern must include the characters &#39;{name}&#39;, which will be replaced with the name of the original entity. For example, the pattern &#39;t_{name}&#39; for an entity name jobs would be converted to &#39;t_jobs&#39;. If unspecified, the default value for this field is &#39;{name}&#39; | [optional] 
**sourceNameTransformation** | **String** | Optional. Additional transformation that can be done on the source entity name before it is being used by the new_name_pattern, for example lower case. If no transformation is desired, use NO_TRANSFORMATION | [optional] 



## Enum: SourceNameTransformationEnum


* `UNSPECIFIED` (value: `"ENTITY_NAME_TRANSFORMATION_UNSPECIFIED"`)

* `NO_TRANSFORMATION` (value: `"ENTITY_NAME_TRANSFORMATION_NO_TRANSFORMATION"`)

* `LOWER_CASE` (value: `"ENTITY_NAME_TRANSFORMATION_LOWER_CASE"`)

* `UPPER_CASE` (value: `"ENTITY_NAME_TRANSFORMATION_UPPER_CASE"`)

* `CAPITALIZED_CASE` (value: `"ENTITY_NAME_TRANSFORMATION_CAPITALIZED_CASE"`)




