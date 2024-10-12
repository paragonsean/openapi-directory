# SquareConnectApi.V1Settlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankAccountId** | **String** | The Square-issued unique identifier for the bank account associated with the settlement. | [optional] 
**entries** | [**[V1SettlementEntry]**](V1SettlementEntry.md) | The entries included in this settlement. | [optional] 
**id** | **String** | The settlement&#39;s unique identifier. | [optional] 
**initiatedAt** | **String** | The time when the settlement was submitted for deposit or withdrawal, in ISO 8601 format. | [optional] 
**status** | **String** | The settlement&#39;s current status. | [optional] 
**totalMoney** | [**V1Money**](V1Money.md) |  | [optional] 


