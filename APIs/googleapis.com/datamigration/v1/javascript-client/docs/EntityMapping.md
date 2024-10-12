# DatabaseMigrationApi.EntityMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draftEntity** | **String** | Target entity full name. The draft entity can also include a column, index or constraint using the same naming notation schema.table.column. | [optional] 
**draftType** | **String** | Type of draft entity. | [optional] 
**mappingLog** | [**[EntityMappingLogEntry]**](EntityMappingLogEntry.md) | Entity mapping log entries. Multiple rules can be effective and contribute changes to a converted entity, such as a rule can handle the entity name, another rule can handle an entity type. In addition, rules which did not change the entity are also logged along with the reason preventing them to do so. | [optional] 
**sourceEntity** | **String** | Source entity full name. The source entity can also be a column, index or constraint using the same naming notation schema.table.column. | [optional] 
**sourceType** | **String** | Type of source entity. | [optional] 



## Enum: DraftTypeEnum


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





## Enum: SourceTypeEnum


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




