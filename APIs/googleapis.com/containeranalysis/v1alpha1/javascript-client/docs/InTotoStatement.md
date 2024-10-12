# ContainerAnalysisApi.InTotoStatement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **String** | Always \&quot;https://in-toto.io/Statement/v0.1\&quot;. | [optional] 
**predicateType** | **String** | \&quot;https://slsa.dev/provenance/v0.1\&quot; for SlsaProvenance. | [optional] 
**provenance** | [**InTotoProvenance**](InTotoProvenance.md) |  | [optional] 
**slsaProvenance** | [**SlsaProvenance**](SlsaProvenance.md) |  | [optional] 
**slsaProvenanceZeroTwo** | [**SlsaProvenanceZeroTwo**](SlsaProvenanceZeroTwo.md) |  | [optional] 
**subject** | [**[Subject]**](Subject.md) | subject is the subjects of the intoto statement | [optional] 


