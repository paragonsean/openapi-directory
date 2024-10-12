

# UpdatePackageVersionsStatusRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**versions** | **List&lt;String&gt;** |  An array of strings that specify the versions of the package with the statuses to update.  |  |
|**versionRevisions** | **Map&lt;String, String&gt;** |  A map of package versions and package version revisions. The map &lt;code&gt;key&lt;/code&gt; is the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;), and the map &lt;code&gt;value&lt;/code&gt; is the package version revision.  |  [optional] |
|**expectedStatus** | [**ExpectedStatusEnum**](#ExpectedStatusEnum) |  The package version’s expected status before it is updated. If &lt;code&gt;expectedStatus&lt;/code&gt; is provided, the package version&#39;s status is updated only if its status at the time &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt; is called matches &lt;code&gt;expectedStatus&lt;/code&gt;.  |  [optional] |
|**targetStatus** | [**TargetStatusEnum**](#TargetStatusEnum) |  The status you want to change the package version status to.  |  |



## Enum: ExpectedStatusEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;Published&quot; |
| UNFINISHED | &quot;Unfinished&quot; |
| UNLISTED | &quot;Unlisted&quot; |
| ARCHIVED | &quot;Archived&quot; |
| DISPOSED | &quot;Disposed&quot; |
| DELETED | &quot;Deleted&quot; |



## Enum: TargetStatusEnum

| Name | Value |
|---- | -----|
| PUBLISHED | &quot;Published&quot; |
| UNFINISHED | &quot;Unfinished&quot; |
| UNLISTED | &quot;Unlisted&quot; |
| ARCHIVED | &quot;Archived&quot; |
| DISPOSED | &quot;Disposed&quot; |
| DELETED | &quot;Deleted&quot; |



