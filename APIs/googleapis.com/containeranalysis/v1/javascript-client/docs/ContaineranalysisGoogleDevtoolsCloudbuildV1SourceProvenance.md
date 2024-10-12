# ContainerAnalysisApi.ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileHashes** | [**{String: ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes}**](ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes.md) | Output only. Hash(es) of the build source, which can be used to verify that the original source integrity was maintained in the build. Note that &#x60;FileHashes&#x60; will only be populated if &#x60;BuildOptions&#x60; has requested a &#x60;SourceProvenanceHash&#x60;. The keys to this map are file paths used as build source and the values contain the hash values for those files. If the build source came in a single package such as a gzipped tarfile (&#x60;.tar.gz&#x60;), the &#x60;FileHash&#x60; will be for the single path to that file. | [optional] [readonly] 
**resolvedConnectedRepository** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1ConnectedRepository**](ContaineranalysisGoogleDevtoolsCloudbuildV1ConnectedRepository.md) |  | [optional] 
**resolvedGitSource** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1GitSource**](ContaineranalysisGoogleDevtoolsCloudbuildV1GitSource.md) |  | [optional] 
**resolvedRepoSource** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource**](ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource.md) |  | [optional] 
**resolvedStorageSource** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource**](ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource.md) |  | [optional] 
**resolvedStorageSourceManifest** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifest**](ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifest.md) |  | [optional] 


