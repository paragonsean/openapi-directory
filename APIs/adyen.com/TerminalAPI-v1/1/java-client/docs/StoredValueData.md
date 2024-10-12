

# StoredValueData

It contains: - the identification of the stored value accounts or the stored value cards, if provided by the Sale System, and - the associated products sold by the Sale System.. Data related to the stored value card.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currency** | **String** | Currency of a monetary amount. |  [optional] |
|**eanUpc** | **Integer** | Standard product code of item purchased with the transaction. |  [optional] |
|**itemAmount** | **BigDecimal** | Total amount of the item line. |  [optional] |
|**originalPOITransaction** | [**OriginalPOITransaction**](OriginalPOITransaction.md) |  |  [optional] |
|**productCode** | **Integer** | Product code of item purchased with the transaction. |  [optional] |
|**storedValueAccountID** | [**StoredValueAccountID**](StoredValueAccountID.md) |  |  [optional] |
|**storedValueProvider** | **String** | If more than one provider to manage on the POI, and StoredValueAccountID absent. |  [optional] |
|**storedValueTransactionType** | **StoredValueTransactionType** |  |  |



