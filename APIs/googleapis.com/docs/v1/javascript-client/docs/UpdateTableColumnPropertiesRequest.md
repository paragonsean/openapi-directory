# GoogleDocsApi.UpdateTableColumnPropertiesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columnIndices** | **[Number]** | The list of zero-based column indices whose property should be updated. If no indices are specified, all columns will be updated. | [optional] 
**fields** | **String** | The fields that should be updated. At least one field must be specified. The root &#x60;tableColumnProperties&#x60; is implied and should not be specified. A single &#x60;\&quot;*\&quot;&#x60; can be used as short-hand for listing every field. For example to update the column width, set &#x60;fields&#x60; to &#x60;\&quot;width\&quot;&#x60;. | [optional] 
**tableColumnProperties** | [**TableColumnProperties**](TableColumnProperties.md) |  | [optional] 
**tableStartLocation** | [**Location**](Location.md) |  | [optional] 


