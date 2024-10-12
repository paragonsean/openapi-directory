

# CurationDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**item** | [**ArticleComplete**](ArticleComplete.md) |  |  |
|**accountId** | **Long** | The ID of the account of the owner of the article of this review. |  |
|**articleId** | **Long** | The ID of the article of this review. |  |
|**assignedTo** | **Long** | The ID of the account to which this review is assigned. |  |
|**commentsCount** | **Long** | The number of comments in the review. |  |
|**createdDate** | **String** | The creation date of the review. |  |
|**groupId** | **Long** | The group in which the article is present. |  |
|**id** | **Long** | The review id |  |
|**modifiedDate** | **String** | The date the review has been modified. |  |
|**reviewDate** | **String** | The last time a comment has been added to the review. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the review. |  |
|**version** | **Long** | The Version number of the article in review. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |
| CLOSED | &quot;closed&quot; |



