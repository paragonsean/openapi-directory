# ContainerAnalysisApi.Version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epoch** | **Number** | Used to correct mistakes in the version numbering scheme. | [optional] 
**inclusive** | **Boolean** | Whether this version is vulnerable, when defining the version bounds. For example, if the minimum version is 2.0, inclusive&#x3D;true would say 2.0 is vulnerable, while inclusive&#x3D;false would say it&#39;s not | [optional] 
**kind** | **String** | Distinguish between sentinel MIN/MAX versions and normal versions. If kind is not NORMAL, then the other fields are ignored. | [optional] 
**name** | **String** | The main part of the version name. | [optional] 
**revision** | **String** | The iteration of the package build from the above version. | [optional] 



## Enum: KindEnum


* `NORMAL` (value: `"NORMAL"`)

* `MINIMUM` (value: `"MINIMUM"`)

* `MAXIMUM` (value: `"MAXIMUM"`)




