

# ContextDefinition

<p>Contains additional details about the context of the request. Verified Permissions evaluates this information in an authorization request as part of the <code>when</code> and <code>unless</code> clauses in a policy.</p> <p>This data type is used as a request parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html\">IsAuthorized</a> and <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html\">IsAuthorizedWithToken</a> operations.</p> <p>Example: <code>\"context\":{\"Context\":{\"&lt;KeyName1&gt;\":{\"boolean\":true},\"&lt;KeyName2&gt;\":{\"long\":1234}}}</code> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contextMap** | [**Map**](Map.md) |  |  [optional] |



