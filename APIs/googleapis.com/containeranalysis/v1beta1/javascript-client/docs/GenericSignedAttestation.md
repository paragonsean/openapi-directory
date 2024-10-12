# ContainerAnalysisApi.GenericSignedAttestation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentType** | **String** | Type (for example schema) of the attestation payload that was signed. The verifier must ensure that the provided type is one that the verifier supports, and that the attestation payload is a valid instantiation of that type (for example by validating a JSON schema). | [optional] 
**serializedPayload** | **Blob** | The serialized payload that is verified by one or more &#x60;signatures&#x60;. The encoding and semantic meaning of this payload must match what is set in &#x60;content_type&#x60;. | [optional] 
**signatures** | [**[Signature]**](Signature.md) | One or more signatures over &#x60;serialized_payload&#x60;. Verifier implementations should consider this attestation message verified if at least one &#x60;signature&#x60; verifies &#x60;serialized_payload&#x60;. See &#x60;Signature&#x60; in common.proto for more details on signature structure and verification. | [optional] 



## Enum: ContentTypeEnum


* `CONTENT_TYPE_UNSPECIFIED` (value: `"CONTENT_TYPE_UNSPECIFIED"`)

* `SIMPLE_SIGNING_JSON` (value: `"SIMPLE_SIGNING_JSON"`)




