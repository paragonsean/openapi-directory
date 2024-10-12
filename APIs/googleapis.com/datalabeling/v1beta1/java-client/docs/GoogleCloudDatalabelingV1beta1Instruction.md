

# GoogleCloudDatalabelingV1beta1Instruction

Instruction of how to perform the labeling task for human operators. Currently only PDF instruction is supported.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockingResources** | **List&lt;String&gt;** | Output only. The names of any related resources that are blocking changes to the instruction. |  [optional] |
|**createTime** | **String** | Output only. Creation time of instruction. |  [optional] |
|**csvInstruction** | [**GoogleCloudDatalabelingV1beta1CsvInstruction**](GoogleCloudDatalabelingV1beta1CsvInstruction.md) |  |  [optional] |
|**dataType** | [**DataTypeEnum**](#DataTypeEnum) | Required. The data type of this instruction. |  [optional] |
|**description** | **String** | Optional. User-provided description of the instruction. The description can be up to 10000 characters long. |  [optional] |
|**displayName** | **String** | Required. The display name of the instruction. Maximum of 64 characters. |  [optional] |
|**name** | **String** | Output only. Instruction resource name, format: projects/{project_id}/instructions/{instruction_id} |  [optional] |
|**pdfInstruction** | [**GoogleCloudDatalabelingV1beta1PdfInstruction**](GoogleCloudDatalabelingV1beta1PdfInstruction.md) |  |  [optional] |
|**updateTime** | **String** | Output only. Last update time of instruction. |  [optional] |



## Enum: DataTypeEnum

| Name | Value |
|---- | -----|
| DATA_TYPE_UNSPECIFIED | &quot;DATA_TYPE_UNSPECIFIED&quot; |
| IMAGE | &quot;IMAGE&quot; |
| VIDEO | &quot;VIDEO&quot; |
| TEXT | &quot;TEXT&quot; |
| GENERAL_DATA | &quot;GENERAL_DATA&quot; |



