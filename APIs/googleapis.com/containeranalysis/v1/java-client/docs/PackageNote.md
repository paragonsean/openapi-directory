

# PackageNote

PackageNote represents a particular package version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | [**ArchitectureEnum**](#ArchitectureEnum) | The CPU architecture for which packages in this distribution channel were built. Architecture will be blank for language packages. |  [optional] |
|**cpeUri** | **String** | The cpe_uri in [CPE format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package. The cpe_uri will be blank for language packages. |  [optional] |
|**description** | **String** | The description of this package. |  [optional] |
|**digest** | [**List&lt;Digest&gt;**](Digest.md) | Hash value, typically a file digest, that allows unique identification a specific package. |  [optional] |
|**distribution** | [**List&lt;Distribution&gt;**](Distribution.md) | Deprecated. The various channels by which a package is distributed. |  [optional] |
|**license** | [**License**](License.md) |  |  [optional] |
|**maintainer** | **String** | A freeform text denoting the maintainer of this package. |  [optional] |
|**name** | **String** | Required. Immutable. The name of the package. |  [optional] |
|**packageType** | **String** | The type of package; whether native or non native (e.g., ruby gems, node.js packages, etc.). |  [optional] |
|**url** | **String** | The homepage for this package. |  [optional] |
|**version** | [**Version**](Version.md) |  |  [optional] |



## Enum: ArchitectureEnum

| Name | Value |
|---- | -----|
| ARCHITECTURE_UNSPECIFIED | &quot;ARCHITECTURE_UNSPECIFIED&quot; |
| X86 | &quot;X86&quot; |
| X64 | &quot;X64&quot; |



