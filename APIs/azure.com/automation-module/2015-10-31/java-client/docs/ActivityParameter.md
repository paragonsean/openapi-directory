

# ActivityParameter

Definition of the activity parameter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Gets or sets the description of the activity parameter. |  [optional] |
|**isDynamic** | **Boolean** | Gets or sets a Boolean value that indicates true if the parameter is dynamic. |  [optional] |
|**isMandatory** | **Boolean** | Gets or sets a Boolean value that indicates true if the parameter is required. If the value is false, the parameter is optional. |  [optional] |
|**name** | **String** | Gets or sets the name of the activity parameter. |  [optional] |
|**position** | **Long** | Gets or sets the position of the activity parameter. |  [optional] |
|**type** | **String** | Gets or sets the type of the activity parameter. |  [optional] |
|**validationSet** | [**List&lt;ActivityParameterValidationSet&gt;**](ActivityParameterValidationSet.md) | Gets or sets the validation set of activity parameter. |  [optional] |
|**valueFromPipeline** | **Boolean** | Gets or sets a Boolean value that indicates true if the parameter can take values from the incoming pipeline objects. This setting is used if the cmdlet must access the complete input object. false indicates that the parameter cannot take values from the complete input object. |  [optional] |
|**valueFromPipelineByPropertyName** | **Boolean** | Gets or sets a Boolean value that indicates true if the parameter can be filled from a property of the incoming pipeline object that has the same name as this parameter. false indicates that the parameter cannot be filled from the incoming pipeline object property with the same name.  |  [optional] |
|**valueFromRemainingArguments** | **Boolean** | Gets or sets a Boolean value that indicates true if the cmdlet parameter accepts all the remaining command-line arguments that are associated with this parameter in the form of an array. false if the cmdlet parameter does not accept all the remaining argument values. |  [optional] |



