# GoToTraining.TrainingReqCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the training | [optional] 
**name** | **String** | Name of the training | 
**organizers** | **[Number]** | List of keys of the co-organizers for this training | [optional] 
**registrationSettings** | [**RegistrationSettings**](RegistrationSettings.md) |  | [optional] 
**timeZone** | **String** | Time zone of the training. (Must be a valid time zone ID, see https://goto-developer.logmein.com/time-zones) | 
**times** | [**[DateTimeRange]**](DateTimeRange.md) | Array with startDate and endDate for the training sessions | 


