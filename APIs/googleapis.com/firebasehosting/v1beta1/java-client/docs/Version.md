

# Version

A `Version` is a configuration and a collection of static files which determine how a site is displayed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | [**ServingConfig**](ServingConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which the version was created. |  [optional] |
|**createUser** | [**ActingUser**](ActingUser.md) |  |  [optional] |
|**deleteTime** | **String** | Output only. The time at which the version was &#x60;DELETED&#x60;. |  [optional] |
|**deleteUser** | [**ActingUser**](ActingUser.md) |  |  [optional] |
|**fileCount** | **String** | Output only. The total number of files associated with the version. This value is calculated after a version is &#x60;FINALIZED&#x60;. |  [optional] |
|**finalizeTime** | **String** | Output only. The time at which the version was &#x60;FINALIZED&#x60;. |  [optional] |
|**finalizeUser** | [**ActingUser**](ActingUser.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels used for extra metadata and/or filtering. |  [optional] |
|**name** | **String** | The fully-qualified resource name for the version, in the format: sites/ SITE_ID/versions/VERSION_ID This name is provided in the response body when you call [&#x60;CreateVersion&#x60;](sites.versions/create). |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The deploy status of the version. For a successful deploy, call [&#x60;CreateVersion&#x60;](sites.versions/create) to make a new version (&#x60;CREATED&#x60; status), [upload all desired files](sites.versions/populateFiles) to the version, then [update](sites.versions/patch) the version to the &#x60;FINALIZED&#x60; status. Note that if you leave the version in the &#x60;CREATED&#x60; state for more than 12 hours, the system will automatically mark the version as &#x60;ABANDONED&#x60;. You can also change the status of a version to &#x60;DELETED&#x60; by calling [&#x60;DeleteVersion&#x60;](sites.versions/delete). |  [optional] |
|**versionBytes** | **String** | Output only. The total stored bytesize of the version. This value is calculated after a version is &#x60;FINALIZED&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VERSION_STATUS_UNSPECIFIED | &quot;VERSION_STATUS_UNSPECIFIED&quot; |
| CREATED | &quot;CREATED&quot; |
| FINALIZED | &quot;FINALIZED&quot; |
| DELETED | &quot;DELETED&quot; |
| ABANDONED | &quot;ABANDONED&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| CLONING | &quot;CLONING&quot; |



