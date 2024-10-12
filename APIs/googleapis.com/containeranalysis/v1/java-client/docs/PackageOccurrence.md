

# PackageOccurrence

Details on how a particular software package was installed on a system.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | Output only. The CPU architecture for which packages in this distribution channel were built. Architecture will be blank for language packages. |  [optional] [readonly] |
|**cpeUri** | **String** | Output only. The cpe_uri in [CPE format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package. The cpe_uri will be blank for language packages. |  [optional] [readonly] |
|**license** | [**License**](License.md) |  |  [optional] |
|**location** | [**List&lt;Location&gt;**](Location.md) | All of the places within the filesystem versions of this package have been found. |  [optional] |
|**name** | **String** | Required. Output only. The name of the installed package. |  [optional] [readonly] |
|**packageType** | **String** | Output only. The type of package; whether native or non native (e.g., ruby gems, node.js packages, etc.). |  [optional] [readonly] |
|**version** | [**Version**](Version.md) |  |  [optional] |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| ARCHITECTURE_UNSPECIFIED | &quot;ARCHITECTURE_UNSPECIFIED&quot; |
| X86 | &quot;X86&quot; |
| X64 | &quot;X64&quot; |



