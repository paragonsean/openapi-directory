# SensitiveDataProtectionDlp.GooglePrivacyDlpV2CloudStorageRegexFileSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucketName** | **String** | The name of a Cloud Storage bucket. Required. | [optional] 
**excludeRegex** | **[String]** | A list of regular expressions matching file paths to exclude. All files in the bucket that match at least one of these regular expressions will be excluded from the scan. Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub. | [optional] 
**includeRegex** | **[String]** | A list of regular expressions matching file paths to include. All files in the bucket that match at least one of these regular expressions will be included in the set of files, except for those that also match an item in &#x60;exclude_regex&#x60;. Leaving this field empty will match all files by default (this is equivalent to including &#x60;.*&#x60; in the list). Regular expressions use RE2 [syntax](https://github.com/google/re2/wiki/Syntax); a guide can be found under the google/re2 repository on GitHub. | [optional] 


