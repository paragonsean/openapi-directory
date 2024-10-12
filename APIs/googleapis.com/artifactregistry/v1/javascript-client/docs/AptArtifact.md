# ArtifactRegistryApi.AptArtifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **String** | Output only. Operating system architecture of the artifact. | [optional] [readonly] 
**component** | **String** | Output only. Repository component of the artifact. | [optional] [readonly] 
**controlFile** | **Blob** | Output only. Contents of the artifact&#39;s control metadata file. | [optional] [readonly] 
**name** | **String** | Output only. The Artifact Registry resource name of the artifact. | [optional] [readonly] 
**packageName** | **String** | Output only. The Apt package name of the artifact. | [optional] [readonly] 
**packageType** | **String** | Output only. An artifact is a binary or source package. | [optional] [readonly] 



## Enum: PackageTypeEnum


* `PACKAGE_TYPE_UNSPECIFIED` (value: `"PACKAGE_TYPE_UNSPECIFIED"`)

* `BINARY` (value: `"BINARY"`)

* `SOURCE` (value: `"SOURCE"`)




