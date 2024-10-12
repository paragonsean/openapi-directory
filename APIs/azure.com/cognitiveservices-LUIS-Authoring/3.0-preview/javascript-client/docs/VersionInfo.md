# LuisAuthoringClient.VersionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignedEndpointKey** | **{String: String}** | The endpoint key. | [optional] 
**createdDateTime** | **Date** | The version&#39;s creation timestamp. | [optional] 
**endpointHitsCount** | **Number** | Number of calls made to this endpoint. | [optional] 
**endpointUrl** | **String** | The Runtime endpoint URL for this model version. | [optional] 
**entitiesCount** | **Number** | Number of entities in this model. | [optional] 
**externalApiKeys** | **Object** | External keys. | [optional] 
**intentsCount** | **Number** | Number of intents in this model. | [optional] 
**lastModifiedDateTime** | **Date** | Timestamp of the last update. | [optional] 
**lastPublishedDateTime** | **Date** | Timestamp when was last published. | [optional] 
**lastTrainedDateTime** | **Date** | Timestamp of the last time the model was trained. | [optional] 
**trainingStatus** | **String** | The current training status. | 
**version** | **String** | The version ID. E.g.: \&quot;0.1\&quot; | 



## Enum: TrainingStatusEnum


* `NeedsTraining` (value: `"NeedsTraining"`)

* `InProgress` (value: `"InProgress"`)

* `Trained` (value: `"Trained"`)




