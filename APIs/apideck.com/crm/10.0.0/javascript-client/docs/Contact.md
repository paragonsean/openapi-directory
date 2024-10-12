# CrmApi.Contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | The active status of the contact. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**birthday** | **String** | The birthday of the contact. | [optional] 
**companyId** | **String** | The company the contact is associated with. | [optional] 
**companyName** | **String** | The name of the company the contact is associated with. | [optional] 
**createdAt** | **Date** | The creation date of the contact. | [optional] [readonly] 
**currentBalance** | **Number** | The current balance of the contact. | [optional] 
**customFields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**department** | **String** | The department of the contact. | [optional] 
**description** | **String** | The description of the contact. | [optional] 
**emailDomain** | **String** |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**fax** | **String** | The fax number of the contact. | [optional] 
**firstCallAt** | **Date** | The first call date of the contact. | [optional] [readonly] 
**firstEmailAt** | **Date** | The first email date of the contact. | [optional] [readonly] 
**firstName** | **String** | The first name of the contact. | [optional] 
**gender** | **String** | The gender of the contact. | [optional] 
**id** | **String** | Unique identifier for the contact. | [optional] [readonly] 
**image** | **String** |  | [optional] 
**language** | **String** | language code according to ISO 639-1. For the United States - EN | [optional] 
**lastActivityAt** | **Date** | The last activity date of the contact. | [optional] [readonly] 
**lastName** | **String** | The last name of the contact. | [optional] 
**leadId** | **String** | The lead the contact is associated with. | [optional] 
**leadSource** | **String** | The lead source of the contact. | [optional] 
**middleName** | **String** | The middle name of the contact. | [optional] 
**name** | **String** | Full name of the contact. | 
**ownerId** | **String** | The owner of the contact. | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**photoUrl** | **String** | The URL of the photo of a person. | [optional] 
**prefix** | **String** | The prefix of the contact. | [optional] 
**socialLinks** | [**[SocialLink]**](SocialLink.md) |  | [optional] 
**status** | **String** | The status of the contact. | [optional] 
**suffix** | **String** | The suffix of the contact. | [optional] 
**tags** | **[String]** |  | [optional] 
**title** | **String** | The job title of the contact. | [optional] 
**type** | **String** | The type of the contact. | [optional] 
**updatedAt** | **Date** | The last update date of the contact. | [optional] [readonly] 
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




