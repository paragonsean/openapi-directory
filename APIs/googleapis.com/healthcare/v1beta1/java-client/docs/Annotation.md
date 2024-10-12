

# Annotation

An annotation record.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationSource** | [**AnnotationSource**](AnnotationSource.md) |  |  [optional] |
|**customData** | **Map&lt;String, String&gt;** | Additional information for this annotation record, such as annotator and verifier information or study campaign. |  [optional] |
|**imageAnnotation** | [**ImageAnnotation**](ImageAnnotation.md) |  |  [optional] |
|**name** | **String** | Identifier. Resource name of the Annotation, of the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}/annotations/{annotation_id}&#x60;. |  [optional] |
|**resourceAnnotation** | [**ResourceAnnotation**](ResourceAnnotation.md) |  |  [optional] |
|**textAnnotation** | [**SensitiveTextAnnotation**](SensitiveTextAnnotation.md) |  |  [optional] |



