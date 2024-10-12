

# CreateRepositoryRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** |  A description of the created repository.  |  [optional] |
|**upstreams** | [**List&lt;UpstreamRepository&gt;**](UpstreamRepository.md) |  A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when CodeArtifact looks for a requested package version. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html\&quot;&gt;Working with upstream repositories&lt;/a&gt;.  |  [optional] |
|**tags** | [**List&lt;Tag&gt;**](Tag.md) | One or more tag key-value pairs for the repository. |  [optional] |



