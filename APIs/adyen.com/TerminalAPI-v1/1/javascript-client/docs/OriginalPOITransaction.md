# AdyenTerminalApi.OriginalPOITransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirerID** | **Number** | Restrict to these Acquirer if present. | [optional] 
**amountValue** | **Number** |  | [optional] 
**approvalCode** | **String** | If referral. | [optional] 
**customerLanguage** | **String** | If the language is selected by the Sale System before the request to the POI. | [optional] 
**hostTransactionID** | [**TransactionIDType**](TransactionIDType.md) |  | [optional] 
**POIID** | **String** | If original transaction is coming from another POI. | [optional] 
**pOITransactionID** | [**TransactionIDType**](TransactionIDType.md) |  | [optional] 
**reuseCardDataFlag** | **Boolean** | Indicate if the card data has to be got from a previous transaction. | [optional] [default to true]
**saleID** | **String** | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol. | [optional] 


