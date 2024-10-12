

# CreateSbomExportRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportFormat** | [**ReportFormatEnum**](#ReportFormatEnum) | The output format for the software bill of materials (SBOM) report. |  |
|**resourceFilterCriteria** | [**CreateSbomExportRequestResourceFilterCriteria**](CreateSbomExportRequestResourceFilterCriteria.md) |  |  [optional] |
|**s3Destination** | [**CreateFindingsReportRequestS3Destination**](CreateFindingsReportRequestS3Destination.md) |  |  |



## Enum: ReportFormatEnum

| Name | Value |
|---- | -----|
| CYCLONEDX_1_4 | &quot;CYCLONEDX_1_4&quot; |
| SPDX_2_3 | &quot;SPDX_2_3&quot; |



