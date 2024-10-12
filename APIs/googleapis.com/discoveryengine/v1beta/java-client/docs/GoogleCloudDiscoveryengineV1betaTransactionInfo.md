

# GoogleCloudDiscoveryengineV1betaTransactionInfo

A transaction represents the entire purchase transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cost** | **Float** | All the costs associated with the products. These can be manufacturing costs, shipping expenses not borne by the end user, or any other costs, such that: * Profit &#x3D; value - tax - cost |  [optional] |
|**currency** | **String** | Required. Currency code. Use three-character ISO-4217 code. |  [optional] |
|**discountValue** | **Float** | The total discount(s) value applied to this transaction. This figure should be excluded from TransactionInfo.value For example, if a user paid TransactionInfo.value amount, then nominal (pre-discount) value of the transaction is the sum of TransactionInfo.value and TransactionInfo.discount_value This means that profit is calculated the same way, regardless of the discount value, and that TransactionInfo.discount_value can be larger than TransactionInfo.value: * Profit &#x3D; value - tax - cost |  [optional] |
|**tax** | **Float** | All the taxes associated with the transaction. |  [optional] |
|**transactionId** | **String** | The transaction ID with a length limit of 128 characters. |  [optional] |
|**value** | **Float** | Required. Total non-zero value associated with the transaction. This value may include shipping, tax, or other adjustments to the total value that you want to include. |  [optional] |



