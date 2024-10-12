# WebApplicationFirewallManagement.PolicySettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customBlockResponseBody** | **String** | If the action type is block, customer can override the response body. The body must be specified in base64 encoding. | [optional] 
**customBlockResponseStatusCode** | **Number** | If the action type is block, customer can override the response status code. | [optional] 
**enabledState** | **String** | Describes if the policy is in enabled or disabled state. Defaults to Enabled if not specified. | [optional] 
**mode** | **String** | Describes if it is in detection mode or prevention mode at policy level. | [optional] 
**redirectUrl** | **String** | If action type is redirect, this field represents redirect URL for the client. | [optional] 



## Enum: EnabledStateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)





## Enum: ModeEnum


* `Prevention` (value: `"Prevention"`)

* `Detection` (value: `"Detection"`)




