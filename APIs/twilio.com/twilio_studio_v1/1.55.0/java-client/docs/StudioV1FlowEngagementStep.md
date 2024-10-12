

# StudioV1FlowEngagementStep


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Step resource. |  [optional] |
|**context** | **Object** | The current state of the Flow&#39;s Execution. As a flow executes, we save its state in this context. We save data that your widgets can access as variables in configuration fields or in text areas as variable substitution. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**engagementSid** | **String** | The SID of the Engagement. |  [optional] |
|**flowSid** | **String** | The SID of the Flow. |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**name** | **String** | The event that caused the Flow to transition to the Step. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Step resource. |  [optional] |
|**transitionedFrom** | **String** | The Widget that preceded the Widget for the Step. |  [optional] |
|**transitionedTo** | **String** | The Widget that will follow the Widget for the Step. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |



