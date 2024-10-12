

# BuildProvenance

Provenance of a build. Contains all information needed to verify the full details about the build from source to completion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildOptions** | **Map&lt;String, String&gt;** | Special options applied to this build. This is a catch-all field where build providers can enter any desired additional details. |  [optional] |
|**builderVersion** | **String** | Version string of the builder at the time this build was executed. |  [optional] |
|**builtArtifacts** | [**List&lt;Artifact&gt;**](Artifact.md) | Output of the build. |  [optional] |
|**commands** | [**List&lt;Command&gt;**](Command.md) | Commands requested by the build. |  [optional] |
|**createTime** | **String** | Time at which the build was created. |  [optional] |
|**creator** | **String** | E-mail address of the user who initiated this build. Note that this was the user&#39;s e-mail address at the time the build was initiated; this address may not represent the same end-user for all time. |  [optional] |
|**finishTime** | **String** | Time at which execution of the build was finished. |  [optional] |
|**id** | **String** | Unique identifier of the build. |  [optional] |
|**logsBucket** | **String** | Google Cloud Storage bucket where logs were written. |  [optional] |
|**projectId** | **String** | ID of the project. |  [optional] |
|**sourceProvenance** | [**Source**](Source.md) |  |  [optional] |
|**startTime** | **String** | Time at which execution of the build was started. |  [optional] |
|**triggerId** | **String** | Trigger identifier if the build was triggered automatically; empty if not. |  [optional] |



