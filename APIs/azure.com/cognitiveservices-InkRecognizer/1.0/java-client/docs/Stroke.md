

# Stroke


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**drawingAttributes** | [**DrawingAttributesPattern**](DrawingAttributesPattern.md) |  |  [optional] |
|**id** | **Integer** | This is treated as a unique identifier for each stroke within a request. If the id is repeated within the same request, the service will return an error. |  |
|**kind** | [**KindEnum**](#KindEnum) | This is an optional property which influences the decision about what the stroke kind is between inkWriting and inkDrawing. This property should be set ONLY if the type of user content is known ahead of time. Not setting this value implies the kind is not known ahead of time. Kind represents the type of content the stroke is a part of. |  [optional] |
|**language** | **String** | The IETF BCP 47 language code (for ex. en-US, en-GB, hi-IN etc.) of the expected language for the handwritten content in this stroke. The response will include results from this language. |  [optional] |
|**points** | [**List&lt;InkPoint&gt;**](InkPoint.md) |  |  |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| INK_DRAWING | &quot;inkDrawing&quot; |
| INK_WRITING | &quot;inkWriting&quot; |



