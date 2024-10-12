# HrisApi.HrisCompany

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**companyNumber** | **String** | An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company. | [optional] 
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**createdBy** | **String** | The user who created the object. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**debtorId** | **String** |  | [optional] 
**deleted** | **Boolean** |  | [optional] [readonly] 
**displayName** | **String** |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**id** | **String** | A unique identifier for an object. | [optional] [readonly] 
**legalName** | **String** |  | 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**status** | **String** |  | [optional] 
**subdomain** | **String** |  | [optional] 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The user who last updated the object. | [optional] [readonly] 
**websites** | [**[Website]**](Website.md) |  | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `trial` (value: `"trial"`)

* `other` (value: `"other"`)




