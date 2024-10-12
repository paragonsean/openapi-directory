

# ExportDicomDataRequest

Exports data from the specified DICOM store. If a given resource, such as a DICOM object with the same SOPInstance UID, already exists in the output, it is overwritten with the version in the source dataset. Exported DICOM data persists when the DICOM store from which it was exported is deleted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryDestination** | [**GoogleCloudHealthcareV1beta1DicomBigQueryDestination**](GoogleCloudHealthcareV1beta1DicomBigQueryDestination.md) |  |  [optional] |
|**filterConfig** | [**DicomFilterConfig**](DicomFilterConfig.md) |  |  [optional] |
|**gcsDestination** | [**GoogleCloudHealthcareV1beta1DicomGcsDestination**](GoogleCloudHealthcareV1beta1DicomGcsDestination.md) |  |  [optional] |



