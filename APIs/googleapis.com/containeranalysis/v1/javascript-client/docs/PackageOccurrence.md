# ContainerAnalysisApi.PackageOccurrence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **String** | Output only. The CPU architecture for which packages in this distribution channel were built. Architecture will be blank for language packages. | [optional] [readonly] 
**cpeUri** | **String** | Output only. The cpe_uri in [CPE format](https://cpe.mitre.org/specification/) denoting the package manager version distributing a package. The cpe_uri will be blank for language packages. | [optional] [readonly] 
**license** | [**License**](License.md) |  | [optional] 
**location** | [**[Location]**](Location.md) | All of the places within the filesystem versions of this package have been found. | [optional] 
**name** | **String** | Required. Output only. The name of the installed package. | [optional] [readonly] 
**packageType** | **String** | Output only. The type of package; whether native or non native (e.g., ruby gems, node.js packages, etc.). | [optional] [readonly] 
**version** | [**Version**](Version.md) |  | [optional] 



## Enum: ArchitectureEnum


* `ARCHITECTURE_UNSPECIFIED` (value: `"ARCHITECTURE_UNSPECIFIED"`)

* `X86` (value: `"X86"`)

* `X64` (value: `"X64"`)




