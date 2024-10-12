# ContainerAnalysisApi.Metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildFinishedOn** | **String** | The timestamp of when the build completed. | [optional] 
**buildInvocationId** | **String** | Identifies the particular build invocation, which can be useful for finding associated logs or other ad-hoc analysis. The value SHOULD be globally unique, per in-toto Provenance spec. | [optional] 
**buildStartedOn** | **String** | The timestamp of when the build started. | [optional] 
**completeness** | [**Completeness**](Completeness.md) |  | [optional] 
**reproducible** | **Boolean** | If true, the builder claims that running the recipe on materials will produce bit-for-bit identical output. | [optional] 


