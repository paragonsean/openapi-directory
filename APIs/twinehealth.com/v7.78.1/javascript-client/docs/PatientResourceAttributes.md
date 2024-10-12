# FitbitPlusApi.PatientResourceAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**archiveHistory** | [**[ArchiveHistory]**](ArchiveHistory.md) |  | [optional] 
**archived** | **Boolean** |  | [optional] [readonly] 
**birthDate** | **Date** |  | [optional] 
**emailAddress** | **String** |  | [optional] 
**enrolledAt** | **String** |  | [optional] [readonly] 
**firstAccessAt** | **String** |  | [optional] [readonly] 
**firstName** | **String** |  | [optional] 
**gender** | **String** |  | [optional] 
**identifiers** | [**[PatientIdentifier]**](PatientIdentifier.md) |  | [optional] 
**invitedAt** | **String** |  | [optional] [readonly] 
**lastAccessAt** | **String** |  | [optional] [readonly] 
**lastName** | **String** |  | [optional] 
**note** | **String** | Coach&#39;s note about the patient. Not visible to the patient. | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**statement** | [**PatientResourceAttributesStatement**](PatientResourceAttributesStatement.md) |  | [optional] 
**updatedAt** | **String** |  | [optional] [readonly] 



## Enum: GenderEnum


* `male` (value: `"male"`)

* `female` (value: `"female"`)

* `other` (value: `"other"`)




