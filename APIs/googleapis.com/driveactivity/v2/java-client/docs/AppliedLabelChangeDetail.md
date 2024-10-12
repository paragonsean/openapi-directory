

# AppliedLabelChangeDetail

A change made to a Label on the Target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldChanges** | [**List&lt;FieldValueChange&gt;**](FieldValueChange.md) | Field Changes. Only present if &#x60;types&#x60; contains &#x60;LABEL_FIELD_VALUE_CHANGED&#x60;. |  [optional] |
|**label** | **String** | The Label name representing the Label that changed. This name always contains the revision of the Label that was used when this Action occurred. The format is &#x60;labels/id@revision&#x60;. |  [optional] |
|**title** | **String** | The human-readable title of the label that changed. |  [optional] |
|**types** | [**List&lt;TypesEnum&gt;**](#List&lt;TypesEnum&gt;) | The types of changes made to the Label on the Target. |  [optional] |



## Enum: List&lt;TypesEnum&gt;

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| LABEL_ADDED | &quot;LABEL_ADDED&quot; |
| LABEL_REMOVED | &quot;LABEL_REMOVED&quot; |
| LABEL_FIELD_VALUE_CHANGED | &quot;LABEL_FIELD_VALUE_CHANGED&quot; |
| LABEL_APPLIED_BY_ITEM_CREATE | &quot;LABEL_APPLIED_BY_ITEM_CREATE&quot; |



