

# EntityIdentifier

<p>Contains the identifier of an entity, including its ID and type.</p> <p>This data type is used as a request parameter for <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html\">IsAuthorized</a> operation, and as a response parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html\">CreatePolicy</a>, <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html\">GetPolicy</a>, and <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html\">UpdatePolicy</a> operations.</p> <p>Example: <code>{\"entityId\":\"<i>string</i>\",\"entityType\":\"<i>string</i>\"}</code> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityType** | [**String**](String.md) |  |  |
|**entityId** | [**String**](String.md) |  |  |



