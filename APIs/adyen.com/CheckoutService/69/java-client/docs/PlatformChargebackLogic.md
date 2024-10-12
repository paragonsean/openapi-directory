

# PlatformChargebackLogic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**behavior** | [**BehaviorEnum**](#BehaviorEnum) | The method of handling the chargeback.  Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**. |  [optional] |
|**costAllocationAccount** | **String** | The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback fees are booked to your liable balance account. |  [optional] |
|**targetAccount** | **String** | The unique identifier of the balance account against which the disputed amount is booked.  Required if &#x60;behavior&#x60; is **deductFromOneBalanceAccount**. |  [optional] |



## Enum: BehaviorEnum

| Name | Value |
|---- | -----|
| DEDUCT_ACCORDING_TO_SPLIT_RATIO | &quot;deductAccordingToSplitRatio&quot; |
| DEDUCT_FROM_LIABLE_ACCOUNT | &quot;deductFromLiableAccount&quot; |
| DEDUCT_FROM_ONE_BALANCE_ACCOUNT | &quot;deductFromOneBalanceAccount&quot; |



