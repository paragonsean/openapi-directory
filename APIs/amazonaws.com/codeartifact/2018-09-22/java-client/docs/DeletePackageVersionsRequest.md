

# DeletePackageVersionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**versions** | **List&lt;String&gt;** |  An array of strings that specify the versions of the package to delete.  |  |
|**expectedStatus** | [**ExpectedStatusEnum**](#ExpectedStatusEnum) |  The expected status of the package version to delete.  |  [optional] |



## Enum: ExpectedStatusEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;Published&quot; |
| UNFINISHED | &quot;Unfinished&quot; |
| UNLISTED | &quot;Unlisted&quot; |
| ARCHIVED | &quot;Archived&quot; |
| DISPOSED | &quot;Disposed&quot; |
| DELETED | &quot;Deleted&quot; |



