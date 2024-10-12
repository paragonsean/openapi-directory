# ContainerAnalysisApi.ContaineranalysisGoogleDevtoolsCloudbuildV1Secret

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kmsKeyName** | **String** | Cloud KMS key name to use to decrypt these envs. | [optional] 
**secretEnv** | **{String: Blob}** | Map of environment variable name to its encrypted value. Secret environment variables must be unique across all of a build&#39;s secrets, and must be used by at least one build step. Values can be at most 64 KB in size. There can be at most 100 secret values across all of a build&#39;s secrets. | [optional] 


