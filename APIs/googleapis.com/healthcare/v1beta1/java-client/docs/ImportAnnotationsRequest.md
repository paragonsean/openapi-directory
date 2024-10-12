

# ImportAnnotationsRequest

Request to import Annotations. The Annotations to be imported must have client-supplied resource names which indicate the annotation resource. The import operation is not atomic. If a failure occurs, any annotations already imported are not removed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcsSource** | [**GoogleCloudHealthcareV1beta1AnnotationGcsSource**](GoogleCloudHealthcareV1beta1AnnotationGcsSource.md) |  |  [optional] |



