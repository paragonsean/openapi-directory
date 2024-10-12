

# ContaineranalysisGoogleDevtoolsCloudbuildV1Secret

Pairs a set of secret environment variables containing encrypted values with the Cloud KMS key to use to decrypt the value. Note: Use `kmsKeyName` with `available_secrets` instead of using `kmsKeyName` with `secret`. For instructions see: https://cloud.google.com/cloud-build/docs/securing-builds/use-encrypted-credentials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyName** | **String** | Cloud KMS key name to use to decrypt these envs. |  [optional] |
|**secretEnv** | **Map&lt;String, byte[]&gt;** | Map of environment variable name to its encrypted value. Secret environment variables must be unique across all of a build&#39;s secrets, and must be used by at least one build step. Values can be at most 64 KB in size. There can be at most 100 secret values across all of a build&#39;s secrets. |  [optional] |



