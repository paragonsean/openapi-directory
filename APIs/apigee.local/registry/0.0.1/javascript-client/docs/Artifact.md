# RegistryApi.Artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **String** | Input only. The contents of the artifact. Provided by API callers when artifacts are created or replaced. To access the contents of an artifact, use GetArtifactContents. | [optional] 
**createTime** | **Date** | Output only. Creation timestamp. | [optional] [readonly] 
**hash** | **String** | Output only. A SHA-256 hash of the artifact&#39;s contents. If the artifact is gzipped, this is the hash of the uncompressed artifact. | [optional] [readonly] 
**mimeType** | **String** | A content type specifier for the artifact. Content type specifiers are Media Types (https://en.wikipedia.org/wiki/Media_type) with a possible \&quot;schema\&quot; parameter that specifies a schema for the stored information. Content types can specify compression. Currently only GZip compression is supported (indicated with \&quot;+gzip\&quot;). | [optional] 
**name** | **String** | Resource name. | [optional] 
**sizeBytes** | **Number** | Output only. The size of the artifact in bytes. If the artifact is gzipped, this is the size of the uncompressed artifact. | [optional] [readonly] 
**updateTime** | **Date** | Output only. Last update timestamp. | [optional] [readonly] 


