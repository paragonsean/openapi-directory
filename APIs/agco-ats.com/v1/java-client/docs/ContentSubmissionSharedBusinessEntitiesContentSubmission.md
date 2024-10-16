

# ContentSubmissionSharedBusinessEntitiesContentSubmission

A content submission

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute&gt;**](ContentSubmissionSharedBusinessEntitiesContentSubmissionAttribute.md) | Attributes of this ContentSubmission |  [optional] |
|**buildID** | **Integer** | ReadOnly. The ID of the Azure DevOps Build which will build the content package. |  [optional] |
|**contentDefinitionID** | **Integer** | The ID of the Content Definition. |  [optional] |
|**contentSubmissionID** | **Integer** | The ID of this Content Submission. |  [optional] |
|**definition** | [**ContentSubmissionSharedBusinessEntitiesContentDefinition**](ContentSubmissionSharedBusinessEntitiesContentDefinition.md) |  |  [optional] |
|**jobRunID** | **Integer** | ReadOnly. The ID of the JobRun which will build the content package. |  [optional] |
|**packageID** | **String** | The ID of package generated by this content submission. |  [optional] |
|**releaseNotes** | **String** | Release Notes for this ContentSubmission |  [optional] |
|**repository** | **String** | The SVN repository used as the source of this content submission |  [optional] |
|**revision** | **Integer** | The SVN revision used as the source of this content submission. |  [optional] |
|**submissionDate** | **OffsetDateTime** | Read Only. The UTC date and time the content submission was made. |  [optional] |
|**userID** | **Integer** | Read Only. The ID of the user who submitted the content |  [optional] |
|**version** | **Integer** | Optional.  The version number assigned to this Content Submission and the resulting Package.              If not provided, version shall be 1 if it is the first content submission for the               ContentDefinitionID otherwise it shall be the highest content submission version for the              specified ContentDefinitionID incremented by 1. |  [optional] |



