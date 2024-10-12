# CloudSchedulerApi.PubsubTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: String}** | Attributes for PubsubMessage. Pubsub message must contain either non-empty data, or at least one attribute. | [optional] 
**data** | **Blob** | The message payload for PubsubMessage. Pubsub message must contain either non-empty data, or at least one attribute. | [optional] 
**topicName** | **String** | Required. The name of the Cloud Pub/Sub topic to which messages will be published when a job is delivered. The topic name must be in the same format as required by Pub/Sub&#39;s [PublishRequest.name](https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#publishrequest), for example &#x60;projects/PROJECT_ID/topics/TOPIC_ID&#x60;. The topic must be in the same project as the Cloud Scheduler job. | [optional] 


