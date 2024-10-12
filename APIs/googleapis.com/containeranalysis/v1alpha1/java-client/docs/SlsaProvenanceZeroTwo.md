

# SlsaProvenanceZeroTwo

SlsaProvenanceZeroTwo is the slsa provenance as defined by the slsa spec. See full explanation of fields at slsa.dev/provenance/v0.2.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildConfig** | **Map&lt;String, Object&gt;** | Lists the steps in the build. |  [optional] |
|**buildType** | **String** | URI indicating what type of build was performed. |  [optional] |
|**builder** | [**GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaBuilder**](GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaBuilder.md) |  |  [optional] |
|**invocation** | [**GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaInvocation**](GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaInvocation.md) |  |  [optional] |
|**materials** | [**List&lt;GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaMaterial&gt;**](GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaMaterial.md) | The collection of artifacts that influenced the build including sources, dependencies, build tools, base images, and so on. |  [optional] |
|**metadata** | [**GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaMetadata**](GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaMetadata.md) |  |  [optional] |



