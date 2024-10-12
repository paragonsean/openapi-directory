

# AutoExportSettings

Settings for the auto export functionality of a meter

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exportFormat** | **String** | The export format |  [optional] |
|**exportInterval** | [**ExportIntervalEnum**](#ExportIntervalEnum) | The export interval of the auto export |  [optional] |
|**meterPointId** | **String** | The meter point id set by the user |  [optional] |
|**uploadType** | **String** | The upload type |  [optional] |



## Enum: ExportIntervalEnum

| Name | Value |
|---- | -----|
| NO_EXPORT | &quot;NoExport&quot; |
| HOURLY | &quot;Hourly&quot; |
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |
| MONTHLY | &quot;Monthly&quot; |
| QUATER_YEARLY | &quot;QuaterYearly&quot; |
| HALF_YEARLY | &quot;HalfYearly&quot; |
| YEARLY | &quot;Yearly&quot; |



