

# ServerlessV1ServiceEnvironmentLog


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Log resource. |  [optional] |
|**buildSid** | **String** | The SID of the build that corresponds to the log. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the Log resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**deploymentSid** | **String** | The SID of the deployment that corresponds to the log. |  [optional] |
|**environmentSid** | **String** | The SID of the environment in which the log occurred. |  [optional] |
|**functionSid** | **String** | The SID of the function whose invocation produced the log. |  [optional] |
|**level** | **LogEnumLevel** |  |  [optional] |
|**message** | **String** | The log message. |  [optional] |
|**requestSid** | **String** | The SID of the request associated with the log. |  [optional] |
|**serviceSid** | **String** | The SID of the Service that the Log resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Log resource. |  [optional] |
|**url** | **URI** | The absolute URL of the Log resource. |  [optional] |



