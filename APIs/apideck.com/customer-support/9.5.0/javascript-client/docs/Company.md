# CustomerSupport.Company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abnBranch** | **String** | An ABN Branch (also known as a GST Branch) is used if part of your business needs to account for GST separately from its parent entity. | [optional] 
**abnOrTfn** | **String** | An ABN is necessary for operating a business, while a TFN (Tax File Number) is required for any person working in Australia. | [optional] 
**acn** | **String** | The Australian Company Number (ACN) is a nine digit number with the last digit being a check digit calculated using a modified modulus 10 calculation. ASIC has adopted a convention of always printing and displaying the ACN in the format XXX XXX XXX; three blocks of three characters, each block separated by a blank. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**annualRevenue** | **String** | Annual revenue | [optional] 
**bankAccounts** | [**[BankAccount]**](BankAccount.md) |  | [optional] 
**birthday** | **Date** | The date of birth of the person. | [optional] 
**createdAt** | **Date** |  | [optional] [readonly] 
**createdBy** | **String** |  | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customFields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**deleted** | **Boolean** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**emails** | [**[Email]**](Email.md) |  | [optional] 
**fax** | **String** |  | [optional] 
**firstName** | **String** | The first name of the person. | [optional] 
**id** | **String** |  | [optional] [readonly] 
**image** | **String** |  | [optional] 
**industry** | **String** | Industry | [optional] 
**interactionCount** | **Number** |  | [optional] [readonly] 
**lastActivityAt** | **Date** |  | [optional] [readonly] 
**lastName** | **String** | The last name of the person. | [optional] 
**name** | **String** |  | 
**numberOfEmployees** | **String** | Number of employees | [optional] 
**ownerId** | **String** |  | [optional] 
**ownership** | **String** | Ownership | [optional] 
**parentId** | **String** | Parent ID | [optional] [readonly] 
**payeeNumber** | **String** |  | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**readOnly** | **Boolean** |  | [optional] 
**rowType** | [**CompanyRowType**](CompanyRowType.md) |  | [optional] 
**salesTaxNumber** | **String** |  | [optional] 
**salutation** | **String** | A formal salutation for the person. For example, &#39;Mr&#39;, &#39;Mrs&#39; | [optional] 
**socialLinks** | [**[SocialLink]**](SocialLink.md) |  | [optional] 
**status** | **String** |  | [optional] 
**tags** | **[String]** |  | [optional] 
**updatedAt** | **Date** |  | [optional] [readonly] 
**updatedBy** | **String** |  | [optional] [readonly] 
**vatNumber** | **String** | VAT number | [optional] 
**websites** | [**[Website]**](Website.md) |  | [optional] 


