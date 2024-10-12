

# DisplayMarkUpParametersValue

The parameters object will contain a key/value pair for each data binding present in the value. The key will match the name of the data binding without the enclosing curly brackets. For example, If \"{{Terms and Conditions}}\" is present in the value, a value with the key \"Terms and Conditions\" will be present in the parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Name of the parameter |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of parameter * &#x60;link&#x60; - The &#39;value&#39; contains a link to external content. The user should be able click on this link to view the content. * &#x60;mailto&#x60; - The &#39;value&#39; contains an email address. The user should be able click on this address to send open their email client. |  [optional] |
|**value** | **String** | Value of this parameter |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| LINK | &quot;link&quot; |
| MAILTO | &quot;mailto&quot; |



