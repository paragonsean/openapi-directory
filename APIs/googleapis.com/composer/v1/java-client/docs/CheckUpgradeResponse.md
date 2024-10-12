

# CheckUpgradeResponse

Message containing information about the result of an upgrade check operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildLogUri** | **String** | Output only. Url for a docker build log of an upgraded image. |  [optional] [readonly] |
|**containsPypiModulesConflict** | [**ContainsPypiModulesConflictEnum**](#ContainsPypiModulesConflictEnum) | Output only. Whether build has succeeded or failed on modules conflicts. |  [optional] [readonly] |
|**imageVersion** | **String** | Composer image for which the build was happening. |  [optional] |
|**pypiConflictBuildLogExtract** | **String** | Output only. Extract from a docker image build log containing information about pypi modules conflicts. |  [optional] [readonly] |
|**pypiDependencies** | **Map&lt;String, String&gt;** | Pypi dependencies specified in the environment configuration, at the time when the build was triggered. |  [optional] |



## Enum: ContainsPypiModulesConflictEnum

| Name | Value |
|---- | -----|
| CONFLICT_RESULT_UNSPECIFIED | &quot;CONFLICT_RESULT_UNSPECIFIED&quot; |
| CONFLICT | &quot;CONFLICT&quot; |
| NO_CONFLICT | &quot;NO_CONFLICT&quot; |



