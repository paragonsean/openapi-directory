# Inspector2.CreateSbomExportRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reportFormat** | **String** | The output format for the software bill of materials (SBOM) report. | 
**resourceFilterCriteria** | [**CreateSbomExportRequestResourceFilterCriteria**](CreateSbomExportRequestResourceFilterCriteria.md) |  | [optional] 
**s3Destination** | [**CreateFindingsReportRequestS3Destination**](CreateFindingsReportRequestS3Destination.md) |  | 



## Enum: ReportFormatEnum


* `CYCLONEDX_1_4` (value: `"CYCLONEDX_1_4"`)

* `SPDX_2_3` (value: `"SPDX_2_3"`)




