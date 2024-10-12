# ContainerAnalysisApi.Distribution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **String** | The CPU architecture for which packages in this distribution channel were built. | [optional] 
**cpeUri** | **String** | Required. The cpe_uri in [CPE format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package. | [optional] 
**description** | **String** | The distribution channel-specific description of this package. | [optional] 
**latestVersion** | [**Version**](Version.md) |  | [optional] 
**maintainer** | **String** | A freeform string denoting the maintainer of this package. | [optional] 
**url** | **String** | The distribution channel-specific homepage for this package. | [optional] 



## Enum: ArchitectureEnum


* `ARCHITECTURE_UNSPECIFIED` (value: `"ARCHITECTURE_UNSPECIFIED"`)

* `X86` (value: `"X86"`)

* `X64` (value: `"X64"`)




