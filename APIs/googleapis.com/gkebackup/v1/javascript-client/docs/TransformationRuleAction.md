# BackupForGkeApi.TransformationRuleAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fromPath** | **String** | Optional. A string containing a JSON Pointer value that references the location in the target document to move the value from. | [optional] 
**op** | **String** | Required. op specifies the operation to perform. | [optional] 
**path** | **String** | Optional. A string containing a JSON-Pointer value that references a location within the target document where the operation is performed. | [optional] 
**value** | **String** | Optional. A string that specifies the desired value in string format to use for transformation. | [optional] 



## Enum: OpEnum


* `OP_UNSPECIFIED` (value: `"OP_UNSPECIFIED"`)

* `REMOVE` (value: `"REMOVE"`)

* `MOVE` (value: `"MOVE"`)

* `COPY` (value: `"COPY"`)

* `ADD` (value: `"ADD"`)

* `TEST` (value: `"TEST"`)

* `REPLACE` (value: `"REPLACE"`)




