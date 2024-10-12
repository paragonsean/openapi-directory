

# PackageInfoNote

PackageInfoNote represents an SPDX Package Information section: https://spdx.github.io/spdx-spec/3-package-information/

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analyzed** | **Boolean** | Indicates whether the file content of this package has been available for or subjected to analysis when creating the SPDX document |  [optional] |
|**attribution** | **String** | A place for the SPDX data creator to record, at the package level, acknowledgements that may be needed to be communicated in some contexts |  [optional] |
|**checksum** | **String** | Provide an independently reproducible mechanism that permits unique identification of a specific package that correlates to the data in this SPDX file |  [optional] |
|**copyright** | **String** | Identify the copyright holders of the package, as well as any dates present |  [optional] |
|**detailedDescription** | **String** | A more detailed description of the package |  [optional] |
|**downloadLocation** | **String** | This section identifies the download Universal Resource Locator (URL), or a specific location within a version control system (VCS) for the package at the time that the SPDX file was created |  [optional] |
|**externalRefs** | [**List&lt;ExternalRef&gt;**](ExternalRef.md) | ExternalRef |  [optional] |
|**filesLicenseInfo** | **List&lt;String&gt;** | Contain the license the SPDX file creator has concluded as governing the This field is to contain a list of all licenses found in the package. The relationship between licenses (i.e., conjunctive, disjunctive) is not specified in this field – it is simply a listing of all licenses found |  [optional] |
|**homePage** | **String** | Provide a place for the SPDX file creator to record a web site that serves as the package&#39;s home page |  [optional] |
|**licenseDeclared** | [**License**](License.md) |  |  [optional] |
|**originator** | **String** | If the package identified in the SPDX file originated from a different person or organization than identified as Package Supplier, this field identifies from where or whom the package originally came |  [optional] |
|**packageType** | **String** | The type of package: OS, MAVEN, GO, GO_STDLIB, etc. |  [optional] |
|**summaryDescription** | **String** | A short description of the package |  [optional] |
|**supplier** | **String** | Identify the actual distribution source for the package/directory identified in the SPDX file |  [optional] |
|**title** | **String** | Identify the full name of the package as given by the Package Originator |  [optional] |
|**verificationCode** | **String** | This field provides an independently reproducible mechanism identifying specific contents of a package based on the actual files (except the SPDX file itself, if it is included in the package) that make up each package and that correlates to the data in this SPDX file |  [optional] |
|**version** | **String** | Identify the version of the package |  [optional] |



