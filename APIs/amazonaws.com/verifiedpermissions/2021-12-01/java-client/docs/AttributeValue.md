

# AttributeValue

<p>The value of an attribute.</p> <p>Contains information about the runtime context for a request for which an authorization decision is made. </p> <p>This data type is used as a member of the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html\">ContextDefinition</a> structure which is uses as a request parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html\">IsAuthorized</a> and <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html\">IsAuthorizedWithToken</a> operations.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_boolean** | [**Boolean**](Boolean.md) |  |  [optional] |
|**entityIdentifier** | [**AttributeValueEntityIdentifier**](AttributeValueEntityIdentifier.md) |  |  [optional] |
|**_long** | [**Integer**](Integer.md) |  |  [optional] |
|**string** | [**String**](String.md) |  |  [optional] |
|**set** | [**List**](List.md) |  |  [optional] |
|**record** | [**Map**](Map.md) |  |  [optional] |



