

# ObjParseError

Details of an error resulting from parsing an OBJ file

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | The type of problem found (required). |  [optional] |
|**endIndex** | **Integer** | The ending character index at which the problem was found. |  [optional] |
|**filePath** | **String** | The file path in which the problem was found. |  [optional] |
|**line** | **String** | The text of the line. Note that this may be truncated if the line was very long. This may not include the error if it occurs after line truncation. |  [optional] |
|**lineNumber** | **Integer** | Line number at which the problem was found. |  [optional] |
|**startIndex** | **Integer** | The starting character index at which the problem was found. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| INCONSISTENT_VERTEX_REFS | &quot;INCONSISTENT_VERTEX_REFS&quot; |
| INVALID_COMMAND | &quot;INVALID_COMMAND&quot; |
| INVALID_NUMBER | &quot;INVALID_NUMBER&quot; |
| INVALID_VERTEX_REF | &quot;INVALID_VERTEX_REF&quot; |
| MISSING_GEOMETRIC_VERTEX | &quot;MISSING_GEOMETRIC_VERTEX&quot; |
| MISSING_TOKEN | &quot;MISSING_TOKEN&quot; |
| TOO_FEW_DIMENSIONS | &quot;TOO_FEW_DIMENSIONS&quot; |
| TOO_FEW_VERTICES | &quot;TOO_FEW_VERTICES&quot; |
| TOO_MANY_DIMENSIONS | &quot;TOO_MANY_DIMENSIONS&quot; |
| UNSUPPORTED_COMMAND | &quot;UNSUPPORTED_COMMAND&quot; |
| UNUSED_TOKENS | &quot;UNUSED_TOKENS&quot; |
| VERTEX_NOT_FOUND | &quot;VERTEX_NOT_FOUND&quot; |
| NUMBER_OUT_OF_RANGE | &quot;NUMBER_OUT_OF_RANGE&quot; |
| INVALID_VALUE | &quot;INVALID_VALUE&quot; |
| INVALID_TEXTURE_OPTION | &quot;INVALID_TEXTURE_OPTION&quot; |
| TOO_MANY_PROBLEMS | &quot;TOO_MANY_PROBLEMS&quot; |
| MISSING_FILE_NAME | &quot;MISSING_FILE_NAME&quot; |
| FILE_NOT_FOUND | &quot;FILE_NOT_FOUND&quot; |
| UNKNOWN_MATERIAL | &quot;UNKNOWN_MATERIAL&quot; |
| NO_MATERIAL_DEFINED | &quot;NO_MATERIAL_DEFINED&quot; |
| INVALID_SMOOTHING_GROUP | &quot;INVALID_SMOOTHING_GROUP&quot; |
| MISSING_VERTEX_COLORS | &quot;MISSING_VERTEX_COLORS&quot; |
| FILE_SUBSTITUTION | &quot;FILE_SUBSTITUTION&quot; |
| LINE_TOO_LONG | &quot;LINE_TOO_LONG&quot; |
| INVALID_FILE_PATH | &quot;INVALID_FILE_PATH&quot; |



