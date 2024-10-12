

# GoogleCloudContactcenterinsightsV1alpha1Entity

The data for an entity annotation. Represents a phrase in the conversation that is a known entity, such as a person, an organization, or location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The representative name for the entity. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Metadata associated with the entity. For most entity types, the metadata is a Wikipedia URL (&#x60;wikipedia_url&#x60;) and Knowledge Graph MID (&#x60;mid&#x60;), if they are available. For the metadata associated with other entity types, see the Type table below. |  [optional] |
|**salience** | **Float** | The salience score associated with the entity in the [0, 1.0] range. The salience score for an entity provides information about the importance or centrality of that entity to the entire document text. Scores closer to 0 are less salient, while scores closer to 1.0 are highly salient. |  [optional] |
|**sentiment** | [**GoogleCloudContactcenterinsightsV1alpha1SentimentData**](GoogleCloudContactcenterinsightsV1alpha1SentimentData.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The entity type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| PERSON | &quot;PERSON&quot; |
| LOCATION | &quot;LOCATION&quot; |
| ORGANIZATION | &quot;ORGANIZATION&quot; |
| EVENT | &quot;EVENT&quot; |
| WORK_OF_ART | &quot;WORK_OF_ART&quot; |
| CONSUMER_GOOD | &quot;CONSUMER_GOOD&quot; |
| OTHER | &quot;OTHER&quot; |
| PHONE_NUMBER | &quot;PHONE_NUMBER&quot; |
| ADDRESS | &quot;ADDRESS&quot; |
| DATE | &quot;DATE&quot; |
| NUMBER | &quot;NUMBER&quot; |
| PRICE | &quot;PRICE&quot; |



