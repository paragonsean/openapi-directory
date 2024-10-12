

# SalesDataTransactionInterface

Transaction interface. A transaction is an interaction between a merchant and a customer such as a purchase, a credit, a refund, and so on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalInformation** | **List&lt;String&gt;** | Array of additional information. Otherwise, null. |  [optional] |
|**childTransactions** | [**List&lt;SalesDataTransactionInterface&gt;**](SalesDataTransactionInterface.md) | Array of child transactions. |  |
|**createdAt** | **String** | Created-at timestamp. |  |
|**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\TransactionInterface |  [optional] |
|**isClosed** | **Integer** | Is-closed flag value. |  |
|**orderId** | **Integer** | Order ID. |  |
|**parentId** | **Integer** | The parent ID for the transaction. Otherwise, null. |  [optional] |
|**parentTxnId** | **String** | Parent transaction business ID. |  |
|**paymentId** | **Integer** | Payment ID. |  |
|**transactionId** | **Integer** | Transaction ID. |  |
|**txnId** | **String** | Transaction business ID. |  |
|**txnType** | **String** | Transaction type. |  |



