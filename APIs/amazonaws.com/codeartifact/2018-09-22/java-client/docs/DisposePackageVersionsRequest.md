

# DisposePackageVersionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**versions** | **List&lt;String&gt;** |  The versions of the package you want to dispose.  |  |
|**versionRevisions** | **Map&lt;String, String&gt;** |  The revisions of the package versions you want to dispose.  |  [optional] |
|**expectedStatus** | [**ExpectedStatusEnum**](#ExpectedStatusEnum) |  The expected status of the package version to dispose.  |  [optional] |



## Enum: ExpectedStatusEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;Published&quot; |
| UNFINISHED | &quot;Unfinished&quot; |
| UNLISTED | &quot;Unlisted&quot; |
| ARCHIVED | &quot;Archived&quot; |
| DISPOSED | &quot;Disposed&quot; |
| DELETED | &quot;Deleted&quot; |



