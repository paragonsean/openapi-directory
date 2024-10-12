

# SynonymEntity

Synonym's parent is a schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customFeatures** | **Map&lt;String, Object&gt;** | Custom engine specific features. |  [optional] |
|**sourceEntity** | **String** | The name of the entity for which the synonym is being created (the source). |  [optional] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | The type of the entity for which the synonym is being created (usually a table or a sequence). |  [optional] |



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



