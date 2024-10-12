

# OriginalPOITransaction

In the Payment or the Loyalty Request message, it allows using the card of a previous CardAcquisition or Payment/Loyalty request. Identification of a previous POI transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acquirerID** | **Integer** | Restrict to these Acquirer if present. |  [optional] |
|**amountValue** | **BigDecimal** |  |  [optional] |
|**approvalCode** | **String** | If referral. |  [optional] |
|**customerLanguage** | **String** | If the language is selected by the Sale System before the request to the POI. |  [optional] |
|**hostTransactionID** | [**TransactionIDType**](TransactionIDType.md) |  |  [optional] |
|**POIID** | **String** | If original transaction is coming from another POI. |  [optional] |
|**poITransactionID** | [**TransactionIDType**](TransactionIDType.md) |  |  [optional] |
|**reuseCardDataFlag** | **Boolean** | Indicate if the card data has to be got from a previous transaction. |  [optional] |
|**saleID** | **String** | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol. |  [optional] |



