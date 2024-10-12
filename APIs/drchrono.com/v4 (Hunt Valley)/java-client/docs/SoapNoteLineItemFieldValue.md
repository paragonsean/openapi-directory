

# SoapNoteLineItemFieldValue

Values entered by doctor when charting a particular appointment

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appointment** | **Integer** | ID of appointment that the value applies to |  |
|**clinicalNoteField** | **Integer** | ID of &#x60;/api/clinical_note_field_types&#x60; object that indicates type of the value |  |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**updatedAt** | **String** |  |  [optional] [readonly] |
|**value** | **String** | Value of the field. Interpretation varies by field type. &#x60;clinical_note_field.data_type&#x60; | Value | Description ------------------------------- | ----- | ----------- &#x60;\&quot;Header\&quot;&#x60; | string |  &#x60;\&quot;SubHeader\&quot;&#x60; | string | &#x60;\&quot;String\&quot;&#x60; | string | If field is single/multiple select field, make sure value presents in allowed values set. &#x60;\&quot;TwoStrings\&quot;&#x60; | string | String is seperated by &#x60;\&quot;/\&quot;&#x60; &#x60;\&quot;NullCheckbox\&quot;&#x60; | string | Can be &#x60;\&quot;0\&quot;&#x60;, &#x60;\&quot;1\&quot;&#x60;, &#x60;\&quot;2\&quot;&#x60;, &#x60;\&quot;0\&quot;&#x60;-&#x60;Not selected&#x60;, &#x60;\&quot;1\&quot;&#x60;-&#x60;No&#x60;, &#x60;\&quot;2\&quot;&#x60;-&#x60;Yes&#x60; &#x60;\&quot;Checkbox\&quot;&#x60; | string | Can be &#x60;\&quot;True\&quot;&#x60;, &#x60;\&quot;False\&quot;&#x60;  |  |



