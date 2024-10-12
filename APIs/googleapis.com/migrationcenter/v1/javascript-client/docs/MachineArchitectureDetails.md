# MigrationCenterApi.MachineArchitectureDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bios** | [**BiosDetails**](BiosDetails.md) |  | [optional] 
**cpuArchitecture** | **String** | CPU architecture, e.g., \&quot;x64-based PC\&quot;, \&quot;x86_64\&quot;, \&quot;i686\&quot; etc. | [optional] 
**cpuName** | **String** | CPU name, e.g., \&quot;Intel Xeon E5-2690\&quot;, \&quot;AMD EPYC 7571\&quot; etc. | [optional] 
**cpuSocketCount** | **Number** | Number of processor sockets allocated to the machine. | [optional] 
**cpuThreadCount** | **Number** | Number of CPU threads allocated to the machine. | [optional] 
**firmwareType** | **String** | Firmware type. | [optional] 
**hyperthreading** | **String** | CPU hyper-threading support. | [optional] 
**vendor** | **String** | Hardware vendor. | [optional] 



## Enum: FirmwareTypeEnum


* `FIRMWARE_TYPE_UNSPECIFIED` (value: `"FIRMWARE_TYPE_UNSPECIFIED"`)

* `BIOS` (value: `"BIOS"`)

* `EFI` (value: `"EFI"`)





## Enum: HyperthreadingEnum


* `CPU_HYPER_THREADING_UNSPECIFIED` (value: `"CPU_HYPER_THREADING_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `ENABLED` (value: `"ENABLED"`)




