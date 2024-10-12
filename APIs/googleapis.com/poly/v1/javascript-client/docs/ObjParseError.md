# PolyApi.ObjParseError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | The type of problem found (required). | [optional] 
**endIndex** | **Number** | The ending character index at which the problem was found. | [optional] 
**filePath** | **String** | The file path in which the problem was found. | [optional] 
**line** | **String** | The text of the line. Note that this may be truncated if the line was very long. This may not include the error if it occurs after line truncation. | [optional] 
**lineNumber** | **Number** | Line number at which the problem was found. | [optional] 
**startIndex** | **Number** | The starting character index at which the problem was found. | [optional] 



## Enum: CodeEnum


* `CODE_UNSPECIFIED` (value: `"CODE_UNSPECIFIED"`)

* `INCONSISTENT_VERTEX_REFS` (value: `"INCONSISTENT_VERTEX_REFS"`)

* `INVALID_COMMAND` (value: `"INVALID_COMMAND"`)

* `INVALID_NUMBER` (value: `"INVALID_NUMBER"`)

* `INVALID_VERTEX_REF` (value: `"INVALID_VERTEX_REF"`)

* `MISSING_GEOMETRIC_VERTEX` (value: `"MISSING_GEOMETRIC_VERTEX"`)

* `MISSING_TOKEN` (value: `"MISSING_TOKEN"`)

* `TOO_FEW_DIMENSIONS` (value: `"TOO_FEW_DIMENSIONS"`)

* `TOO_FEW_VERTICES` (value: `"TOO_FEW_VERTICES"`)

* `TOO_MANY_DIMENSIONS` (value: `"TOO_MANY_DIMENSIONS"`)

* `UNSUPPORTED_COMMAND` (value: `"UNSUPPORTED_COMMAND"`)

* `UNUSED_TOKENS` (value: `"UNUSED_TOKENS"`)

* `VERTEX_NOT_FOUND` (value: `"VERTEX_NOT_FOUND"`)

* `NUMBER_OUT_OF_RANGE` (value: `"NUMBER_OUT_OF_RANGE"`)

* `INVALID_VALUE` (value: `"INVALID_VALUE"`)

* `INVALID_TEXTURE_OPTION` (value: `"INVALID_TEXTURE_OPTION"`)

* `TOO_MANY_PROBLEMS` (value: `"TOO_MANY_PROBLEMS"`)

* `MISSING_FILE_NAME` (value: `"MISSING_FILE_NAME"`)

* `FILE_NOT_FOUND` (value: `"FILE_NOT_FOUND"`)

* `UNKNOWN_MATERIAL` (value: `"UNKNOWN_MATERIAL"`)

* `NO_MATERIAL_DEFINED` (value: `"NO_MATERIAL_DEFINED"`)

* `INVALID_SMOOTHING_GROUP` (value: `"INVALID_SMOOTHING_GROUP"`)

* `MISSING_VERTEX_COLORS` (value: `"MISSING_VERTEX_COLORS"`)

* `FILE_SUBSTITUTION` (value: `"FILE_SUBSTITUTION"`)

* `LINE_TOO_LONG` (value: `"LINE_TOO_LONG"`)

* `INVALID_FILE_PATH` (value: `"INVALID_FILE_PATH"`)




