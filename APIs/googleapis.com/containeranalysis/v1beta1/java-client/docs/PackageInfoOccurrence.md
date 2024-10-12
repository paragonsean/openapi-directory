

# PackageInfoOccurrence

PackageInfoOccurrence represents an SPDX Package Information section: https://spdx.github.io/spdx-spec/3-package-information/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | A place for the SPDX file creator to record any general comments about the package being described |  [optional] |
|**filename** | **String** | Provide the actual file name of the package, or path of the directory being treated as a package |  [optional] |
|**homePage** | **String** | Output only. Provide a place for the SPDX file creator to record a web site that serves as the package&#39;s home page |  [optional] [readonly] |
|**id** | **String** | Uniquely identify any element in an SPDX document which may be referenced by other elements |  [optional] |
|**licenseConcluded** | [**License**](License.md) |  |  [optional] |
|**packageType** | **String** | Output only. The type of package: OS, MAVEN, GO, GO_STDLIB, etc. |  [optional] [readonly] |
|**sourceInfo** | **String** | Provide a place for the SPDX file creator to record any relevant background information or additional comments about the origin of the package |  [optional] |
|**summaryDescription** | **String** | Output only. A short description of the package |  [optional] [readonly] |
|**title** | **String** | Output only. Identify the full name of the package as given by the Package Originator |  [optional] [readonly] |
|**version** | **String** | Output only. Identify the version of the package |  [optional] [readonly] |



