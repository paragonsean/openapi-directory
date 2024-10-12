# DialogflowApi.GoogleCloudDialogflowV2AnnotatedMessagePart

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityType** | **String** | The [Dialogflow system entity type](https://cloud.google.com/dialogflow/docs/reference/system-entities) of this message part. If this is empty, Dialogflow could not annotate the phrase part with a system entity. | [optional] 
**formattedValue** | **Object** | The [Dialogflow system entity formatted value ](https://cloud.google.com/dialogflow/docs/reference/system-entities) of this message part. For example for a system entity of type &#x60;@sys.unit-currency&#x60;, this may contain: { \&quot;amount\&quot;: 5, \&quot;currency\&quot;: \&quot;USD\&quot; }  | [optional] 
**text** | **String** | A part of a message possibly annotated with an entity. | [optional] 


