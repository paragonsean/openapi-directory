# MigrationCenterApi.RunningService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmdline** | **String** | Service command line. | [optional] 
**exePath** | **String** | Service binary path. | [optional] 
**pid** | **String** | Service pid. | [optional] 
**serviceName** | **String** | Service name. | [optional] 
**startMode** | **String** | Service start mode (OS-agnostic). | [optional] 
**state** | **String** | Service state (OS-agnostic). | [optional] 



## Enum: StartModeEnum


* `START_MODE_UNSPECIFIED` (value: `"START_MODE_UNSPECIFIED"`)

* `BOOT` (value: `"BOOT"`)

* `SYSTEM` (value: `"SYSTEM"`)

* `AUTO` (value: `"AUTO"`)

* `MANUAL` (value: `"MANUAL"`)

* `DISABLED` (value: `"DISABLED"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `PAUSED` (value: `"PAUSED"`)

* `STOPPED` (value: `"STOPPED"`)




