# ContainerAnalysisApi.BuildProvenance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildOptions** | **{String: String}** | Special options applied to this build. This is a catch-all field where build providers can enter any desired additional details. | [optional] 
**builderVersion** | **String** | Version string of the builder at the time this build was executed. | [optional] 
**builtArtifacts** | [**[Artifact]**](Artifact.md) | Output of the build. | [optional] 
**commands** | [**[Command]**](Command.md) | Commands requested by the build. | [optional] 
**createTime** | **String** | Time at which the build was created. | [optional] 
**creator** | **String** | E-mail address of the user who initiated this build. Note that this was the user&#39;s e-mail address at the time the build was initiated; this address may not represent the same end-user for all time. | [optional] 
**endTime** | **String** | Time at which execution of the build was finished. | [optional] 
**id** | **String** | Required. Unique identifier of the build. | [optional] 
**logsUri** | **String** | URI where any logs for this provenance were written. | [optional] 
**projectId** | **String** | ID of the project. | [optional] 
**sourceProvenance** | [**Source**](Source.md) |  | [optional] 
**startTime** | **String** | Time at which execution of the build was started. | [optional] 
**triggerId** | **String** | Trigger identifier if the build was triggered automatically; empty if not. | [optional] 


