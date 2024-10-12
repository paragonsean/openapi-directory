# TicketmasterPublishApi.Change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from** | **String** | Json path of the source entity when using the move operation. | [optional] 
**op** | **String** | Operation to apply on the entity. | 
**path** | **String** | Json path from the root of the document to the place where the change should be applied. | 
**value** | **Object** | Data to change. MUST be a valid json object. | [optional] 



## Enum: OpEnum


* `add` (value: `"add"`)

* `remove` (value: `"remove"`)

* `replace` (value: `"replace"`)

* `move` (value: `"move"`)

* `copy` (value: `"copy"`)

* `test` (value: `"test"`)




