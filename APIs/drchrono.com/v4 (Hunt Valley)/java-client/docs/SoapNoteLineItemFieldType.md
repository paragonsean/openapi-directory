

# SoapNoteLineItemFieldType


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedValues** | **List&lt;String&gt;** | Value options the field type relies on if applicable, otherwise it will be an empty array |  [optional] |
|**archived** | **Boolean** | Indicates that the field has been soft-deleted by the doctor and will not be used in future notes |  [optional] |
|**clinicalNoteTemplate** | **String** | ID of the &#x60;/api/clinical_note_templates&#x60; object that the field belongs to |  [optional] [readonly] |
|**comment** | **String** | Comment |  [optional] |
|**dataType** | **String** | One of &#x60;\&quot;\&quot;&#x60;, &#x60;\&quot;Checkbox\&quot;&#x60;, &#x60;\&quot;NullCheckbox\&quot;&#x60;, &#x60;\&quot;String\&quot;&#x60;, &#x60;\&quot;TwoStrings\&quot;&#x60;, &#x60;\&quot;FreeDraw\&quot;&#x60;, &#x60;\&quot;Photo\&quot;&#x60;, &#x60;\&quot;Header\&quot;&#x60;, &#x60;\&quot;Subheader\&quot;&#x60; |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |
|**required** | **Boolean** | Indicates that a note should not be locked unless a value is provided for this field |  [optional] |



