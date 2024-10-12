# CloudDocumentAiApi.GoogleCloudDocumentaiV1DocumentProvenance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Number** | The Id of this operation. Needs to be unique within the scope of the revision. | [optional] 
**parents** | [**[GoogleCloudDocumentaiV1DocumentProvenanceParent]**](GoogleCloudDocumentaiV1DocumentProvenanceParent.md) | References to the original elements that are replaced. | [optional] 
**revision** | **Number** | The index of the revision that produced this element. | [optional] 
**type** | **String** | The type of provenance operation. | [optional] 



## Enum: TypeEnum


* `OPERATION_TYPE_UNSPECIFIED` (value: `"OPERATION_TYPE_UNSPECIFIED"`)

* `ADD` (value: `"ADD"`)

* `REMOVE` (value: `"REMOVE"`)

* `UPDATE` (value: `"UPDATE"`)

* `REPLACE` (value: `"REPLACE"`)

* `EVAL_REQUESTED` (value: `"EVAL_REQUESTED"`)

* `EVAL_APPROVED` (value: `"EVAL_APPROVED"`)

* `EVAL_SKIPPED` (value: `"EVAL_SKIPPED"`)




