# PolyApi.AssetImportMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | The code associated with this message. | [optional] 
**filePath** | **String** | An optional file path. Only present for those error codes that specify it. | [optional] 
**imageError** | [**ImageError**](ImageError.md) |  | [optional] 
**objParseError** | [**ObjParseError**](ObjParseError.md) |  | [optional] 



## Enum: CodeEnum


* `CODE_UNSPECIFIED` (value: `"CODE_UNSPECIFIED"`)

* `NO_IMPORTABLE_FILE` (value: `"NO_IMPORTABLE_FILE"`)

* `EMPTY_MODEL` (value: `"EMPTY_MODEL"`)

* `OBJ_PARSE_ERROR` (value: `"OBJ_PARSE_ERROR"`)

* `EXPIRED` (value: `"EXPIRED"`)

* `IMAGE_ERROR` (value: `"IMAGE_ERROR"`)

* `EXTRA_FILES_WITH_ARCHIVE` (value: `"EXTRA_FILES_WITH_ARCHIVE"`)

* `DEFAULT_MATERIALS` (value: `"DEFAULT_MATERIALS"`)

* `FATAL_ERROR` (value: `"FATAL_ERROR"`)

* `INVALID_ELEMENT_TYPE` (value: `"INVALID_ELEMENT_TYPE"`)




