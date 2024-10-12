# CustomerSupport.Contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** |  | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**birthday** | **String** |  | [optional] 
**companyId** | **String** |  | [optional] 
**companyName** | **String** |  | [optional] 
**createdAt** | **Date** |  | [optional] [readonly] 
**currentBalance** | **Number** |  | [optional] 
**customFields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**department** | **String** |  | [optional] 
**description** | **String** |  | [optional] 
**emailDomain** | **String** |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**fax** | **String** |  | [optional] 
**firstCallAt** | **Date** |  | [optional] [readonly] 
**firstEmailAt** | **Date** |  | [optional] [readonly] 
**firstName** | **String** |  | [optional] 
**gender** | **String** |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**image** | **String** |  | [optional] 
**language** | **String** | language code according to ISO 639-1. For the United States - EN | [optional] 
**lastActivityAt** | **Date** |  | [optional] [readonly] 
**lastName** | **String** |  | [optional] 
**leadId** | **String** |  | [optional] 
**leadSource** | **String** |  | [optional] 
**middleName** | **String** |  | [optional] 
**name** | **String** |  | 
**ownerId** | **String** |  | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**photoUrl** | **String** | The URL of the photo of a person. | [optional] 
**prefix** | **String** |  | [optional] 
**socialLinks** | [**[SocialLink]**](SocialLink.md) |  | [optional] 
**status** | **String** |  | [optional] 
**suffix** | **String** |  | [optional] 
**tags** | **[String]** |  | [optional] 
**title** | **String** |  | [optional] 
**type** | **String** |  | [optional] 
**updatedAt** | **Date** |  | [optional] [readonly] 
**websites** | [**[Website]**](Website.md) |  | [optional] 



## Enum: GenderEnum


* `male` (value: `"male"`)

* `female` (value: `"female"`)

* `unisex` (value: `"unisex"`)





## Enum: TypeEnum


* `customer` (value: `"customer"`)

* `supplier` (value: `"supplier"`)

* `employee` (value: `"employee"`)

* `personal` (value: `"personal"`)




