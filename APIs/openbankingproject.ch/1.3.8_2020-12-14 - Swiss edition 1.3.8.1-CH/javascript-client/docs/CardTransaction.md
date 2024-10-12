# SwissNextGenBankingApiFramework.CardTransaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptorTransactionDateTime** | **Date** | Timestamp of the actual card transaction within the acceptance system | [optional] 
**bookingDate** | **Date** | The date when an entry is posted to an account on the ASPSPs books.  | [optional] 
**cardAcceptorAddress** | [**Address**](Address.md) |  | [optional] 
**cardAcceptorId** | **String** |  | [optional] 
**cardAcceptorPhone** | **String** | Merchant phone number It consists of a \&quot;+\&quot; followed by the country code (from 1 to 3 characters) then a \&quot;-\&quot; and finally, any combination of numbers, \&quot;(\&quot;, \&quot;)\&quot;, \&quot;+\&quot; and \&quot;-\&quot; (up to 30 characters). pattern according to ISO20022 \\+[0-9]{1,3}-[0-9()+\\-]{1,30}  | [optional] 
**cardTransactionId** | **String** | Unique end to end identity. | [optional] 
**currencyExchange** | [**[ReportExchangeRate]**](ReportExchangeRate.md) | Array of exchange rates. | [optional] 
**invoiced** | **Boolean** |  | [optional] 
**markupFee** | [**Amount**](Amount.md) |  | [optional] 
**markupFeePercentage** | **String** |  | [optional] 
**maskedPAN** | **String** | Masked Primary Account Number.  | [optional] 
**merchantCategoryCode** | **String** | Merchant category code. | [optional] 
**originalAmount** | [**Amount**](Amount.md) |  | [optional] 
**proprietaryBankTransactionCode** | **String** | Proprietary bank transaction code as used within a community or within an ASPSP e.g. for MT94x based transaction reports.  | [optional] 
**terminalId** | **String** | Identification of the Terminal, where the card has been used. | [optional] 
**transactionAmount** | [**Amount**](Amount.md) |  | 
**transactionDate** | **Date** | Date of the actual card transaction. | [optional] 
**transactionDetails** | **String** |  | [optional] 


