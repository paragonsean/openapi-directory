# ContainerAnalysisApi.SBOMStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **String** | Output only. If there was an error generating an SBOM, this will indicate what that error was. | [optional] [readonly] 
**sbomState** | **String** | Output only. The progress of the SBOM generation. | [optional] [readonly] 



## Enum: SbomStateEnum


* `SBOM_STATE_UNSPECIFIED` (value: `"SBOM_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `COMPLETE` (value: `"COMPLETE"`)




