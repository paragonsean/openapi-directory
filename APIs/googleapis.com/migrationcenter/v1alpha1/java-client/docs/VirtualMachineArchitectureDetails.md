

# VirtualMachineArchitectureDetails

Details of the VM architecture.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bios** | [**BiosDetails**](BiosDetails.md) |  |  [optional] |
|**cpuArchitecture** | **String** | CPU architecture, e.g., \&quot;x64-based PC\&quot;, \&quot;x86_64\&quot;, \&quot;i686\&quot; etc. |  [optional] |
|**cpuManufacturer** | **String** | CPU manufacturer, e.g., \&quot;Intel\&quot;, \&quot;AMD\&quot;. |  [optional] |
|**cpuName** | **String** | CPU name, e.g., \&quot;Intel Xeon E5-2690\&quot;, \&quot;AMD EPYC 7571\&quot; etc. |  [optional] |
|**cpuSocketCount** | **Integer** | Number of processor sockets allocated to the machine. |  [optional] |
|**cpuThreadCount** | **Integer** | Number of CPU threads allocated to the machine. |  [optional] |
|**firmware** | **String** | Firmware (BIOS/efi). |  [optional] |
|**hyperthreading** | [**HyperthreadingEnum**](#HyperthreadingEnum) | CPU hyperthreading support. |  [optional] |
|**vendor** | **String** | Hardware vendor. |  [optional] |



## Enum: HyperthreadingEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;HYPER_THREADING_UNSPECIFIED&quot; |
| DISABLED | &quot;HYPER_THREADING_DISABLED&quot; |
| ENABLED | &quot;HYPER_THREADING_ENABLED&quot; |



