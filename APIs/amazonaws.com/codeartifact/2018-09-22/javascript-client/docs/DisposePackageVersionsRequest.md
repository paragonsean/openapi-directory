# CodeArtifact.DisposePackageVersionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **[String]** |  The versions of the package you want to dispose.  | 
**versionRevisions** | **{String: String}** |  The revisions of the package versions you want to dispose.  | [optional] 
**expectedStatus** | **String** |  The expected status of the package version to dispose.  | [optional] 



## Enum: ExpectedStatusEnum


* `Published` (value: `"Published"`)

* `Unfinished` (value: `"Unfinished"`)

* `Unlisted` (value: `"Unlisted"`)

* `Archived` (value: `"Archived"`)

* `Disposed` (value: `"Disposed"`)

* `Deleted` (value: `"Deleted"`)




