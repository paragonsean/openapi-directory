

# Action

<p>Information about an action.</p> <p>Each rule must include exactly one of the following types of actions: <code>forward</code>, <code>fixed-response</code>, or <code>redirect</code>, and it must be the last action to be performed.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**ActionTypeEnum**](ActionTypeEnum.md) |  |  |
|**targetGroupArn** | [**String**](String.md) |  |  [optional] |
|**authenticateOidcConfig** | [**ActionAuthenticateOidcConfig**](ActionAuthenticateOidcConfig.md) |  |  [optional] |
|**authenticateCognitoConfig** | [**ActionAuthenticateCognitoConfig**](ActionAuthenticateCognitoConfig.md) |  |  [optional] |
|**order** | [**Integer**](Integer.md) |  |  [optional] |
|**redirectConfig** | [**ActionRedirectConfig**](ActionRedirectConfig.md) |  |  [optional] |
|**fixedResponseConfig** | [**ActionFixedResponseConfig**](ActionFixedResponseConfig.md) |  |  [optional] |
|**forwardConfig** | [**ActionForwardConfig**](ActionForwardConfig.md) |  |  [optional] |



