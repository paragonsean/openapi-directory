# CloudSpannerApi.DiagnosticMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**metric** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**metricSpecific** | **Boolean** | Whether this message is specific only for the current metric. By default Diagnostics are shown for all metrics, regardless which metric is the currently selected metric in the UI. However occasionally a metric will generate so many messages that the resulting visual clutter becomes overwhelming. In this case setting this to true, will show the diagnostic messages for that metric only if it is the currently selected metric. | [optional] 
**severity** | **String** | The severity of the diagnostic message. | [optional] 
**shortMessage** | [**LocalizedString**](LocalizedString.md) |  | [optional] 



## Enum: SeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `INFO` (value: `"INFO"`)

* `WARNING` (value: `"WARNING"`)

* `ERROR` (value: `"ERROR"`)

* `FATAL` (value: `"FATAL"`)




