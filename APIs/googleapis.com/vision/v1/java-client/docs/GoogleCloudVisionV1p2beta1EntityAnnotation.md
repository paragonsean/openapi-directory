

# GoogleCloudVisionV1p2beta1EntityAnnotation

Set of detected entity features.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boundingPoly** | [**GoogleCloudVisionV1p2beta1BoundingPoly**](GoogleCloudVisionV1p2beta1BoundingPoly.md) |  |  [optional] |
|**confidence** | **Float** | **Deprecated. Use &#x60;score&#x60; instead.** The accuracy of the entity detection in an image. For example, for an image in which the \&quot;Eiffel Tower\&quot; entity is detected, this field represents the confidence that there is a tower in the query image. Range [0, 1]. |  [optional] |
|**description** | **String** | Entity textual description, expressed in its &#x60;locale&#x60; language. |  [optional] |
|**locale** | **String** | The language code for the locale in which the entity textual &#x60;description&#x60; is expressed. |  [optional] |
|**locations** | [**List&lt;GoogleCloudVisionV1p2beta1LocationInfo&gt;**](GoogleCloudVisionV1p2beta1LocationInfo.md) | The location information for the detected entity. Multiple &#x60;LocationInfo&#x60; elements can be present because one location may indicate the location of the scene in the image, and another location may indicate the location of the place where the image was taken. Location information is usually present for landmarks. |  [optional] |
|**mid** | **String** | Opaque entity ID. Some IDs may be available in [Google Knowledge Graph Search API](https://developers.google.com/knowledge-graph/). |  [optional] |
|**properties** | [**List&lt;GoogleCloudVisionV1p2beta1Property&gt;**](GoogleCloudVisionV1p2beta1Property.md) | Some entities may have optional user-supplied &#x60;Property&#x60; (name/value) fields, such a score or string that qualifies the entity. |  [optional] |
|**score** | **Float** | Overall score of the result. Range [0, 1]. |  [optional] |
|**topicality** | **Float** | The relevancy of the ICA (Image Content Annotation) label to the image. For example, the relevancy of \&quot;tower\&quot; is likely higher to an image containing the detected \&quot;Eiffel Tower\&quot; than to an image containing a detected distant towering building, even though the confidence that there is a tower in each image may be the same. Range [0, 1]. |  [optional] |



