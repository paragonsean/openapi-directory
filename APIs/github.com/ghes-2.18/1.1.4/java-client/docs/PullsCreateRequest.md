

# PullsCreateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**base** | **String** | The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository. |  |
|**body** | **String** | The contents of the pull request. |  [optional] |
|**draft** | **Boolean** | Indicates whether the pull request is a draft. See \&quot;[Draft Pull Requests](https://help.github.com/en/articles/about-pull-requests#draft-pull-requests)\&quot; in the GitHub Help documentation to learn more. |  [optional] |
|**head** | **String** | The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace &#x60;head&#x60; with a user like this: &#x60;username:branch&#x60;. |  |
|**issue** | **Integer** |  |  [optional] |
|**maintainerCanModify** | **Boolean** | Indicates whether [maintainers can modify](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request. |  [optional] |
|**title** | **String** | The title of the new pull request. |  [optional] |



