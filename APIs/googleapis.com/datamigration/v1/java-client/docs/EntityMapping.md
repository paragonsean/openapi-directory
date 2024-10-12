

# EntityMapping

Details of the mappings of a database entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**draftEntity** | **String** | Target entity full name. The draft entity can also include a column, index or constraint using the same naming notation schema.table.column. |  [optional] |
|**draftType** | [**DraftTypeEnum**](#DraftTypeEnum) | Type of draft entity. |  [optional] |
|**mappingLog** | [**List&lt;EntityMappingLogEntry&gt;**](EntityMappingLogEntry.md) | Entity mapping log entries. Multiple rules can be effective and contribute changes to a converted entity, such as a rule can handle the entity name, another rule can handle an entity type. In addition, rules which did not change the entity are also logged along with the reason preventing them to do so. |  [optional] |
|**sourceEntity** | **String** | Source entity full name. The source entity can also be a column, index or constraint using the same naming notation schema.table.column. |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Type of source entity. |  [optional] |



## Enum: DraftTypeEnum

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



## Enum: SourceTypeEnum

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



