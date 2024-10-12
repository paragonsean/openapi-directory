# GoogleSlidesApi.UpdateTableRowPropertiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;tableRowProperties&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example to update the minimum row height, set &#x60;fields&#x60; to &#x60;\&quot;min_row_height\&quot;&#x60;. If &#39;\&quot;min_row_height\&quot;&#39; is included in the field mask but the property is left unset, the minimum row height will default to 0. | [optional] 
**objectId** | **String** | The object ID of the table. | [optional] 
**rowIndices** | **[Number]** | The list of zero-based indices specifying which rows to update. If no indices are provided, all rows in the table will be updated. | [optional] 
**tableRowProperties** | [**TableRowProperties**](TableRowProperties.md) |  | [optional] 


