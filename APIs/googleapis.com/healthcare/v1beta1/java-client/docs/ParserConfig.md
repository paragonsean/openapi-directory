

# ParserConfig

The configuration for the parser. It determines how the server parses the messages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowNullHeader** | **Boolean** | Determines whether messages with no header are allowed. |  [optional] |
|**schema** | [**SchemaPackage**](SchemaPackage.md) |  |  [optional] |
|**segmentTerminator** | **byte[]** | Byte(s) to use as the segment terminator. If this is unset, &#39;\\r&#39; is used as segment terminator, matching the HL7 version 2 specification. |  [optional] |
|**version** | [**VersionEnum**](#VersionEnum) | Immutable. Determines the version of both the default parser to be used when &#x60;schema&#x60; is not given, as well as the schematized parser used when &#x60;schema&#x60; is specified. This field is immutable after HL7v2 store creation. |  [optional] |



## Enum: VersionEnum

| Name | Value |
|---- | -----|
| PARSER_VERSION_UNSPECIFIED | &quot;PARSER_VERSION_UNSPECIFIED&quot; |
| V1 | &quot;V1&quot; |
| V2 | &quot;V2&quot; |
| V3 | &quot;V3&quot; |



