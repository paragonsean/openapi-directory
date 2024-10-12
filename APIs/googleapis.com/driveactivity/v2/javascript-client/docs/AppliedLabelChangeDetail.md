# DriveActivityApi.AppliedLabelChangeDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldChanges** | [**[FieldValueChange]**](FieldValueChange.md) | Field Changes. Only present if &#x60;types&#x60; contains &#x60;LABEL_FIELD_VALUE_CHANGED&#x60;. | [optional] 
**label** | **String** | The Label name representing the Label that changed. This name always contains the revision of the Label that was used when this Action occurred. The format is &#x60;labels/id@revision&#x60;. | [optional] 
**title** | **String** | The human-readable title of the label that changed. | [optional] 
**types** | **[String]** | The types of changes made to the Label on the Target. | [optional] 



## Enum: [TypesEnum]


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `LABEL_ADDED` (value: `"LABEL_ADDED"`)

* `LABEL_REMOVED` (value: `"LABEL_REMOVED"`)

* `LABEL_FIELD_VALUE_CHANGED` (value: `"LABEL_FIELD_VALUE_CHANGED"`)

* `LABEL_APPLIED_BY_ITEM_CREATE` (value: `"LABEL_APPLIED_BY_ITEM_CREATE"`)




