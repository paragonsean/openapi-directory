# DatabaseMigrationApi.MappingRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditionalColumnSetValue** | [**ConditionalColumnSetValue**](ConditionalColumnSetValue.md) |  | [optional] 
**convertRowidColumn** | [**ConvertRowIdToColumn**](ConvertRowIdToColumn.md) |  | [optional] 
**displayName** | **String** | Optional. A human readable name | [optional] 
**entityMove** | [**EntityMove**](EntityMove.md) |  | [optional] 
**filter** | [**MappingRuleFilter**](MappingRuleFilter.md) |  | [optional] 
**filterTableColumns** | [**FilterTableColumns**](FilterTableColumns.md) |  | [optional] 
**multiColumnDataTypeChange** | [**MultiColumnDatatypeChange**](MultiColumnDatatypeChange.md) |  | [optional] 
**multiEntityRename** | [**MultiEntityRename**](MultiEntityRename.md) |  | [optional] 
**name** | **String** | Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}. | [optional] 
**revisionCreateTime** | **String** | Output only. The timestamp that the revision was created. | [optional] [readonly] 
**revisionId** | **String** | Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string. | [optional] [readonly] 
**ruleOrder** | **String** | Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden. | [optional] 
**ruleScope** | **String** | Required. The rule scope | [optional] 
**setTablePrimaryKey** | [**SetTablePrimaryKey**](SetTablePrimaryKey.md) |  | [optional] 
**singleColumnChange** | [**SingleColumnChange**](SingleColumnChange.md) |  | [optional] 
**singleEntityRename** | [**SingleEntityRename**](SingleEntityRename.md) |  | [optional] 
**singlePackageChange** | [**SinglePackageChange**](SinglePackageChange.md) |  | [optional] 
**sourceSqlChange** | [**SourceSqlChange**](SourceSqlChange.md) |  | [optional] 
**state** | **String** | Optional. The mapping rule state | [optional] 



## Enum: RuleScopeEnum


* `UNSPECIFIED` (value: `"DATABASE_ENTITY_TYPE_UNSPECIFIED"`)

* `SCHEMA` (value: `"DATABASE_ENTITY_TYPE_SCHEMA"`)

* `TABLE` (value: `"DATABASE_ENTITY_TYPE_TABLE"`)

* `COLUMN` (value: `"DATABASE_ENTITY_TYPE_COLUMN"`)

* `CONSTRAINT` (value: `"DATABASE_ENTITY_TYPE_CONSTRAINT"`)

* `INDEX` (value: `"DATABASE_ENTITY_TYPE_INDEX"`)

* `TRIGGER` (value: `"DATABASE_ENTITY_TYPE_TRIGGER"`)

* `VIEW` (value: `"DATABASE_ENTITY_TYPE_VIEW"`)

* `SEQUENCE` (value: `"DATABASE_ENTITY_TYPE_SEQUENCE"`)

* `STORED_PROCEDURE` (value: `"DATABASE_ENTITY_TYPE_STORED_PROCEDURE"`)

* `FUNCTION` (value: `"DATABASE_ENTITY_TYPE_FUNCTION"`)

* `SYNONYM` (value: `"DATABASE_ENTITY_TYPE_SYNONYM"`)

* `DATABASE_PACKAGE` (value: `"DATABASE_ENTITY_TYPE_DATABASE_PACKAGE"`)

* `UDT` (value: `"DATABASE_ENTITY_TYPE_UDT"`)

* `MATERIALIZED_VIEW` (value: `"DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW"`)

* `DATABASE` (value: `"DATABASE_ENTITY_TYPE_DATABASE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ENABLED` (value: `"ENABLED"`)

* `DISABLED` (value: `"DISABLED"`)

* `DELETED` (value: `"DELETED"`)




