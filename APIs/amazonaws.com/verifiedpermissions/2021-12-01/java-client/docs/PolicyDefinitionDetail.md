

# PolicyDefinitionDetail

<p>A structure that describes a policy definition. It must always have either an <code>static</code> or a <code>templateLinked</code> element.</p> <p>This data type is used as a response parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html\">GetPolicy</a> operation.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_static** | [**PolicyDefinitionDetailStatic**](PolicyDefinitionDetailStatic.md) |  |  [optional] |
|**templateLinked** | [**PolicyDefinitionDetailTemplateLinked**](PolicyDefinitionDetailTemplateLinked.md) |  |  [optional] |



