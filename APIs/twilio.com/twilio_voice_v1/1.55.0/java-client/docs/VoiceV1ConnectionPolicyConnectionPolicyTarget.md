

# VoiceV1ConnectionPolicyConnectionPolicyTarget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Target resource. |  [optional] |
|**connectionPolicySid** | **String** | The SID of the Connection Policy that owns the Target. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**enabled** | **Boolean** | Whether the target is enabled. The default is &#x60;true&#x60;. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**priority** | **Integer** | The relative importance of the target. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important target. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Target resource. |  [optional] |
|**target** | **URI** | The SIP address you want Twilio to route your calls to. This must be a &#x60;sip:&#x60; schema. &#x60;sips&#x60; is NOT supported. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**weight** | **Integer** | The value that determines the relative share of the load the Target should receive compared to other Targets with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. Targets with higher values receive more load than those with lower ones with the same priority. |  [optional] |



