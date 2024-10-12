# MagentoB2B.SalesDataTransactionInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalInformation** | **[String]** | Array of additional information. Otherwise, null. | [optional] 
**childTransactions** | [**[SalesDataTransactionInterface]**](SalesDataTransactionInterface.md) | Array of child transactions. | 
**createdAt** | **String** | Created-at timestamp. | 
**extensionAttributes** | **Object** | ExtensionInterface class for @see \\Magento\\Sales\\Api\\Data\\TransactionInterface | [optional] 
**isClosed** | **Number** | Is-closed flag value. | 
**orderId** | **Number** | Order ID. | 
**parentId** | **Number** | The parent ID for the transaction. Otherwise, null. | [optional] 
**parentTxnId** | **String** | Parent transaction business ID. | 
**paymentId** | **Number** | Payment ID. | 
**transactionId** | **Number** | Transaction ID. | 
**txnId** | **String** | Transaction business ID. | 
**txnType** | **String** | Transaction type. | 


