

# Envelope

MUST match https://github.com/secure-systems-lab/dsse/blob/master/envelope.proto. An authenticated message of arbitrary type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payload** | **byte[]** |  |  [optional] |
|**payloadType** | **String** |  |  [optional] |
|**signatures** | [**List&lt;EnvelopeSignature&gt;**](EnvelopeSignature.md) |  |  [optional] |



