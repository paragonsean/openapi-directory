

# VerifyV2ServiceRateLimitBucket


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Rate Limit resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**interval** | **Integer** | Number of seconds that the rate limit will be enforced over. |  [optional] |
|**max** | **Integer** | Maximum number of requests permitted in during the interval. |  [optional] |
|**rateLimitSid** | **String** | The Twilio-provided string that uniquely identifies the Rate Limit resource. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this Bucket. |  [optional] |
|**url** | **URI** | The URL of this resource. |  [optional] |



