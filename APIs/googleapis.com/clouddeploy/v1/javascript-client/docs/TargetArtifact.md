# CloudDeployApi.TargetArtifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifactUri** | **String** | Output only. URI of a directory containing the artifacts. This contains deployment configuration used by Skaffold during a rollout, and all paths are relative to this location. | [optional] [readonly] 
**manifestPath** | **String** | Output only. File path of the rendered manifest relative to the URI. | [optional] [readonly] 
**phaseArtifacts** | [**{String: PhaseArtifact}**](PhaseArtifact.md) | Output only. Map from the phase ID to the phase artifacts for the &#x60;Target&#x60;. | [optional] [readonly] 
**skaffoldConfigPath** | **String** | Output only. File path of the resolved Skaffold configuration relative to the URI. | [optional] [readonly] 


