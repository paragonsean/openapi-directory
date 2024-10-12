

# ActionIdentifier

<p>Contains information about an action for a request for which an authorization decision is made.</p> <p>This data type is used as an request parameter to the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html\">IsAuthorized</a> and <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html\">IsAuthorizedWithToken</a> operations.</p> <p>Example: <code>{ \"actionId\": \"&lt;action name&gt;\", \"actionType\": \"Action\" }</code> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionType** | [**String**](String.md) |  |  |
|**actionId** | [**String**](String.md) |  |  |



