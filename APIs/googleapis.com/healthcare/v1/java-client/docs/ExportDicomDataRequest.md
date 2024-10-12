

# ExportDicomDataRequest

Exports data from the specified DICOM store. If a given resource, such as a DICOM object with the same SOPInstance UID, already exists in the output, it is overwritten with the version in the source dataset. Exported DICOM data persists when the DICOM store from which it was exported is deleted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryDestination** | [**GoogleCloudHealthcareV1DicomBigQueryDestination**](GoogleCloudHealthcareV1DicomBigQueryDestination.md) |  |  [optional] |
|**gcsDestination** | [**GoogleCloudHealthcareV1DicomGcsDestination**](GoogleCloudHealthcareV1DicomGcsDestination.md) |  |  [optional] |



