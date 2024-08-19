# BillPaymentValidator.BillPayAccountValidation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | Consumer account number populated in the message.  The minimum length is 8 and the maximum length is 22. | [optional] 
**billerId** | **String** | Biller ID populated in the message. The maximum length is 10. | [optional] 
**customerIdentifier1** | **String** | Consumer identifier populated in the message. | [optional] 
**customerIdentifier2** | **String** | Consumer identifier populated in the message. | [optional] 
**customerIdentifier3** | **String** | Consumer identifier populated in the message. | [optional] 
**customerIdentifier4** | **String** | Consumer identifier populated in the message. | [optional] 
**responseString** | **String** | Indicates if the bill payment transaction information passed all RPPS transaction processing edits for the specified biller ID or indicates errors. The minimum length is 0 and the maximum length is 120. | [optional] 
**rppsId** | **String** | Originator RPPS ID populated in the message.  The maximum length is 8. | [optional] 
**transactionAmount** | **String** | Amount populated in the message. | [optional] 


