

# DeveloperMetadataLocation

A location where metadata may be associated in a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensionRange** | [**DimensionRange**](DimensionRange.md) |  |  [optional] |
|**locationType** | [**LocationTypeEnum**](#LocationTypeEnum) | The type of location this object represents. This field is read-only. |  [optional] |
|**sheetId** | **Integer** | The ID of the sheet when metadata is associated with an entire sheet. |  [optional] |
|**spreadsheet** | **Boolean** | True when metadata is associated with an entire spreadsheet. |  [optional] |



## Enum: LocationTypeEnum

| Name | Value |
|---- | -----|
| DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED | &quot;DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED&quot; |
| ROW | &quot;ROW&quot; |
| COLUMN | &quot;COLUMN&quot; |
| SHEET | &quot;SHEET&quot; |
| SPREADSHEET | &quot;SPREADSHEET&quot; |



