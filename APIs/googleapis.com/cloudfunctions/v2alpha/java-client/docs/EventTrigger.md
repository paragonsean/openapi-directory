

# EventTrigger

Describes EventTrigger, used to request events to be sent from another service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | **String** | Optional. The name of the channel associated with the trigger in &#x60;projects/{project}/locations/{location}/channels/{channel}&#x60; format. You must provide a channel to receive events from Eventarc SaaS partners. |  [optional] |
|**eventFilters** | [**List&lt;EventFilter&gt;**](EventFilter.md) | Criteria used to filter events. |  [optional] |
|**eventType** | **String** | Required. The type of event to observe. For example: &#x60;google.cloud.audit.log.v1.written&#x60; or &#x60;google.cloud.pubsub.topic.v1.messagePublished&#x60;. |  [optional] |
|**pubsubTopic** | **String** | Optional. The name of a Pub/Sub topic in the same project that will be used as the transport topic for the event delivery. Format: &#x60;projects/{project}/topics/{topic}&#x60;. This is only valid for events of type &#x60;google.cloud.pubsub.topic.v1.messagePublished&#x60;. The topic provided here will not be deleted at function deletion. |  [optional] |
|**retryPolicy** | [**RetryPolicyEnum**](#RetryPolicyEnum) | Optional. If unset, then defaults to ignoring failures (i.e. not retrying them). |  [optional] |
|**service** | **String** | Optional. The hostname of the service that 1st Gen function should be observed. If no string is provided, the default service implementing the API will be used. For example, &#x60;storage.googleapis.com&#x60; is the default for all event types in the &#x60;google.storage&#x60; namespace. The field is only applicable to 1st Gen functions. |  [optional] |
|**serviceAccountEmail** | **String** | Optional. The email of the trigger&#39;s service account. The service account must have permission to invoke Cloud Run services, the permission is &#x60;run.routes.invoke&#x60;. If empty, defaults to the Compute Engine default service account: &#x60;{project_number}-compute@developer.gserviceaccount.com&#x60;. |  [optional] |
|**trigger** | **String** | Output only. The resource name of the Eventarc trigger. The format of this field is &#x60;projects/{project}/locations/{region}/triggers/{trigger}&#x60;. |  [optional] [readonly] |
|**triggerRegion** | **String** | The region that the trigger will be in. The trigger will only receive events originating in this region. It can be the same region as the function, a different region or multi-region, or the global region. If not provided, defaults to the same region as the function. |  [optional] |



## Enum: RetryPolicyEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;RETRY_POLICY_UNSPECIFIED&quot; |
| DO_NOT_RETRY | &quot;RETRY_POLICY_DO_NOT_RETRY&quot; |
| RETRY | &quot;RETRY_POLICY_RETRY&quot; |



