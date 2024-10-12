# CallFireApiDocumentation.CreateContactListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactIds** | **[Number]** | A list of ids of existing contacts in CallFire system | [optional] 
**contactNumbers** | **[String]** | List of numbers in E.164 format (11-digit). Example: 12132000384 | [optional] 
**contactNumbersField** | **String** | A type of a phone number (homePhone, workPhone, mobilePhone). This parameter is used with contactNumbers and specifies which types of phone numbers are included to a contact list | [optional] 
**contacts** | [**[Contact]**](Contact.md) | A list of new contact objects to be added | [optional] 
**name** | **String** | A name of a contact list | [optional] 
**useCustomFields** | **Boolean** | A flag to indicate how to define property names for contacts. If true, uses the field and property names exactly as defined. If false will assign custom properties and fields to A, B, C, etc | [optional] 


