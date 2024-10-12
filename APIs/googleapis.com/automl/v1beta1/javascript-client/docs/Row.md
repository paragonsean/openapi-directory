# CloudAutoMlApi.Row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columnSpecIds** | **[String]** | The resource IDs of the column specs describing the columns of the row. If set must contain, but possibly in a different order, all input feature column_spec_ids of the Model this row is being passed to. Note: The below &#x60;values&#x60; field must match order of this field, if this field is set. | [optional] 
**values** | **[Object]** | Required. The values of the row cells, given in the same order as the column_spec_ids, or, if not set, then in the same order as input feature column_specs of the Model this row is being passed to. | [optional] 


