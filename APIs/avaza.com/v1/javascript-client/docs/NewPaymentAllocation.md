# AvazaApiDocumentation.NewPaymentAllocation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationAmount** | **Number** | The Amount being allocated to the invoice. Expects same currency as invoice currency | [optional] 
**allocationDate** | **Date** | Optional. Defaults to the current time in the Avaza account&#39;s timezone. The date the allocation is applied to the invoice. Can be difference from the Payment Date when doing prepayments etc. | [optional] 
**invoiceTransactionIDFK** | **Number** | The Avaza Invoice TransactionID that is having a payment amount allocated to it. | [optional] 


