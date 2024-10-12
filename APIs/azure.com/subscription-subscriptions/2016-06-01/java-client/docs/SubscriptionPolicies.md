

# SubscriptionPolicies

Subscription policies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationPlacementId** | **String** | The subscription location placement ID. The ID indicates which regions are visible for a subscription. For example, a subscription with a location placement Id of Public_2014-09-01 has access to Azure public regions. |  [optional] [readonly] |
|**quotaId** | **String** | The subscription quota ID. |  [optional] [readonly] |
|**spendingLimit** | [**SpendingLimitEnum**](#SpendingLimitEnum) | The subscription spending limit. |  [optional] [readonly] |



## Enum: SpendingLimitEnum

| Name | Value |
|---- | -----|
| ON | &quot;On&quot; |
| OFF | &quot;Off&quot; |
| CURRENT_PERIOD_OFF | &quot;CurrentPeriodOff&quot; |



