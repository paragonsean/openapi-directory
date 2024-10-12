# Learnifier.AddUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The name shown when the user is listed | [optional] 
**externalId** | **String** | The external id (foreign key). Must not exceed 255 characters. | [optional] 
**firstName** | **String** | The first (given) name of the user | [optional] 
**hardLock** | **Boolean** | True if the user should be locked from the system | [optional] 
**homeOrg** | **Number** | The primary organization for the user. Must match the id of an Organization Unit. | [optional] 
**lastName** | **Object** | The last name (surname) of the user | [optional] 
**locale** | **String** | The user&#39;s preferred language/locale setting. Affects date and number formatting. | [optional] 
**primaryEmail** | **String** | The primary email for the user. Used for communication from the platform. | [optional] 


