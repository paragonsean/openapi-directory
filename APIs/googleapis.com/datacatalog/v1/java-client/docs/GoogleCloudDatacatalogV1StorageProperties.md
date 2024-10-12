

# GoogleCloudDatacatalogV1StorageProperties

Details the properties of the underlying storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filePattern** | **List&lt;String&gt;** | Patterns to identify a set of files for this fileset. Examples of a valid &#x60;file_pattern&#x60;: * &#x60;gs://bucket_name/dir/_*&#x60;: matches all files in the &#x60;bucket_name/dir&#x60; directory * &#x60;gs://bucket_name/dir/_**&#x60;: matches all files in the &#x60;bucket_name/dir&#x60; and all subdirectories recursively * &#x60;gs://bucket_name/file*&#x60;: matches files prefixed by &#x60;file&#x60; in &#x60;bucket_name&#x60; * &#x60;gs://bucket_name/??.txt&#x60;: matches files with two characters followed by &#x60;.txt&#x60; in &#x60;bucket_name&#x60; * &#x60;gs://bucket_name/[aeiou].txt&#x60;: matches files that contain a single vowel character followed by &#x60;.txt&#x60; in &#x60;bucket_name&#x60; * &#x60;gs://bucket_name/[a-m].txt&#x60;: matches files that contain &#x60;a&#x60;, &#x60;b&#x60;, ... or &#x60;m&#x60; followed by &#x60;.txt&#x60; in &#x60;bucket_name&#x60; * &#x60;gs://bucket_name/a/_*_/b&#x60;: matches all files in &#x60;bucket_name&#x60; that match the &#x60;a/_*_/b&#x60; pattern, such as &#x60;a/c/b&#x60;, &#x60;a/d/b&#x60; * &#x60;gs://another_bucket/a.txt&#x60;: matches &#x60;gs://another_bucket/a.txt&#x60; |  [optional] |
|**fileType** | **String** | File type in MIME format, for example, &#x60;text/plain&#x60;. |  [optional] |



