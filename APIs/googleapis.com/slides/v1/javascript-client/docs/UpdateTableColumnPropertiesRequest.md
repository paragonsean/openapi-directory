# GoogleSlidesApi.UpdateTableColumnPropertiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columnIndices** | **[Number]** | The list of zero-based indices specifying which columns to update. If no indices are provided, all columns in the table will be updated. | [optional] 
**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;tableColumnProperties&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example to update the column width, set &#x60;fields&#x60; to &#x60;\&quot;column_width\&quot;&#x60;. If &#39;\&quot;column_width\&quot;&#39; is included in the field mask but the property is left unset, the column width will default to 406,400 EMU (32 points). | [optional] 
**objectId** | **String** | The object ID of the table. | [optional] 
**tableColumnProperties** | [**TableColumnProperties**](TableColumnProperties.md) |  | [optional] 


