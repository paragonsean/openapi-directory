# CloudHealthcareApi.SchemaPackage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignoreMinOccurs** | **Boolean** | Flag to ignore all min_occurs restrictions in the schema. This means that incoming messages can omit any group, segment, field, component, or subcomponent. | [optional] 
**schemas** | [**[Hl7SchemaConfig]**](Hl7SchemaConfig.md) | Schema configs that are layered based on their VersionSources that match the incoming message. Schema configs present in higher indices override those in lower indices with the same message type and trigger event if their VersionSources all match an incoming message. | [optional] 
**schematizedParsingType** | **String** | Determines how messages that fail to parse are handled. | [optional] 
**types** | [**[Hl7TypesConfig]**](Hl7TypesConfig.md) | Schema type definitions that are layered based on their VersionSources that match the incoming message. Type definitions present in higher indices override those in lower indices with the same type name if their VersionSources all match an incoming message. | [optional] 
**unexpectedSegmentHandling** | **String** | Determines how unexpected segments (segments not matched to the schema) are handled. | [optional] 



## Enum: SchematizedParsingTypeEnum


* `SCHEMATIZED_PARSING_TYPE_UNSPECIFIED` (value: `"SCHEMATIZED_PARSING_TYPE_UNSPECIFIED"`)

* `SOFT_FAIL` (value: `"SOFT_FAIL"`)

* `HARD_FAIL` (value: `"HARD_FAIL"`)





## Enum: UnexpectedSegmentHandlingEnum


* `UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED` (value: `"UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED"`)

* `FAIL` (value: `"FAIL"`)

* `SKIP` (value: `"SKIP"`)

* `PARSE` (value: `"PARSE"`)




