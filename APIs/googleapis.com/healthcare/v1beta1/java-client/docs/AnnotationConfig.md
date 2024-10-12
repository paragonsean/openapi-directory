

# AnnotationConfig

Specifies how to store annotations during de-identification operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationStoreName** | **String** | The name of the annotation store, in the form &#x60;projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/annotationStores/{annotation_store_id}&#x60;). * The destination annotation store must be in the same project as the source data. De-identifying data across multiple projects is not supported. * The destination annotation store must exist when using DeidentifyDicomStore or DeidentifyFhirStore. DeidentifyDataset automatically creates the destination annotation store. |  [optional] |
|**storeQuote** | **Boolean** | If set to true, the sensitive texts are included in SensitiveTextAnnotation of Annotation. |  [optional] |



