# GitHubV3RestApi.PullRequestReview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PullRequestReviewLinks**](PullRequestReviewLinks.md) |  | 
**authorAssociation** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**body** | **String** | The text of the review. | 
**bodyHtml** | **String** |  | [optional] 
**bodyText** | **String** |  | [optional] 
**commitId** | **String** | A commit SHA for the review. If the commit object was garbage collected or forcibly deleted, then it no longer exists in Git and this value will be &#x60;null&#x60;. | 
**htmlUrl** | **String** |  | 
**id** | **Number** | Unique identifier of the review | 
**nodeId** | **String** |  | 
**pullRequestUrl** | **String** |  | 
**state** | **String** |  | 
**submittedAt** | **Date** |  | [optional] 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 


