# CloudComposerApi.CheckUpgradeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildLogUri** | **String** | Output only. Url for a docker build log of an upgraded image. | [optional] [readonly] 
**containsPypiModulesConflict** | **String** | Output only. Whether build has succeeded or failed on modules conflicts. | [optional] [readonly] 
**imageVersion** | **String** | Composer image for which the build was happening. | [optional] 
**pypiConflictBuildLogExtract** | **String** | Output only. Extract from a docker image build log containing information about pypi modules conflicts. | [optional] [readonly] 
**pypiDependencies** | **{String: String}** | Pypi dependencies specified in the environment configuration, at the time when the build was triggered. | [optional] 



## Enum: ContainsPypiModulesConflictEnum


* `CONFLICT_RESULT_UNSPECIFIED` (value: `"CONFLICT_RESULT_UNSPECIFIED"`)

* `CONFLICT` (value: `"CONFLICT"`)

* `NO_CONFLICT` (value: `"NO_CONFLICT"`)




