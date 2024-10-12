

# StudioV1FlowExecution


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Execution resource. |  [optional] |
|**contactChannelAddress** | **String** | The phone number, SIP address or Client identifier that triggered the Execution. Phone numbers are in E.164 format (e.g. +16175551212). SIP addresses are formatted as &#x60;name@company.com&#x60;. Client identifiers are formatted &#x60;client:name&#x60;. |  [optional] |
|**contactSid** | **String** | The SID of the Contact. |  [optional] |
|**context** | **Object** | The current state of the Flow&#39;s Execution. As a flow executes, we save its state in this context. We save data that your widgets can access as variables in configuration fields or in text areas as variable substitution. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**flowSid** | **String** | The SID of the Flow. |  [optional] |
|**links** | **Object** | The URLs of nested resources. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Execution resource. |  [optional] |
|**status** | **ExecutionEnumStatus** |  |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |



