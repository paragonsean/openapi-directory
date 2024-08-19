

# PullsCreateReviewCommentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | The text of the review comment. |  |
|**commitId** | **String** | The SHA of the commit needing a comment. Not using the latest commit SHA may render your comment outdated if a subsequent commit modifies the line you specify as the &#x60;position&#x60;. |  [optional] |
|**inReplyTo** | **Integer** |  |  [optional] |
|**line** | **Integer** | The line of the blob in the pull request diff that the comment applies to. For a multi-line comment, the last line of the range that your comment applies to. |  [optional] |
|**path** | **String** | The relative path to the file that necessitates a comment. |  [optional] |
|**position** | **Integer** | The position in the diff where you want to add a review comment. Note this value is not the same as the line number in the file. For help finding the position value, read the note above. |  [optional] |
|**side** | [**SideEnum**](#SideEnum) | In a split diff view, the side of the diff that the pull request&#39;s changes appear on. Can be &#x60;LEFT&#x60; or &#x60;RIGHT&#x60;. Use &#x60;LEFT&#x60; for deletions that appear in red. Use &#x60;RIGHT&#x60; for additions that appear in green or unchanged lines that appear in white and are shown for context. For a multi-line comment, side represents whether the last line of the comment range is a deletion or addition. For more information, see \&quot;[Diff view options](https://help.github.com/en/articles/about-comparing-branches-in-pull-requests#diff-view-options)\&quot; in the GitHub Help documentation. |  [optional] |
|**startLine** | **Integer** | **Required when using multi-line comments**. The &#x60;start_line&#x60; is the first line in the pull request diff that your multi-line comment applies to. To learn more about multi-line comments, see \&quot;[Commenting on a pull request](https://help.github.com/en/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)\&quot; in the GitHub Help documentation. |  [optional] |
|**startSide** | [**StartSideEnum**](#StartSideEnum) | **Required when using multi-line comments**. The &#x60;start_side&#x60; is the starting side of the diff that the comment applies to. Can be &#x60;LEFT&#x60; or &#x60;RIGHT&#x60;. To learn more about multi-line comments, see \&quot;[Commenting on a pull request](https://help.github.com/en/articles/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)\&quot; in the GitHub Help documentation. See &#x60;side&#x60; in this table for additional context. |  [optional] |



## Enum: SideEnum

| Name | Value |
|---- | -----|
| LEFT | &quot;LEFT&quot; |
| RIGHT | &quot;RIGHT&quot; |



## Enum: StartSideEnum

| Name | Value |
|---- | -----|
| LEFT | &quot;LEFT&quot; |
| RIGHT | &quot;RIGHT&quot; |
| SIDE | &quot;side&quot; |



