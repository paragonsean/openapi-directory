# AvazaApiDocumentation.NewEstimate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**companyIDFK** | **Number** | If left blank then you must specify Company Name. | [optional] 
**companyName** | **String** | If left blank then you must specify Company ID. Specified Name will be used to match existing customer record. If not matched then it will be used to create a new customer. First Name, Last Name and Email will only be used if it is a new company. If the Company name appears multiple times we will check the email address to find a matching company. If email address doesn&#39;t identify a matching company then the Estimate creation will be rejected. | [optional] 
**currencyCode** | **String** | Expects ISO Standard 3 character currency code. If left blank the currency will default to account&#39;s currency in general setting. For existing companies this field will be ignored and the Estimate will use the currency of the customer. For new customers if the currency is not specified then account currency will be used otherwise the specified currency will be used. | [optional] 
**customerPONumber** | **String** | Plain UTF8 text. 100 characters max | [optional] 
**dateIssued** | **Date** | If not specified it will use today&#39;s date. The date should be specified as local date. | [optional] 
**dueDate** | **Date** | It will be auto calculated based on the payment term and issue date. Due Date must be greater than or equal to Issue Date. If the Due Date is specified then Payment Terms will be set to -1 (Custom) | [optional] 
**email** | **String** | Specified value will be used to create a new customer contact only if a new customer is being created. | [optional] 
**estimateNumber** | **String** | Pass any string. If left blank it will use the next number in the auto incrementing sequence. If an integer is passed then the largest integer will be use as the seed to auto generate the next Estimate number in the sequence. | [optional] 
**estimatePrefix** | **String** | A prefix for the Estimate number. e.g. &#39;INV&#39;. If left blank it will be set to the account default. Max length 20 characters. | [optional] 
**estimateTaxConfigCode** | **String** | Possible values are (EX --- Tax Exclusive, INC --- Tax Inclusive). If left empty it will use the account default. | [optional] 
**exchangeRate** | **Number** | Exchange rate is only valid for Estimates in currency other than default account currency. If not specified it will get the market rate based on the Date Issued. | [optional] 
**firstname** | **String** | Specified value will be used to create a new customer contact only if a new customer is being created. | [optional] 
**invoiceTemplateIDFK** | **Number** | If left blank the account default Estimate template will be used. | [optional] 
**lastname** | **String** | Specified value will be used to create a new customer contact only if a new customer is being created. | [optional] 
**lineItems** | [**[NewEstimateLineItem]**](NewEstimateLineItem.md) |  | [optional] 
**notes** | **String** | Plain UTF8 text. (no HTML). Max 2000 characters | [optional] 
**subject** | **String** | Plain UTF8 text. (no HTML). 255 characters max | [optional] 


