

# InTotoStatement

Spec defined at https://github.com/in-toto/attestation/tree/main/spec#statement The serialized InTotoStatement will be stored as Envelope.payload. Envelope.payloadType is always \"application/vnd.in-toto+json\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | Always \&quot;https://in-toto.io/Statement/v0.1\&quot;. |  [optional] |
|**predicateType** | **String** | \&quot;https://slsa.dev/provenance/v0.1\&quot; for SlsaProvenance. |  [optional] |
|**provenance** | [**InTotoProvenance**](InTotoProvenance.md) |  |  [optional] |
|**slsaProvenance** | [**SlsaProvenance**](SlsaProvenance.md) |  |  [optional] |
|**slsaProvenanceZeroTwo** | [**SlsaProvenanceZeroTwo**](SlsaProvenanceZeroTwo.md) |  |  [optional] |
|**subject** | [**List&lt;Subject&gt;**](Subject.md) | subject is the subjects of the intoto statement |  [optional] |



