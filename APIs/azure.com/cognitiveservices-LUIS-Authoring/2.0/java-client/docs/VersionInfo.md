

# VersionInfo

Object model of an application version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignedEndpointKey** | **Map&lt;String, String&gt;** | The endpoint key. |  [optional] |
|**createdDateTime** | **OffsetDateTime** | The version&#39;s creation timestamp. |  [optional] |
|**endpointHitsCount** | **Integer** | Number of calls made to this endpoint. |  [optional] |
|**endpointUrl** | **String** | The Runtime endpoint URL for this model version. |  [optional] |
|**entitiesCount** | **Integer** | Number of entities in this model. |  [optional] |
|**externalApiKeys** | **Object** | External keys. |  [optional] |
|**intentsCount** | **Integer** | Number of intents in this model. |  [optional] |
|**lastModifiedDateTime** | **OffsetDateTime** | Timestamp of the last update. |  [optional] |
|**lastPublishedDateTime** | **OffsetDateTime** | Timestamp when was last published. |  [optional] |
|**lastTrainedDateTime** | **OffsetDateTime** | Timestamp of the last time the model was trained. |  [optional] |
|**trainingStatus** | [**TrainingStatusEnum**](#TrainingStatusEnum) | The current training status. |  |
|**version** | **String** | The version ID. E.g.: \&quot;0.1\&quot; |  |



## Enum: TrainingStatusEnum

| Name | Value |
|---- | -----|
| NEEDS_TRAINING | &quot;NeedsTraining&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| TRAINED | &quot;Trained&quot; |



