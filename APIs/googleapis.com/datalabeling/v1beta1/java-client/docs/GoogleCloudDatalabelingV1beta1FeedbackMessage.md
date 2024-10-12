

# GoogleCloudDatalabelingV1beta1FeedbackMessage

A feedback message inside a feedback thread.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | String content of the feedback. Maximum of 10000 characters. |  [optional] |
|**createTime** | **String** | Create time. |  [optional] |
|**image** | **byte[]** | The image storing this feedback if the feedback is an image representing operator&#39;s comments. |  [optional] |
|**name** | **String** | Name of the feedback message in a feedback thread. Format: &#39;project/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset_id}/feedbackThreads/{feedback_thread_id}/feedbackMessage/{feedback_message_id}&#39; |  [optional] |
|**operatorFeedbackMetadata** | **Object** | Metadata describing the feedback from the operator. |  [optional] |
|**requesterFeedbackMetadata** | **Object** | Metadata describing the feedback from the labeling task requester. |  [optional] |



