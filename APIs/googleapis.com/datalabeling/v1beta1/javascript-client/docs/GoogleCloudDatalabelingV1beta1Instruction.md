# DataLabelingApi.GoogleCloudDatalabelingV1beta1Instruction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockingResources** | **[String]** | Output only. The names of any related resources that are blocking changes to the instruction. | [optional] 
**createTime** | **String** | Output only. Creation time of instruction. | [optional] 
**csvInstruction** | [**GoogleCloudDatalabelingV1beta1CsvInstruction**](GoogleCloudDatalabelingV1beta1CsvInstruction.md) |  | [optional] 
**dataType** | **String** | Required. The data type of this instruction. | [optional] 
**description** | **String** | Optional. User-provided description of the instruction. The description can be up to 10000 characters long. | [optional] 
**displayName** | **String** | Required. The display name of the instruction. Maximum of 64 characters. | [optional] 
**name** | **String** | Output only. Instruction resource name, format: projects/{project_id}/instructions/{instruction_id} | [optional] 
**pdfInstruction** | [**GoogleCloudDatalabelingV1beta1PdfInstruction**](GoogleCloudDatalabelingV1beta1PdfInstruction.md) |  | [optional] 
**updateTime** | **String** | Output only. Last update time of instruction. | [optional] 



## Enum: DataTypeEnum


* `DATA_TYPE_UNSPECIFIED` (value: `"DATA_TYPE_UNSPECIFIED"`)

* `IMAGE` (value: `"IMAGE"`)

* `VIDEO` (value: `"VIDEO"`)

* `TEXT` (value: `"TEXT"`)

* `GENERAL_DATA` (value: `"GENERAL_DATA"`)




