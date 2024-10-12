# CodeArtifact.UpdatePackageVersionsStatusRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | **[String]** |  An array of strings that specify the versions of the package with the statuses to update.  | 
**versionRevisions** | **{String: String}** |  A map of package versions and package version revisions. The map &lt;code&gt;key&lt;/code&gt; is the package version (for example, &lt;code&gt;3.5.2&lt;/code&gt;), and the map &lt;code&gt;value&lt;/code&gt; is the package version revision.  | [optional] 
**expectedStatus** | **String** |  The package version’s expected status before it is updated. If &lt;code&gt;expectedStatus&lt;/code&gt; is provided, the package version&#39;s status is updated only if its status at the time &lt;code&gt;UpdatePackageVersionsStatus&lt;/code&gt; is called matches &lt;code&gt;expectedStatus&lt;/code&gt;.  | [optional] 
**targetStatus** | **String** |  The status you want to change the package version status to.  | 



## Enum: ExpectedStatusEnum


* `Published` (value: `"Published"`)

* `Unfinished` (value: `"Unfinished"`)

* `Unlisted` (value: `"Unlisted"`)

* `Archived` (value: `"Archived"`)

* `Disposed` (value: `"Disposed"`)

* `Deleted` (value: `"Deleted"`)





## Enum: TargetStatusEnum


* `Published` (value: `"Published"`)

* `Unfinished` (value: `"Unfinished"`)

* `Unlisted` (value: `"Unlisted"`)

* `Archived` (value: `"Archived"`)

* `Disposed` (value: `"Disposed"`)

* `Deleted` (value: `"Deleted"`)




