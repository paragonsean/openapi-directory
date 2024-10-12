

# PolicyDefinition

<p>A structure that contains the details for a Cedar policy definition. It includes the policy type, a description, and a policy body. This is a top level data type used to create a policy.</p> <p>This data type is used as a request parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html\">CreatePolicy</a> operation. This structure must always have either an <code>static</code> or a <code>templateLinked</code> element.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_static** | [**PolicyDefinitionStatic**](PolicyDefinitionStatic.md) |  |  [optional] |
|**templateLinked** | [**PolicyDefinitionTemplateLinked**](PolicyDefinitionTemplateLinked.md) |  |  [optional] |



