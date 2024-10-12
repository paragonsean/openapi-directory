# ThePlaidApi.DepositSwitchStateUpdateWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depositSwitchId** | **String** | The ID of the deposit switch. | [optional] 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | [optional] 
**state** | **String** |  The state, or status, of the deposit switch.  &#x60;initialized&#x60;: The deposit switch has been initialized with the user entering the information required to submit the deposit switch request.  &#x60;processing&#x60;: The deposit switch request has been submitted and is being processed.  &#x60;completed&#x60;: The user&#39;s employer has fulfilled and completed the deposit switch request.  &#x60;error&#x60;: There was an error processing the deposit switch request.  For more information, see the [Deposit Switch API reference](/docs/deposit-switch/reference#deposit_switchget). | [optional] 
**webhookCode** | **String** | &#x60;\&quot;SWITCH_STATE_UPDATE\&quot;&#x60; | [optional] 
**webhookType** | **String** | &#x60;\&quot;DEPOSIT_SWITCH\&quot;&#x60; | [optional] 


