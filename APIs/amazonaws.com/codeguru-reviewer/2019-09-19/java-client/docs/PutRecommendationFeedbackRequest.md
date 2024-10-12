

# PutRecommendationFeedbackRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**codeReviewArn** | **String** | The Amazon Resource Name (ARN) of the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html\&quot;&gt;CodeReview&lt;/a&gt; object.  |  |
|**recommendationId** | **String** | The recommendation ID that can be used to track the provided recommendations and then to collect the feedback. |  |
|**reactions** | **List&lt;Reaction&gt;** | List for storing reactions. Reactions are utf-8 text code for emojis. If you send an empty list it clears all your feedback. |  |



