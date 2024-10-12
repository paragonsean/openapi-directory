

# MachineArchitectureDetails

Details of the machine architecture.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bios** | [**BiosDetails**](BiosDetails.md) |  |  [optional] |
|**cpuArchitecture** | **String** | CPU architecture, e.g., \&quot;x64-based PC\&quot;, \&quot;x86_64\&quot;, \&quot;i686\&quot; etc. |  [optional] |
|**cpuName** | **String** | CPU name, e.g., \&quot;Intel Xeon E5-2690\&quot;, \&quot;AMD EPYC 7571\&quot; etc. |  [optional] |
|**cpuSocketCount** | **Integer** | Number of processor sockets allocated to the machine. |  [optional] |
|**cpuThreadCount** | **Integer** | Number of CPU threads allocated to the machine. |  [optional] |
|**firmwareType** | [**FirmwareTypeEnum**](#FirmwareTypeEnum) | Firmware type. |  [optional] |
|**hyperthreading** | [**HyperthreadingEnum**](#HyperthreadingEnum) | CPU hyper-threading support. |  [optional] |
|**vendor** | **String** | Hardware vendor. |  [optional] |



## Enum: FirmwareTypeEnum

| Name | Value |
|---- | -----|
| FIRMWARE_TYPE_UNSPECIFIED | &quot;FIRMWARE_TYPE_UNSPECIFIED&quot; |
| BIOS | &quot;BIOS&quot; |
| EFI | &quot;EFI&quot; |



## Enum: HyperthreadingEnum

| Name | Value |
|---- | -----|
| CPU_HYPER_THREADING_UNSPECIFIED | &quot;CPU_HYPER_THREADING_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| ENABLED | &quot;ENABLED&quot; |



