

# ReposCreateReleaseRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Text describing the contents of the tag. |  [optional] |
|**draft** | **Boolean** | &#x60;true&#x60; to create a draft (unpublished) release, &#x60;false&#x60; to create a published one. |  [optional] |
|**name** | **String** | The name of the release. |  [optional] |
|**prerelease** | **Boolean** | &#x60;true&#x60; to identify the release as a prerelease. &#x60;false&#x60; to identify the release as a full release. |  [optional] |
|**tagName** | **String** | The name of the tag. |  |
|**targetCommitish** | **String** | Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository&#39;s default branch (usually &#x60;master&#x60;). |  [optional] |



