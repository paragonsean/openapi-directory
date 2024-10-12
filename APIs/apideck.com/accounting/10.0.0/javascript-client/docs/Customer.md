# AccountingApi.Customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**LinkedLedgerAccount**](LinkedLedgerAccount.md) |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**bankAccounts** | [**[BankAccount]**](BankAccount.md) |  | [optional] 
**channel** | **String** | The channel through which the transaction is processed. | [optional] 
**companyName** | **String** | The name of the company. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**displayId** | **String** | Display ID | [optional] 
**displayName** | **String** | Display name | [optional] 
**downstreamId** | **String** | The third-party API ID of original entity | [optional] [readonly] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**firstName** | **String** | The first name of the person. | [optional] 
**id** | **String** | A unique identifier for an object. | [readonly] 
**individual** | **Boolean** | Is this an individual or business customer | [optional] 
**lastName** | **String** | The last name of the person. | [optional] 
**middleName** | **String** | Middle name of the person. | [optional] 
**notes** | **String** | Some notes about this customer | [optional] 
**parent** | [**LinkedParentCustomer**](LinkedParentCustomer.md) |  | [optional] 
**paymentMethod** | **String** | Payment method used for the transaction, such as cash, credit card, bank transfer, or check | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**project** | **Boolean** | If true, indicates this is a Project. | [optional] 
**rowVersion** | **String** | A binary value used to detect updates to a object and prevent data conflicts. It is incremented each time an update is made to the object. | [optional] 
**status** | **String** | Customer status | [optional] 
**suffix** | **String** |  | [optional] 
**taxNumber** | **String** |  | [optional] 
**taxRate** | [**LinkedTaxRate**](LinkedTaxRate.md) |  | [optional] 
**title** | **String** | The job title of the person. | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 
**websites** | [**[Website]**](Website.md) |  | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `archived` (value: `"archived"`)

* `gdpr-erasure-request` (value: `"gdpr-erasure-request"`)

* `unknown` (value: `"unknown"`)




