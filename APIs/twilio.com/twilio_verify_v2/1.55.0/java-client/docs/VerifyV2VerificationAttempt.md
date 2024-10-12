

# VerifyV2VerificationAttempt


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Verification resource. |  [optional] |
|**channel** | **VerificationAttemptEnumChannels** |  |  [optional] |
|**channelData** | **Object** | An object containing the channel specific information for an attempt. |  [optional] |
|**conversionStatus** | **VerificationAttemptEnumConversionStatus** |  |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date that this Attempt was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this Attempt was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**price** | **Object** | An object containing the charge for this verification attempt related to the channel costs and the currency used. The costs related to the succeeded verifications are not included. May not be immediately available. More information on pricing is available [here](https://www.twilio.com/en-us/verify/pricing). |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) used to generate the attempt. |  [optional] |
|**sid** | **String** | The SID that uniquely identifies the verification attempt resource. |  [optional] |
|**url** | **URI** |  |  [optional] |
|**verificationSid** | **String** | The SID of the [Verification](https://www.twilio.com/docs/verify/api/verification) that generated the attempt. |  [optional] |



