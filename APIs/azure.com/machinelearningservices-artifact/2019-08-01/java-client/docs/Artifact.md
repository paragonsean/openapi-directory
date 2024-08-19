

# Artifact

Details of an Artifact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactId** | **String** | The identifier of an Artifact. Format of ArtifactId - {Origin}/{Container}/{Path}. |  [optional] |
|**container** | **String** | The name of container. Artifacts can be grouped by container. |  |
|**createdTime** | **OffsetDateTime** | The Date and Time at which the Artifact is created. The DateTime is in UTC. |  [optional] [readonly] |
|**dataPath** | [**DataPath**](DataPath.md) |  |  [optional] |
|**etag** | **String** | The Etag of the Artifact. |  [optional] [readonly] |
|**origin** | **String** | The origin of the Artifact creation request. Available origins are &#39;ExperimentRun&#39;, &#39;LocalUpload&#39;, &#39;WebUpload&#39;, &#39;Dataset&#39; and &#39;Unknown&#39;. |  |
|**path** | **String** | The path to the Artifact in a container. |  |



