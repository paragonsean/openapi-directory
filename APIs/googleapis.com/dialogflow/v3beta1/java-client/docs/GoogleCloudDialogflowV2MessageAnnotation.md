

# GoogleCloudDialogflowV2MessageAnnotation

Represents the result of annotation for the message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containEntities** | **Boolean** | Indicates whether the text message contains entities. |  [optional] |
|**parts** | [**List&lt;GoogleCloudDialogflowV2AnnotatedMessagePart&gt;**](GoogleCloudDialogflowV2AnnotatedMessagePart.md) | The collection of annotated message parts ordered by their position in the message. You can recover the annotated message by concatenating [AnnotatedMessagePart.text]. |  [optional] |



