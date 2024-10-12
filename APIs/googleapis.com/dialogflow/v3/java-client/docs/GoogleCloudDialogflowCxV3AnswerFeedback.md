

# GoogleCloudDialogflowCxV3AnswerFeedback

Stores information about feedback provided by users about a response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customRating** | **String** | Optional. Custom rating from the user about the provided answer, with maximum length of 1024 characters. For example, client could use a customized JSON object to indicate the rating. |  [optional] |
|**rating** | [**RatingEnum**](#RatingEnum) | Optional. Rating from user for the specific Dialogflow response. |  [optional] |
|**ratingReason** | [**GoogleCloudDialogflowCxV3AnswerFeedbackRatingReason**](GoogleCloudDialogflowCxV3AnswerFeedbackRatingReason.md) |  |  [optional] |



## Enum: RatingEnum

| Name | Value |
|---- | -----|
| RATING_UNSPECIFIED | &quot;RATING_UNSPECIFIED&quot; |
| THUMBS_UP | &quot;THUMBS_UP&quot; |
| THUMBS_DOWN | &quot;THUMBS_DOWN&quot; |



