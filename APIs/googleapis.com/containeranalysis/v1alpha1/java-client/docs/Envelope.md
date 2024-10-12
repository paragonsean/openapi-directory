

# Envelope

MUST match https://github.com/secure-systems-lab/dsse/blob/master/envelope.proto. An authenticated message of arbitrary type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payload** | **byte[]** | The bytes being signed |  [optional] |
|**payloadType** | **String** | The type of payload being signed |  [optional] |
|**signatures** | [**List&lt;EnvelopeSignature&gt;**](EnvelopeSignature.md) | The signatures over the payload |  [optional] |



