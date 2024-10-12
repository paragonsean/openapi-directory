# DatabaseMigrationApi.SynonymEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customFeatures** | **{String: Object}** | Custom engine specific features. | [optional] 
**sourceEntity** | **String** | The name of the entity for which the synonym is being created (the source). | [optional] 
**sourceType** | **String** | The type of the entity for which the synonym is being created (usually a table or a sequence). | [optional] 



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




