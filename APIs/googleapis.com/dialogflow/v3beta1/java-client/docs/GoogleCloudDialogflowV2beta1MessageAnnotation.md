

# GoogleCloudDialogflowV2beta1MessageAnnotation

Represents the result of annotation for the message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containEntities** | **Boolean** | Required. Indicates whether the text message contains entities. |  [optional] |
|**parts** | [**List&lt;GoogleCloudDialogflowV2beta1AnnotatedMessagePart&gt;**](GoogleCloudDialogflowV2beta1AnnotatedMessagePart.md) | Optional. The collection of annotated message parts ordered by their position in the message. You can recover the annotated message by concatenating [AnnotatedMessagePart.text]. |  [optional] |



