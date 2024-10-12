# SquareConnectApi.SubscriptionPhase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cadence** | **String** | The billing cadence of the phase. For example, weekly or monthly. This field cannot be changed after a &#x60;SubscriptionPhase&#x60; is created. | 
**ordinal** | **Number** | The position this phase appears in the sequence of phases defined for the plan, indexed from 0. This field cannot be changed after a &#x60;SubscriptionPhase&#x60; is created. | [optional] 
**periods** | **Number** | The number of &#x60;cadence&#x60;s the phase lasts. If not set, the phase never ends. Only the last phase can be indefinite. This field cannot be changed after a &#x60;SubscriptionPhase&#x60; is created. | [optional] 
**recurringPriceMoney** | [**Money**](Money.md) |  | 
**uid** | **String** | The Square-assigned ID of the subscription phase. This field cannot be changed after a &#x60;SubscriptionPhase&#x60; is created. | [optional] 


