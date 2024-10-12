

# CodeReviewType

<p>The type of a code review. There are two code review types:</p> <ul> <li> <p> <code>PullRequest</code> - A code review that is automatically triggered by a pull request on an associated repository.</p> </li> <li> <p> <code>RepositoryAnalysis</code> - A code review that analyzes all code under a specified branch in an associated repository. The associated repository is specified using its ARN in <a href=\"https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CreateCodeReview\">CreateCodeReview</a>.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**repositoryAnalysis** | [**CreateCodeReviewRequestTypeRepositoryAnalysis**](CreateCodeReviewRequestTypeRepositoryAnalysis.md) |  |  |
|**analysisTypes** | [**List**](List.md) |  |  [optional] |



