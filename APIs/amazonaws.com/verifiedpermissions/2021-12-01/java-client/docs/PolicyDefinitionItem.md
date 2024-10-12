

# PolicyDefinitionItem

<p>A structure that describes a <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_PolicyDefinintion.html\">PolicyDefinintion</a>. It will always have either an <code>StaticPolicy</code> or a <code>TemplateLinkedPolicy</code> element.</p> <p>This data type is used as a response parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html\">CreatePolicy</a> and <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html\">ListPolicies</a> operations. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_static** | [**PolicyDefinitionItemStatic**](PolicyDefinitionItemStatic.md) |  |  [optional] |
|**templateLinked** | [**PolicyDefinitionItemTemplateLinked**](PolicyDefinitionItemTemplateLinked.md) |  |  [optional] |



