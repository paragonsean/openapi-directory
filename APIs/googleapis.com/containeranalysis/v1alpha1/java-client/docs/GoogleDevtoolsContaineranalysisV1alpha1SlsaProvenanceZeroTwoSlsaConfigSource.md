

# GoogleDevtoolsContaineranalysisV1alpha1SlsaProvenanceZeroTwoSlsaConfigSource

Describes where the config file that kicked off the build came from. This is effectively a pointer to the source where buildConfig came from.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**digest** | **Map&lt;String, String&gt;** | Collection of cryptographic digests for the contents of the artifact specified by invocation.configSource.uri. |  [optional] |
|**entryPoint** | **String** | String identifying the entry point into the build. |  [optional] |
|**uri** | **String** | URI indicating the identity of the source of the config. |  [optional] |



