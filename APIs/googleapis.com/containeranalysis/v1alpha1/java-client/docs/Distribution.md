

# Distribution

This represents a particular channel of distribution for a given package. e.g. Debian's jessie-backports dpkg mirror

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | The CPU architecture for which packages in this distribution channel were built |  [optional] |
|**cpeUri** | **String** | The cpe_uri in [cpe format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package. |  [optional] |
|**description** | **String** | The distribution channel-specific description of this package. |  [optional] |
|**latestVersion** | [**Version**](Version.md) |  |  [optional] |
|**maintainer** | **String** | A freeform string denoting the maintainer of this package. |  [optional] |
|**url** | **String** | The distribution channel-specific homepage for this package. |  [optional] |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| ARCHITECTURE_UNSPECIFIED | &quot;ARCHITECTURE_UNSPECIFIED&quot; |
| X86 | &quot;X86&quot; |
| X64 | &quot;X64&quot; |



