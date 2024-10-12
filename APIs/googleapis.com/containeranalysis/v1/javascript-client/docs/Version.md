# ContainerAnalysisApi.Version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epoch** | **Number** | Used to correct mistakes in the version numbering scheme. | [optional] 
**fullName** | **String** | Human readable version string. This string is of the form :- and is only set when kind is NORMAL. | [optional] 
**inclusive** | **Boolean** | Whether this version is specifying part of an inclusive range. Grafeas does not have the capability to specify version ranges; instead we have fields that specify start version and end versions. At times this is insufficient - we also need to specify whether the version is included in the range or is excluded from the range. This boolean is expected to be set to true when the version is included in a range. | [optional] 
**kind** | **String** | Required. Distinguishes between sentinel MIN/MAX versions and normal versions. | [optional] 
**name** | **String** | Required only when version kind is NORMAL. The main part of the version name. | [optional] 
**revision** | **String** | The iteration of the package build from the above version. | [optional] 



## Enum: KindEnum


* `VERSION_KIND_UNSPECIFIED` (value: `"VERSION_KIND_UNSPECIFIED"`)

* `NORMAL` (value: `"NORMAL"`)

* `MINIMUM` (value: `"MINIMUM"`)

* `MAXIMUM` (value: `"MAXIMUM"`)




