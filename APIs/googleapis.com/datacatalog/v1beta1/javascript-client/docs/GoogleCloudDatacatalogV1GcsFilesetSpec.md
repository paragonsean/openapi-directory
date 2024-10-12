# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1GcsFilesetSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filePatterns** | **[String]** | Required. Patterns to identify a set of files in Google Cloud Storage. For more information, see [Wildcard Names] (https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames). Note: Currently, bucket wildcards are not supported. Examples of valid &#x60;file_patterns&#x60;: * &#x60;gs://bucket_name/dir/_*&#x60;: matches all files in &#x60;bucket_name/dir&#x60; directory * &#x60;gs://bucket_name/dir/_**&#x60;: matches all files in &#x60;bucket_name/dir&#x60; and all subdirectories * &#x60;gs://bucket_name/file*&#x60;: matches files prefixed by &#x60;file&#x60; in &#x60;bucket_name&#x60; * &#x60;gs://bucket_name/??.txt&#x60;: matches files with two characters followed by &#x60;.txt&#x60; in &#x60;bucket_name&#x60; * &#x60;gs://bucket_name/[aeiou].txt&#x60;: matches files that contain a single vowel character followed by &#x60;.txt&#x60; in &#x60;bucket_name&#x60; * &#x60;gs://bucket_name/[a-m].txt&#x60;: matches files that contain &#x60;a&#x60;, &#x60;b&#x60;, ... or &#x60;m&#x60; followed by &#x60;.txt&#x60; in &#x60;bucket_name&#x60; * &#x60;gs://bucket_name/a/_*_/b&#x60;: matches all files in &#x60;bucket_name&#x60; that match the &#x60;a/_*_/b&#x60; pattern, such as &#x60;a/c/b&#x60;, &#x60;a/d/b&#x60; * &#x60;gs://another_bucket/a.txt&#x60;: matches &#x60;gs://another_bucket/a.txt&#x60; You can combine wildcards to match complex sets of files, for example: &#x60;gs://bucket_name/[a-m]??.j*g&#x60; | [optional] 
**sampleGcsFileSpecs** | [**[GoogleCloudDatacatalogV1GcsFileSpec]**](GoogleCloudDatacatalogV1GcsFileSpec.md) | Output only. Sample files contained in this fileset, not all files contained in this fileset are represented here. | [optional] [readonly] 


