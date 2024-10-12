

# SchemaPackage

A schema package contains a set of schemas and type definitions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ignoreMinOccurs** | **Boolean** | Flag to ignore all min_occurs restrictions in the schema. This means that incoming messages can omit any group, segment, field, component, or subcomponent. |  [optional] |
|**schemas** | [**List&lt;Hl7SchemaConfig&gt;**](Hl7SchemaConfig.md) | Schema configs that are layered based on their VersionSources that match the incoming message. Schema configs present in higher indices override those in lower indices with the same message type and trigger event if their VersionSources all match an incoming message. |  [optional] |
|**schematizedParsingType** | [**SchematizedParsingTypeEnum**](#SchematizedParsingTypeEnum) | Determines how messages that fail to parse are handled. |  [optional] |
|**types** | [**List&lt;Hl7TypesConfig&gt;**](Hl7TypesConfig.md) | Schema type definitions that are layered based on their VersionSources that match the incoming message. Type definitions present in higher indices override those in lower indices with the same type name if their VersionSources all match an incoming message. |  [optional] |
|**unexpectedSegmentHandling** | [**UnexpectedSegmentHandlingEnum**](#UnexpectedSegmentHandlingEnum) | Determines how unexpected segments (segments not matched to the schema) are handled. |  [optional] |



## Enum: SchematizedParsingTypeEnum

| Name | Value |
|---- | -----|
| SCHEMATIZED_PARSING_TYPE_UNSPECIFIED | &quot;SCHEMATIZED_PARSING_TYPE_UNSPECIFIED&quot; |
| SOFT_FAIL | &quot;SOFT_FAIL&quot; |
| HARD_FAIL | &quot;HARD_FAIL&quot; |



## Enum: UnexpectedSegmentHandlingEnum

| Name | Value |
|---- | -----|
| UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED | &quot;UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED&quot; |
| FAIL | &quot;FAIL&quot; |
| SKIP | &quot;SKIP&quot; |
| PARSE | &quot;PARSE&quot; |



