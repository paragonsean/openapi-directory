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
**invoiceNumber** | **String** | Invoice Number. | [optional] [readonly] 
**newCredit** | [**Amount**](Amount.md) |  | [optional] 
**transactionDate** | **Date** | Transaction Date. | [optional] [readonly] 



## Enum: EventTypeEnum


* `NewCredit` (value: `"NewCredit"`)

* `ExpiredCredit` (value: `"ExpiredCredit"`)

* `SettledCharges` (value: `"SettledCharges"`)




