# CustomerSupport.CustomerSupportCustomer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**bankAccounts** | [**BankAccount**](BankAccount.md) |  | [optional] 
**companyName** | **String** | The name of the company. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**firstName** | **String** | The first name of the person. | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**individual** | **Boolean** |  | [optional] 
**lastName** | **String** | The last name of the person. | [optional] 
**notes** | **String** |  | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**status** | **String** | Customer status | [optional] 
**taxNumber** | **String** |  | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `archived` (value: `"archived"`)

* `gdpr-erasure-request` (value: `"gdpr-erasure-request"`)

* `unknown` (value: `"unknown"`)




