# CloudHealthcareApi.PubsubDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubsubTopic** | **String** | The [Pub/Sub](https://cloud.google.com/pubsub/docs/) topic that Pub/Sub messages are published on. Supplied by the client. The &#x60;PubsubMessage&#x60; contains the following fields: * &#x60;PubsubMessage.Data&#x60; contains the resource name. * &#x60;PubsubMessage.MessageId&#x60; is the ID of this notification. It is guaranteed to be unique within the topic. * &#x60;PubsubMessage.PublishTime&#x60; is the time when the message was published. [Topic names](https://cloud.google.com/pubsub/docs/overview#names) must be scoped to a project. The Cloud Healthcare API service account, service-PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com, must have publisher permissions on the given Pub/Sub topic. Not having adequate permissions causes the calls that send notifications to fail. | [optional] 


