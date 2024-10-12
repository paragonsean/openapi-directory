

# MetadataExport

The details of a metadata export operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseDumpType** | [**DatabaseDumpTypeEnum**](#DatabaseDumpTypeEnum) | Output only. The type of the database dump. |  [optional] [readonly] |
|**destinationGcsUri** | **String** | Output only. A Cloud Storage URI of a folder that metadata are exported to, in the form of gs:////, where is automatically generated. |  [optional] [readonly] |
|**endTime** | **String** | Output only. The time when the export ended. |  [optional] [readonly] |
|**startTime** | **String** | Output only. The time when the export started. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the export. |  [optional] [readonly] |



## Enum: DatabaseDumpTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| MYSQL | &quot;MYSQL&quot; |
| AVRO | &quot;AVRO&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |



