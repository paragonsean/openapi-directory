# MicrosoftNetApp.VolumePatchProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exportPolicy** | [**VolumePatchPropertiesExportPolicy**](VolumePatchPropertiesExportPolicy.md) |  | [optional] 
**serviceLevel** | **String** | The service level of the file system | [optional] [default to &#39;Premium&#39;]
**usageThreshold** | **Number** | Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. | [optional] [default to 107374182400]



## Enum: ServiceLevelEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)

* `Ultra` (value: `"Ultra"`)




