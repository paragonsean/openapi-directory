

# AutopilotV1AssistantModelBuild


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ModelBuild resource. |  [optional] |
|**assistantSid** | **String** | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource. |  [optional] |
|**buildDuration** | **Integer** | The time in seconds it took to build the model. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**errorCode** | **Integer** | If the &#x60;status&#x60; for the model build is &#x60;failed&#x60;, this value is a code to more information about the failure. This value will be null for all other statuses. See [error code dictionary](https://www.twilio.com/docs/api/errors) for a description of the error. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the ModelBuild resource. |  [optional] |
|**status** | **ModelBuildEnumStatus** |  |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. |  [optional] |
|**url** | **URI** | The absolute URL of the ModelBuild resource. |  [optional] |



