

# NewInvoice

New invoice to be created

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**companyIDFK** | **Integer** | If left blank then you must specify Company Name. |  [optional] |
|**companyName** | **String** | If left blank then you must specify Company ID. Specified Name will be used to match existing customer record. If not matched then it will be used to create a new customer. First Name, Last Name and Email will only be used if it is a new company. If the Company name appears multiple times we will check the email address to find a matching company. If email address doesn&#39;t identify a matching company then the invoice creation will be rejected. |  [optional] |
|**currencyCode** | **String** | Expects ISO Standard 3 character currency code. If left blank the currency will default to account&#39;s currency in general setting. For existing companies this field will be ignored and the invoice will use the currency of the customer. For new customers if the currency is not specified then account currency will be used otherwise the specified currency will be used. |  [optional] |
|**customerPONumber** | **String** | Plain UTF8 text. 100 characters max |  [optional] |
|**dateIssued** | **OffsetDateTime** | If not specified it will use today&#39;s date. The date should be specified as local date. |  [optional] |
|**dueDate** | **OffsetDateTime** | It will be auto calculated based on the payment term and issue date. Due Date must be greater than or equal to Issue Date. If the Due Date is specified then Payment Terms will be set to -1 (Custom) |  [optional] |
|**email** | **String** | Specified value will be used to create a new customer contact only if a new customer is being created. |  [optional] |
|**exchangeRate** | **Double** | Exchange rate is only valid for invoices in currency other than default account currency. If not specified it will get the market rate based on the Date Issued. |  [optional] |
|**firstname** | **String** | Specified value will be used to create a new customer contact only if a new customer is being created. |  [optional] |
|**invoiceNumber** | **String** | Pass any string. If left blank it will use the next number in the auto incrementing sequence. If an integer is passed then the largest integer will be use as the seed to auto generate the next invoice number in the sequence. |  [optional] |
|**invoiceTemplateIDFK** | **Integer** | If left blank the account default invoice template will be used. |  [optional] |
|**lastname** | **String** | Specified value will be used to create a new customer contact only if a new customer is being created. |  [optional] |
|**lineItems** | [**List&lt;NewInvoiceLineItem&gt;**](NewInvoiceLineItem.md) |  |  [optional] |
|**notes** | **String** | Plain UTF8 text. (no HTML). Max 2000 characters |  [optional] |
|**paymentTerms** | **Integer** |  \&quot;If left blank we will set it to customer default. If specified then it must match one of your existing pre configured payment term periods. Your account starts with:  (-1 --- Custom, 0 --- Upon Receipt, 7 --- 7 Days, 15 --- 15 Days, 30 --- 30 Days, 45 --- 45 Days, 60 --- 60 Days) |  [optional] |
|**subject** | **String** | Plain UTF8 text. (no HTML). 255 characters max |  [optional] |
|**transactionPrefix** | **String** | A prefix for the Invoice number. e.g. &#39;INV&#39;. If left blank it will be set to the account default. Max length 20 characters. |  [optional] |
|**transactionTaxConfigCode** | **String** | Possible values are (EX --- Tax Exclusive, INC --- Tax Inclusive). If left empty it will use the account default. |  [optional] |



