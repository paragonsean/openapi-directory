

# StudioV1FlowEngagement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Engagement resource. |  [optional] |
|**contactChannelAddress** | **String** | The phone number, SIP address or Client identifier that triggered this Engagement. Phone numbers are in E.164 format (+16175551212). SIP addresses are formatted as &#x60;name@company.com&#x60;. Client identifiers are formatted &#x60;client:name&#x60;. |  [optional] |
|**contactSid** | **String** | The SID of the Contact. |  [optional] |
|**context** | **Object** | The current state of the execution flow. As your flow executes, we save the state in a flow context. Your widgets can access the data in the flow context as variables, either in configuration fields or in text areas as variable substitution. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the Engagement was created in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the Engagement was updated in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**flowSid** | **String** | The SID of the Flow. |  [optional] |
|**links** | **Object** | The URLs of the Engagement&#39;s nested resources. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Engagement resource. |  [optional] |
|**status** | **EngagementEnumStatus** |  |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |



