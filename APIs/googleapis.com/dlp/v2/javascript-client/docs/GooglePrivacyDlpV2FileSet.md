# SensitiveDataProtectionDlp.GooglePrivacyDlpV2FileSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regexFileSet** | [**GooglePrivacyDlpV2CloudStorageRegexFileSet**](GooglePrivacyDlpV2CloudStorageRegexFileSet.md) |  | [optional] 
**url** | **String** | The Cloud Storage url of the file(s) to scan, in the format &#x60;gs:///&#x60;. Trailing wildcard in the path is allowed. If the url ends in a trailing slash, the bucket or directory represented by the url will be scanned non-recursively (content in sub-directories will not be scanned). This means that &#x60;gs://mybucket/&#x60; is equivalent to &#x60;gs://mybucket/_*&#x60;, and &#x60;gs://mybucket/directory/&#x60; is equivalent to &#x60;gs://mybucket/directory/_*&#x60;. Exactly one of &#x60;url&#x60; or &#x60;regex_file_set&#x60; must be set. | [optional] 


