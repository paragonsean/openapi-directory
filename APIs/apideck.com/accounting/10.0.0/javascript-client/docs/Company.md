# AccountingApi.Company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abnBranch** | **String** | An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity. | [optional] 
**abnOrTfn** | **String** | An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia. | [optional] 
**acn** | **String** | The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**annualRevenue** | **String** | The annual revenue of the company | [optional] 
**bankAccounts** | [**[BankAccount]**](BankAccount.md) |  | [optional] 
**birthday** | **Date** | The date of birth of the person. | [optional] 
**createdAt** | **Date** | Creation date | [optional] [readonly] 
**createdBy** | **String** | Created by user ID | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customFields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**deleted** | **Boolean** | Whether the company is deleted or not | [optional] [readonly] 
**description** | **String** | A description of the company | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**fax** | **String** | The fax number of the company | [optional] 
**firstName** | **String** | The first name of the person. | [optional] 
**id** | **String** | Unique identifier for the company | [optional] [readonly] 
**image** | **String** | The Image URL of the company | [optional] 
**industry** | **String** | The industry represents the type of business the company is in. | [optional] 
**interactionCount** | **Number** | Number of interactions | [optional] [readonly] 
**lastActivityAt** | **Date** | Last activity date | [optional] [readonly] 
**lastName** | **String** | The last name of the person. | [optional] 
**name** | **String** | Name of the company | 
**numberOfEmployees** | **String** | Number of employees | [optional] 
**ownerId** | **String** | Owner ID | [optional] 
**ownership** | **String** | The ownership indicates the type of ownership of the company. | [optional] 
**parentId** | **String** | Parent ID | [optional] [readonly] 
**payeeNumber** | **String** | A payee number is a unique number that identifies a payee for tax purposes. | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**readOnly** | **Boolean** | Whether the company is read-only or not | [optional] 
**rowType** | [**CompanyRowType**](CompanyRowType.md) |  | [optional] 
**salesTaxNumber** | **String** | A sales tax number is a unique number that identifies a company for tax purposes. | [optional] 
**salutation** | **String** | A formal salutation for the person. For example, &#39;Mr&#39;, &#39;Mrs&#39; | [optional] 
**socialLinks** | [**[SocialLink]**](SocialLink.md) |  | [optional] 
**status** | **String** | The status of the company | [optional] 
**tags** | **[String]** |  | [optional] 
**updatedAt** | **Date** | Last updated date | [optional] [readonly] 
**updatedBy** | **String** | Updated by user ID | [optional] [readonly] 
**vatNumber** | **String** | The VAT number of the company | [optional] 
**websites** | [**[Website]**](Website.md) |  | [optional] 


