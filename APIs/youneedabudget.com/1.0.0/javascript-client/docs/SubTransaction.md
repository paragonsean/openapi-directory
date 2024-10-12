# YnabApiEndpoints.SubTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The subtransaction amount in milliunits format | 
**categoryId** | **String** |  | [optional] 
**categoryName** | **String** |  | [optional] 
**deleted** | **Boolean** | Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests. | 
**id** | **String** |  | 
**memo** | **String** |  | [optional] 
**payeeId** | **String** |  | [optional] 
**payeeName** | **String** |  | [optional] 
**transactionId** | **String** |  | 
**transferAccountId** | **String** | If a transfer, the account_id which the subtransaction transfers to | [optional] 
**transferTransactionId** | **String** | If a transfer, the id of transaction on the other side of the transfer | [optional] 


