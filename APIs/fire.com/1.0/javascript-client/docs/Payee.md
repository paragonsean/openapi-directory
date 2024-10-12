# FireFinancialServicesBusinessApi.Payee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderName** | **String** | The name on the payee bank account. | [optional] 
**accountName** | **String** | The alias attributed to the payee, usually set by the user when creating the payee. | [optional] 
**accountNumber** | **String** | The Account Number of the account if currency is GBP. | [optional] 
**bic** | **String** | The BIC of the account if currency is EUR. | [optional] 
**createdBy** | **String** | The creation source of the payee. | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**dateCreated** | **Date** | The date the payee was created. ISO Date Time. | [optional] 
**iban** | **String** | The IBAN of the account if currency is EUR. | [optional] 
**id** | **Number** | Identifier for the fire.com payee bank account (assigned by fire.com). | [optional] 
**nsc** | **String** | The Sort Code of the account if currency is GBP. | [optional] 
**status** | **String** | The status of the payee. Only payees in LIVE status can be selected as a destination account for an outgoing payment.   * &#39;CREATED&#39; - The payee has been set-up via Bank Transfer Received, Direct Debit, or Open Banking. This payee must be converted to LIVE status to select as a destination account for an outgoing payment.   * &#39;LIVE&#39; - The payee can be selected as a destination account for an outgoing payment.   * &#39;CLOSED&#39;   * &#39;ARCHIVED&#39; - The payee has been deleted and must be added again to be selected as a destination account for an outgoing payment.  | [optional] 



## Enum: CreatedByEnum


* `CUSTOMER` (value: `"CUSTOMER"`)

* `LODGEMENT` (value: `"LODGEMENT"`)

* `DIRECT DEBIT` (value: `"DIRECT DEBIT"`)

* `OPEN BANKING` (value: `"OPEN BANKING"`)

* `FIRE OPEN PAYMENT` (value: `"FIRE OPEN PAYMENT"`)

* `FIRE DIRECT` (value: `"FIRE DIRECT"`)





## Enum: StatusEnum


* `CREATED` (value: `"CREATED"`)

* `LIVE` (value: `"LIVE"`)

* `CLOSED` (value: `"CLOSED"`)

* `ARCHIVED` (value: `"ARCHIVED"`)




