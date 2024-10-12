

# PullRequestReview

Pull Request Reviews are reviews on pull requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**PullRequestReviewLinks**](PullRequestReviewLinks.md) |  |  |
|**authorAssociation** | **AuthorAssociation** |  |  |
|**body** | **String** | The text of the review. |  |
|**bodyHtml** | **String** |  |  [optional] |
|**bodyText** | **String** |  |  [optional] |
|**commitId** | **String** | A commit SHA for the review. If the commit object was garbage collected or forcibly deleted, then it no longer exists in Git and this value will be &#x60;null&#x60;. |  |
|**htmlUrl** | **URI** |  |  |
|**id** | **Integer** | Unique identifier of the review |  |
|**nodeId** | **String** |  |  |
|**pullRequestUrl** | **URI** |  |  |
|**state** | **String** |  |  |
|**submittedAt** | **OffsetDateTime** |  |  [optional] |
|**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |



