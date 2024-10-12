# CallFireApiDocumentation.AddContactListContactsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactIds** | **[Number]** | A list of ids of existing contacts in CallFire system | [optional] 
**contactNumbers** | **[String]** | A phone number in E.164 format (11-digit). Examples: 12132000384 | [optional] 
**contactNumbersField** | **String** | A type of phone number (homePhone, workPhone, mobilePhone). This parameter works together with contactNumbers and specifies which types of numbers are included to a list | [optional] 
**contacts** | [**[Contact]**](Contact.md) | A list of new contact objects which need to be added | [optional] 
**useCustomFields** | **Boolean** | A flag to indicate how to define property names for contacts. If true, uses the field and property names exactly as defined. If false will assign custom properties and fields to A, B, C, etc | [optional] 


