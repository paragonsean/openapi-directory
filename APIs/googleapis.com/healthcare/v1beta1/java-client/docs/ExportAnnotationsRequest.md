

# ExportAnnotationsRequest

Request to export Annotations. The export operation is not atomic. If a failure occurs, any annotations already exported are not removed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryDestination** | [**GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination**](GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination.md) |  |  [optional] |
|**gcsDestination** | [**GoogleCloudHealthcareV1beta1AnnotationGcsDestination**](GoogleCloudHealthcareV1beta1AnnotationGcsDestination.md) |  |  [optional] |



