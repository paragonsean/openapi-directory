# ApigeeRegistryApi.Artifact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Annotations attach non-identifying metadata to resources. Annotation keys and values are less restricted than those of labels, but should be generally used for small values of broad interest. Larger, topic- specific metadata should be stored in Artifacts. | [optional] 
**contents** | **Blob** | Input only. The contents of the artifact. Provided by API callers when artifacts are created or replaced. To access the contents of an artifact, use GetArtifactContents. | [optional] 
**createTime** | **String** | Output only. Creation timestamp. | [optional] [readonly] 
**hash** | **String** | Output only. A SHA-256 hash of the artifact&#39;s contents. If the artifact is gzipped, this is the hash of the uncompressed artifact. | [optional] [readonly] 
**labels** | **{String: String}** | Labels attach identifying metadata to resources. Identifying metadata can be used to filter list operations. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one resource (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with \&quot;registry.googleapis.com/\&quot; and cannot be changed. | [optional] 
**mimeType** | **String** | A content type specifier for the artifact. Content type specifiers are Media Types (https://en.wikipedia.org/wiki/Media_type) with a possible \&quot;schema\&quot; parameter that specifies a schema for the stored information. Content types can specify compression. Currently only GZip compression is supported (indicated with \&quot;+gzip\&quot;). | [optional] 
**name** | **String** | Resource name. | [optional] 
**sizeBytes** | **Number** | Output only. The size of the artifact in bytes. If the artifact is gzipped, this is the size of the uncompressed artifact. | [optional] [readonly] 
**updateTime** | **String** | Output only. Last update timestamp. | [optional] [readonly] 


