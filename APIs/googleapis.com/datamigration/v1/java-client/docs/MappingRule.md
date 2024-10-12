

# MappingRule

Definition of a transformation that is to be applied to a group of entities in the source schema. Several such transformations can be applied to an entity sequentially to define the corresponding entity in the target schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conditionalColumnSetValue** | [**ConditionalColumnSetValue**](ConditionalColumnSetValue.md) |  |  [optional] |
|**convertRowidColumn** | [**ConvertRowIdToColumn**](ConvertRowIdToColumn.md) |  |  [optional] |
|**displayName** | **String** | Optional. A human readable name |  [optional] |
|**entityMove** | [**EntityMove**](EntityMove.md) |  |  [optional] |
|**filter** | [**MappingRuleFilter**](MappingRuleFilter.md) |  |  [optional] |
|**filterTableColumns** | [**FilterTableColumns**](FilterTableColumns.md) |  |  [optional] |
|**multiColumnDataTypeChange** | [**MultiColumnDatatypeChange**](MultiColumnDatatypeChange.md) |  |  [optional] |
|**multiEntityRename** | [**MultiEntityRename**](MultiEntityRename.md) |  |  [optional] |
|**name** | **String** | Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}. |  [optional] |
|**revisionCreateTime** | **String** | Output only. The timestamp that the revision was created. |  [optional] [readonly] |
|**revisionId** | **String** | Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string. |  [optional] [readonly] |
|**ruleOrder** | **String** | Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden. |  [optional] |
|**ruleScope** | [**RuleScopeEnum**](#RuleScopeEnum) | Required. The rule scope |  [optional] |
|**setTablePrimaryKey** | [**SetTablePrimaryKey**](SetTablePrimaryKey.md) |  |  [optional] |
|**singleColumnChange** | [**SingleColumnChange**](SingleColumnChange.md) |  |  [optional] |
|**singleEntityRename** | [**SingleEntityRename**](SingleEntityRename.md) |  |  [optional] |
|**singlePackageChange** | [**SinglePackageChange**](SinglePackageChange.md) |  |  [optional] |
|**sourceSqlChange** | [**SourceSqlChange**](SourceSqlChange.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Optional. The mapping rule state |  [optional] |



## Enum: RuleScopeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DATABASE_ENTITY_TYPE_UNSPECIFIED&quot; |
| SCHEMA | &quot;DATABASE_ENTITY_TYPE_SCHEMA&quot; |
| TABLE | &quot;DATABASE_ENTITY_TYPE_TABLE&quot; |
| COLUMN | &quot;DATABASE_ENTITY_TYPE_COLUMN&quot; |
| CONSTRAINT | &quot;DATABASE_ENTITY_TYPE_CONSTRAINT&quot; |
| INDEX | &quot;DATABASE_ENTITY_TYPE_INDEX&quot; |
| TRIGGER | &quot;DATABASE_ENTITY_TYPE_TRIGGER&quot; |
| VIEW | &quot;DATABASE_ENTITY_TYPE_VIEW&quot; |
| SEQUENCE | &quot;DATABASE_ENTITY_TYPE_SEQUENCE&quot; |
| STORED_PROCEDURE | &quot;DATABASE_ENTITY_TYPE_STORED_PROCEDURE&quot; |
| FUNCTION | &quot;DATABASE_ENTITY_TYPE_FUNCTION&quot; |
| SYNONYM | &quot;DATABASE_ENTITY_TYPE_SYNONYM&quot; |
| DATABASE_PACKAGE | &quot;DATABASE_ENTITY_TYPE_DATABASE_PACKAGE&quot; |
| UDT | &quot;DATABASE_ENTITY_TYPE_UDT&quot; |
| MATERIALIZED_VIEW | &quot;DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW&quot; |
| DATABASE | &quot;DATABASE_ENTITY_TYPE_DATABASE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| DELETED | &quot;DELETED&quot; |



