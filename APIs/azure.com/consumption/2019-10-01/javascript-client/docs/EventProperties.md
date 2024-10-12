# ConsumptionManagementClient.EventProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustments** | [**Amount**](Amount.md) |  | [optional] 
**charges** | [**Amount**](Amount.md) |  | [optional] 
**closedBalance** | [**Amount**](Amount.md) |  | [optional] 
**creditExpired** | [**Amount**](Amount.md) |  | [optional] 
**description** | **String** | Transaction description. | [optional] [readonly] 
**eventType** | **String** | The type of event. | [optional] 
**invoiceNumber** | **String** | Invoice number. | [optional] [readonly] 
**newCredit** | [**Amount**](Amount.md) |  | [optional] 
**transactionDate** | **Date** | Transaction date. | [optional] [readonly] 



## Enum: EventTypeEnum


* `SettledCharges` (value: `"SettledCharges"`)

* `PendingCharges` (value: `"PendingCharges"`)

* `PendingAdjustments` (value: `"PendingAdjustments"`)

* `PendingNewCredit` (value: `"PendingNewCredit"`)

* `PendingExpiredCredit` (value: `"PendingExpiredCredit"`)

* `UnKnown` (value: `"UnKnown"`)

* `NewCredit` (value: `"NewCredit"`)




