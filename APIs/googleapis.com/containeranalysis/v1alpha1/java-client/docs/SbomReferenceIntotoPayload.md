

# SbomReferenceIntotoPayload

The actual payload that contains the SBOM Reference data. The payload follows the intoto statement specification. See https://github.com/in-toto/attestation/blob/main/spec/v1.0/statement.md for more details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | Identifier for the schema of the Statement. |  [optional] |
|**predicate** | [**SbomReferenceIntotoPredicate**](SbomReferenceIntotoPredicate.md) |  |  [optional] |
|**predicateType** | **String** | URI identifying the type of the Predicate. |  [optional] |
|**subject** | [**List&lt;Subject&gt;**](Subject.md) | Set of software artifacts that the attestation applies to. Each element represents a single software artifact. |  [optional] |



