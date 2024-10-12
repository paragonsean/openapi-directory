

# ReposCreateReleaseRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Text describing the contents of the tag. |  [optional] |
|**draft** | **Boolean** | &#x60;true&#x60; to create a draft (unpublished) release, &#x60;false&#x60; to create a published one. |  [optional] |
|**generateReleaseNotes** | **Boolean** | Whether to automatically generate the name and body for this release. If &#x60;name&#x60; is specified, the specified name will be used; otherwise, a name will be automatically generated. If &#x60;body&#x60; is specified, the body will be pre-pended to the automatically generated notes. |  [optional] |
|**name** | **String** | The name of the release. |  [optional] |
|**prerelease** | **Boolean** | &#x60;true&#x60; to identify the release as a prerelease. &#x60;false&#x60; to identify the release as a full release. |  [optional] |
|**tagName** | **String** | The name of the tag. |  |
|**targetCommitish** | **String** | Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository&#39;s default branch (usually &#x60;master&#x60;). |  [optional] |



