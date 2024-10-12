

# Usage

Configuration controlling usage of a service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**producerNotificationChannel** | **String** | The full resource name of a channel used for sending notifications to the service producer. Google Service Management currently only supports [Google Cloud Pub/Sub](https://cloud.google.com/pubsub) as a notification channel. To use Google Cloud Pub/Sub as the channel, this must be the name of a Cloud Pub/Sub topic that uses the Cloud Pub/Sub topic name format documented in https://cloud.google.com/pubsub/docs/overview. |  [optional] |
|**requirements** | **List&lt;String&gt;** | Requirements that must be satisfied before a consumer project can use the service. Each requirement is of the form /; for example &#39;serviceusage.googleapis.com/billing-enabled&#39;. For Google APIs, a Terms of Service requirement must be included here. Google Cloud APIs must include \&quot;serviceusage.googleapis.com/tos/cloud\&quot;. Other Google APIs should include \&quot;serviceusage.googleapis.com/tos/universal\&quot;. Additional ToS can be included based on the business needs. |  [optional] |
|**rules** | [**List&lt;UsageRule&gt;**](UsageRule.md) | A list of usage rules that apply to individual API methods. **NOTE:** All service configuration rules follow \&quot;last one wins\&quot; order. |  [optional] |



