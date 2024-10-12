

# PublishedOralQuestion


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answeringBody** | **String** |  |  [optional] |
|**answeringBodyId** | **Integer** |  |  [optional] |
|**answeringMinister** | [**MemberForDate**](MemberForDate.md) |  |  [optional] |
|**answeringMinisterId** | **Integer** |  |  [optional] |
|**answeringMinisterTitle** | **String** |  |  [optional] |
|**answeringWhen** | **OffsetDateTime** |  |  [optional] |
|**askingMember** | [**MemberForDate**](MemberForDate.md) |  |  [optional] |
|**askingMemberId** | **Integer** |  |  [optional] |
|**declarableInterestDetail** | **String** |  |  [optional] |
|**hansardLink** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**number** | **Integer** |  |  [optional] |
|**questionText** | **String** |  |  [optional] |
|**questionType** | [**QuestionTypeEnum**](#QuestionTypeEnum) |  |  [optional] |
|**removedFromToBeAskedWhen** | **OffsetDateTime** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tabledWhen** | **OffsetDateTime** |  |  [optional] |
|**UIN** | **Integer** |  |  [optional] |



## Enum: QuestionTypeEnum

| Name | Value |
|---- | -----|
| SUBSTANTIVE | &quot;Substantive&quot; |
| TOPICAL | &quot;Topical&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;Submitted&quot; |
| CARDED | &quot;Carded&quot; |
| UNSAVED | &quot;Unsaved&quot; |
| READY_FOR_SHUFFLE | &quot;ReadyForShuffle&quot; |
| TO_BE_ASKED | &quot;ToBeAsked&quot; |
| SHUFFLE_UNSUCCESSFUL | &quot;ShuffleUnsuccessful&quot; |
| WITHDRAWN | &quot;Withdrawn&quot; |
| UNSTARRED | &quot;Unstarred&quot; |
| DRAFT | &quot;Draft&quot; |
| FOR_REVIEW | &quot;ForReview&quot; |
| UNASKED | &quot;Unasked&quot; |
| TRANSFERRED | &quot;Transferred&quot; |



