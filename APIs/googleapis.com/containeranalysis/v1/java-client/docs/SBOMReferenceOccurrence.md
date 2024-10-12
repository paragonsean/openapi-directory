

# SBOMReferenceOccurrence

The occurrence representing an SBOM reference as applied to a specific resource. The occurrence follows the DSSE specification. See https://github.com/secure-systems-lab/dsse/blob/master/envelope.md for more details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payload** | [**SbomReferenceIntotoPayload**](SbomReferenceIntotoPayload.md) |  |  [optional] |
|**payloadType** | **String** | The kind of payload that SbomReferenceIntotoPayload takes. Since it&#39;s in the intoto format, this value is expected to be &#39;application/vnd.in-toto+json&#39;. |  [optional] |
|**signatures** | [**List&lt;EnvelopeSignature&gt;**](EnvelopeSignature.md) | The signatures over the payload. |  [optional] |



