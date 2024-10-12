

# TriggerPubsubExecutionRequest

Request for the TriggerPubsubExecution method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gcPCloudEventsMode** | **String** | Required. LINT: LEGACY_NAMES The query parameter value for __GCP_CloudEventsMode, set by the Eventarc service when configuring triggers. |  [optional] |
|**deliveryAttempt** | **Integer** | The number of attempts that have been made to deliver this message. This is set by Pub/Sub for subscriptions that have the \&quot;dead letter\&quot; feature enabled, and hence provided here for compatibility, but is ignored by Workflows. |  [optional] |
|**message** | [**PubsubMessage**](PubsubMessage.md) |  |  [optional] |
|**subscription** | **String** | Required. The subscription of the Pub/Sub push notification. Format: projects/{project}/subscriptions/{sub} |  [optional] |



