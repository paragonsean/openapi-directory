

# ImportDicomDataRequest

Imports data into the specified DICOM store. Returns an error if any of the files to import are not DICOM files. This API accepts duplicate DICOM instances by ignoring the newly-pushed instance. It does not overwrite.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcsSource** | [**GoogleCloudHealthcareV1DicomGcsSource**](GoogleCloudHealthcareV1DicomGcsSource.md) |  |  [optional] |



